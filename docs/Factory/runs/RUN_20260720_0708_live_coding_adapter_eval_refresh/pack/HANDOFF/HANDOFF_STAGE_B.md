# Handoff Stage B

## Version
v2

## Change Log
- v1 (2026-07-05): Initial Stage B handoff in the upstream planning run.
- v2 (2026-07-20): Re-ran intent red-team for the refreshed pack.

## Stage
STAGE_B Red Team Intent

## Inputs (LOAD)
- `pack/intent.md`

## Inputs (DISK)
- `pack/external_source_review.md`

## Skill Routing Contract
- Skill used (or `NONE`): `NONE`

## Outputs Produced (paths)
- `pack/intent_redteam.md`

## Verification Steps Recommended
- `./scripts/factoryctl stage-lint --run RUN_20260720_0708_live_coding_adapter_eval_refresh --stage B`

## Exit Criteria Status
- PASS

## Iteration: 1 of max 2
- Critical accidental-probe and source-contradiction risks were identified.
