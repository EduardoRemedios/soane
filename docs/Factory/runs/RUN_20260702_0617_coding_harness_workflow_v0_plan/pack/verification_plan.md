# Verification Plan

## Version

v1

## Change Log

- v1 (2026-07-02): Initial Stage F verification plan.

## Strategy

Verify Coding Harness Workflow v0 with deterministic CLI tests over existing coding harness fixtures before any TUI, live provider, repository mutation, persistence, product shell, or Workspace Shell work.

## Verification Tiers

- V0 artifact proof
- V1 static or mechanical check
- V2 focused fixture or unit test
- V3 regression suite
- V4 live or external proof

## Required Checks

| Check ID | Tier | Required Proof |
| --- | --- | --- |
| VC-001 | V2 | CLI command delegates to existing coding harness service functions. |
| VC-002 | V2 | CLI can list deterministic coding harness fixtures. |
| VC-003 | V2 | CLI can run a selected fixture and emit text plus JSON summaries. |
| VC-004 | V2 | Summary includes intake readiness, discovery stop condition, context package, provider invocation, output candidate, and review status. |
| VC-005 | V2 | Provider summary identifies mocked adapter twin invocation and `live_call_performed=false`. |
| VC-006 | V2 | Proposed provider output remains candidate-only unless reviewed through Candidate Review and Promotion. |
| VC-007 | V2 | Brownfield blocked fixture summary shows provider invocation is unavailable. |
| VC-008 | V1 | No live provider, live CLI, live SDK, database, external connector, or repository mutation is required or invoked. |
| VC-009 | V1 | Optional TUI is skipped or delegates to shared service functions if implemented. |
| VC-010 | V1 | No product shell or Workspace Shell implementation is introduced. |

## Deferred Verification

- TUI verification is deferred unless MS-05 is included.
- Live provider verification is deferred.
- Persistence verification is deferred.
- Product UI and Workspace Shell verification are deferred.

## Acceptance Standard

Future implementation is ready for review when all V1 and V2 checks pass locally and the CLI makes the coding harness workflow inspectable without changing harness semantics.
