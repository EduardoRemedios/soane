from __future__ import annotations

import os
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

from soane.project_memory.contract import (
    ContractValidationError,
    EvidenceLevel,
    LifecycleStatus,
    MemoryObjectType,
    Visibility,
    validate_memory_object,
)
from soane.project_memory.markdown_ingestion import (
    ExclusionReason,
    MarkdownChangeState,
    MarkdownIngestionError,
    MarkdownIngestionRequest,
    compare_markdown_snapshots,
    ingest_markdown,
)
from soane.project_memory.markdown_roles import MarkdownAuthorityMode, MarkdownRole
from soane.project_memory.review import ReviewDecision, ReviewOutcome, review_candidate


REPO_ROOT = Path(__file__).resolve().parents[1]
EXCERPT = REPO_ROOT / "tests/fixtures/project_memory/markdown_ingestion/project_memory_architecture_excerpt.md"
CANONICAL_PATH = "docs/PROJECT_MEMORY_ARCHITECTURE.md"


class MarkdownIngestionTests(unittest.TestCase):
    def test_valid_claim_candidates_preserve_exact_source_semantics(self) -> None:
        with self._repo("# Architecture\n\n## Purpose\n\nThe system preserves exact project understanding.\n") as root:
            result = self._ingest(root)

        self.assertEqual(1, len(result.candidates))
        candidate = result.candidates[0]
        self.assertEqual(MemoryObjectType.CLAIM, candidate.type)
        self.assertEqual(LifecycleStatus.PROPOSED, candidate.status)
        self.assertEqual(Visibility.PROJECT, candidate.visibility)
        self.assertEqual(EvidenceLevel.E1_SOURCE_REFERENCE, candidate.provenance.evidence_level)
        self.assertIsNone(candidate.authority_ref)
        self.assertEqual("asserted", candidate.metadata["epistemic_status"])
        self.assertEqual("project", candidate.metadata["knowledge_scope"])
        self.assertEqual("canonical", candidate.metadata["markdown_role"])
        self.assertEqual("authored_authority", candidate.metadata["authority_mode"])
        self.assertEqual("repo-canonical-docs", candidate.metadata["source_authority"])
        self.assertEqual("Architecture > Purpose", candidate.metadata["heading_path"])
        self.assertEqual(5, candidate.metadata["start_line"])
        self.assertEqual(5, candidate.metadata["end_line"])
        self.assertIn(CANONICAL_PATH, candidate.provenance.source_refs)
        validate_memory_object(candidate)

    def test_claim_candidate_contract_rejects_invalid_combinations(self) -> None:
        with self._repo("# Architecture\n\n## Purpose\n\nA bounded claim.\n") as root:
            candidate = self._ingest(root).candidates[0]

        invalid = (
            replace(candidate, status=LifecycleStatus.ACCEPTED),
            replace(candidate, visibility=Visibility.PUBLIC),
            replace(candidate, authority_ref="authority://unexpected"),
            replace(candidate, provenance=replace(candidate.provenance, evidence_level=EvidenceLevel.E2_REVIEWED_SYNTHESIS)),
            replace(candidate, metadata={**candidate.metadata, "epistemic_status": "verified"}),
            replace(candidate, metadata={**candidate.metadata, "knowledge_scope": "portfolio"}),
            replace(candidate, metadata={**candidate.metadata, "proposition": "Different proposition"}),
            replace(candidate, metadata={key: value for key, value in candidate.metadata.items() if key != "source_authority"}),
        )
        for memory_object in invalid:
            with self.subTest(memory_object=memory_object):
                with self.assertRaises(ContractValidationError):
                    validate_memory_object(memory_object)

    def test_existing_review_service_accepts_claim_without_verifying_it(self) -> None:
        with self._repo("# Architecture\n\n## Purpose\n\nA reviewable claim.\n") as root:
            candidate = self._ingest(root).candidates[0]
        reviewed = review_candidate(
            candidate,
            ReviewDecision(
                outcome=ReviewOutcome.ACCEPT,
                reviewer="human-reviewer",
                rationale="Accept the claim into memory without treating it as verified fact.",
            ),
        ).reviewed_object

        self.assertEqual(LifecycleStatus.ACCEPTED, reviewed.status)
        self.assertEqual("asserted", reviewed.metadata["epistemic_status"])
        self.assertFalse(reviewed.metadata["candidate"])
        self.assertIn(candidate.id, reviewed.provenance.derivation_refs)
        validate_memory_object(reviewed)

    def test_ineligible_roles_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            constitutional = root / "docs/VISION.md"
            constitutional.parent.mkdir(parents=True)
            constitutional.write_text("# Vision\n\n## Purpose\n\nConstitutional claim.\n", encoding="utf-8")
            working = root / "notes.md"
            working.write_text("# Notes\n\n## Topic\n\nWorking claim.\n", encoding="utf-8")

            constitutional_result = self._ingest(root, source_path="docs/VISION.md")
            working_result = self._ingest(root, source_path="notes.md")

        self.assertEqual((), constitutional_result.candidates)
        self.assertEqual(ExclusionReason.CONSTITUTIONAL_AUTHORITY, constitutional_result.exclusions[0].reason)
        self.assertEqual(MarkdownRole.CONSTITUTIONAL, constitutional_result.snapshot.markdown_role)
        self.assertEqual((), working_result.candidates)
        self.assertEqual(ExclusionReason.INELIGIBLE_ROLE, working_result.exclusions[0].reason)

    def test_parser_extracts_only_prose_and_reports_structured_exclusions(self) -> None:
        text = """---
owner: test
---
Outside any heading.

# Architecture

## Purpose

This introduces:

Eligible prose paragraph.

- list item
- second item

> quoted text

| A | B |
| --- | --- |
| 1 | 2 |

<section>HTML block</section>

    indented code

```python
print("not a claim")
```
"""
        with self._repo(text) as root:
            result = self._ingest(root)

        self.assertEqual(["Eligible prose paragraph."], [item.title for item in result.candidates])
        reasons = {exclusion.reason for exclusion in result.exclusions}
        self.assertTrue(
            {
                ExclusionReason.FRONT_MATTER,
                ExclusionReason.OUTSIDE_HEADING,
                ExclusionReason.STRUCTURED_INTRO,
                ExclusionReason.LIST,
                ExclusionReason.BLOCKQUOTE,
                ExclusionReason.TABLE,
                ExclusionReason.HTML,
                ExclusionReason.INDENTED_CODE,
                ExclusionReason.FENCED_CODE,
            }.issubset(reasons)
        )

    def test_candidate_budget_is_deterministic_and_explained(self) -> None:
        text = "# Architecture\n\n## Purpose\n\nFirst.\n\nSecond.\n\nThird.\n"
        with self._repo(text) as root:
            first = self._ingest(root, candidate_limit=2)
            second = self._ingest(root, candidate_limit=2)

        self.assertEqual(2, len(first.candidates))
        self.assertTrue(first.truncated)
        self.assertEqual([candidate.id for candidate in first.candidates], [candidate.id for candidate in second.candidates])
        self.assertTrue(any(item.reason == ExclusionReason.CANDIDATE_BUDGET for item in first.exclusions))
        self.assertTrue(first.warnings)

    def test_ids_and_fingerprints_ignore_line_ending_style(self) -> None:
        source = "# Architecture\n\n## Purpose\n\nStable paragraph.\n"
        with self._repo(source) as left_root, self._repo(source.replace("\n", "\r\n")) as right_root:
            left = self._ingest(left_root)
            right = self._ingest(right_root)

        self.assertEqual(left.snapshot.document_fingerprint, right.snapshot.document_fingerprint)
        self.assertEqual(left.snapshot.blocks, right.snapshot.blocks)
        self.assertEqual(left.candidates[0].id, right.candidates[0].id)

    def test_comparison_reports_unchanged_and_mode_change(self) -> None:
        text = "# Architecture\n\n## Purpose\n\nStable paragraph.\n"
        with self._repo(text) as before_root, self._repo(text) as after_root:
            before = self._ingest(before_root)
            unchanged_after = self._ingest(after_root)
            mode_after = self._ingest(after_root, authority_mode=MarkdownAuthorityMode.CURATED_ROUND_TRIP)

        unchanged = compare_markdown_snapshots(before.snapshot, unchanged_after.snapshot)
        changed = compare_markdown_snapshots(before.snapshot, mode_after.snapshot)
        self.assertEqual([MarkdownChangeState.UNCHANGED], [event.state for event in unchanged.events])
        self.assertEqual([MarkdownChangeState.MODE_CHANGED], [event.state for event in changed.events])

    def test_comparison_reports_modified_moved_deleted_and_added(self) -> None:
        with self._repo("# Architecture\n\n## One\n\nOriginal.\n") as before_root:
            before = self._ingest(before_root)
            with self._repo("# Architecture\n\n## One\n\nModified.\n") as modified_root:
                modified = compare_markdown_snapshots(before.snapshot, self._ingest(modified_root).snapshot)
            with self._repo("# Architecture\n\n## Two\n\nOriginal.\n") as moved_root:
                moved = compare_markdown_snapshots(before.snapshot, self._ingest(moved_root).snapshot)
            with self._repo("# Architecture\n\n## Two\n\nReplacement.\n") as replaced_root:
                replaced = compare_markdown_snapshots(before.snapshot, self._ingest(replaced_root).snapshot)

        self.assertEqual([MarkdownChangeState.MODIFIED], [event.state for event in modified.events])
        self.assertEqual([MarkdownChangeState.MOVED], [event.state for event in moved.events])
        self.assertEqual(
            {MarkdownChangeState.DELETED, MarkdownChangeState.ADDED},
            {event.state for event in replaced.events},
        )

    def test_duplicate_lineage_fails_closed(self) -> None:
        before_text = "# Architecture\n\n## One\n\nRepeated.\n\n## Two\n\nRepeated.\n"
        after_text = "# Architecture\n\n## Three\n\nRepeated.\n\n## Four\n\nRepeated.\n"
        with self._repo(before_text) as before_root, self._repo(after_text) as after_root:
            comparison = compare_markdown_snapshots(
                self._ingest(before_root).snapshot,
                self._ingest(after_root).snapshot,
            )

        self.assertEqual([MarkdownChangeState.AMBIGUOUS_DUPLICATE], [event.state for event in comparison.events])
        self.assertEqual(2, len(comparison.events[0].before_occurrence_ids))
        self.assertEqual(2, len(comparison.events[0].after_occurrence_ids))

    def test_source_boundaries_and_input_validation_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as outside_tmp:
            root = Path(tmp)
            outside = Path(outside_tmp) / "outside.md"
            outside.write_text("# Outside\n", encoding="utf-8")
            link = root / "docs/PROJECT_MEMORY_ARCHITECTURE.md"
            link.parent.mkdir(parents=True)
            os.symlink(outside, link)
            with self.assertRaisesRegex(MarkdownIngestionError, "escapes repository root"):
                self._ingest(root)

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs").mkdir()
            (root / "docs/bad.md").write_bytes(b"\xff\xfe")
            (root / "docs/not-markdown.txt").write_text("text", encoding="utf-8")
            (root / "docs/directory.md").mkdir()
            invalid = (
                ("/tmp/absolute.md", "repository-relative"),
                ("docs/missing.md", "does not exist"),
                ("docs/not-markdown.txt", "must use .md"),
                ("docs/directory.md", "not a file"),
                ("docs/bad.md", "not valid UTF-8"),
            )
            for source_path, message in invalid:
                with self.subTest(source_path=source_path):
                    with self.assertRaisesRegex(MarkdownIngestionError, message):
                        self._ingest(root, source_path=source_path)

    def test_fixed_canonical_excerpt_is_bounded_and_reviewable(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / CANONICAL_PATH
            path.parent.mkdir(parents=True)
            path.write_text(EXCERPT.read_text(encoding="utf-8"), encoding="utf-8")
            result = self._ingest(root, candidate_limit=10)

        self.assertEqual(4, len(result.candidates))
        self.assertLessEqual(len(result.candidates), 10)
        self.assertTrue(all(candidate.metadata["source_path"] == CANONICAL_PATH for candidate in result.candidates))
        self.assertTrue(any(item.reason == ExclusionReason.LIST for item in result.exclusions))
        self.assertTrue(any(item.reason == ExclusionReason.FENCED_CODE for item in result.exclusions))

    def _ingest(
        self,
        root: Path,
        *,
        source_path: str = CANONICAL_PATH,
        authority_mode: MarkdownAuthorityMode = MarkdownAuthorityMode.AUTHORED_AUTHORITY,
        candidate_limit: int = 20,
    ):
        return ingest_markdown(
            MarkdownIngestionRequest(
                root=root,
                source_path=source_path,
                authority_mode=authority_mode,
                source_authority="repo-canonical-docs",
                candidate_limit=candidate_limit,
            )
        )

    class _RepoContext:
        def __init__(self, test_case: "MarkdownIngestionTests", text: str):
            self.test_case = test_case
            self.text = text
            self.temp = tempfile.TemporaryDirectory()

        def __enter__(self) -> Path:
            root = Path(self.temp.name)
            path = root / CANONICAL_PATH
            path.parent.mkdir(parents=True)
            path.write_text(self.text, encoding="utf-8", newline="")
            return root

        def __exit__(self, exc_type, exc, traceback) -> None:
            self.temp.cleanup()

    def _repo(self, text: str) -> "MarkdownIngestionTests._RepoContext":
        return self._RepoContext(self, text)


if __name__ == "__main__":
    unittest.main()
