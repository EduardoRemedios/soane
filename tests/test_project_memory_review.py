from __future__ import annotations

import json
import unittest
from pathlib import Path

from soane.project_memory.context import ContextRequest, build_context_package
from soane.project_memory.contract import (
    EvidenceLevel,
    LifecycleStatus,
    MemoryObject,
    MemoryObjectType,
    Provenance,
    Relationship,
    RelationshipType,
    Visibility,
    deterministic_fixture_id,
    validate_memory_object,
)
from soane.project_memory.review import (
    CandidateReviewError,
    ReviewDecision,
    ReviewOutcome,
    is_candidate_object,
    review_candidate,
)
from soane.project_memory.semantics import PROJECT_READER, PROJECT_REVIEWER, ProjectMemory


FIXTURE_DIR = Path(__file__).parent / "fixtures" / "project_memory" / "review"
REVIEWED_AT_SOURCE = "tests/fixtures/project_memory/review"


class ProjectMemoryReviewTests(unittest.TestCase):
    def test_fixture_corpus_covers_required_review_cases(self) -> None:
        fixture_ids = {
            json.loads(path.read_text(encoding="utf-8"))["fixture_id"]
            for path in sorted(FIXTURE_DIR.glob("CRP-GF-*.json"))
        }
        self.assertEqual({f"CRP-GF-{index:03d}" for index in range(1, 7)}, fixture_ids)

    def test_candidate_requires_explicit_review_before_current_truth(self) -> None:
        candidate = _candidate("CRP-GF-001", "Accept reviewed assumption")
        memory = ProjectMemory([candidate])
        package = build_context_package(
            memory,
            ContextRequest(purpose="candidate review proof", access=PROJECT_READER),
        )

        self.assertTrue(is_candidate_object(candidate))
        self.assertEqual((), memory.current_objects(PROJECT_READER))
        self.assertEqual((), package.current)
        self.assertEqual((candidate.id,), tuple(item.object.id for item in package.surfaced))

    def test_accept_candidate_preserves_original_and_adds_review_provenance(self) -> None:
        candidate = _candidate("CRP-GF-001", "Accept reviewed assumption")
        decision = ReviewDecision(
            outcome=ReviewOutcome.ACCEPT,
            reviewer="human-reviewer",
            rationale="Evidence is sufficient for local truth.",
        )

        result = review_candidate(candidate, decision)
        reviewed = result.reviewed_object
        memory = ProjectMemory([candidate, reviewed])

        self.assertEqual(LifecycleStatus.PROPOSED, candidate.status)
        self.assertEqual(LifecycleStatus.ACCEPTED, reviewed.status)
        self.assertEqual((reviewed,), memory.current_objects(PROJECT_READER))
        self.assertIn(candidate.id, reviewed.provenance.derivation_refs)
        self.assertIn("source://CRP-GF-001", reviewed.provenance.source_refs)
        self.assertTrue(any(ref.startswith("candidate-review://") for ref in reviewed.provenance.source_refs))
        self.assertFalse(reviewed.metadata["candidate"])
        self.assertFalse(reviewed.metadata["promotion_required"])
        self.assertEqual("accept", reviewed.metadata["review_outcome"])
        self.assertIsNone(reviewed.authority_ref)
        self.assertFalse(any(relationship.type == RelationshipType.HAS_AUTHORITY for relationship in reviewed.relationships))

    def test_reject_defer_and_keep_open_are_inspectable_but_not_current_truth(self) -> None:
        cases = (
            (ReviewOutcome.REJECT, LifecycleStatus.REJECTED, "Rejected because source is contradicted."),
            (ReviewOutcome.DEFER, LifecycleStatus.DEFERRED, "Deferred until product owner confirms."),
            (ReviewOutcome.KEEP_OPEN, LifecycleStatus.OPEN, ""),
        )
        for outcome, expected_status, rationale in cases:
            with self.subTest(outcome=outcome.value):
                candidate = _candidate(f"CRP-{outcome.value}", f"{outcome.value} candidate")
                reviewed = review_candidate(
                    candidate,
                    ReviewDecision(outcome=outcome, reviewer="human-reviewer", rationale=rationale),
                ).reviewed_object
                memory = ProjectMemory([candidate, reviewed])

                self.assertEqual(expected_status, reviewed.status)
                self.assertEqual((), memory.current_objects(PROJECT_READER))
                self.assertEqual(reviewed, memory.inspect(reviewed.id))
                validate_memory_object(reviewed)

    def test_terminal_review_outcomes_require_rationale(self) -> None:
        candidate = _candidate("CRP-GF-002", "Reject without rationale")
        for outcome in (ReviewOutcome.ACCEPT, ReviewOutcome.REJECT, ReviewOutcome.DEFER, ReviewOutcome.AMEND):
            with self.subTest(outcome=outcome.value):
                decision = ReviewDecision(
                    outcome=outcome,
                    reviewer="human-reviewer",
                    amended_title="Amended title" if outcome == ReviewOutcome.AMEND else None,
                )
                with self.assertRaises(CandidateReviewError):
                    review_candidate(candidate, decision)

    def test_amend_candidate_retains_lineage_to_original_candidate(self) -> None:
        candidate = _candidate("CRP-GF-004", "Original uncertain claim")
        result = review_candidate(
            candidate,
            ReviewDecision(
                outcome=ReviewOutcome.AMEND,
                reviewer="human-reviewer",
                rationale="Original claim was too broad.",
                amended_title="Narrowed accepted claim",
            ),
        )
        reviewed = result.reviewed_object

        self.assertEqual("Narrowed accepted claim", reviewed.title)
        self.assertEqual(LifecycleStatus.ACCEPTED, reviewed.status)
        self.assertIn(candidate.id, reviewed.provenance.derivation_refs)
        self.assertIn(
            (RelationshipType.DERIVED_FROM, candidate.id),
            {(relationship.type, relationship.target_id) for relationship in reviewed.relationships},
        )
        self.assertEqual("amend", reviewed.metadata["review_outcome"])
        self.assertEqual("Narrowed accepted claim", reviewed.metadata["amended_title"])

    def test_unauthorized_promotion_is_blocked_when_candidate_requires_authority(self) -> None:
        candidate = _candidate(
            "CRP-GF-005",
            "Launch production migration",
            metadata={"candidate": True, "promotion_required": True, "requires_authority": True},
        )
        with self.assertRaisesRegex(CandidateReviewError, "authority_ref is required"):
            review_candidate(
                candidate,
                ReviewDecision(
                    outcome=ReviewOutcome.ACCEPT,
                    reviewer="human-reviewer",
                    rationale="Looks useful, but authority is absent.",
                ),
            )

        reviewed = review_candidate(
            candidate,
            ReviewDecision(
                outcome=ReviewOutcome.ACCEPT,
                reviewer="human-reviewer",
                rationale="Authority reference is now present.",
                authority_ref="external_authority_change_board",
            ),
        ).reviewed_object
        self.assertEqual("external_authority_change_board", reviewed.authority_ref)
        self.assertIn(
            (RelationshipType.HAS_AUTHORITY, "external_authority_change_board"),
            {(relationship.type, relationship.target_id) for relationship in reviewed.relationships},
        )

    def test_conflicting_candidates_remain_explicit_after_review(self) -> None:
        left_id = deterministic_fixture_id("CRP-GF-006-left", MemoryObjectType.ASSUMPTION, "Use live adapters first")
        right_id = deterministic_fixture_id("CRP-GF-006-right", MemoryObjectType.ASSUMPTION, "Use mock adapters first")
        left = _candidate(
            "CRP-GF-006-left",
            "Use live adapters first",
            relationships=(Relationship(type=RelationshipType.CONTRADICTS, target_id=right_id),),
        )
        right = _candidate(
            "CRP-GF-006-right",
            "Use mock adapters first",
            relationships=(Relationship(type=RelationshipType.CONTRADICTS, target_id=left_id),),
        )
        reviewed = review_candidate(
            left,
            ReviewDecision(
                outcome=ReviewOutcome.ACCEPT,
                reviewer="human-reviewer",
                rationale="Accepted for this fixture while preserving contradiction.",
            ),
        ).reviewed_object
        memory = ProjectMemory([left, right, reviewed])

        contradiction_titles = {
            tuple(sorted((left_obj.title, right_obj.title)))
            for left_obj, right_obj in memory.contradictions(PROJECT_REVIEWER)
        }
        self.assertIn(tuple(sorted(("Use live adapters first", "Use mock adapters first"))), contradiction_titles)
        self.assertIn(
            (RelationshipType.CONTRADICTS, right.id),
            {(relationship.type, relationship.target_id) for relationship in reviewed.relationships},
        )
        self.assertEqual((reviewed,), memory.current_objects(PROJECT_REVIEWER))

    def test_review_service_is_deterministic(self) -> None:
        candidate = _candidate("CRP-GF-001", "Deterministic review")
        decision = ReviewDecision(
            outcome=ReviewOutcome.ACCEPT,
            reviewer="human-reviewer",
            rationale="Stable review fixture.",
        )

        first = review_candidate(candidate, decision)
        second = review_candidate(candidate, decision)

        self.assertEqual(first, second)


def _candidate(
    fixture_id: str,
    title: str,
    *,
    metadata: dict[str, object] | None = None,
    relationships: tuple[Relationship, ...] = (),
) -> MemoryObject:
    return MemoryObject(
        id=deterministic_fixture_id(fixture_id, MemoryObjectType.ASSUMPTION, title),
        type=MemoryObjectType.ASSUMPTION,
        title=title,
        status=LifecycleStatus.PROPOSED,
        visibility=Visibility.PROJECT,
        provenance=Provenance(
            source_refs=(f"source://{fixture_id}", REVIEWED_AT_SOURCE),
            created_by="thinking-engine-intake",
            created_at=ReviewDecision(outcome=ReviewOutcome.KEEP_OPEN, reviewer="fixture").reviewed_at,
            evidence_level=EvidenceLevel.E2_REVIEWED_SYNTHESIS,
        ),
        relationships=relationships,
        metadata=metadata or {"candidate": True, "promotion_required": True},
    )


if __name__ == "__main__":
    unittest.main()
