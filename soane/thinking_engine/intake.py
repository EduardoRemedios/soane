"""Thinking Engine Intake v0 local semantics.

This module is deliberately deterministic and connector-free. It models the
minimum intake behavior needed before Soane delegates work or plans features.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from enum import StrEnum
from hashlib import sha256
from pathlib import Path
from typing import Any, Mapping

from soane.project_memory.contract import (
    CONTRACT_VERSION,
    EvidenceLevel,
    LifecycleStatus,
    MemoryObject,
    MemoryObjectType,
    Provenance,
    Visibility,
    validate_memory_object,
)


INTAKE_FIXTURE_CREATED_AT = datetime(2026, 7, 1, tzinfo=timezone.utc)


class IntakeValidationError(ValueError):
    """Raised when an intake fixture or request is invalid."""


class IntakeCategory(StrEnum):
    GREENFIELD = "greenfield"
    BROWNFIELD_SINGLE_REPO = "brownfield_single_repo"
    BROWNFIELD_MULTI_REPO = "brownfield_multi_repo"
    NON_REPOSITORY_CONTEXT = "non_repository_context"


class ReadinessState(StrEnum):
    NOT_READY = "not_ready"
    READY_FOR_DISCOVERY = "ready_for_discovery"
    READY_FOR_PLANNING = "ready_for_planning"
    READY_FOR_DECISION = "ready_for_decision"
    READY_FOR_DELEGATION = "ready_for_delegation"
    BLOCKED = "blocked"


@dataclass(frozen=True)
class ContextSource:
    id: str
    type: str
    title: str
    location: str
    owner: str | None = None
    available: bool = True
    evidence_level: EvidenceLevel = EvidenceLevel.E1_SOURCE_REFERENCE


@dataclass(frozen=True)
class ContextBaseline:
    project_name: str
    category: IntakeCategory
    goal: str
    goals: tuple[str, ...]
    non_goals: tuple[str, ...]
    repositories: tuple[ContextSource, ...]
    external_sources: tuple[ContextSource, ...]
    canonical_docs: tuple[str, ...]
    assumptions: tuple[str, ...]
    constraints: tuple[str, ...]
    open_questions: tuple[str, ...]
    missing_context: tuple[str, ...]
    build_commands: tuple[str, ...] = ()
    test_commands: tuple[str, ...] = ()
    system_boundary: str | None = None


@dataclass(frozen=True)
class DiscoveryPlaybook:
    id: str
    title: str
    applies_to: IntakeCategory
    required_sources: tuple[str, ...]
    output_objects: tuple[MemoryObjectType, ...]


@dataclass(frozen=True)
class ReadinessAssessment:
    state: ReadinessState
    dimensions: Mapping[str, str]
    blockers: tuple[str, ...]
    missing_context: tuple[str, ...]


@dataclass(frozen=True)
class IntakeAssessment:
    fixture_id: str
    baseline: ContextBaseline
    readiness: ReadinessAssessment
    playbooks: tuple[DiscoveryPlaybook, ...]
    memory_candidates: tuple[MemoryObject, ...]
    live_call_performed: bool = False


@dataclass(frozen=True)
class IntakeFixture:
    fixture_id: str
    title: str
    payload: Mapping[str, Any]
    expected_category: IntakeCategory
    expected_readiness: ReadinessState
    expected_playbooks: tuple[str, ...]
    path: Path


def load_intake_fixture(path: Path | str) -> IntakeFixture:
    fixture_path = Path(path)
    payload = json.loads(fixture_path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise IntakeValidationError(f"{fixture_path} must contain a JSON object")
    fixture_id = _required_str(payload, "fixture_id", fixture_path)
    title = _required_str(payload, "title", fixture_path)
    expected = payload.get("expected")
    if not isinstance(expected, dict):
        raise IntakeValidationError(f"{fixture_path} requires expected")
    return IntakeFixture(
        fixture_id=fixture_id,
        title=title,
        payload=payload,
        expected_category=IntakeCategory(_required_str(expected, "category", fixture_path)),
        expected_readiness=ReadinessState(_required_str(expected, "readiness", fixture_path)),
        expected_playbooks=tuple(_required_str_list(expected, "playbooks", fixture_path)),
        path=fixture_path,
    )


def load_intake_fixtures(directory: Path | str) -> tuple[IntakeFixture, ...]:
    root = Path(directory)
    return tuple(load_intake_fixture(path) for path in sorted(root.glob("TEI-GF-*.json")))


def assess_intake(fixture: IntakeFixture) -> IntakeAssessment:
    payload = fixture.payload
    project = _required_mapping(payload, "project", fixture.path)
    category = _classify(payload, fixture.path)
    baseline = ContextBaseline(
        project_name=_required_str(project, "name", fixture.path),
        category=category,
        goal=_required_str(project, "goal", fixture.path),
        goals=tuple(_optional_str_list(payload, "goals")),
        non_goals=tuple(_optional_str_list(payload, "non_goals")),
        repositories=_parse_sources(payload.get("repositories", []), fixture.path),
        external_sources=_parse_sources(payload.get("external_sources", []), fixture.path),
        canonical_docs=tuple(_optional_str_list(payload, "canonical_docs")),
        assumptions=tuple(_optional_str_list(payload, "assumptions")),
        constraints=tuple(_optional_str_list(payload, "constraints")),
        open_questions=tuple(_optional_str_list(payload, "open_questions")),
        missing_context=tuple(_optional_str_list(payload, "missing_context")),
        build_commands=tuple(_optional_str_list(payload, "build_commands")),
        test_commands=tuple(_optional_str_list(payload, "test_commands")),
        system_boundary=project.get("system_boundary") if isinstance(project.get("system_boundary"), str) else None,
    )
    readiness = _readiness_for(payload, baseline)
    playbooks = _select_playbooks(payload, baseline)
    candidates = _memory_candidates(fixture.fixture_id, baseline, readiness)
    for candidate in candidates:
        validate_memory_object(candidate)
    return IntakeAssessment(
        fixture_id=fixture.fixture_id,
        baseline=baseline,
        readiness=readiness,
        playbooks=playbooks,
        memory_candidates=candidates,
        live_call_performed=False,
    )


def _classify(payload: Mapping[str, Any], fixture_path: Path) -> IntakeCategory:
    project = _required_mapping(payload, "project", fixture_path)
    declared = project.get("declared_category")
    if isinstance(declared, str) and declared:
        return IntakeCategory(declared)
    repositories = payload.get("repositories", [])
    external_sources = payload.get("external_sources", [])
    if isinstance(repositories, list) and len(repositories) > 1:
        return IntakeCategory.BROWNFIELD_MULTI_REPO
    if isinstance(repositories, list) and len(repositories) == 1:
        return IntakeCategory.BROWNFIELD_SINGLE_REPO
    if isinstance(external_sources, list) and external_sources:
        return IntakeCategory.NON_REPOSITORY_CONTEXT
    return IntakeCategory.GREENFIELD


def _readiness_for(payload: Mapping[str, Any], baseline: ContextBaseline) -> ReadinessAssessment:
    blocking_missing = bool(payload.get("blocking_missing_context", False))
    dimensions = {
        "goal_clarity": "present" if baseline.goal else "missing",
        "boundary_clarity": "present" if baseline.system_boundary or baseline.category == IntakeCategory.GREENFIELD else "needs_discovery",
        "context_sources": "present" if baseline.repositories or baseline.external_sources or baseline.canonical_docs else "missing",
        "evidence_sufficiency": "gapped" if baseline.missing_context else "initial",
        "assumption_risk": "visible" if baseline.assumptions else "none_recorded",
        "open_question_severity": "blocking" if blocking_missing else ("open" if baseline.open_questions else "none_recorded"),
        "authority_status": "not_assessed",
        "verification_path": "fixture_backed",
    }
    if blocking_missing:
        state = ReadinessState.BLOCKED
        blockers = baseline.missing_context or ("blocking context missing",)
    elif baseline.missing_context:
        state = ReadinessState.READY_FOR_DISCOVERY
        blockers = ()
    elif baseline.repositories or baseline.external_sources or baseline.canonical_docs:
        state = ReadinessState.READY_FOR_PLANNING
        blockers = ()
    else:
        state = ReadinessState.NOT_READY
        blockers = ("no usable context sources",)
    return ReadinessAssessment(
        state=state,
        dimensions=dimensions,
        blockers=tuple(blockers),
        missing_context=baseline.missing_context,
    )


def _select_playbooks(payload: Mapping[str, Any], baseline: ContextBaseline) -> tuple[DiscoveryPlaybook, ...]:
    domain = payload.get("domain")
    if baseline.category == IntakeCategory.GREENFIELD:
        return (
            _playbook("greenfield_product_definition", "Greenfield Product Definition", baseline.category, ("brief",)),
            _playbook("context_baseline_discovery", "Context Baseline Discovery", baseline.category, ("canonical_docs",)),
        )
    if baseline.category == IntakeCategory.BROWNFIELD_SINGLE_REPO:
        return (
            _playbook("brownfield_repository_audit", "Brownfield Repository Audit", baseline.category, ("repository",)),
            _playbook("software_engineering_discovery", "Software Engineering Discovery", baseline.category, ("repository", "docs")),
        )
    if baseline.category == IntakeCategory.BROWNFIELD_MULTI_REPO:
        return (
            _playbook("brownfield_system_audit", "Brownfield System Audit", baseline.category, ("repository_map",)),
            _playbook("integration_boundary_discovery", "Integration Boundary Discovery", baseline.category, ("service_map",)),
        )
    if domain == "digital_marketing":
        return (
            _playbook("digital_marketing_campaign_discovery", "Digital Marketing Campaign Discovery", baseline.category, ("analytics", "campaign_assets")),
            _playbook("external_context_review", "External Context Review", baseline.category, ("external_sources",)),
        )
    return (
        _playbook("external_context_review", "External Context Review", baseline.category, ("external_sources",)),
    )


def _playbook(
    playbook_id: str,
    title: str,
    category: IntakeCategory,
    required_sources: tuple[str, ...],
) -> DiscoveryPlaybook:
    return DiscoveryPlaybook(
        id=playbook_id,
        title=title,
        applies_to=category,
        required_sources=required_sources,
        output_objects=(
            MemoryObjectType.QUESTION,
            MemoryObjectType.ASSUMPTION,
            MemoryObjectType.EVIDENCE_ARTIFACT,
            MemoryObjectType.RESEARCH_FINDING,
        ),
    )


def _memory_candidates(
    fixture_id: str,
    baseline: ContextBaseline,
    readiness: ReadinessAssessment,
) -> tuple[MemoryObject, ...]:
    source_refs = (f"thinking-intake-fixture://{fixture_id}",)
    candidates: list[MemoryObject] = [
        _candidate_object(
            fixture_id,
            MemoryObjectType.PROJECT,
            baseline.project_name,
            LifecycleStatus.PROPOSED,
            source_refs,
            {
                "candidate": True,
                "promotion_required": True,
                "intake_category": baseline.category.value,
                "readiness_state": readiness.state.value,
            },
        )
    ]
    for question in (*baseline.open_questions, *baseline.missing_context):
        candidates.append(
            _candidate_object(
                fixture_id,
                MemoryObjectType.QUESTION,
                question,
                LifecycleStatus.OPEN,
                source_refs,
                {"candidate": True, "promotion_required": True, "source": "thinking_engine_intake"},
            )
        )
    for assumption in baseline.assumptions:
        candidates.append(
            _candidate_object(
                fixture_id,
                MemoryObjectType.ASSUMPTION,
                assumption,
                LifecycleStatus.PROPOSED,
                source_refs,
                {"candidate": True, "promotion_required": True, "source": "thinking_engine_intake"},
            )
        )
    for constraint in baseline.constraints:
        candidates.append(
            _candidate_object(
                fixture_id,
                MemoryObjectType.CONSTRAINT,
                constraint,
                LifecycleStatus.PROPOSED,
                source_refs,
                {"candidate": True, "promotion_required": True, "source": "thinking_engine_intake"},
            )
        )
    return tuple(candidates)


def _candidate_object(
    fixture_id: str,
    object_type: MemoryObjectType,
    title: str,
    status: LifecycleStatus,
    source_refs: tuple[str, ...],
    metadata: Mapping[str, object],
) -> MemoryObject:
    return MemoryObject(
        id=_deterministic_candidate_id(fixture_id, object_type, title),
        type=object_type,
        title=title,
        status=status,
        visibility=Visibility.PROJECT,
        provenance=Provenance(
            source_refs=source_refs,
            created_by="thinking-engine-intake",
            created_at=INTAKE_FIXTURE_CREATED_AT,
            evidence_level=EvidenceLevel.E2_REVIEWED_SYNTHESIS,
        ),
        metadata=metadata,
    )


def _deterministic_candidate_id(fixture_id: str, object_type: MemoryObjectType, title: str) -> str:
    seed = f"{CONTRACT_VERSION}:thinking-intake:{fixture_id}:{object_type.value}:{title}".strip().lower()
    digest = sha256(seed.encode("utf-8")).hexdigest()[:16]
    return f"pmem_{object_type.value}_{digest}"


def _parse_sources(raw_sources: Any, fixture_path: Path) -> tuple[ContextSource, ...]:
    if not isinstance(raw_sources, list):
        raise IntakeValidationError(f"{fixture_path} sources must be a list")
    sources: list[ContextSource] = []
    for raw_source in raw_sources:
        if not isinstance(raw_source, dict):
            raise IntakeValidationError(f"{fixture_path} source entries must be objects")
        sources.append(
            ContextSource(
                id=_required_str(raw_source, "id", fixture_path),
                type=_required_str(raw_source, "type", fixture_path),
                title=_required_str(raw_source, "title", fixture_path),
                location=_required_str(raw_source, "location", fixture_path),
                owner=raw_source.get("owner") if isinstance(raw_source.get("owner"), str) else None,
                available=bool(raw_source.get("available", True)),
                evidence_level=EvidenceLevel(raw_source.get("evidence_level", "E1")),
            )
        )
    return tuple(sources)


def _required_mapping(payload: Mapping[str, Any], key: str, fixture_path: Path) -> Mapping[str, Any]:
    value = payload.get(key)
    if not isinstance(value, dict):
        raise IntakeValidationError(f"{fixture_path} requires object field: {key}")
    return value


def _required_str(payload: Mapping[str, Any], key: str, fixture_path: Path) -> str:
    value = payload.get(key)
    if not isinstance(value, str) or not value.strip():
        raise IntakeValidationError(f"{fixture_path} requires non-empty string field: {key}")
    return value


def _required_str_list(payload: Mapping[str, Any], key: str, fixture_path: Path) -> tuple[str, ...]:
    values = payload.get(key)
    if not isinstance(values, list) or not values:
        raise IntakeValidationError(f"{fixture_path} requires non-empty string list field: {key}")
    if not all(isinstance(item, str) and item.strip() for item in values):
        raise IntakeValidationError(f"{fixture_path} field {key} must contain only non-empty strings")
    return tuple(values)


def _optional_str_list(payload: Mapping[str, Any], key: str) -> tuple[str, ...]:
    values = payload.get(key, [])
    if not isinstance(values, list):
        return ()
    return tuple(item for item in values if isinstance(item, str) and item.strip())
