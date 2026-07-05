# Handoff Stage B

## Version
v1

## Change Log
- v1 (2026-07-05): Initial Stage B handoff.

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
- `./scripts/factoryctl stage-lint --run RUN_20260705_0923_live_coding_adapter_eval_plan --stage B`

## Exit Criteria Status
- PASS

## Iteration: 1 of max 2
- Critical ambiguity around live invocation was identified.
