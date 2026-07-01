# Intent Synthesis: Coding Proof Harness v0

## Version

v1

## Change Log

- v1 (2026-07-01): Stage C synthesis after intent red team.

## Iteration

Iteration: 1 of max 2

## Changes Made

- Clarified the harness is service-first and any CLI wrapper is optional.
- Added explicit Candidate Review and Promotion gate for proposed provider outputs.
- Added Greenfield/Brownfield fixture requirements.
- Added provider capability versus authority separation.
- Added explicit no-live-tool and no-repository-mutation requirements.

## Red Team Resolution

| Finding | Resolution |
| --- | --- |
| Harness could become product workflow | Bound to local service surface; optional wrapper only. |
| Provider output could bypass review | Added REQ-007, REQ-008, and verification gates. |
| Greenfield/Brownfield flattening | Added REQ-002 and REQ-009 with fixture requirements. |
| Adapter selection implies authority | Added REQ-006 authority/capability separation. |
| Verification requires live tools | Added REQ-010 and V1/V2/V3-only checks. |

## Scope Expansion

- None.

## Open Issues

### BLOCKING

- None.

### NON-BLOCKING

- Optional CLI wrapper remains deferrable.
- Multi-repository Brownfield fixture may be included if it fits the file-touch budget.
