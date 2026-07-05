"""Coding Proof Harness v0 local semantics.

The harness composes existing Soane primitives to prove a coding workflow
without live providers, repository mutation, persistence, or product UI.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from typing import Any, Mapping

from soane.project_memory.adapters import AdapterSurface, AdapterTwinResult, default_adapter_twins
from soane.project_memory.context import ContextPackage, ContextRequest, build_context_package
from soane.project_memory.contract import (
    CONTRACT_VERSION,
    EvidenceLevel,
    LifecycleStatus,
    MemoryObject,
    MemoryObjectType,
    Provenance,
    Relationship,
    RelationshipType,
    Visibility,
    validate_memory_object,
)
from soane.project_memory.review import CandidateReviewResult, ReviewDecision, review_candidate
from soane.project_memory.semantics import PROJECT_READER, ProjectMemory
from soane.thinking_engine.discovery import DiscoverySession, DiscoveryStopCondition, start_discovery_session
from soane.thinking_engine.intake import IntakeAssessment, IntakeFixture, ReadinessState, assess_intake, load_intake_fixture


CODING_HARNESS_FIXTURE_CREATED_AT = datetime(2026, 7, 1, 16, 0, tzinfo=timezone.utc)


class CodingHarnessValidationError(ValueError):
    """Raised when Coding Proof Harness v0 inputs violate local semantics."""


@dataclass(frozen=True)
class CodingTask:
    title: str
    prompt: str


@dataclass(frozen=True)
class MultiRepoSystemContext:
    repository_map: tuple[Mapping[str, object], ...]
    relevant_repositories: tuple[str, ...]
    out_of_scope_repositories: tuple[str, ...]
    service_boundaries: tuple[str, ...]
    integration_contracts: tuple[str, ...]
    ownership: tuple[str, ...]
    build_test_responsibility: tuple[str, ...]
    documentation_gaps: tuple[str, ...]
    authority_path: tuple[str, ...]

    @property
    def ready_for_provider(self) -> bool:
        return all(
            (
                self.repository_map,
                self.relevant_repositories,
                self.service_boundaries,
                self.integration_contracts,
                self.ownership,
                self.build_test_responsibility,
                self.authority_path,
            )
        )

    def as_metadata(self) -> dict[str, object]:
        return {
            "repository_map": list(self.repository_map),
            "relevant_repositories": list(self.relevant_repositories),
            "out_of_scope_repositories": list(self.out_of_scope_repositories),
            "service_boundaries": list(self.service_boundaries),
            "integration_contracts": list(self.integration_contracts),
            "ownership": list(self.ownership),
            "build_test_responsibility": list(self.build_test_responsibility),
            "documentation_gaps": list(self.documentation_gaps),
            "authority_path": list(self.authority_path),
            "ready_for_provider": self.ready_for_provider,
        }


@dataclass(frozen=True)
class CodingHarnessFixture:
    fixture_id: str
    title: str
    intake_fixture: IntakeFixture
    task: CodingTask
    provider_surface: AdapterSurface
    proposed_output: str
    expected_ready_for_provider: bool
    path: Path
    multi_repo_system: MultiRepoSystemContext | None = None


@dataclass(frozen=True)
class CodingHarnessResult:
    fixture_id: str
    intake: IntakeAssessment
    discovery: DiscoverySession
    context_package: ContextPackage
    provider_surface: AdapterSurface
    provider_result: AdapterTwinResult | None
    provider_invocation: MemoryObject | None
    output_candidate: MemoryObject | None
    memory_objects: tuple[MemoryObject, ...]
    ready_for_provider: bool
    multi_repo_system: MultiRepoSystemContext | None = None
    live_call_performed: bool = False
    repository_mutation_performed: bool = False


def load_coding_harness_fixture(path: Path | str) -> CodingHarnessFixture:
    fixture_path = Path(path)
    intake_fixture = load_intake_fixture(fixture_path)
    payload = intake_fixture.payload
    harness = _required_mapping(payload, "harness", fixture_path)
    task_payload = _required_mapping(harness, "task", fixture_path)
    expected = _required_mapping(harness, "expected", fixture_path)
    return CodingHarnessFixture(
        fixture_id=intake_fixture.fixture_id,
        title=intake_fixture.title,
        intake_fixture=intake_fixture,
        task=CodingTask(
            title=_required_str(task_payload, "title", fixture_path),
            prompt=_required_str(task_payload, "prompt", fixture_path),
        ),
        provider_surface=AdapterSurface(_required_str(harness, "provider_surface", fixture_path)),
        proposed_output=_required_str(harness, "proposed_output", fixture_path),
        expected_ready_for_provider=bool(expected.get("ready_for_provider", False)),
        path=fixture_path,
        multi_repo_system=_parse_multi_repo_system(payload.get("multi_repo_system"), fixture_path),
    )


def load_coding_harness_fixtures(directory: Path | str) -> tuple[CodingHarnessFixture, ...]:
    root = Path(directory)
    return tuple(load_coding_harness_fixture(path) for path in sorted(root.glob("CPH-*.json")))


def run_coding_proof(fixture: CodingHarnessFixture) -> CodingHarnessResult:
    """Run the deterministic mock coding proof path for one fixture."""

    intake = assess_intake(fixture.intake_fixture)
    discovery = start_discovery_session(intake)
    base_memory_objects = (*intake.memory_candidates, *discovery.memory_candidates)
    context_package = build_context_package(
        ProjectMemory(base_memory_objects),
        ContextRequest(
            purpose=f"coding proof: {fixture.task.title}",
            access=PROJECT_READER,
            boundary="external_adapter_context",
        ),
    )
    ready_for_provider = _ready_for_provider(intake, discovery, fixture)

    provider_result: AdapterTwinResult | None = None
    provider_invocation: MemoryObject | None = None
    output_candidate: MemoryObject | None = None
    memory_objects = base_memory_objects

    if ready_for_provider:
        provider_result = _invoke_provider(fixture, context_package)
        provider_invocation = _stable_invocation_object(provider_result)
        output_candidate = _output_candidate(fixture, provider_invocation)
        memory_objects = (*memory_objects, provider_invocation, output_candidate)

    if ready_for_provider != fixture.expected_ready_for_provider:
        raise CodingHarnessValidationError(
            f"{fixture.fixture_id} ready_for_provider expected "
            f"{fixture.expected_ready_for_provider}, got {ready_for_provider}"
        )

    return CodingHarnessResult(
        fixture_id=fixture.fixture_id,
        intake=intake,
        discovery=discovery,
        context_package=context_package,
        provider_surface=fixture.provider_surface,
        provider_result=provider_result,
        provider_invocation=provider_invocation,
        output_candidate=output_candidate,
        memory_objects=memory_objects,
        ready_for_provider=ready_for_provider,
        multi_repo_system=fixture.multi_repo_system,
        live_call_performed=False,
        repository_mutation_performed=False,
    )


def review_provider_output(result: CodingHarnessResult, decision: ReviewDecision) -> CandidateReviewResult:
    """Promote, reject, or defer proposed provider output through Candidate Review."""

    if result.output_candidate is None:
        raise CodingHarnessValidationError("provider output is unavailable for review")
    return review_candidate(result.output_candidate, decision)


def _ready_for_provider(intake: IntakeAssessment, discovery: DiscoverySession, fixture: CodingHarnessFixture) -> bool:
    base_ready = (
        intake.readiness.state == ReadinessState.READY_FOR_PLANNING
        and discovery.stop_condition == DiscoveryStopCondition.READY_FOR_PLANNING
    )
    if not base_ready:
        return False
    if intake.baseline.category.value == "brownfield_multi_repo":
        return fixture.multi_repo_system is not None and fixture.multi_repo_system.ready_for_provider
    return True


def _invoke_provider(fixture: CodingHarnessFixture, context_package: ContextPackage) -> AdapterTwinResult:
    twins = default_adapter_twins()
    if fixture.provider_surface not in twins:
        raise CodingHarnessValidationError(f"unsupported provider surface: {fixture.provider_surface.value}")
    context_refs = tuple(
        item.object.id
        for item in (*context_package.current, *context_package.surfaced)
    )
    return twins[fixture.provider_surface].invoke(
        purpose=fixture.task.prompt,
        input_refs=context_refs,
        output_refs=(f"coding-proof-output://{fixture.fixture_id}",),
        policy_context="mock_coding_proof_harness",
        privacy_classification="project",
        evidence_refs=("docs/INTEGRATION_ARCHITECTURE.md", "docs/ROADMAP.md"),
        confidence=0.74,
        cost_estimate={"unit": "mock", "amount": 0},
        latency_ms=0,
    )


def _stable_invocation_object(provider_result: AdapterTwinResult) -> MemoryObject:
    memory_object = provider_result.to_memory_object(created_by="coding-proof-harness")
    stable = replace(
        memory_object,
        provenance=replace(memory_object.provenance, created_at=CODING_HARNESS_FIXTURE_CREATED_AT),
    )
    validate_memory_object(stable)
    return stable


def _output_candidate(fixture: CodingHarnessFixture, provider_invocation: MemoryObject) -> MemoryObject:
    metadata = {
        "candidate": True,
        "promotion_required": True,
        "source": "coding_proof_harness",
        "task_title": fixture.task.title,
        "task_prompt": fixture.task.prompt,
        "provider_surface": fixture.provider_surface.value,
        "provider_invocation_id": provider_invocation.id,
        "proposed_output": fixture.proposed_output,
    }
    if fixture.multi_repo_system is not None:
        metadata["multi_repo_system"] = fixture.multi_repo_system.as_metadata()
    candidate = MemoryObject(
        id=_deterministic_output_id(fixture),
        type=MemoryObjectType.EVIDENCE_ARTIFACT,
        title=f"Proposed coding output: {fixture.task.title}",
        status=LifecycleStatus.SUBMITTED,
        visibility=Visibility.PROJECT,
        provenance=Provenance(
            source_refs=(f"coding-proof-output://{fixture.fixture_id}",),
            created_by="coding-proof-harness",
            created_at=CODING_HARNESS_FIXTURE_CREATED_AT,
            evidence_level=EvidenceLevel.E2_REVIEWED_SYNTHESIS,
            derivation_refs=(provider_invocation.id,),
        ),
        relationships=(
            Relationship(type=RelationshipType.PRODUCED_BY, target_id=provider_invocation.id),
            Relationship(type=RelationshipType.DERIVED_FROM, target_id=provider_invocation.id),
        ),
        confidence=0.42,
        metadata=metadata,
    )
    validate_memory_object(candidate)
    return candidate


def _deterministic_output_id(fixture: CodingHarnessFixture) -> str:
    seed = (
        f"{CONTRACT_VERSION}:coding-proof-harness:{fixture.fixture_id}:"
        f"{fixture.provider_surface.value}:{fixture.task.title}:{fixture.proposed_output}"
    ).strip().lower()
    digest = sha256(seed.encode("utf-8")).hexdigest()[:16]
    return f"pmem_{MemoryObjectType.EVIDENCE_ARTIFACT.value}_{digest}"


def _required_mapping(payload: Mapping[str, Any], key: str, fixture_path: Path) -> Mapping[str, Any]:
    value = payload.get(key)
    if not isinstance(value, dict):
        raise CodingHarnessValidationError(f"{fixture_path} requires object field: {key}")
    return value


def _parse_multi_repo_system(raw_value: Any, fixture_path: Path) -> MultiRepoSystemContext | None:
    if raw_value is None:
        return None
    if not isinstance(raw_value, dict):
        raise CodingHarnessValidationError(f"{fixture_path} multi_repo_system must be an object")
    return MultiRepoSystemContext(
        repository_map=_parse_repository_map(raw_value.get("repository_map", []), fixture_path),
        relevant_repositories=_string_list(
            raw_value.get("relevant_repositories", []),
            "relevant_repositories",
            fixture_path,
        ),
        out_of_scope_repositories=_string_list(
            raw_value.get("out_of_scope_repositories", []),
            "out_of_scope_repositories",
            fixture_path,
        ),
        service_boundaries=_string_list(raw_value.get("service_boundaries", []), "service_boundaries", fixture_path),
        integration_contracts=_string_list(
            raw_value.get("integration_contracts", []),
            "integration_contracts",
            fixture_path,
        ),
        ownership=_string_list(raw_value.get("ownership", []), "ownership", fixture_path),
        build_test_responsibility=_string_list(
            raw_value.get("build_test_responsibility", []),
            "build_test_responsibility",
            fixture_path,
        ),
        documentation_gaps=_string_list(raw_value.get("documentation_gaps", []), "documentation_gaps", fixture_path),
        authority_path=_string_list(raw_value.get("authority_path", []), "authority_path", fixture_path),
    )


def _parse_repository_map(raw_value: Any, fixture_path: Path) -> tuple[Mapping[str, object], ...]:
    if not isinstance(raw_value, list):
        raise CodingHarnessValidationError(f"{fixture_path} repository_map must be a list")
    repositories: list[Mapping[str, object]] = []
    for item in raw_value:
        if not isinstance(item, dict):
            raise CodingHarnessValidationError(f"{fixture_path} repository_map entries must be objects")
        repo_id = _required_str(item, "id", fixture_path)
        repositories.append(
            {
                "id": repo_id,
                "title": _required_str(item, "title", fixture_path),
                "role": _required_str(item, "role", fixture_path),
                "task_relevant": bool(item.get("task_relevant", False)),
                "reason": item.get("reason") if isinstance(item.get("reason"), str) else "",
            }
        )
    return tuple(repositories)


def _string_list(raw_value: Any, field_name: str, fixture_path: Path) -> tuple[str, ...]:
    if not isinstance(raw_value, list):
        raise CodingHarnessValidationError(f"{fixture_path} {field_name} must be a list")
    if not all(isinstance(item, str) and item.strip() for item in raw_value):
        raise CodingHarnessValidationError(f"{fixture_path} {field_name} must contain only non-empty strings")
    return tuple(raw_value)


def _required_str(payload: Mapping[str, Any], key: str, fixture_path: Path) -> str:
    value = payload.get(key)
    if not isinstance(value, str) or not value.strip():
        raise CodingHarnessValidationError(f"{fixture_path} requires non-empty string field: {key}")
    return value
