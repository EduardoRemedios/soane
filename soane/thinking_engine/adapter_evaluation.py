"""Deterministic documentation-level evaluation of coding adapter surfaces."""

from __future__ import annotations

import copy
import json
from dataclasses import dataclass
from datetime import date
from enum import StrEnum
from pathlib import Path
from typing import Any, Mapping, Sequence

from soane.project_memory.adapters import AdapterSurface, AdapterSurfaceKind


PROFILE_SCHEMA_VERSION = "lcae-profile-v1"
EVALUATION_SCHEMA_VERSION = "lcae-evaluation-v1"
SCORING_VERSION = "lcae-score-v1"
SUPPORTED_SURFACES = frozenset(AdapterSurface)
OFFICIAL_SOURCE_PREFIXES = (
    "https://developers.openai.com/",
    "https://learn.chatgpt.com/",
    "https://openai.github.io/openai-agents-python/",
    "https://cursor.com/",
    "https://docs.cursor.com/",
)


class AdapterEvaluationError(ValueError):
    """Raised when local evaluation inputs violate the locked contract."""


class EvidenceKind(StrEnum):
    OFFICIAL_DOCUMENTATION = "official_documentation"
    LOCALLY_MEASURED = "locally_measured"


class SourceState(StrEnum):
    CURRENT_CONSISTENT = "current_consistent"
    CURRENT_CONTRADICTORY = "current_contradictory"


class FirstProofMode(StrEnum):
    LOCAL_READ_ONLY = "local_read_only"
    MUTATION_CAPABLE = "mutation_capable"
    EXTERNALLY_HOSTED = "externally_hosted"
    LIVE_ONLY = "live_only"


class HardBlocker(StrEnum):
    SOURCE_CONTRADICTION = "source_contradiction"
    SOURCE_REVALIDATION_REQUIRED = "source_revalidation_required"
    HARD_READ_ONLY_UNPROVEN = "hard_read_only_unproven"
    REPOSITORY_SCOPE_UNBOUNDED = "repository_scope_unbounded"
    AUTHORITY_OR_PERMISSION_MISSING = "authority_or_permission_missing"
    TRACE_PRIVACY_UNCLEAR = "trace_privacy_unclear"
    CANDIDATE_REVIEW_BYPASS = "candidate_review_bypass"
    LIVE_ONLY_EVALUATION_REQUIRED = "live_only_evaluation_required"


@dataclass(frozen=True)
class SourceEvidence:
    url: str
    accessed_on: date
    evidence_kind: EvidenceKind
    claims: tuple[str, ...]


@dataclass(frozen=True)
class AdapterProfile:
    schema_version: str
    surface: AdapterSurface
    surface_kind: AdapterSurfaceKind
    sources: tuple[SourceEvidence, ...]
    source_state: SourceState
    invocation_modes: tuple[str, ...]
    authentication_modes: tuple[str, ...]
    authentication_state: str
    capabilities: tuple[str, ...]
    capability_state: str
    requires_authority: bool
    requires_project_permission: bool
    authority_control: str
    project_permission_control: str
    sandbox_state: str
    repository_scope_controls: tuple[str, ...]
    mutation_controls: tuple[str, ...]
    first_proof_mode: FirstProofMode
    structured_output: tuple[str, ...]
    traceability: tuple[str, ...]
    session_identity: tuple[str, ...]
    cost_metadata: str
    latency_metadata: str
    trace_privacy: str
    privacy_controls: tuple[str, ...]
    candidate_review_required: bool
    declared_hard_blockers: tuple[HardBlocker, ...]
    limitations: tuple[str, ...]
    path: Path


@dataclass(frozen=True)
class SurfaceEvaluation:
    profile: AdapterProfile
    eligible: bool
    blockers: tuple[HardBlocker, ...]
    score: int | None
    score_components: Mapping[str, int]


@dataclass(frozen=True)
class AdapterEvaluationResult:
    source_revalidation_date: date
    context: Mapping[str, Any]
    surfaces: tuple[SurfaceEvaluation, ...]
    recommended_surface: AdapterSurface | None
    recommendation_reason: str


SCORE_WEIGHTS = {
    "repository_scope": 20,
    "mutation_control": 25,
    "structured_output": 15,
    "traceability": 15,
    "session_identity": 10,
    "cost_metadata": 5,
    "latency_metadata": 5,
    "privacy_control": 5,
}


def load_adapter_profiles(
    directory: Path | str,
    *,
    required_access_date: date,
) -> tuple[AdapterProfile, ...]:
    """Load exactly one contained profile for every supported surface."""

    root = Path(directory).resolve()
    if not root.is_dir():
        raise AdapterEvaluationError(f"profile directory does not exist: {root}")
    profiles = tuple(
        load_adapter_profile(path, profile_root=root)
        for path in sorted(root.glob("*.json"))
    )
    _validate_profile_set(profiles)
    if not isinstance(required_access_date, date):
        raise AdapterEvaluationError("required_access_date must be a date")
    return tuple(sorted(profiles, key=lambda item: item.surface.value))


def load_adapter_profile(
    path: Path | str,
    *,
    profile_root: Path | str,
) -> AdapterProfile:
    """Load one profile and reject any path outside the explicit profile root."""

    root = Path(profile_root).resolve()
    profile_path = Path(path).resolve()
    if not profile_path.is_relative_to(root):
        raise AdapterEvaluationError(f"profile path escapes profile directory: {profile_path}")
    if not profile_path.is_file():
        raise AdapterEvaluationError(f"profile file does not exist: {profile_path}")
    try:
        payload = json.loads(profile_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise AdapterEvaluationError(f"invalid profile JSON: {profile_path}") from exc
    if not isinstance(payload, dict):
        raise AdapterEvaluationError(f"profile must contain a JSON object: {profile_path}")
    return _profile_from_payload(payload, profile_path)


def evaluate_adapter_profiles(
    profiles: Sequence[AdapterProfile],
    context_payload: Mapping[str, Any],
    *,
    required_access_date: date,
) -> AdapterEvaluationResult:
    """Apply hard gates and then score only eligible documentation profiles."""

    _validate_profile_set(profiles)
    context = _validated_context_payload(context_payload)
    evaluations = tuple(
        _evaluate_surface(profile, required_access_date)
        for profile in sorted(profiles, key=lambda item: item.surface.value)
    )
    eligible = tuple(item for item in evaluations if item.eligible)
    recommended_surface: AdapterSurface | None = None
    reason = "no_eligible_surface"

    if context["selection_state"] == "blocked":
        reason = "context_not_ready"
    elif eligible:
        highest_score = max(item.score or 0 for item in eligible)
        leaders = tuple(item for item in eligible if item.score == highest_score)
        if len(leaders) == 1:
            recommended_surface = leaders[0].profile.surface
            reason = "highest_eligible_score"
        else:
            reason = "top_score_tie"

    return AdapterEvaluationResult(
        source_revalidation_date=required_access_date,
        context=context,
        surfaces=evaluations,
        recommended_surface=recommended_surface,
        recommendation_reason=reason,
    )


def evaluation_result_payload(result: AdapterEvaluationResult) -> dict[str, Any]:
    """Return the stable local JSON contract for an evaluation result."""

    return {
        "ok": True,
        "schema_version": EVALUATION_SCHEMA_VERSION,
        "scoring_version": SCORING_VERSION,
        "evidence_state": {
            "kind": EvidenceKind.OFFICIAL_DOCUMENTATION.value,
            "measured_behavior": False,
            "source_revalidation_date": result.source_revalidation_date.isoformat(),
            "future_live_revalidation_required": True,
        },
        "recommendation": {
            "surface": result.recommended_surface.value if result.recommended_surface else None,
            "reason": result.recommendation_reason,
            "authorizes_live_use": False,
        },
        "surfaces": [_surface_payload(item) for item in result.surfaces],
        "context": copy.deepcopy(dict(result.context)),
        "governance": {
            "candidate_review_required": True,
            "project_memory_write_performed": False,
            "provider_invocation_record_created": False,
        },
        "side_effects": {
            "provider_invocation_performed": False,
            "credential_or_user_state_read": False,
            "network_call_performed": False,
            "repository_mutation_performed": False,
        },
    }


def _profile_from_payload(payload: Mapping[str, Any], path: Path) -> AdapterProfile:
    schema_version = _required_str(payload, "schema_version", path)
    if schema_version != PROFILE_SCHEMA_VERSION:
        raise AdapterEvaluationError(f"{path} unsupported schema_version: {schema_version}")
    try:
        surface = AdapterSurface(_required_str(payload, "surface", path))
        surface_kind = AdapterSurfaceKind(_required_str(payload, "surface_kind", path))
        source_state = SourceState(_required_str(payload, "source_state", path))
        first_proof_mode = FirstProofMode(_required_str(payload, "first_proof_mode", path))
    except ValueError as exc:
        raise AdapterEvaluationError(f"{path} contains an unsupported enum value") from exc
    expected_kind = (
        AdapterSurfaceKind.CLI
        if surface in {AdapterSurface.CODEX_CLI, AdapterSurface.CURSOR_CLI}
        else AdapterSurfaceKind.SDK
    )
    if surface_kind != expected_kind:
        raise AdapterEvaluationError(
            f"{path} surface_kind {surface_kind.value} does not match {surface.value}"
        )

    raw_sources = payload.get("sources")
    if not isinstance(raw_sources, list) or not raw_sources:
        raise AdapterEvaluationError(f"{path} requires non-empty sources")
    sources = tuple(_source_from_payload(item, path) for item in raw_sources)
    raw_blockers = _required_str_list(payload, "hard_blockers", path, allow_empty=True)
    try:
        blockers = tuple(HardBlocker(item) for item in raw_blockers)
    except ValueError as exc:
        raise AdapterEvaluationError(f"{path} contains an unsupported hard blocker") from exc

    candidate_review_required = payload.get("candidate_review_required")
    if not isinstance(candidate_review_required, bool):
        raise AdapterEvaluationError(f"{path} requires boolean candidate_review_required")
    requires_authority = payload.get("requires_authority")
    if not isinstance(requires_authority, bool):
        raise AdapterEvaluationError(f"{path} requires boolean requires_authority")
    requires_project_permission = payload.get("requires_project_permission")
    if not isinstance(requires_project_permission, bool):
        raise AdapterEvaluationError(f"{path} requires boolean requires_project_permission")

    return AdapterProfile(
        schema_version=schema_version,
        surface=surface,
        surface_kind=surface_kind,
        sources=sources,
        source_state=source_state,
        invocation_modes=_required_str_list(payload, "invocation_modes", path),
        authentication_modes=_required_str_list(payload, "authentication_modes", path),
        authentication_state=_required_str(payload, "authentication_state", path),
        capabilities=_required_str_list(payload, "capabilities", path),
        capability_state=_required_str(payload, "capability_state", path),
        requires_authority=requires_authority,
        requires_project_permission=requires_project_permission,
        authority_control=_required_str(payload, "authority_control", path),
        project_permission_control=_required_str(payload, "project_permission_control", path),
        sandbox_state=_required_str(payload, "sandbox_state", path),
        repository_scope_controls=_required_str_list(
            payload, "repository_scope_controls", path, allow_empty=True
        ),
        mutation_controls=_required_str_list(payload, "mutation_controls", path, allow_empty=True),
        first_proof_mode=first_proof_mode,
        structured_output=_required_str_list(payload, "structured_output", path, allow_empty=True),
        traceability=_required_str_list(payload, "traceability", path, allow_empty=True),
        session_identity=_required_str_list(payload, "session_identity", path, allow_empty=True),
        cost_metadata=_required_str(payload, "cost_metadata", path),
        latency_metadata=_required_str(payload, "latency_metadata", path),
        trace_privacy=_required_str(payload, "trace_privacy", path),
        privacy_controls=_required_str_list(payload, "privacy_controls", path, allow_empty=True),
        candidate_review_required=candidate_review_required,
        declared_hard_blockers=blockers,
        limitations=_required_str_list(payload, "limitations", path),
        path=path,
    )


def _source_from_payload(payload: Any, path: Path) -> SourceEvidence:
    if not isinstance(payload, dict):
        raise AdapterEvaluationError(f"{path} source entries must be objects")
    url = _required_str(payload, "url", path)
    if not url.startswith(OFFICIAL_SOURCE_PREFIXES):
        raise AdapterEvaluationError(f"{path} source URL is outside the official allowlist: {url}")
    try:
        accessed_on = date.fromisoformat(_required_str(payload, "accessed_on", path))
        evidence_kind = EvidenceKind(_required_str(payload, "evidence_kind", path))
    except ValueError as exc:
        raise AdapterEvaluationError(f"{path} has invalid source evidence") from exc
    return SourceEvidence(
        url=url,
        accessed_on=accessed_on,
        evidence_kind=evidence_kind,
        claims=_required_str_list(payload, "claims", path),
    )


def _validate_profile_set(profiles: Sequence[AdapterProfile]) -> None:
    if not profiles:
        raise AdapterEvaluationError("no adapter profiles supplied")
    surfaces = tuple(profile.surface for profile in profiles)
    if len(set(surfaces)) != len(surfaces):
        raise AdapterEvaluationError("duplicate adapter surface profile")
    actual = frozenset(surfaces)
    if actual != SUPPORTED_SURFACES:
        missing = sorted(item.value for item in SUPPORTED_SURFACES - actual)
        extra = sorted(item.value for item in actual - SUPPORTED_SURFACES)
        raise AdapterEvaluationError(f"profile set mismatch: missing={missing} extra={extra}")


def _evaluate_surface(profile: AdapterProfile, required_access_date: date) -> SurfaceEvaluation:
    blockers = set(profile.declared_hard_blockers)
    if profile.source_state == SourceState.CURRENT_CONTRADICTORY:
        blockers.add(HardBlocker.SOURCE_CONTRADICTION)
    if any(
        source.accessed_on != required_access_date
        or source.evidence_kind != EvidenceKind.OFFICIAL_DOCUMENTATION
        for source in profile.sources
    ):
        blockers.add(HardBlocker.SOURCE_REVALIDATION_REQUIRED)
    if (
        "read_only_sandbox" not in profile.mutation_controls
        or profile.sandbox_state != "documented_read_only"
        or profile.first_proof_mode == FirstProofMode.MUTATION_CAPABLE
    ):
        blockers.add(HardBlocker.HARD_READ_ONLY_UNPROVEN)
    if not profile.repository_scope_controls:
        blockers.add(HardBlocker.REPOSITORY_SCOPE_UNBOUNDED)
    if (
        not profile.requires_authority
        or not profile.requires_project_permission
        or profile.authority_control != "explicit_external_precondition"
        or profile.project_permission_control != "explicit_external_precondition"
    ):
        blockers.add(HardBlocker.AUTHORITY_OR_PERMISSION_MISSING)
    if profile.trace_privacy == "unclear":
        blockers.add(HardBlocker.TRACE_PRIVACY_UNCLEAR)
    if not profile.candidate_review_required:
        blockers.add(HardBlocker.CANDIDATE_REVIEW_BYPASS)
    if profile.first_proof_mode in {FirstProofMode.EXTERNALLY_HOSTED, FirstProofMode.LIVE_ONLY}:
        blockers.add(HardBlocker.LIVE_ONLY_EVALUATION_REQUIRED)

    ordered_blockers = tuple(sorted(blockers, key=lambda item: item.value))
    if ordered_blockers:
        return SurfaceEvaluation(
            profile=profile,
            eligible=False,
            blockers=ordered_blockers,
            score=None,
            score_components={},
        )
    components = _score_components(profile)
    return SurfaceEvaluation(
        profile=profile,
        eligible=True,
        blockers=(),
        score=sum(components.values()),
        score_components=components,
    )


def _score_components(profile: AdapterProfile) -> dict[str, int]:
    return {
        "repository_scope": SCORE_WEIGHTS["repository_scope"]
        if profile.repository_scope_controls
        else 0,
        "mutation_control": SCORE_WEIGHTS["mutation_control"]
        if "read_only_sandbox" in profile.mutation_controls
        else 0,
        "structured_output": SCORE_WEIGHTS["structured_output"] if profile.structured_output else 0,
        "traceability": SCORE_WEIGHTS["traceability"] if profile.traceability else 0,
        "session_identity": SCORE_WEIGHTS["session_identity"] if profile.session_identity else 0,
        "cost_metadata": SCORE_WEIGHTS["cost_metadata"]
        if profile.cost_metadata != "unavailable"
        else 0,
        "latency_metadata": SCORE_WEIGHTS["latency_metadata"]
        if profile.latency_metadata != "unavailable"
        else 0,
        "privacy_control": SCORE_WEIGHTS["privacy_control"] if profile.privacy_controls else 0,
    }


def _validated_context_payload(payload: Mapping[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, Mapping):
        raise AdapterEvaluationError("context payload must be an object")
    try:
        cloned = json.loads(json.dumps(payload, sort_keys=True))
    except (TypeError, ValueError) as exc:
        raise AdapterEvaluationError("context payload must be JSON serializable") from exc
    if cloned.get("ok") is not True or cloned.get("command") != "agent-context":
        raise AdapterEvaluationError("context payload must be successful agent-context output")
    if cloned.get("selection_state") not in {"ready", "degraded", "blocked"}:
        raise AdapterEvaluationError("context payload has invalid selection_state")
    if cloned.get("refresh_state") not in {"refreshed", "reused", "failed"}:
        raise AdapterEvaluationError("context payload has invalid refresh_state")
    required_shapes = {
        "budgets": dict,
        "graph": dict,
        "memory": dict,
        "documents": list,
        "explanation": list,
    }
    for key, expected_type in required_shapes.items():
        if not isinstance(cloned.get(key), expected_type):
            raise AdapterEvaluationError(f"context payload requires {key} as {expected_type.__name__}")
    return cloned


def _surface_payload(evaluation: SurfaceEvaluation) -> dict[str, Any]:
    profile = evaluation.profile
    return {
        "surface": profile.surface.value,
        "surface_kind": profile.surface_kind.value,
        "eligible": evaluation.eligible,
        "blockers": [item.value for item in evaluation.blockers],
        "score": evaluation.score,
        "score_components": dict(evaluation.score_components),
        "sources": [
            {
                "url": source.url,
                "accessed_on": source.accessed_on.isoformat(),
                "evidence_kind": source.evidence_kind.value,
                "claims": list(source.claims),
            }
            for source in profile.sources
        ],
        "source_state": profile.source_state.value,
        "invocation_modes": list(profile.invocation_modes),
        "authentication": {
            "modes": list(profile.authentication_modes),
            "state": profile.authentication_state,
        },
        "capability": {
            "claims": list(profile.capabilities),
            "state": profile.capability_state,
        },
        "requires_authority": profile.requires_authority,
        "requires_project_permission": profile.requires_project_permission,
        "authority_control": profile.authority_control,
        "project_permission_control": profile.project_permission_control,
        "sandbox_state": profile.sandbox_state,
        "repository_scope_controls": list(profile.repository_scope_controls),
        "mutation_controls": list(profile.mutation_controls),
        "first_proof_mode": profile.first_proof_mode.value,
        "structured_output": list(profile.structured_output),
        "traceability": list(profile.traceability),
        "session_identity": list(profile.session_identity),
        "cost_metadata": profile.cost_metadata,
        "latency_metadata": profile.latency_metadata,
        "trace_privacy": profile.trace_privacy,
        "privacy_controls": list(profile.privacy_controls),
        "candidate_review_required": profile.candidate_review_required,
        "limitations": list(profile.limitations),
    }


def _required_str(payload: Mapping[str, Any], key: str, path: Path) -> str:
    value = payload.get(key)
    if not isinstance(value, str) or not value.strip():
        raise AdapterEvaluationError(f"{path} requires non-empty string field: {key}")
    return value


def _required_str_list(
    payload: Mapping[str, Any],
    key: str,
    path: Path,
    *,
    allow_empty: bool = False,
) -> tuple[str, ...]:
    value = payload.get(key)
    if (
        not isinstance(value, list)
        or (not allow_empty and not value)
        or not all(isinstance(item, str) and item.strip() for item in value)
    ):
        qualifier = "string list" if allow_empty else "non-empty string list"
        raise AdapterEvaluationError(f"{path} requires {qualifier} field: {key}")
    return tuple(value)
