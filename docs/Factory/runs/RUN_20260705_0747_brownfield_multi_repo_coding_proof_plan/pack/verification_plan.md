# Verification Plan

## Version

v1

## Change Log

- v1 (2026-07-05): Initial Stage F verification plan.

## Strategy

Verify the future Brownfield multi-repo coding proof with deterministic fixture and unit tests. The proof remains mock-first and local.

## Verification Tiers

- V0 artifact proof
- V1 static or mechanical check
- V2 focused fixture or unit test
- V3 regression suite
- V4 live or external proof

## Required Checks

| Check ID | Tier | Required Proof |
| --- | --- | --- |
| VC-001 | V2 | Ready multi-repo fixture records repository map, in-scope and out-of-scope repositories, service boundary, integration contracts, ownership, and build/test responsibility. |
| VC-002 | V2 | Intake classifies the ready fixture as `brownfield_multi_repo` and selects Brownfield system audit plus integration boundary discovery playbooks. |
| VC-003 | V2 | Context assembly and harness summary expose task-relevant repositories and cross-repository context without treating every repository as relevant. |
| VC-004 | V2 | Blocked multi-repo fixture records missing system-boundary, owner, contract, build/test, or authority context and prevents provider invocation. |
| VC-005 | V2 | Ready multi-repo provider output remains candidate-only unless explicitly reviewed through Candidate Review and Promotion. |
| VC-006 | V2 | Blocked multi-repo workflow summary shows no provider invocation and no output candidate. |
| VC-007 | V2 | CLI workflow lists and runs multi-repo fixtures while delegating to shared harness functions. |
| VC-008 | V1 | No live provider, live CLI, live SDK, database, external connector, real repository clone, real command execution, or repository mutation is required or invoked. |
| VC-009 | V3 | Existing Greenfield and Brownfield single-repo coding proof and workflow tests still pass. |
| VC-010 | V1 | No product shell or Workspace Shell implementation is introduced. |

## Deferred Verification

- Live repository audit is deferred.
- Live provider verification is deferred.
- Persistence verification is deferred.
- Product UI and Workspace Shell verification are deferred.

## Acceptance Standard

Future implementation is ready for review when VC-001 through VC-010 pass and the workflow makes multi-repo system boundaries inspectable without live side effects.
