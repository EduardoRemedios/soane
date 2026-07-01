from __future__ import annotations

import unittest
from datetime import datetime, timezone
from pathlib import Path

from soane.project_memory.contract import LifecycleStatus, RelationshipType
from soane.project_memory.fixtures import load_fixtures
from soane.project_memory.semantics import (
    EXTERNAL_ADAPTER,
    PROJECT_READER,
    PROJECT_REVIEWER,
    AccessContext,
    MemorySemanticsError,
    ProjectMemory,
)


FIXTURE_DIR = Path(__file__).parent / "fixtures" / "project_memory" / "golden"


class ProjectMemorySemanticsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixtures = load_fixtures(FIXTURE_DIR)
        cls.memory = ProjectMemory.from_fixtures(cls.fixtures)
        cls.by_fixture = {fixture.fixture_id: fixture for fixture in cls.fixtures}

    def test_decision_evidence_relationship_is_queryable(self) -> None:
        fixture = self.by_fixture["GF-001"]
        decision = fixture.objects["decision"]
        evidence = fixture.objects["evidence"]
        linked = self.memory.evidence_for(decision, PROJECT_READER)
        self.assertEqual((evidence,), linked)

    def test_lifecycle_transition_preserves_provenance(self) -> None:
        fixture = self.by_fixture["GF-001"]
        decision = fixture.objects["decision"]
        memory = ProjectMemory(fixture.objects.values())
        updated_at = datetime(2026, 7, 1, 10, 0, tzinfo=timezone.utc)
        transitioned = memory.transition(decision.id, LifecycleStatus.STALE, updated_at=updated_at)
        self.assertEqual(LifecycleStatus.STALE, transitioned.status)
        self.assertEqual(decision.provenance, transitioned.provenance)
        self.assertEqual(updated_at, transitioned.updated_at)

    def test_invalid_lifecycle_transition_is_rejected(self) -> None:
        fixture = self.by_fixture["GF-001"]
        decision = fixture.objects["decision"]
        memory = ProjectMemory(fixture.objects.values())
        with self.assertRaises(MemorySemanticsError):
            memory.transition(decision.id, LifecycleStatus.PROPOSED)

    def test_restricted_object_is_blocked_for_external_adapter_and_visible_to_reviewer(self) -> None:
        restricted = self.by_fixture["GF-009"].objects["restricted_decision"]
        self.assertIsNone(self.memory.get(restricted.id, EXTERNAL_ADAPTER))
        self.assertEqual(restricted, self.memory.get(restricted.id, PROJECT_REVIEWER))

    def test_suppressed_object_is_not_visible_without_suppressed_audit_scope(self) -> None:
        suppressed = self.by_fixture["GF-008"].objects["suppressed_note"]
        audit = AccessContext(scopes=("suppressed_audit",), include_suppressed=True)
        self.assertIsNone(self.memory.get(suppressed.id, PROJECT_REVIEWER))
        self.assertEqual(suppressed, self.memory.get(suppressed.id, audit))

    def test_stale_and_superseded_records_are_inspectable_but_not_current_truth(self) -> None:
        stale = self.by_fixture["GF-004"].objects["evidence"]
        superseded = self.by_fixture["GF-010"].objects["old_decision"]
        current_ids = {item.id for item in self.memory.current_objects(PROJECT_READER)}
        self.assertEqual(stale, self.memory.inspect(stale.id))
        self.assertEqual(superseded, self.memory.inspect(superseded.id))
        self.assertNotIn(stale.id, current_ids)
        self.assertNotIn(superseded.id, current_ids)

    def test_contradictions_remain_explicit(self) -> None:
        pairs = self.memory.contradictions(PROJECT_READER)
        pair_titles = {tuple(sorted((left.title, right.title))) for left, right in pairs}
        self.assertIn(
            tuple(
                sorted(
                    (
                        "Source A says live adapters should be used first",
                        "Source B says mock-first adapters should be used first",
                    )
                )
            ),
            pair_titles,
        )

    def test_relationship_targets_respect_visibility(self) -> None:
        fixture = self.by_fixture["GF-012"]
        memory = ProjectMemory(fixture.objects.values())
        allowed_question = fixture.objects["allowed_question"]
        restricted_evidence = fixture.objects["restricted_evidence"]
        linked_question = memory.relationship_targets(
            allowed_question,
            RelationshipType.REFERENCES,
            PROJECT_READER,
        )
        linked_reviewer = memory.relationship_targets(
            allowed_question,
            RelationshipType.REFERENCES,
            PROJECT_REVIEWER,
        )
        self.assertEqual((), linked_question)
        self.assertEqual((restricted_evidence,), linked_reviewer)
        self.assertIsNone(memory.get(restricted_evidence.id, EXTERNAL_ADAPTER))


if __name__ == "__main__":
    unittest.main()
