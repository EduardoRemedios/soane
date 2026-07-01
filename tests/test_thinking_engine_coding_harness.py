from __future__ import annotations

import unittest
from pathlib import Path

from soane.project_memory.adapters import AdapterSurface
from soane.project_memory.contract import LifecycleStatus, MemoryObjectType, RelationshipType, validate_memory_object
from soane.project_memory.review import ReviewDecision, ReviewOutcome, is_candidate_object
from soane.project_memory.semantics import PROJECT_READER, ProjectMemory
from soane.thinking_engine.coding_harness import (
    CodingHarnessValidationError,
    load_coding_harness_fixtures,
    review_provider_output,
    run_coding_proof,
)
from soane.thinking_engine.discovery import DiscoveryStopCondition
from soane.thinking_engine.intake import IntakeCategory, ReadinessState


FIXTURE_DIR = Path(__file__).parent / "fixtures" / "coding_proof_harness"


class ThinkingEngineCodingHarnessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixtures = load_coding_harness_fixtures(FIXTURE_DIR)
        cls.by_id = {fixture.fixture_id: fixture for fixture in cls.fixtures}
        cls.results = {
            fixture.fixture_id: run_coding_proof(fixture)
            for fixture in cls.fixtures
        }

    def test_fixture_corpus_covers_greenfield_brownfield_and_blocked_paths(self) -> None:
        self.assertEqual({"CPH-GF-001", "CPH-GF-002", "CPH-GF-003"}, set(self.by_id))
        self.assertEqual(IntakeCategory.GREENFIELD, self.results["CPH-GF-001"].intake.baseline.category)
        self.assertEqual(IntakeCategory.BROWNFIELD_SINGLE_REPO, self.results["CPH-GF-002"].intake.baseline.category)
        self.assertEqual(IntakeCategory.BROWNFIELD_SINGLE_REPO, self.results["CPH-GF-003"].intake.baseline.category)
        self.assertTrue(self.results["CPH-GF-001"].ready_for_provider)
        self.assertTrue(self.results["CPH-GF-002"].ready_for_provider)
        self.assertFalse(self.results["CPH-GF-003"].ready_for_provider)

    def test_harness_composes_existing_services_and_assembles_context(self) -> None:
        result = self.results["CPH-GF-002"]

        self.assertEqual(ReadinessState.READY_FOR_PLANNING, result.intake.readiness.state)
        self.assertEqual(DiscoveryStopCondition.READY_FOR_PLANNING, result.discovery.stop_condition)
        self.assertEqual("coding proof: Plan endpoint change", result.context_package.purpose)
        self.assertEqual("external_adapter_context", result.context_package.boundary)
        self.assertTrue(result.context_package.surfaced)
        self.assertTrue(result.discovery.questions)
        self.assertTrue(result.intake.memory_candidates)

    def test_provider_selection_uses_existing_adapter_twin_vocabulary(self) -> None:
        self.assertEqual(AdapterSurface.CODEX_CLI, self.results["CPH-GF-001"].provider_surface)
        self.assertEqual(AdapterSurface.CURSOR_CLI, self.results["CPH-GF-002"].provider_surface)
        for result in (self.results["CPH-GF-001"], self.results["CPH-GF-002"]):
            self.assertIsNotNone(result.provider_result)
            self.assertIsNotNone(result.provider_invocation)
            assert result.provider_result is not None
            assert result.provider_invocation is not None
            self.assertFalse(result.provider_result.live_call_performed)
            self.assertTrue(result.provider_invocation.metadata["adapter_twin"])
            self.assertTrue(result.provider_invocation.metadata["mock"])
            self.assertFalse(result.provider_invocation.metadata["live_call_performed"])
            self.assertEqual(result.provider_surface.value, result.provider_invocation.metadata["adapter_surface"])

    def test_provider_invocation_preserves_capability_and_authority_separation(self) -> None:
        result = self.results["CPH-GF-001"]
        invocation = result.provider_invocation
        assert invocation is not None

        validate_memory_object(invocation)
        self.assertEqual(MemoryObjectType.PROVIDER_INVOCATION, invocation.type)
        self.assertEqual(LifecycleStatus.ACCEPTED, invocation.status)
        self.assertIsNone(invocation.authority_ref)
        self.assertIsNone(invocation.metadata["authority_ref"])
        self.assertTrue(invocation.metadata["capability_ref"])
        self.assertIn(
            invocation.metadata["capability_ref"],
            [
                relationship.target_id
                for relationship in invocation.relationships
                if relationship.type == RelationshipType.HAS_CAPABILITY
            ],
        )
        self.assertFalse(
            any(relationship.type == RelationshipType.HAS_AUTHORITY for relationship in invocation.relationships)
        )

    def test_provider_output_is_candidate_not_current_truth(self) -> None:
        result = self.results["CPH-GF-002"]
        candidate = result.output_candidate
        assert candidate is not None

        validate_memory_object(candidate)
        self.assertTrue(is_candidate_object(candidate))
        self.assertEqual(MemoryObjectType.EVIDENCE_ARTIFACT, candidate.type)
        self.assertEqual(LifecycleStatus.SUBMITTED, candidate.status)
        self.assertEqual("coding_proof_harness", candidate.metadata["source"])
        self.assertEqual(result.provider_invocation.id, candidate.metadata["provider_invocation_id"])

        memory = ProjectMemory(result.memory_objects)
        self.assertNotIn(candidate, memory.current_objects(PROJECT_READER))

    def test_candidate_review_is_only_promotion_path_for_provider_output(self) -> None:
        result = self.results["CPH-GF-001"]
        candidate = result.output_candidate
        assert candidate is not None

        memory = ProjectMemory(result.memory_objects)
        self.assertNotIn(candidate, memory.current_objects(PROJECT_READER))

        reviewed = review_provider_output(
            result,
            ReviewDecision(
                outcome=ReviewOutcome.ACCEPT,
                reviewer="human-reviewer",
                rationale="Accepted as reviewed coding proof output for this fixture.",
            ),
        ).reviewed_object
        reviewed_memory = ProjectMemory((*result.memory_objects, reviewed))
        self.assertIn(reviewed, reviewed_memory.current_objects(PROJECT_READER))
        self.assertIn(candidate.id, reviewed.provenance.derivation_refs)

    def test_brownfield_blocked_audit_gaps_prevent_provider_invocation(self) -> None:
        result = self.results["CPH-GF-003"]

        self.assertEqual(ReadinessState.BLOCKED, result.intake.readiness.state)
        self.assertEqual(DiscoveryStopCondition.BLOCKED, result.discovery.stop_condition)
        self.assertFalse(result.ready_for_provider)
        self.assertIsNone(result.provider_result)
        self.assertIsNone(result.provider_invocation)
        self.assertIsNone(result.output_candidate)
        with self.assertRaises(CodingHarnessValidationError):
            review_provider_output(
                result,
                ReviewDecision(
                    outcome=ReviewOutcome.ACCEPT,
                    reviewer="human-reviewer",
                    rationale="Should not review absent output.",
                ),
            )

    def test_harness_is_deterministic_and_has_no_live_side_effects(self) -> None:
        for fixture in self.fixtures:
            first = run_coding_proof(fixture)
            second = run_coding_proof(fixture)
            self.assertEqual(first, second)
            self.assertFalse(first.live_call_performed)
            self.assertFalse(first.repository_mutation_performed)


if __name__ == "__main__":
    unittest.main()
