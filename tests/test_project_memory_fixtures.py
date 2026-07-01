from __future__ import annotations

import unittest
from pathlib import Path

from soane.project_memory.contract import (
    LifecycleStatus,
    MemoryObjectType,
    RelationshipType,
    Visibility,
    deterministic_fixture_id,
)
from soane.project_memory.fixtures import load_fixtures


FIXTURE_DIR = Path(__file__).parent / "fixtures" / "project_memory" / "golden"


class ProjectMemoryFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixtures = load_fixtures(FIXTURE_DIR)
        cls.by_id = {fixture.fixture_id: fixture for fixture in cls.fixtures}

    def test_all_required_golden_fixtures_exist(self) -> None:
        self.assertEqual({f"GF-{index:03d}" for index in range(1, 13)}, set(self.by_id))

    def test_fixture_object_ids_are_deterministic(self) -> None:
        for fixture in self.fixtures:
            for memory_object in fixture.objects.values():
                expected = deterministic_fixture_id(fixture.fixture_id, memory_object.type, memory_object.title)
                self.assertEqual(expected, memory_object.id)

    def test_fixture_relationships_resolve_to_fixture_objects_or_external_refs(self) -> None:
        for fixture in self.fixtures:
            local_ids = {memory_object.id for memory_object in fixture.objects.values()}
            for memory_object in fixture.objects.values():
                for relationship in memory_object.relationships:
                    self.assertTrue(
                        relationship.target_id in local_ids or relationship.target_id.startswith("external_"),
                        f"{fixture.fixture_id} unresolved relationship target {relationship.target_id}",
                    )

    def test_decision_linked_to_evidence_fixture(self) -> None:
        fixture = self.by_id["GF-001"]
        decision = fixture.objects["decision"]
        evidence = fixture.objects["evidence"]
        self.assertEqual(MemoryObjectType.DECISION, decision.type)
        self.assertIn(
            evidence.id,
            [relationship.target_id for relationship in decision.relationships if relationship.type == RelationshipType.EVIDENCES],
        )

    def test_capability_without_authority_fixture(self) -> None:
        capability = self.by_id["GF-007"].objects["capability"]
        self.assertEqual(MemoryObjectType.CAPABILITY_REFERENCE, capability.type)
        self.assertIsNone(capability.authority_ref)
        self.assertFalse(capability.metadata["authority_present"])

    def test_visibility_and_suppression_fixtures(self) -> None:
        self.assertEqual(Visibility.SUPPRESSED, self.by_id["GF-008"].objects["suppressed_note"].visibility)
        self.assertEqual(Visibility.RESTRICTED, self.by_id["GF-009"].objects["restricted_decision"].visibility)

    def test_superseded_fixture_records_history(self) -> None:
        old_decision = self.by_id["GF-010"].objects["old_decision"]
        self.assertEqual(LifecycleStatus.SUPERSEDED, old_decision.status)
        self.assertTrue(old_decision.superseded_by)

    def test_provider_invocation_fixture_is_mocked(self) -> None:
        invocation = self.by_id["GF-006"].objects["invocation"]
        self.assertEqual(MemoryObjectType.PROVIDER_INVOCATION, invocation.type)
        self.assertTrue(invocation.metadata["mock"])
        self.assertEqual("codex_cli", invocation.metadata["provider"])


if __name__ == "__main__":
    unittest.main()

