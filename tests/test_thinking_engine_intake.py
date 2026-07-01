from __future__ import annotations

import unittest
from pathlib import Path

from soane.project_memory.contract import LifecycleStatus, MemoryObjectType, validate_memory_object
from soane.thinking_engine.intake import (
    IntakeCategory,
    ReadinessState,
    assess_intake,
    load_intake_fixtures,
)


FIXTURE_DIR = Path(__file__).parent / "fixtures" / "thinking_engine" / "intake"


class ThinkingEngineIntakeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixtures = load_intake_fixtures(FIXTURE_DIR)
        cls.by_id = {fixture.fixture_id: fixture for fixture in cls.fixtures}
        cls.assessments = {
            fixture.fixture_id: assess_intake(fixture)
            for fixture in cls.fixtures
        }

    def test_fixture_corpus_covers_required_intake_categories(self) -> None:
        self.assertEqual(
            {
                "TEI-GF-001",
                "TEI-GF-002",
                "TEI-GF-003",
                "TEI-GF-004",
                "TEI-GF-005",
            },
            set(self.by_id),
        )
        categories = {assessment.baseline.category for assessment in self.assessments.values()}
        self.assertEqual(
            {
                IntakeCategory.GREENFIELD,
                IntakeCategory.BROWNFIELD_SINGLE_REPO,
                IntakeCategory.BROWNFIELD_MULTI_REPO,
                IntakeCategory.NON_REPOSITORY_CONTEXT,
            },
            categories,
        )

    def test_each_fixture_matches_expected_category_readiness_and_playbooks(self) -> None:
        for fixture in self.fixtures:
            assessment = self.assessments[fixture.fixture_id]
            self.assertEqual(fixture.expected_category, assessment.baseline.category)
            self.assertEqual(fixture.expected_readiness, assessment.readiness.state)
            self.assertEqual(
                fixture.expected_playbooks,
                tuple(playbook.id for playbook in assessment.playbooks),
            )

    def test_greenfield_missing_context_requires_discovery_before_planning(self) -> None:
        assessment = self.assessments["TEI-GF-001"]
        self.assertEqual(ReadinessState.READY_FOR_DISCOVERY, assessment.readiness.state)
        self.assertEqual((), assessment.baseline.repositories)
        self.assertEqual(("VISION.md", "CORE_CONCEPTS.md", "ROADMAP.md"), assessment.baseline.missing_context)
        self.assertIn("Who owns the first decision review?", assessment.baseline.open_questions)

    def test_brownfield_single_repo_retains_repo_audit_context(self) -> None:
        assessment = self.assessments["TEI-GF-002"]
        self.assertEqual(IntakeCategory.BROWNFIELD_SINGLE_REPO, assessment.baseline.category)
        self.assertEqual(1, len(assessment.baseline.repositories))
        self.assertEqual(("npm run build",), assessment.baseline.build_commands)
        self.assertEqual(("npm test",), assessment.baseline.test_commands)
        self.assertEqual(("README.md", "ARCHITECTURE.md"), assessment.baseline.canonical_docs)

    def test_brownfield_multi_repo_retains_system_boundary(self) -> None:
        assessment = self.assessments["TEI-GF-003"]
        self.assertEqual(IntakeCategory.BROWNFIELD_MULTI_REPO, assessment.baseline.category)
        self.assertEqual(3, len(assessment.baseline.repositories))
        self.assertEqual("web app, API service, and shared package", assessment.baseline.system_boundary)
        self.assertEqual(
            {"repo-web", "repo-api", "repo-shared"},
            {source.id for source in assessment.baseline.repositories},
        )

    def test_non_repository_context_keeps_external_sources_outside_git(self) -> None:
        assessment = self.assessments["TEI-GF-004"]
        self.assertEqual(IntakeCategory.NON_REPOSITORY_CONTEXT, assessment.baseline.category)
        self.assertEqual((), assessment.baseline.repositories)
        self.assertEqual(
            {"analytics_dashboard", "campaign_asset", "ad_account"},
            {source.type for source in assessment.baseline.external_sources},
        )

    def test_blocked_intake_explains_missing_context_without_score(self) -> None:
        assessment = self.assessments["TEI-GF-005"]
        self.assertEqual(ReadinessState.BLOCKED, assessment.readiness.state)
        self.assertTrue(assessment.readiness.blockers)
        self.assertEqual(assessment.baseline.missing_context, assessment.readiness.missing_context)
        self.assertNotIn("score", assessment.readiness.dimensions)
        self.assertNotIn("readiness_score", assessment.readiness.dimensions)
        self.assertEqual("not_assessed", assessment.readiness.dimensions["authority_status"])

    def test_memory_candidates_are_write_back_candidates_not_accepted_truth(self) -> None:
        for assessment in self.assessments.values():
            self.assertTrue(assessment.memory_candidates)
            for candidate in assessment.memory_candidates:
                validate_memory_object(candidate)
                self.assertTrue(candidate.metadata["candidate"])
                self.assertTrue(candidate.metadata["promotion_required"])
                self.assertNotEqual(LifecycleStatus.ACCEPTED, candidate.status)
                self.assertIn(f"thinking-intake-fixture://{assessment.fixture_id}", candidate.provenance.source_refs)
            self.assertIn(
                MemoryObjectType.PROJECT,
                {candidate.type for candidate in assessment.memory_candidates},
            )

    def test_intake_service_is_deterministic_and_connector_free(self) -> None:
        for fixture in self.fixtures:
            first = assess_intake(fixture)
            second = assess_intake(fixture)
            self.assertFalse(first.live_call_performed)
            self.assertEqual(first.baseline, second.baseline)
            self.assertEqual(first.readiness, second.readiness)
            self.assertEqual(first.memory_candidates, second.memory_candidates)


if __name__ == "__main__":
    unittest.main()
