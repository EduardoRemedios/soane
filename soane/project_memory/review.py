"""Candidate review and promotion semantics for Project Memory v0.

This module is local, deterministic, and storage-free. It converts candidate
Project Memory objects into reviewed outcomes without mutating the source
candidate.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from enum import StrEnum
from hashlib import sha256
from typing import Mapping

from soane.project_memory.contract import (
    CONTRACT_VERSION,
    EvidenceLevel,
    LifecycleStatus,
    MemoryObject,
    Provenance,
    Relationship,
    RelationshipType,
    validate_memory_object,
)


REVIEW_FIXTURE_REVIEWED_AT = datetime(2026, 7, 1, 15, 0, tzinfo=timezone.utc)


class CandidateReviewError(ValueError):
    """Raised when a candidate review request violates v0 review semantics."""


class ReviewOutcome(StrEnum):
    ACCEPT = "accept"
    REJECT = "reject"
    DEFER = "defer"
    AMEND = "amend"
    KEEP_OPEN = "keep_open"


@dataclass(frozen=True)
class ReviewDecision:
    outcome: ReviewOutcome
    reviewer: str
    rationale: str = ""
    reviewed_at: datetime = REVIEW_FIXTURE_REVIEWED_AT
    amended_title: str | None = None
    authority_ref: str | None = None


@dataclass(frozen=True)
class CandidateReviewResult:
    candidate: MemoryObject
    reviewed_object: MemoryObject
    decision: ReviewDecision


def review_candidate(candidate: MemoryObject, decision: ReviewDecision) -> CandidateReviewResult:
    """Return a reviewed object derived from a candidate memory object."""

    validate_memory_object(candidate)
    _validate_decision(candidate, decision)

    title = decision.amended_title if decision.outcome == ReviewOutcome.AMEND else candidate.title
    assert title is not None
    status = _status_for(decision.outcome)
    relationships = _relationships_for(candidate, decision)
    reviewed = MemoryObject(
        id=_reviewed_object_id(candidate, decision, title),
        type=candidate.type,
        title=title,
        status=status,
        visibility=candidate.visibility,
        provenance=Provenance(
            source_refs=(*candidate.provenance.source_refs, _review_source_ref(candidate, decision)),
            created_by=decision.reviewer,
            created_at=decision.reviewed_at,
            evidence_level=EvidenceLevel.E2_REVIEWED_SYNTHESIS,
            derivation_refs=(candidate.id, *candidate.provenance.derivation_refs),
        ),
        relationships=relationships,
        authority_ref=decision.authority_ref,
        confidence=candidate.confidence,
        metadata=_review_metadata(candidate.metadata, candidate.id, decision),
    )
    validate_memory_object(reviewed)
    return CandidateReviewResult(candidate=candidate, reviewed_object=reviewed, decision=decision)


def is_candidate_object(memory_object: MemoryObject) -> bool:
    """Return whether a memory object is explicitly marked as a candidate."""

    return bool(memory_object.metadata.get("candidate")) or bool(memory_object.metadata.get("promotion_required"))


def _validate_decision(candidate: MemoryObject, decision: ReviewDecision) -> None:
    if not is_candidate_object(candidate):
        raise CandidateReviewError("review requires a candidate object")
    if not decision.reviewer.strip():
        raise CandidateReviewError("reviewer is required")
    if decision.reviewed_at.tzinfo is None:
        raise CandidateReviewError("reviewed_at must be timezone-aware")
    if decision.outcome in {ReviewOutcome.ACCEPT, ReviewOutcome.REJECT, ReviewOutcome.DEFER, ReviewOutcome.AMEND}:
        if not decision.rationale.strip():
            raise CandidateReviewError(f"rationale is required for {decision.outcome.value}")
    if decision.outcome == ReviewOutcome.AMEND and not (decision.amended_title and decision.amended_title.strip()):
        raise CandidateReviewError("amended_title is required for amend")
    if decision.outcome != ReviewOutcome.AMEND and decision.amended_title is not None:
        raise CandidateReviewError("amended_title is only valid for amend")
    if decision.outcome in {ReviewOutcome.ACCEPT, ReviewOutcome.AMEND}:
        if candidate.metadata.get("requires_authority") and not decision.authority_ref:
            raise CandidateReviewError("authority_ref is required to promote this candidate")


def _status_for(outcome: ReviewOutcome) -> LifecycleStatus:
    if outcome in {ReviewOutcome.ACCEPT, ReviewOutcome.AMEND}:
        return LifecycleStatus.ACCEPTED
    if outcome == ReviewOutcome.REJECT:
        return LifecycleStatus.REJECTED
    if outcome == ReviewOutcome.DEFER:
        return LifecycleStatus.DEFERRED
    if outcome == ReviewOutcome.KEEP_OPEN:
        return LifecycleStatus.OPEN
    raise CandidateReviewError(f"unsupported review outcome: {outcome.value}")


def _relationships_for(candidate: MemoryObject, decision: ReviewDecision) -> tuple[Relationship, ...]:
    relationships = [
        *candidate.relationships,
        Relationship(type=RelationshipType.DERIVED_FROM, target_id=candidate.id),
    ]
    if decision.authority_ref:
        relationships.append(Relationship(type=RelationshipType.HAS_AUTHORITY, target_id=decision.authority_ref))
    return tuple(relationships)


def _review_metadata(
    candidate_metadata: Mapping[str, object],
    candidate_id: str,
    decision: ReviewDecision,
) -> Mapping[str, object]:
    metadata = dict(candidate_metadata)
    metadata.update(
        {
            "candidate": False,
            "promotion_required": False,
            "review_outcome": decision.outcome.value,
            "review_rationale": decision.rationale,
            "reviewed_by": decision.reviewer,
            "original_candidate_id": candidate_id,
        }
    )
    if decision.amended_title is not None:
        metadata["amended_title"] = decision.amended_title
    if decision.authority_ref is not None:
        metadata["authority_ref"] = decision.authority_ref
    return metadata


def _reviewed_object_id(candidate: MemoryObject, decision: ReviewDecision, title: str) -> str:
    seed = (
        f"{CONTRACT_VERSION}:candidate-review:{candidate.id}:"
        f"{decision.outcome.value}:{title}:{decision.reviewer}:{decision.rationale}:"
        f"{decision.authority_ref or ''}"
    ).strip().lower()
    digest = sha256(seed.encode("utf-8")).hexdigest()[:16]
    return f"pmem_{candidate.type.value}_{digest}"


def _review_source_ref(candidate: MemoryObject, decision: ReviewDecision) -> str:
    seed = f"{candidate.id}:{decision.outcome.value}:{decision.reviewer}:{decision.rationale}".strip().lower()
    digest = sha256(seed.encode("utf-8")).hexdigest()[:16]
    return f"candidate-review://{digest}"
