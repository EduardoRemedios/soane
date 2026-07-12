# Verification Plan: VEH-V1-001

## Version
v1

## Change Log
- v1 (2026-07-12): Stage F verification plan.

## Strategy

Use direct document inspection, exact-term scans, repository lint, context-index refresh, Factory validation, and the full deterministic test suite. Documentation semantics require V1 review evidence; repository behavior remains protected by V3 regression.

## Required Checks

| Check | Tier | Required Proof |
| --- | --- | --- |
| VC-001 | V1 | Project Memory wording distinguishes current governed understanding from external source authority. |
| VC-002 | V1 | Agent judgement is bounded, revocable, accountable, and incapable of creating Authority. |
| VC-003 | V1 | Knowledge scope fails closed and promotion propagates provenance and restrictions. |
| VC-004 | V1 | Authored authority, generated projection, and curated round trip have distinct write rules. |
| VC-005 | V1 | Project state and architecture explicitly defer runtime representation. |
| VC-006 | V1 | Decision Review connects expected outcome, observation, assumptions, learning, and change. |
| VC-007 | V1 | Success measures exclude artifact-volume optimization. |
| VC-008 | V1 | Diff stays inside file budget and portfolio ownership remains unchanged. |
| VC-009 | V3 | `python3 -m unittest discover -s tests` exits 0. |
| VC-010 | V1 | Knowledge lint, context-index refresh, Factory pack lint, and `git diff --check` pass. |

## V1 Coverage Explanation

Critical and High risks concern constitutional language, so exact source review and contradiction scans are the appropriate executable boundary. V3 regression additionally proves no existing runtime behavior was changed.

## Acceptance Standard

VC-001 through VC-010 pass. Any failure in VC-001 through VC-005 or VC-008 blocks acceptance.
