from __future__ import annotations

import unittest
from dataclasses import replace
from pathlib import Path

from soane.project_memory.contract import LifecycleStatus, MemoryObjectType, validate_memory_object
from soane.project_memory.context import ContextRequest, build_context_package
from soane.project_memory.review import ReviewDecision, ReviewOutcome, is_candidate_object, review_candidate
from soane.project_memory.semantics import PROJECT_READER, ProjectMemory
from soane.thinking_engine.discovery import (
    DiscoveryStopCondition,
    QuestionSourceKind,
    capture_answer,
    determine_stop_condition,
    start_discovery_session,
)
from soane.thinking_engine.intake import (
    IntakeCategory,
    ReadinessAssessment,
    ReadinessState,
    assess_intake,
    load_intake_fixtures,
)


FIXTURE_DIR = Path(__file__).parent / "fixtures" / "thinking_engine" / "intake"


class ThinkingEngineDiscoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixtures = load_intake_fixtures(FIXTURE_DIR)
        cls.assessments = {
            fixture.fixture_id: assess_intake(fixture)
            for fixture in cls.fixtures
        }
        cls.sessions = {
            fixture_id: start_discovery_session(assessment)
            for fixture_id, assessment in cls.assessments.items()
        }

    def test_discovery_sessions_cover_required_context_types(self) -> None:
        categories = {session.baseline.category for session in self.sessions.values()}
        self.assertEqual(
            {
                IntakeCategory.GREENFIELD,
                IntakeCategory.BROWNFIELD_SINGLE_REPO,
                IntakeCategory.BROWNFIELD_MULTI_REPO,
                IntakeCategory.NON_REPOSITORY_CONTEXT,
            },
            categories,
        )
        self.assertEqual(DiscoveryStopCondition.BLOCKED, self.sessions["TEI-GF-005"].stop_condition)
        self.assertFalse(any(session.live_call_performed for session in self.sessions.values()))

    def test_every_question_has_a_source_reason_and_candidate(self) -> None:
        for session in self.sessions.values():
            self.assertTrue(session.questions)
            for question in session.questions:
                self.assertTrue(question.source_reason)
                self.assertTrue(question.source_ref)
                self.assertTrue(is_candidate_object(question.candidate))
                self.assertEqual(MemoryObjectType.QUESTION, question.candidate.type)
                self.assertEqual(LifecycleStatus.OPEN, question.candidate.status)
                self.assertEqual(question.source_reason, question.candidate.metadata["question_source_reason"])
                validate_memory_object(question.candidate)

    def test_playbook_references_influence_question_selection(self) -> None:
        for fixture_id, assessment in self.assessments.items():
            session = self.sessions[fixture_id]
            playbook_question_ids = {
                question.playbook_id
                for question in session.questions
                if question.source_kind == QuestionSourceKind.PLAYBOOK_PROMPT
            }
            self.assertEqual(
                {playbook.id for playbook in assessment.playbooks},
                playbook_question_ids,
            )

    def test_answer_capture_produces_project_memory_candidate_not_truth(self) -> None:
        session = self.sessions["TEI-GF-001"]
        answered = capture_answer(
            session,
            session.questions[0].id,
            "The founding documents will be drafted and reviewed by the project owner.",
            answered_by="project-owner",
        )
        answer = answered.answers[0]

        self.assertTrue(is_candidate_object(answer.candidate))
        self.assertEqual(MemoryObjectType.EVIDENCE_ARTIFACT, answer.candidate.type)
        self.assertEqual(LifecycleStatus.SUBMITTED, answer.candidate.status)
        self.assertIn(session.questions[0].source_ref, answer.candidate.provenance.source_refs)
        self.assertEqual(answer.answer_text, answer.candidate.metadata["answer_text"])

        memory = ProjectMemory(answered.memory_candidates)
        package = build_context_package(
            memory,
            ContextRequest(purpose="socratic answer candidate proof", access=PROJECT_READER),
        )
        self.assertEqual((), memory.current_objects(PROJECT_READER))
        self.assertEqual((), package.current)

    def test_hypothesis_generation_preserves_uncertainty_and_evidence_gaps(self) -> None:
        session = self.sessions["TEI-GF-002"]
        answered = capture_answer(
            session,
            session.questions[0].id,
            "Deployment checks are documented in the release runbook.",
        )
        hypothesis = answered.hypotheses[0]

        self.assertTrue(is_candidate_object(hypothesis.candidate))
        self.assertEqual(MemoryObjectType.HYPOTHESIS, hypothesis.candidate.type)
        self.assertEqual(LifecycleStatus.PROPOSED, hypothesis.candidate.status)
        self.assertEqual("unverified_answer", hypothesis.uncertainty_state)
        self.assertEqual((session.questions[0].source_ref,), hypothesis.evidence_gap_links)
        self.assertEqual("unverified_answer", hypothesis.candidate.metadata["uncertainty_state"])
        self.assertEqual(list(hypothesis.evidence_gap_links), hypothesis.candidate.metadata["evidence_gap_links"])
        validate_memory_object(hypothesis.candidate)

    def test_stop_conditions_distinguish_evidence_authority_blocked_and_ready(self) -> None:
        greenfield = self.sessions["TEI-GF-001"]
        brownfield_ready = self.sessions["TEI-GF-002"]
        blocked = self.sessions["TEI-GF-005"]
        authority_assessment = self._authority_gap_assessment()

        self.assertEqual(DiscoveryStopCondition.NEEDS_EVIDENCE, greenfield.stop_condition)
        self.assertEqual(DiscoveryStopCondition.READY_FOR_PLANNING, brownfield_ready.stop_condition)
        self.assertEqual(DiscoveryStopCondition.BLOCKED, blocked.stop_condition)
        self.assertEqual(
            DiscoveryStopCondition.NEEDS_AUTHORITY,
            determine_stop_condition(authority_assessment.baseline, authority_assessment.readiness.state),
        )

    def test_candidate_review_is_the_only_promotion_path(self) -> None:
        session = self.sessions["TEI-GF-004"]
        answered = capture_answer(
            session,
            session.questions[0].id,
            "The GA4 acquisition dashboard is the evidence source for marginal opportunity.",
        )
        answer_candidate = answered.answers[0].candidate

        memory = ProjectMemory(answered.memory_candidates)
        self.assertEqual((), memory.current_objects(PROJECT_READER))

        reviewed = review_candidate(
            answer_candidate,
            ReviewDecision(
                outcome=ReviewOutcome.ACCEPT,
                reviewer="human-reviewer",
                rationale="Accepted as reviewed discovery evidence for this local fixture.",
            ),
        ).reviewed_object
        reviewed_memory = ProjectMemory((*answered.memory_candidates, reviewed))
        self.assertEqual((reviewed,), reviewed_memory.current_objects(PROJECT_READER))

    def test_discovery_service_is_deterministic_and_connector_free(self) -> None:
        for assessment in self.assessments.values():
            first = start_discovery_session(assessment)
            second = start_discovery_session(assessment)
            self.assertEqual(first, second)
            self.assertFalse(first.live_call_performed)
            answered_first = capture_answer(first, first.questions[0].id, "Stable answer.")
            answered_second = capture_answer(second, second.questions[0].id, "Stable answer.")
            self.assertEqual(answered_first, answered_second)
            self.assertFalse(answered_first.live_call_performed)

    def _authority_gap_assessment(self):
        assessment = self.assessments["TEI-GF-002"]
        baseline = replace(
            assessment.baseline,
            missing_context=("change approval path",),
            constraints=("Feature planning requires explicit approval before execution.",),
        )
        readiness = ReadinessAssessment(
            state=ReadinessState.READY_FOR_DISCOVERY,
            dimensions=assessment.readiness.dimensions,
            blockers=(),
            missing_context=baseline.missing_context,
        )
        return replace(assessment, baseline=baseline, readiness=readiness)


if __name__ == "__main__":
    unittest.main()
