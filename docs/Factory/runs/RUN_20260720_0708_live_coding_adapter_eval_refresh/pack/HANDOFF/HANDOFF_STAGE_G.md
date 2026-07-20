# Handoff Stage G

## Version
v2

## Change Log
- v1 (2026-07-05): Initial Stage G handoff in the upstream planning run.
- v2 (2026-07-20): Re-sequenced around tests, profiles, pure evaluation, CLI, and closeout.

## Stage
STAGE_G Micro-Sprint Sequencing

## Inputs (LOAD)
- `pack/intent.md`
- `pack/risk_register.md`
- `pack/verification_plan.md`

## Inputs (DISK)
- `pack/traceability_matrix.md`

## Skill Routing Contract
- Skill used (or `NONE`): `NONE`

## Outputs Produced (paths)
- `pack/micro_sprints.md`

## Verification Steps Recommended
- `./scripts/factoryctl stage-lint --run RUN_20260720_0708_live_coding_adapter_eval_refresh --stage G`

## Exit Criteria Status
- PASS

## Notes
- Sequence starts with verification and source revalidation before any implementation.
