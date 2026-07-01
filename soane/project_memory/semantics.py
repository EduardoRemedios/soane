"""Local Project Memory v0 semantics.

This module provides deterministic in-memory behavior over the v0 contract.
It is not a database, context assembly engine, CLI, TUI, or adapter runtime.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from datetime import datetime
from typing import Iterable, Mapping

from soane.project_memory.contract import (
    ContractValidationError,
    LifecycleStatus,
    MemoryObject,
    Relationship,
    RelationshipType,
    Visibility,
    can_transition,
    utc_now,
    validate_memory_object,
)
from soane.project_memory.fixtures import GoldenFixture


class MemorySemanticsError(ValueError):
    """Raised when local Project Memory semantics are violated."""


@dataclass(frozen=True)
class AccessContext:
    """Minimal access context for v0 visibility checks."""

    scopes: tuple[str, ...]
    include_suppressed: bool = False


PROJECT_READER = AccessContext(scopes=("project",))
PROJECT_REVIEWER = AccessContext(scopes=("project", "project_reviewer"))
EXTERNAL_ADAPTER = AccessContext(scopes=("external_adapter",))

NON_CURRENT_STATUSES = frozenset(
    {
        LifecycleStatus.SUPERSEDED,
        LifecycleStatus.INVALIDATED,
        LifecycleStatus.RETIRED,
        LifecycleStatus.ARCHIVED,
        LifecycleStatus.STALE,
        LifecycleStatus.REVOKED,
        LifecycleStatus.REJECTED,
    }
)


class ProjectMemory:
    """A local, inspectable collection of Project Memory objects."""

    def __init__(self, objects: Iterable[MemoryObject] = ()) -> None:
        self._objects: dict[str, MemoryObject] = {}
        for memory_object in objects:
            self.add(memory_object)
        self._validate_relationship_targets()

    @classmethod
    def from_fixtures(cls, fixtures: Iterable[GoldenFixture]) -> "ProjectMemory":
        objects: list[MemoryObject] = []
        for fixture in fixtures:
            objects.extend(fixture.objects.values())
        return cls(objects)

    def add(self, memory_object: MemoryObject) -> None:
        validate_memory_object(memory_object)
        if memory_object.id in self._objects:
            raise MemorySemanticsError(f"duplicate memory object id: {memory_object.id}")
        self._objects[memory_object.id] = memory_object

    def inspect(self, object_id: str) -> MemoryObject | None:
        """Return an object without visibility filtering for audit/internal inspection."""

        return self._objects.get(object_id)

    def get(self, object_id: str, access: AccessContext) -> MemoryObject | None:
        """Return an object only if visible to the access context."""

        memory_object = self._objects.get(object_id)
        if memory_object is None or not is_visible(memory_object, access):
            return None
        return memory_object

    def visible_objects(self, access: AccessContext) -> tuple[MemoryObject, ...]:
        return tuple(obj for obj in self._objects.values() if is_visible(obj, access))

    def current_objects(self, access: AccessContext) -> tuple[MemoryObject, ...]:
        return tuple(
            obj
            for obj in self.visible_objects(access)
            if obj.status not in NON_CURRENT_STATUSES and obj.visibility != Visibility.SUPPRESSED
        )

    def transition(self, object_id: str, to_status: LifecycleStatus, updated_at: datetime | None = None) -> MemoryObject:
        memory_object = self._require_object(object_id)
        if not can_transition(memory_object.status, to_status):
            raise MemorySemanticsError(f"invalid lifecycle transition: {memory_object.status.value} -> {to_status.value}")
        transitioned = replace(memory_object, status=to_status, updated_at=updated_at or utc_now())
        validate_memory_object(transitioned)
        self._objects[object_id] = transitioned
        return transitioned

    def relationship_targets(
        self,
        memory_object: MemoryObject,
        relationship_type: RelationshipType,
        access: AccessContext | None = None,
    ) -> tuple[MemoryObject, ...]:
        targets: list[MemoryObject] = []
        for relationship in memory_object.relationships:
            if relationship.type != relationship_type:
                continue
            target = self._objects.get(relationship.target_id)
            if target is None:
                continue
            if access is None or is_visible(target, access):
                targets.append(target)
        return tuple(targets)

    def evidence_for(self, memory_object: MemoryObject, access: AccessContext | None = None) -> tuple[MemoryObject, ...]:
        return self.relationship_targets(memory_object, RelationshipType.EVIDENCES, access)

    def contradictions(self, access: AccessContext) -> tuple[tuple[MemoryObject, MemoryObject], ...]:
        pairs: list[tuple[MemoryObject, MemoryObject]] = []
        seen: set[frozenset[str]] = set()
        for memory_object in self.visible_objects(access):
            for relationship in memory_object.relationships:
                if relationship.type != RelationshipType.CONTRADICTS:
                    continue
                target = self.get(relationship.target_id, access)
                if target is None:
                    continue
                pair_key = frozenset({memory_object.id, target.id})
                if pair_key not in seen:
                    seen.add(pair_key)
                    pairs.append((memory_object, target))
        return tuple(pairs)

    def _require_object(self, object_id: str) -> MemoryObject:
        memory_object = self._objects.get(object_id)
        if memory_object is None:
            raise MemorySemanticsError(f"unknown memory object id: {object_id}")
        return memory_object

    def _validate_relationship_targets(self) -> None:
        for memory_object in self._objects.values():
            for relationship in memory_object.relationships:
                if relationship.target_id.startswith("pmem_") and relationship.target_id not in self._objects:
                    raise MemorySemanticsError(
                        f"{memory_object.id} references unknown memory object {relationship.target_id}"
                    )


def is_visible(memory_object: MemoryObject, access: AccessContext) -> bool:
    """Return whether an object is visible to an access context."""

    if memory_object.visibility == Visibility.PUBLIC:
        return True
    if memory_object.visibility == Visibility.PROJECT:
        return "project" in access.scopes or "project_reviewer" in access.scopes
    if memory_object.visibility == Visibility.RESTRICTED:
        allowed_scopes = _metadata_string_set(memory_object.metadata, "allowed_scopes")
        if allowed_scopes:
            return bool(allowed_scopes.intersection(access.scopes))
        return "project_reviewer" in access.scopes
    if memory_object.visibility == Visibility.SUPPRESSED:
        return access.include_suppressed and "suppressed_audit" in access.scopes
    return False


def _metadata_string_set(metadata: Mapping[str, object], key: str) -> frozenset[str]:
    raw_value = metadata.get(key)
    if not isinstance(raw_value, list):
        return frozenset()
    return frozenset(item for item in raw_value if isinstance(item, str) and item)

