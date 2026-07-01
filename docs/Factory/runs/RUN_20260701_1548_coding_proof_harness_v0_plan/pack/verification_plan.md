# Verification Plan

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage F verification plan.

## Strategy

Verify Coding Proof Harness v0 with deterministic local fixtures and unit tests before any live provider, persistence, repository mutation, product shell, or Workspace Shell work.

## Verification Tiers

- V0 artifact proof
- V1 static or mechanical check
- V2 focused fixture or unit test
- V3 regression suite
- V4 live or external proof

## Required Checks

| Check ID | Tier | Required Proof |
| --- | --- | --- |
| VC-001 | V2 | Harness composes existing Intake, Socratic Discovery, Project Memory context, adapter-twin, and Candidate Review services. |
| VC-002 | V2 | Greenfield and Brownfield coding fixtures produce distinct readiness and discovery behavior. |
| VC-003 | V2 | Task-specific Project Memory context is assembled for a coding task. |
| VC-004 | V2 | Mock provider surface selection uses the existing adapter-twin vocabulary. |
| VC-005 | V2 | Provider Invocation records preserve capability and authority separation. |
| VC-006 | V2 | Proposed provider output is captured as Project Memory candidates and does not become accepted truth. |
| VC-007 | V2 | Candidate Review and Promotion is the only promotion path for proposed provider output. |
| VC-008 | V1 | No live model, live CLI, live SDK, database, external connector, or repository mutation is required or invoked. |
| VC-009 | V2 | Brownfield blocked/audit gaps prevent ready-for-planning. |
| VC-010 | V1 | CLI/TUI wrappers call shared service functions if implemented. |
| VC-011 | V1 | No product shell or Workspace Shell implementation is introduced. |

## Deferred Verification

- Live Codex, Cursor, OpenAI, and other provider behavior is deferred.
- Repository mutation verification is deferred.
- Product UI and Workspace Shell verification are deferred.
- Persistence and migration verification are deferred.
- Multi-repository Brownfield proof may be deferred if the first implementation chooses single-repo Brownfield only.

## Acceptance Standard

Future implementation is ready for review when all V1 and V2 checks pass locally and the harness proves a coding workflow with candidate-only provider output, traceable invocation records, and review-gated promotion.
