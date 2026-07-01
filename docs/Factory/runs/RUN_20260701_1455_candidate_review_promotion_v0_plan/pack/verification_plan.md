# Verification Plan

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage F verification plan.

## Strategy

Verify Candidate Review and Promotion v0 with deterministic local fixtures and unit tests before any CLI, persistence, live integration, or product-shell work.

## Verification Tiers

- V0 artifact proof
- V1 static or mechanical check
- V2 focused fixture or unit test
- V3 regression suite
- V4 live or external proof

## Required Checks

| Check ID | Tier | Required Proof |
| --- | --- | --- |
| VC-001 | V2 | Candidate review requires an explicit review decision before accepted truth is produced. |
| VC-002 | V2 | Accept, reject, defer, amend, and keep-open outcomes require valid status, reviewer provenance, and rationale where applicable. |
| VC-003 | V2 | Rejected, deferred, stale, superseded, and candidate-only records remain inspectable but excluded from current truth. |
| VC-004 | V2 | Amended outcomes retain derivation lineage to the original candidate. |
| VC-005 | V2 | Accepted outcomes preserve original candidate provenance and add review provenance. |
| VC-006 | V2 | Accepted memory does not imply authority without an explicit Authority Reference or authority relationship. |
| VC-007 | V2 | Conflicting candidates remain explicit and are not flattened into one accepted truth without review. |
| VC-008 | V1 | CLI/TUI wrappers call shared service functions if implemented. |
| VC-009 | V1 | No live integrations are required or invoked. |
| VC-010 | V1 | No product shell, database, or live adapter is introduced. |

## Deferred Verification

- Product UI verification is deferred.
- Persistence and migration verification are deferred.
- Live Cursor, Codex, OpenAI, analytics, CRM, ads, design, and repository connector verification is deferred.
- Socratic discovery flow verification is deferred.

## Acceptance Standard

Future implementation is ready for review when all V1 and V2 checks pass locally and the review service proves that candidate output cannot become accepted truth without explicit review action.
