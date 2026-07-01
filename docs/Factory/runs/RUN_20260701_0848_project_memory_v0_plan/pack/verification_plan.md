# Verification Plan

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage F verification plan.

## Verification Strategy

The first implementation should prove Project Memory semantics through deterministic local checks before any live CLI, SDK, database, or product UI integration.

Verification should begin with fixture-backed contract tests over local data.

## Verification Tiers

- V0 artifact proof: planning artifact or checklist.
- V1 static or mechanical check: schema validation, lint, or deterministic contract check.
- V2 focused fixture/test: golden fixture test for one invariant.
- V3 regression or conformance gate: repeatable suite covering v0 contract.
- V4 live/external proof: live CLI, SDK, browser, or external provider evidence.

## Required Checks For Implementation

| Check ID | Tier | Required Proof |
| --- | --- | --- |
| VC-001 | V2 | Decision links to Evidence. |
| VC-002 | V2 | Assumption can be superseded by Evidence. |
| VC-003 | V2 | Contradictions remain explicit. |
| VC-004 | V2 | Stale Evidence is surfaced and not silently used as current support. |
| VC-005 | V2 | Markdown output maps to source memory objects. |
| VC-006 | V2 | Mock Provider Invocation records adapter metadata. |
| VC-007 | V2 | Capability does not imply Authority. |
| VC-008 | V2 | Redaction or retrieval suppression blocks exposure. |
| VC-009 | V2 | Direct lookup, search, and context assembly enforce visibility consistently. |
| VC-010 | V2 | Superseded records remain inspectable but excluded from current truth. |
| VC-011 | V2 | Promoted claims retain reconstructable provenance lineage. |
| VC-012 | V2 | Context assembly respects visibility and propagation rules. |
| VC-013 | V1 | Object IDs are deterministic for fixtures. |
| VC-014 | V1 | Local storage is portable and inspectable. |
| VC-015 | V1 | CLI commands call the same service/contract layer as tests. |
| VC-016 | V0 | TUI scope remains navigation-only over CLI/service primitives. |

## Deferred Verification

- Live Cursor CLI, Codex CLI, Cursor SDK, OpenAI SDK, and OpenAI Agents SDK checks are deferred until the mock adapter contract passes.
- Browser or product UI verification is deferred until the Workspace Shell architecture is accepted.
- Final database migration verification is deferred until storage selection is justified.

## Commands To Add Later

Exact commands are implementation details, but the future prototype should add equivalents of:

- `soane memory validate`
- `soane memory fixture-test`
- `soane memory context-build`
- `soane memory export-markdown`

## Acceptance Standard

Implementation should not be considered ready for TUI work until all V1 and V2 checks for Project Memory v0 pass locally.

