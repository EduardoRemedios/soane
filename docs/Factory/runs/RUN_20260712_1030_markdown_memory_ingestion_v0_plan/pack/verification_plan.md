# Verification Plan: MMI-V0-001

## Version
v1

## Change Log
- v1 (2026-07-12): Stage F verification plan.

## Strategy

Use deterministic unit and CLI tests over a storage-neutral ingestion service. Add adversarial filesystem fixtures and fixed Markdown comparison pairs, then run the complete repository suite and static scope checks.

## Required Checks

| Check | Tier | Required Proof |
| --- | --- | --- |
| VC-001 | V2 | Valid Claim candidates are proposed/asserted Project objects with E1 provenance, promotion flags, and every required metadata field. |
| VC-002 | V2 | Missing, malformed, conflicting, accepted, verified, non-Project, or authority-bearing ingestion candidates fail contract validation. |
| VC-003 | V2 | Path traversal, absolute path, symlink escape, missing/non-file/non-Markdown, and decode failures are rejected before ingestion. |
| VC-004 | V2 | Role, authority mode, source authority, evidence level, lifecycle, epistemic status, and Knowledge Scope stay distinct; ineligible roles fail closed. |
| VC-005 | V2 | Only exact prose paragraphs under ATX headings become candidates; all excluded Markdown constructs produce reasons and respect budget. |
| VC-006 | V2 | IDs, document/block fingerprints, occurrence identities, anchors, and ordering are deterministic across repeated runs and line-ending normalization. |
| VC-007 | V2 | Every comparison state is deterministic; duplicate ambiguity is reported without guessed lineage. |
| VC-008 | V2 | Ingestion/comparison never calls review, emits accepted objects, assigns Authority, or mutates source/accepted MemoryObjects. |
| VC-009 | V2 | Existing MarkdownRole imports, classifications, priorities, and agent-context behavior remain compatible after any vocabulary move. |
| VC-010 | V2 | `ingest-markdown` and `compare-markdown` return stable JSON with candidates, snapshots, exclusions, warnings, events, and reasons; interchange export is review-compatible. |
| VC-011 | V2 | Fixed real architecture excerpt produces a bounded, human-reviewable candidate set with exact origin metadata. |
| VC-012 | V3 | `python3 -m unittest discover -s tests` exits 0. |
| VC-013 | V1 | Diff adds no persistence, database schema, external dependency, embedding, provider, UI, live adapter, Factory-index schema, or neighbouring-product change. |
| VC-014 | V1 | Project State, Roadmap, Changelog, knowledge lint, context-index refresh, pack lint, and diff hygiene are truthful and clean. |

## Failure Injection

- Resolve a symlinked Markdown path outside a temporary repository and confirm the read is blocked.
- Supply duplicate identical paragraphs whose before/after anchors cannot establish one-to-one lineage and confirm `ambiguous_duplicate`.
- Patch or spy on `review_candidate` during ingestion and confirm it is never invoked.
- Attempt to construct a Claim candidate with accepted lifecycle, verified epistemic status, public visibility, or missing source authority and confirm validation failure.

## Acceptance Standard

VC-001 through VC-014 pass. Any failure in VC-001 through VC-008 or VC-013 blocks acceptance.
