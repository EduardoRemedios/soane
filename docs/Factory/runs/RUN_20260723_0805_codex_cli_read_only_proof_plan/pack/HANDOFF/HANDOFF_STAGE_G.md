# Handoff Stage G

## Version

v2

## Change Log

- v1 (2026-07-23): Sequenced offline implementation and one-shot live proof.
- v2 (2026-07-23): Added exact credential-isolation work to MS-02.

## Stage

STAGE_G Micro-Sprint Sequencing

## Inputs (LOAD)

- `pack/intent.md`
- `pack/risk_register.md`
- `pack/verification_plan.md`

## Inputs (DISK)

- `pack/traceability_matrix.md`
- `pack/intent_synthesis.md`

## Skill Routing Contract

- Skill used (or `NONE`): `NONE`

## Outputs Produced (paths)

- `pack/micro_sprints.md`

## Verification Steps Recommended

- `./scripts/factoryctl stage-lint --run RUN_20260723_0805_codex_cli_read_only_proof_plan --stage G`

## Exit Criteria Status

- PASS

## Notes

- Provider use is isolated to MS-04 after all offline gates and a distinct human
  authorization checkpoint.
- MS-04 has a terminal no-retry rule under every outcome.
