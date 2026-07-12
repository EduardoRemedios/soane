"""Project Memory v0 object contract.

This module is intentionally small and storage-neutral. It defines the
minimum vocabulary, required fields, lifecycle transitions, and deterministic
fixture ID convention that later memory services, fixtures, CLI commands, and
TUI views must wrap.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import StrEnum
from hashlib import sha256
from typing import Mapping, Sequence


CONTRACT_VERSION = "project-memory-v0"


class ContractValidationError(ValueError):
    """Raised when a Project Memory object violates the v0 contract."""


class MemoryObjectType(StrEnum):
    PROJECT = "project"
    CONVERSATION = "conversation"
    CLAIM = "claim"
    QUESTION = "question"
    ASSUMPTION = "assumption"
    HYPOTHESIS = "hypothesis"
    CONSTRAINT = "constraint"
    DECISION = "decision"
    EVIDENCE_ARTIFACT = "evidence_artifact"
    VERIFICATION = "verification"
    MISSION_REFERENCE = "mission_reference"
    AUTHORITY_REFERENCE = "authority_reference"
    CAPABILITY_REFERENCE = "capability_reference"
    RESEARCH_FINDING = "research_finding"
    OPERATIONAL_LEARNING = "operational_learning"
    CANONICAL_KNOWLEDGE_ARTIFACT = "canonical_knowledge_artifact"
    PROVIDER_INVOCATION = "provider_invocation"


class LifecycleStatus(StrEnum):
    PROPOSED = "proposed"
    ACTIVE = "active"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    SUPERSEDED = "superseded"
    INVALIDATED = "invalidated"
    RETIRED = "retired"
    ARCHIVED = "archived"
    OPEN = "open"
    UNDER_INVESTIGATION = "under_investigation"
    ANSWERED = "answered"
    DEFERRED = "deferred"
    BLOCKED = "blocked"
    SUBMITTED = "submitted"
    REVIEWED = "reviewed"
    CHALLENGED = "challenged"
    STALE = "stale"
    REVOKED = "revoked"
    AMENDED = "amended"


class EvidenceLevel(StrEnum):
    E0_STATED_INTENT = "E0"
    E1_SOURCE_REFERENCE = "E1"
    E2_REVIEWED_SYNTHESIS = "E2"
    E3_MECHANICAL_VERIFICATION = "E3"
    E4_RUNTIME_OR_MISSION_EVIDENCE = "E4"
    E5_AUTHORITY_OR_PROOF_REFERENCE = "E5"


class Visibility(StrEnum):
    PUBLIC = "public"
    PROJECT = "project"
    RESTRICTED = "restricted"
    SUPPRESSED = "suppressed"


class RelationshipType(StrEnum):
    CONTAINS = "contains"
    REFERENCES = "references"
    SUPPORTS = "supports"
    CHALLENGES = "challenges"
    DEPENDS_ON = "depends_on"
    SUPERSEDES = "supersedes"
    INVALIDATES = "invalidates"
    DERIVED_FROM = "derived_from"
    EVIDENCES = "evidences"
    HAS_CAPABILITY = "has_capability"
    HAS_AUTHORITY = "has_authority"
    PRODUCED_BY = "produced_by"
    BLOCKS = "blocks"
    ANSWERS = "answers"
    CONTRADICTS = "contradicts"
    MAPS_TO = "maps_to"


MEMORY_OBJECT_TYPES = frozenset(item.value for item in MemoryObjectType)
EVIDENCE_LEVELS = frozenset(item.value for item in EvidenceLevel)
RELATIONSHIP_TYPES = frozenset(item.value for item in RelationshipType)

LIFECYCLE_TRANSITIONS: Mapping[LifecycleStatus, frozenset[LifecycleStatus]] = {
    LifecycleStatus.PROPOSED: frozenset(
        {
            LifecycleStatus.ACTIVE,
            LifecycleStatus.ACCEPTED,
            LifecycleStatus.REJECTED,
            LifecycleStatus.DEFERRED,
        }
    ),
    LifecycleStatus.ACTIVE: frozenset(
        {
            LifecycleStatus.ACCEPTED,
            LifecycleStatus.SUPERSEDED,
            LifecycleStatus.INVALIDATED,
            LifecycleStatus.RETIRED,
            LifecycleStatus.STALE,
        }
    ),
    LifecycleStatus.ACCEPTED: frozenset(
        {
            LifecycleStatus.AMENDED,
            LifecycleStatus.SUPERSEDED,
            LifecycleStatus.INVALIDATED,
            LifecycleStatus.RETIRED,
            LifecycleStatus.STALE,
        }
    ),
    LifecycleStatus.AMENDED: frozenset(
        {
            LifecycleStatus.ACCEPTED,
            LifecycleStatus.SUPERSEDED,
            LifecycleStatus.INVALIDATED,
            LifecycleStatus.RETIRED,
        }
    ),
    LifecycleStatus.OPEN: frozenset(
        {
            LifecycleStatus.UNDER_INVESTIGATION,
            LifecycleStatus.ANSWERED,
            LifecycleStatus.DEFERRED,
            LifecycleStatus.BLOCKED,
        }
    ),
    LifecycleStatus.UNDER_INVESTIGATION: frozenset(
        {
            LifecycleStatus.ANSWERED,
            LifecycleStatus.DEFERRED,
            LifecycleStatus.BLOCKED,
            LifecycleStatus.OPEN,
        }
    ),
    LifecycleStatus.SUBMITTED: frozenset(
        {
            LifecycleStatus.REVIEWED,
            LifecycleStatus.ACCEPTED,
            LifecycleStatus.CHALLENGED,
            LifecycleStatus.STALE,
            LifecycleStatus.REVOKED,
        }
    ),
    LifecycleStatus.REVIEWED: frozenset(
        {
            LifecycleStatus.ACCEPTED,
            LifecycleStatus.CHALLENGED,
            LifecycleStatus.STALE,
            LifecycleStatus.REVOKED,
        }
    ),
}

GOVERNED_INVARIANTS: Mapping[str, str] = {
    "scope": "Direct lookup, search, and context assembly enforce the same visibility constraints.",
    "time": "Stale, superseded, invalidated, and revoked records remain inspectable without becoming current truth.",
    "provenance": "Promoted claims retain source, writer, time, evidence level, and derivation lineage.",
    "propagation": "Context assembly controls memory crossing task, actor, project, and adapter boundaries.",
    "resolution": "Contradictions remain explicit until reviewed and are not flattened by deduplication.",
}


@dataclass(frozen=True)
class Provenance:
    source_refs: tuple[str, ...]
    created_by: str
    created_at: datetime
    evidence_level: EvidenceLevel
    derivation_refs: tuple[str, ...] = ()


@dataclass(frozen=True)
class Relationship:
    type: RelationshipType
    target_id: str
    evidence_ids: tuple[str, ...] = ()


@dataclass(frozen=True)
class MemoryObject:
    id: str
    type: MemoryObjectType
    title: str
    status: LifecycleStatus
    provenance: Provenance
    visibility: Visibility
    relationships: tuple[Relationship, ...] = ()
    updated_at: datetime | None = None
    supersedes: tuple[str, ...] = ()
    superseded_by: tuple[str, ...] = ()
    authority_ref: str | None = None
    confidence: float | None = None
    metadata: Mapping[str, object] = field(default_factory=dict)


def deterministic_fixture_id(fixture_id: str, object_type: MemoryObjectType, title: str) -> str:
    """Return a stable fixture object ID for contract and fixture tests."""

    seed = f"{CONTRACT_VERSION}:{fixture_id}:{object_type.value}:{title}".strip().lower()
    digest = sha256(seed.encode("utf-8")).hexdigest()[:16]
    return f"pmem_{object_type.value}_{digest}"


def validate_memory_object(memory_object: MemoryObject) -> None:
    """Validate common Project Memory v0 contract invariants."""

    _require(memory_object.id.startswith(f"pmem_{memory_object.type.value}_"), "id prefix does not match object type")
    _require(memory_object.title.strip(), "title is required")
    _require(memory_object.provenance.created_by.strip(), "provenance.created_by is required")
    _require(memory_object.provenance.source_refs, "at least one provenance source_ref is required")
    _require(
        memory_object.provenance.created_at.tzinfo is not None,
        "provenance.created_at must be timezone-aware",
    )
    if memory_object.updated_at is not None:
        _require(memory_object.updated_at.tzinfo is not None, "updated_at must be timezone-aware")
        _require(memory_object.updated_at >= memory_object.provenance.created_at, "updated_at precedes created_at")
    if memory_object.status in {LifecycleStatus.SUPERSEDED, LifecycleStatus.INVALIDATED}:
        _require(
            bool(memory_object.supersedes or memory_object.superseded_by or memory_object.relationships),
            "superseded or invalidated objects require relationship history",
        )
    if memory_object.type == MemoryObjectType.CAPABILITY_REFERENCE:
        _require(
            memory_object.authority_ref is None,
            "capability reference must not embed authority; use an Authority Reference relationship",
        )
    if memory_object.type == MemoryObjectType.CLAIM:
        _validate_claim(memory_object)
    if memory_object.confidence is not None:
        _require(0.0 <= memory_object.confidence <= 1.0, "confidence must be between 0 and 1")
    for relationship in memory_object.relationships:
        _require(relationship.target_id.strip(), "relationship.target_id is required")


def can_transition(from_status: LifecycleStatus, to_status: LifecycleStatus) -> bool:
    """Return whether a lifecycle transition is allowed by the v0 contract."""

    return to_status in LIFECYCLE_TRANSITIONS.get(from_status, frozenset())


def utc_now() -> datetime:
    """Return a timezone-aware UTC timestamp."""

    return datetime.now(timezone.utc)


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ContractValidationError(message)


def _validate_claim(memory_object: MemoryObject) -> None:
    metadata = memory_object.metadata
    required_strings = (
        "proposition",
        "source_path",
        "heading_path",
        "anchor_key",
        "occurrence_id",
        "block_fingerprint",
        "document_fingerprint",
        "markdown_role",
        "authority_mode",
        "source_authority",
        "knowledge_scope",
        "epistemic_status",
        "extraction_method",
        "source_snapshot_version",
    )
    for key in required_strings:
        value = metadata.get(key)
        _require(isinstance(value, str) and bool(value.strip()), f"claim metadata.{key} is required")

    _require(metadata["proposition"] == memory_object.title, "claim proposition must match title")

    start_line = metadata.get("start_line")
    end_line = metadata.get("end_line")
    _require(type(start_line) is int and start_line > 0, "claim metadata.start_line must be positive")
    _require(type(end_line) is int and end_line >= start_line, "claim metadata.end_line precedes start_line")
    _require(metadata["knowledge_scope"] == "project", "claim knowledge_scope must be project in v0")
    _require(
        metadata["markdown_role"]
        in {"constitutional", "canonical", "working", "generated", "evidence", "deprecated"},
        "claim markdown_role is invalid",
    )
    _require(
        metadata["authority_mode"] in {"authored_authority", "generated_projection", "curated_round_trip"},
        "claim authority_mode is invalid",
    )
    for key in ("block_fingerprint", "document_fingerprint"):
        value = str(metadata[key])
        _require(len(value) == 64 and all(char in "0123456789abcdef" for char in value), f"claim {key} is invalid")
    _require(metadata["source_path"] in memory_object.provenance.source_refs, "claim source_path must be a source_ref")

    is_candidate = bool(metadata.get("candidate")) or bool(metadata.get("promotion_required"))
    if is_candidate:
        _require(metadata.get("candidate") is True, "claim candidate flag must be true")
        _require(metadata.get("promotion_required") is True, "claim promotion_required flag must be true")
        _require(memory_object.status == LifecycleStatus.PROPOSED, "claim candidate status must be proposed")
        _require(memory_object.visibility == Visibility.PROJECT, "claim candidate visibility must be project")
        _require(
            memory_object.provenance.evidence_level == EvidenceLevel.E1_SOURCE_REFERENCE,
            "claim candidate evidence level must be E1",
        )
        _require(metadata["epistemic_status"] == "asserted", "claim candidate epistemic_status must be asserted")
        _require(memory_object.authority_ref is None, "claim candidate must not embed authority")
