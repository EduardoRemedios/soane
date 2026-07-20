# Handoff Stage A

## Version
v2

## Change Log
- v1 (2026-07-05): Initial Stage A handoff in the upstream planning run.
- v2 (2026-07-20): Refreshed Stage A against current repository and official-source evidence.

## Stage
STAGE_A Intent Contracting

## Inputs (LOAD)
- `raw_brief.md`
- `CONTEXT_RECALL_REPORT.md`

## Inputs (DISK)
- `KNOWLEDGE_LINT.txt`
- `EXECUTION_MODE.txt`

## Skill Routing Contract
- Skill used (or `NONE`): `factory-root-planner`

## Outputs Produced (paths)
- `pack/intent.md`
- `pack/external_source_review.md`

## Verification Steps Recommended
- `./scripts/factoryctl stage-lint --run RUN_20260720_0708_live_coding_adapter_eval_refresh --stage A`

## Exit Criteria Status
- PASS

## Notes
- Generated recall was repaired through direct review of the five unresolved production-code sources.
- Current official-source review found a material Cursor CLI write-control contradiction.
