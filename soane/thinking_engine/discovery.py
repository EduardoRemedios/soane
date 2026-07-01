"""Socratic Discovery v0 local semantics.

This module turns Thinking Engine Intake gaps into deterministic discovery
questions and candidate Project Memory objects. It is deliberately local,
storage-free, and connector-free.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from datetime import datetime, timezone
from enum import StrEnum
from hashlib import sha256
from typing import Mapping

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
from soane.thinking_engine.intake import (
    ContextBaseline,
    DiscoveryPlaybook,
    IntakeAssessment,
    ReadinessState,
)


DISCOVERY_FIXTURE_CREATED_AT = datetime(2026, 7, 1, 15, 45, tzinfo=timezone.utc)


class DiscoveryValidationError(ValueError):
    """Raised when Socratic Discovery v0 inputs violate local semantics."""


class DiscoveryStopCondition(StrEnum):
    BLOCKED = "blocked"
    NEEDS_EVIDENCE = "needs_evidence"
    NEEDS_AUTHORITY = "needs_authority"
    READY_FOR_PLANNING = "ready_for_planning"


class QuestionSourceKind(StrEnum):
    MISSING_CONTEXT = "missing_context"
    OPEN_QUESTION = "open_question"
    ASSUMPTION = "assumption"
    CONSTRAINT = "constraint"
    PLAYBOOK_PROMPT = "playbook_prompt"


@dataclass(frozen=True)
class DiscoveryQuestion:
    id: str
    text: str
    source_kind: QuestionSourceKind
    source_ref: str
    source_reason: str
    playbook_id: str | None
    candidate: MemoryObject


@dataclass(frozen=True)
class DiscoveryAnswer:
    question_id: str
    answer_text: str
    answered_by: str
    source_ref: str
    candidate: MemoryObject


@dataclass(frozen=True)
class DiscoveryHypothesis:
    id: str
    title: str
    uncertainty_state: str
    evidence_gap_links: tuple[str, ...]
    candidate: MemoryObject


@dataclass(frozen=True)
class DiscoverySession:
    fixture_id: str
    baseline: ContextBaseline
    playbooks: tuple[DiscoveryPlaybook, ...]
    questions: tuple[DiscoveryQuestion, ...]
    answers: tuple[DiscoveryAnswer, ...]
    hypotheses: tuple[DiscoveryHypothesis, ...]
    stop_condition: DiscoveryStopCondition
    memory_candidates: tuple[MemoryObject, ...]
    live_call_performed: bool = False


def start_discovery_session(assessment: IntakeAssessment) -> DiscoverySession:
    """Start a deterministic discovery session from an intake assessment."""

    questions = generate_questions(assessment.fixture_id, assessment.baseline, assessment.playbooks)
    candidates = tuple(question.candidate for question in questions)
    stop_condition = determine_stop_condition(assessment.baseline, assessment.readiness.state)
    return DiscoverySession(
        fixture_id=assessment.fixture_id,
        baseline=assessment.baseline,
        playbooks=assessment.playbooks,
        questions=questions,
        answers=(),
        hypotheses=(),
        stop_condition=stop_condition,
        memory_candidates=candidates,
        live_call_performed=False,
    )


def generate_questions(
    fixture_id: str,
    baseline: ContextBaseline,
    playbooks: tuple[DiscoveryPlaybook, ...],
) -> tuple[DiscoveryQuestion, ...]:
    """Generate traceable local questions from baseline gaps and playbooks."""

    questions: list[DiscoveryQuestion] = []
    for item in baseline.missing_context:
        questions.append(
            _question(
                fixture_id,
                f"What source will provide {item} for {baseline.project_name}?",
                QuestionSourceKind.MISSING_CONTEXT,
                f"thinking-intake-fixture://{fixture_id}#missing_context:{_anchor(item)}",
                f"missing_context:{item}",
                None,
            )
        )
    for item in baseline.open_questions:
        questions.append(
            _question(
                fixture_id,
                item,
                QuestionSourceKind.OPEN_QUESTION,
                f"thinking-intake-fixture://{fixture_id}#open_question:{_anchor(item)}",
                f"open_question:{item}",
                None,
            )
        )
    for item in baseline.assumptions:
        questions.append(
            _question(
                fixture_id,
                f"What evidence would confirm or challenge this assumption: {item}?",
                QuestionSourceKind.ASSUMPTION,
                f"thinking-intake-fixture://{fixture_id}#assumption:{_anchor(item)}",
                f"assumption:{item}",
                None,
            )
        )
    for item in baseline.constraints:
        questions.append(
            _question(
                fixture_id,
                f"What confirms this constraint and its authority boundary: {item}?",
                QuestionSourceKind.CONSTRAINT,
                f"thinking-intake-fixture://{fixture_id}#constraint:{_anchor(item)}",
                f"constraint:{item}",
                None,
            )
        )
    for playbook in playbooks:
        for source in playbook.required_sources:
            questions.append(
                _question(
                    fixture_id,
                    f"Which {source} source should be reviewed for {playbook.title}?",
                    QuestionSourceKind.PLAYBOOK_PROMPT,
                    f"discovery-playbook://{playbook.id}#required_source:{_anchor(source)}",
                    f"playbook:{playbook.id}:required_source:{source}",
                    playbook.id,
                )
            )
    _validate_questions(questions)
    return tuple(questions)


def capture_answer(
    session: DiscoverySession,
    question_id: str,
    answer_text: str,
    *,
    answered_by: str = "human",
    source_ref: str | None = None,
) -> DiscoverySession:
    """Capture an answer and derive an uncertainty-preserving hypothesis."""

    question = _require_question(session, question_id)
    if not answer_text.strip():
        raise DiscoveryValidationError("answer_text is required")
    if not answered_by.strip():
        raise DiscoveryValidationError("answered_by is required")

    answer_source_ref = source_ref or f"socratic-discovery-answer://{session.fixture_id}/{question_id}"
    answer_candidate = _candidate_object(
        session.fixture_id,
        MemoryObjectType.EVIDENCE_ARTIFACT,
        f"Answer to: {question.text}",
        LifecycleStatus.SUBMITTED,
        (answer_source_ref, question.source_ref),
        {
            "candidate": True,
            "promotion_required": True,
            "source": "socratic_discovery",
            "question_id": question_id,
            "question_text": question.text,
            "answer_text": answer_text,
        },
        relationships=(Relationship(type=RelationshipType.ANSWERS, target_id=question.candidate.id),),
        created_by="socratic-discovery",
    )
    hypothesis = _hypothesis_from_answer(session.fixture_id, question, answer_text, answer_candidate)
    answers = (
        *session.answers,
        DiscoveryAnswer(
            question_id=question_id,
            answer_text=answer_text,
            answered_by=answered_by,
            source_ref=answer_source_ref,
            candidate=answer_candidate,
        ),
    )
    hypotheses = (*session.hypotheses, hypothesis)
    candidates = (*session.memory_candidates, answer_candidate, hypothesis.candidate)
    return replace(
        session,
        answers=answers,
        hypotheses=hypotheses,
        memory_candidates=candidates,
        live_call_performed=False,
    )


def determine_stop_condition(
    baseline: ContextBaseline,
    readiness_state: ReadinessState,
) -> DiscoveryStopCondition:
    """Return the next local discovery state without granting execution authority."""

    if readiness_state == ReadinessState.BLOCKED:
        return DiscoveryStopCondition.BLOCKED
    if _has_authority_gap(baseline):
        return DiscoveryStopCondition.NEEDS_AUTHORITY
    if readiness_state == ReadinessState.READY_FOR_DISCOVERY or baseline.missing_context:
        return DiscoveryStopCondition.NEEDS_EVIDENCE
    return DiscoveryStopCondition.READY_FOR_PLANNING


def _question(
    fixture_id: str,
    text: str,
    source_kind: QuestionSourceKind,
    source_ref: str,
    source_reason: str,
    playbook_id: str | None,
) -> DiscoveryQuestion:
    candidate = _candidate_object(
        fixture_id,
        MemoryObjectType.QUESTION,
        text,
        LifecycleStatus.OPEN,
        (source_ref,),
        {
            "candidate": True,
            "promotion_required": True,
            "source": "socratic_discovery",
            "question_source_kind": source_kind.value,
            "question_source_reason": source_reason,
            "playbook_id": playbook_id,
        },
        created_by="socratic-discovery",
    )
    return DiscoveryQuestion(
        id=candidate.id,
        text=text,
        source_kind=source_kind,
        source_ref=source_ref,
        source_reason=source_reason,
        playbook_id=playbook_id,
        candidate=candidate,
    )


def _hypothesis_from_answer(
    fixture_id: str,
    question: DiscoveryQuestion,
    answer_text: str,
    answer_candidate: MemoryObject,
) -> DiscoveryHypothesis:
    title = f"Hypothesis: {_truncate(answer_text, 96)}"
    evidence_gap_links = (question.source_ref,)
    candidate = _candidate_object(
        fixture_id,
        MemoryObjectType.HYPOTHESIS,
        title,
        LifecycleStatus.PROPOSED,
        (*answer_candidate.provenance.source_refs, question.source_ref),
        {
            "candidate": True,
            "promotion_required": True,
            "source": "socratic_discovery",
            "uncertainty_state": "unverified_answer",
            "evidence_gap_links": list(evidence_gap_links),
            "question_id": question.id,
            "answer_candidate_id": answer_candidate.id,
        },
        relationships=(
            Relationship(type=RelationshipType.DERIVED_FROM, target_id=answer_candidate.id),
            Relationship(type=RelationshipType.DEPENDS_ON, target_id=question.candidate.id),
        ),
        confidence=0.35,
        created_by="socratic-discovery",
    )
    return DiscoveryHypothesis(
        id=candidate.id,
        title=title,
        uncertainty_state="unverified_answer",
        evidence_gap_links=evidence_gap_links,
        candidate=candidate,
    )


def _candidate_object(
    fixture_id: str,
    object_type: MemoryObjectType,
    title: str,
    status: LifecycleStatus,
    source_refs: tuple[str, ...],
    metadata: Mapping[str, object],
    *,
    relationships: tuple[Relationship, ...] = (),
    confidence: float | None = None,
    created_by: str,
) -> MemoryObject:
    candidate = MemoryObject(
        id=_deterministic_candidate_id(fixture_id, object_type, title, metadata),
        type=object_type,
        title=title,
        status=status,
        visibility=Visibility.PROJECT,
        provenance=Provenance(
            source_refs=source_refs,
            created_by=created_by,
            created_at=DISCOVERY_FIXTURE_CREATED_AT,
            evidence_level=EvidenceLevel.E2_REVIEWED_SYNTHESIS,
        ),
        relationships=relationships,
        confidence=confidence,
        metadata=metadata,
    )
    validate_memory_object(candidate)
    return candidate


def _deterministic_candidate_id(
    fixture_id: str,
    object_type: MemoryObjectType,
    title: str,
    metadata: Mapping[str, object],
) -> str:
    discriminator = metadata.get("question_source_reason") or metadata.get("question_id") or metadata.get("answer_candidate_id")
    seed = f"{CONTRACT_VERSION}:socratic-discovery:{fixture_id}:{object_type.value}:{title}:{discriminator or ''}"
    digest = sha256(seed.strip().lower().encode("utf-8")).hexdigest()[:16]
    return f"pmem_{object_type.value}_{digest}"


def _require_question(session: DiscoverySession, question_id: str) -> DiscoveryQuestion:
    for question in session.questions:
        if question.id == question_id:
            return question
    raise DiscoveryValidationError(f"unknown question_id: {question_id}")


def _validate_questions(questions: list[DiscoveryQuestion]) -> None:
    seen: set[str] = set()
    for question in questions:
        if not question.source_reason.strip():
            raise DiscoveryValidationError("question source_reason is required")
        if not question.source_ref.strip():
            raise DiscoveryValidationError("question source_ref is required")
        if question.id in seen:
            raise DiscoveryValidationError(f"duplicate question id: {question.id}")
        seen.add(question.id)


def _has_authority_gap(baseline: ContextBaseline) -> bool:
    authority_terms = ("authority", "approval", "permission")
    texts = (*baseline.missing_context, *baseline.open_questions, *baseline.constraints)
    return any(term in text.lower() for text in texts for term in authority_terms)


def _anchor(text: str) -> str:
    return "-".join(text.strip().lower().replace("/", " ").split())


def _truncate(text: str, limit: int) -> str:
    normalized = " ".join(text.split())
    if len(normalized) <= limit:
        return normalized
    return normalized[: limit - 3].rstrip() + "..."
