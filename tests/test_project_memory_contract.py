from __future__ import annotations

import unittest
from datetime import datetime, timezone

from soane.project_memory.contract import (
    EVIDENCE_LEVELS,
    GOVERNED_INVARIANTS,
    MEMORY_OBJECT_TYPES,
    RELATIONSHIP_TYPES,
    ContractValidationError,
    EvidenceLevel,
    LifecycleStatus,
    MemoryObject,
    MemoryObjectType,
    Provenance,
    Relationship,
    RelationshipType,
    Visibility,
    can_transition,
    deterministic_fixture_id,
    validate_memory_object,
)


class ProjectMemoryContractTests(unittest.TestCase):
    def test_contract_declares_required_object_types(self) -> None:
        expected = {
            "project",
            "conversation",
            "question",
            "assumption",
            "hypothesis",
            "constraint",
            "decision",
            "evidence_artifact",
            "verification",
            "mission_reference",
            "authority_reference",
            "capability_reference",
            "research_finding",
            "operational_learning",
            "canonical_knowledge_artifact",
            "provider_invocation",
        }
        self.assertTrue(expected.issubset(MEMORY_OBJECT_TYPES))

    def test_contract_declares_required_governed_invariants(self) -> None:
        self.assertEqual(
            {"scope", "time", "provenance", "propagation", "resolution"},
            set(GOVERNED_INVARIANTS),
        )

    def test_contract_declares_evidence_and_relationship_vocabularies(self) -> None:
        self.assertEqual({"E0", "E1", "E2", "E3", "E4", "E5"}, EVIDENCE_LEVELS)
        self.assertIn("evidences", RELATIONSHIP_TYPES)
        self.assertIn("has_capability", RELATIONSHIP_TYPES)
        self.assertIn("has_authority", RELATIONSHIP_TYPES)
        self.assertIn("contradicts", RELATIONSHIP_TYPES)

    def test_deterministic_fixture_id_is_stable_and_typed(self) -> None:
        first = deterministic_fixture_id("GF-001", MemoryObjectType.DECISION, "Accept local v0")
        second = deterministic_fixture_id("GF-001", MemoryObjectType.DECISION, "Accept local v0")
        self.assertEqual(first, second)
        self.assertTrue(first.startswith("pmem_decision_"))

    def test_validate_memory_object_accepts_decision_linked_to_evidence(self) -> None:
        created_at = datetime(2026, 7, 1, tzinfo=timezone.utc)
        decision = MemoryObject(
            id=deterministic_fixture_id("GF-001", MemoryObjectType.DECISION, "Accept local v0"),
            type=MemoryObjectType.DECISION,
            title="Accept local v0",
            status=LifecycleStatus.ACCEPTED,
            visibility=Visibility.PROJECT,
            provenance=Provenance(
                source_refs=("docs/ROADMAP.md",),
                created_by="human-review",
                created_at=created_at,
                evidence_level=EvidenceLevel.E2_REVIEWED_SYNTHESIS,
            ),
            relationships=(
                Relationship(
                    type=RelationshipType.EVIDENCES,
                    target_id="pmem_evidence_artifact_1234567890abcdef",
                ),
            ),
        )
        validate_memory_object(decision)

    def test_capability_reference_cannot_embed_authority(self) -> None:
        capability = MemoryObject(
            id=deterministic_fixture_id("GF-007", MemoryObjectType.CAPABILITY_REFERENCE, "Codex CLI can edit files"),
            type=MemoryObjectType.CAPABILITY_REFERENCE,
            title="Codex CLI can edit files",
            status=LifecycleStatus.ACCEPTED,
            visibility=Visibility.PROJECT,
            provenance=Provenance(
                source_refs=("docs/INTEGRATION_ARCHITECTURE.md",),
                created_by="contract-test",
                created_at=datetime(2026, 7, 1, tzinfo=timezone.utc),
                evidence_level=EvidenceLevel.E1_SOURCE_REFERENCE,
            ),
            authority_ref="auth-should-not-be-embedded",
        )
        with self.assertRaises(ContractValidationError):
            validate_memory_object(capability)

    def test_lifecycle_transition_rules_are_explicit(self) -> None:
        self.assertTrue(can_transition(LifecycleStatus.PROPOSED, LifecycleStatus.ACCEPTED))
        self.assertTrue(can_transition(LifecycleStatus.ACCEPTED, LifecycleStatus.SUPERSEDED))
        self.assertFalse(can_transition(LifecycleStatus.REJECTED, LifecycleStatus.ACCEPTED))


if __name__ == "__main__":
    unittest.main()

