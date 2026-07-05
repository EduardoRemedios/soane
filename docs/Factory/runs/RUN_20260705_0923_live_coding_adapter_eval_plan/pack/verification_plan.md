# Verification Plan: LCAE-V0-001

## Version

v1

## Change Log

- v1 (2026-07-05): Initial Stage F verification plan.

## Strategy

Future implementation should verify adapter evaluation with deterministic profiles, fixtures, and unit tests. No live providers, credentials, installs, external repositories, or network calls are required.

## Verification Tiers

- V0 artifact proof
- V1 static or mechanical check
- V2 focused fixture or unit test
- V3 regression suite
- V4 live or external proof

## Required Checks

| Check ID | Tier | Required Proof |
| --- | --- | --- |
| VC-001 | V2 | Evaluation fixture set covers Codex CLI, Cursor CLI, Cursor SDK, OpenAI SDK, and OpenAI Agents SDK. |
| VC-002 | V2 | Each profile records source refs, source date, invocation modes, auth modes, sandbox/mutation controls, output capture, traceability, cost/latency metadata path, and known limitations. |
| VC-003 | V2 | Capability, authentication, authority, and project permission are distinct fields and cannot satisfy each other. |
| VC-004 | V2 | Unsafe or unclear mutation controls produce blocked evaluation status. |
| VC-005 | V2 | SDK surfaces are not recommended ahead of CLI surfaces unless deterministic evidence records why. |
| VC-006 | V2 | Any simulated provider output remains candidate-only and cannot become current truth without Candidate Review and Promotion. |
| VC-007 | V2 | Recommendation output selects a first live proof surface and records rejected alternatives with reasons. |
| VC-008 | V1 | No live CLI, SDK, API, cloud agent, network call, dependency install, credential read, external repository access, or repository mutation occurs. |
| VC-009 | V3 | Existing Project Memory, adapter twin, coding harness, coding workflow, and Brownfield multi-repo tests still pass. |
| VC-010 | V1 | No product UI, Workspace Shell, persistence, or mission execution is introduced. |

## Deferred Verification

- V4 live provider invocation is deferred.
- Credential provisioning is deferred.
- Real repository mutation and patch application are deferred.
- Runtime cost and latency measurement are deferred until a later authorized live proof.

## Acceptance Standard

Future implementation is ready for review when VC-001 through VC-010 pass and the recommendation can be reviewed without performing any live provider action.
