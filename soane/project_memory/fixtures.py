"""Golden fixture loader for Project Memory v0."""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping

from soane.project_memory.contract import (
    EvidenceLevel,
    LifecycleStatus,
    MemoryObject,
    MemoryObjectType,
    Provenance,
    Relationship,
    RelationshipType,
    Visibility,
    deterministic_fixture_id,
    validate_memory_object,
)


class FixtureValidationError(ValueError):
    """Raised when a golden fixture file violates the fixture contract."""


@dataclass(frozen=True)
class GoldenFixture:
    fixture_id: str
    title: str
    objects: Mapping[str, MemoryObject]
    expectations: tuple[str, ...]
    path: Path


def load_fixture(path: Path | str) -> GoldenFixture:
    """Load and validate one Project Memory golden fixture file."""

    fixture_path = Path(path)
    payload = json.loads(fixture_path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise FixtureValidationError(f"{fixture_path} must contain a JSON object")

    fixture_id = _required_str(payload, "fixture_id", fixture_path)
    title = _required_str(payload, "title", fixture_path)
    raw_objects = payload.get("objects")
    if not isinstance(raw_objects, list) or not raw_objects:
        raise FixtureValidationError(f"{fixture_path} requires a non-empty objects list")

    key_to_id: dict[str, str] = {}
    for raw_object in raw_objects:
        if not isinstance(raw_object, dict):
            raise FixtureValidationError(f"{fixture_path} object entries must be JSON objects")
        key = _required_str(raw_object, "key", fixture_path)
        object_type = MemoryObjectType(_required_str(raw_object, "type", fixture_path))
        object_title = _required_str(raw_object, "title", fixture_path)
        object_id = deterministic_fixture_id(fixture_id, object_type, object_title)
        explicit_id = raw_object.get("id")
        if explicit_id is not None and explicit_id != object_id:
            raise FixtureValidationError(f"{fixture_path} object {key} id is not deterministic")
        if key in key_to_id:
            raise FixtureValidationError(f"{fixture_path} duplicate object key: {key}")
        key_to_id[key] = object_id

    objects: dict[str, MemoryObject] = {}
    for raw_object in raw_objects:
        key = _required_str(raw_object, "key", fixture_path)
        memory_object = _parse_memory_object(
            fixture_id=fixture_id,
            raw_object=raw_object,
            key_to_id=key_to_id,
            fixture_path=fixture_path,
        )
        validate_memory_object(memory_object)
        objects[key] = memory_object

    raw_expectations = payload.get("expectations", [])
    if not isinstance(raw_expectations, list) or not all(isinstance(item, str) for item in raw_expectations):
        raise FixtureValidationError(f"{fixture_path} expectations must be a list of strings")

    return GoldenFixture(
        fixture_id=fixture_id,
        title=title,
        objects=objects,
        expectations=tuple(raw_expectations),
        path=fixture_path,
    )


def load_fixtures(directory: Path | str) -> tuple[GoldenFixture, ...]:
    """Load all golden fixtures from a directory in deterministic path order."""

    root = Path(directory)
    return tuple(load_fixture(path) for path in sorted(root.glob("GF-*.json")))


def _parse_memory_object(
    fixture_id: str,
    raw_object: Mapping[str, Any],
    key_to_id: Mapping[str, str],
    fixture_path: Path,
) -> MemoryObject:
    key = _required_str(raw_object, "key", fixture_path)
    object_type = MemoryObjectType(_required_str(raw_object, "type", fixture_path))
    title = _required_str(raw_object, "title", fixture_path)
    provenance_payload = raw_object.get("provenance")
    if not isinstance(provenance_payload, dict):
        raise FixtureValidationError(f"{fixture_path} object {key} requires provenance")

    relationships = tuple(
        _parse_relationship(raw_relationship, key_to_id, fixture_path)
        for raw_relationship in raw_object.get("relationships", [])
    )

    return MemoryObject(
        id=deterministic_fixture_id(fixture_id, object_type, title),
        type=object_type,
        title=title,
        status=LifecycleStatus(_required_str(raw_object, "status", fixture_path)),
        visibility=Visibility(_required_str(raw_object, "visibility", fixture_path)),
        provenance=Provenance(
            source_refs=tuple(_required_str_list(provenance_payload, "source_refs", fixture_path)),
            created_by=_required_str(provenance_payload, "created_by", fixture_path),
            created_at=_parse_datetime(_required_str(provenance_payload, "created_at", fixture_path), fixture_path),
            evidence_level=EvidenceLevel(_required_str(provenance_payload, "evidence_level", fixture_path)),
            derivation_refs=tuple(provenance_payload.get("derivation_refs", [])),
        ),
        relationships=relationships,
        updated_at=_parse_optional_datetime(raw_object.get("updated_at"), fixture_path),
        supersedes=tuple(_resolve_refs(raw_object.get("supersedes_keys", []), key_to_id, fixture_path)),
        superseded_by=tuple(_resolve_refs(raw_object.get("superseded_by_keys", []), key_to_id, fixture_path)),
        authority_ref=raw_object.get("authority_ref"),
        confidence=raw_object.get("confidence"),
        metadata=raw_object.get("metadata", {}),
    )


def _parse_relationship(
    raw_relationship: Mapping[str, Any],
    key_to_id: Mapping[str, str],
    fixture_path: Path,
) -> Relationship:
    if not isinstance(raw_relationship, dict):
        raise FixtureValidationError(f"{fixture_path} relationship entries must be JSON objects")
    target_id = raw_relationship.get("target_id")
    target_key = raw_relationship.get("target_key")
    if target_key is not None:
        target_id = _resolve_ref(target_key, key_to_id, fixture_path)
    if not isinstance(target_id, str) or not target_id.strip():
        raise FixtureValidationError(f"{fixture_path} relationship requires target_key or target_id")
    evidence_ids = tuple(_resolve_refs(raw_relationship.get("evidence_keys", []), key_to_id, fixture_path))
    return Relationship(
        type=RelationshipType(_required_str(raw_relationship, "type", fixture_path)),
        target_id=target_id,
        evidence_ids=evidence_ids,
    )


def _resolve_refs(raw_keys: Any, key_to_id: Mapping[str, str], fixture_path: Path) -> tuple[str, ...]:
    if not isinstance(raw_keys, list):
        raise FixtureValidationError(f"{fixture_path} reference keys must be a list")
    return tuple(_resolve_ref(key, key_to_id, fixture_path) for key in raw_keys)


def _resolve_ref(key: Any, key_to_id: Mapping[str, str], fixture_path: Path) -> str:
    if not isinstance(key, str) or not key:
        raise FixtureValidationError(f"{fixture_path} reference key must be a non-empty string")
    if key not in key_to_id:
        raise FixtureValidationError(f"{fixture_path} unknown fixture object key: {key}")
    return key_to_id[key]


def _parse_datetime(raw_value: str, fixture_path: Path) -> datetime:
    try:
        value = datetime.fromisoformat(raw_value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise FixtureValidationError(f"{fixture_path} invalid datetime: {raw_value}") from exc
    if value.tzinfo is None:
        raise FixtureValidationError(f"{fixture_path} datetime must be timezone-aware: {raw_value}")
    return value


def _parse_optional_datetime(raw_value: Any, fixture_path: Path) -> datetime | None:
    if raw_value is None:
        return None
    if not isinstance(raw_value, str):
        raise FixtureValidationError(f"{fixture_path} optional datetime must be a string")
    return _parse_datetime(raw_value, fixture_path)


def _required_str(payload: Mapping[str, Any], key: str, fixture_path: Path) -> str:
    value = payload.get(key)
    if not isinstance(value, str) or not value.strip():
        raise FixtureValidationError(f"{fixture_path} requires non-empty string field: {key}")
    return value


def _required_str_list(payload: Mapping[str, Any], key: str, fixture_path: Path) -> tuple[str, ...]:
    value = payload.get(key)
    if not isinstance(value, list) or not value or not all(isinstance(item, str) and item for item in value):
        raise FixtureValidationError(f"{fixture_path} requires non-empty string list field: {key}")
    return tuple(value)

