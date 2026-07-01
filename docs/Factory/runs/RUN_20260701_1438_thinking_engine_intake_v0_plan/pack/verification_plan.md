# Verification Plan

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage F verification plan.

## Strategy

Verify Thinking Engine Intake v0 with deterministic local fixtures and service tests before any live integrations or product shell work.

## Verification Tiers

- V0 artifact proof
- V1 static or mechanical check
- V2 focused fixture or unit test
- V3 regression suite
- V4 live or external proof

## Required Checks

| Check ID | Tier | Required Proof |
| --- | --- | --- |
| VC-001 | V1 | Implementation scope remains local and deterministic. |
| VC-002 | V2 | Greenfield intake creates missing-context baseline candidates. |
| VC-003 | V2 | Brownfield single-repo intake records repo, docs, build, and test context. |
| VC-004 | V2 | Brownfield multi-repo intake records system boundary and repository map. |
| VC-005 | V2 | Non-repository intake records external context artifacts. |
| VC-006 | V2 | Context Baseline is separate from accepted Project Memory truth. |
| VC-007 | V2 | Readiness Assessment uses explainable states and dimensions, not a score. |
| VC-008 | V2 | Thinking outputs are write-back candidates with provenance. |
| VC-009 | V1 | No live integrations are required or invoked. |
| VC-010 | V1 | CLI/TUI wrappers call shared service functions if implemented. |
| VC-011 | V1 | No product shell, database, or live adapter is introduced. |

## Deferred Verification

- Live repository scanning is deferred.
- Live analytics, CRM, advertising, and design-tool connectors are deferred.
- Cursor, Codex, OpenAI, and agent SDK calls are deferred.
- Product web UI and database verification are deferred.

## Acceptance Standard

Future implementation is ready for review when all V1 and V2 checks pass locally and blockers are recorded as Questions, Constraints, or Decision needs.
