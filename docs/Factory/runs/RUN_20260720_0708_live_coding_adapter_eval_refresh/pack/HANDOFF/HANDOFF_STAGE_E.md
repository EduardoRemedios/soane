# Handoff Stage E

## Version
v2

## Change Log
- v1 (2026-07-05): Initial Stage E handoff in the upstream planning run.
- v2 (2026-07-20): Refreshed failure scenarios and risk coverage.

## Stage
STAGE_E Pre-Mortem And Risk Register

## Inputs (LOAD)
- `pack/intent.md`

## Inputs (DISK)
- `pack/intent_lock_report.md`

## Skill Routing Contract
- Skill used (or `NONE`): `NONE`

## Outputs Produced (paths)
- `pack/premortem.md`
- `pack/risk_register.md`

## Verification Steps Recommended
- `./scripts/factoryctl stage-lint --run RUN_20260720_0708_live_coding_adapter_eval_refresh --stage E`

## Exit Criteria Status
- PASS

## Notes
- Top risks include accidental probing, mutation, source contradiction, context duplication, trace privacy, and recommendation bias.
