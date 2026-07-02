# Intent Synthesis: Coding Harness Workflow v0

## Version

v1

## Change Log

- v1 (2026-07-02): Stage C synthesis after intent red team.

## Iteration

Iteration: 1 of max 2

## Changes Made

- Clarified that the workflow owns command/navigation shape only.
- Added explicit delegation requirements to existing harness services.
- Added explicit candidate/review status summary requirements.
- Added no-live-provider and no-repository-mutation verification requirements.
- Kept TUI optional and bounded.

## Red Team Resolution

| Finding | Resolution |
| --- | --- |
| CLI wrapper could duplicate harness logic | Added REQ-007 and service delegation requirements. |
| Workflow could imply live execution | Added explicit no-live-provider summary and verification requirements. |
| Review status could be unclear | Added REQ-004 and REQ-006. |
| Optional TUI could become product shell | Kept TUI optional and skippable. |

## Scope Expansion

- None.

## Open Issues

### BLOCKING

- None.

### NON-BLOCKING

- TUI inclusion remains a future implementation decision after CLI tests pass.
