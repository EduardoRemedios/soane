# Execution Prompt: VEH-V1-001

Execute only the locked `VEH-V1-001` documentation envelope.

## Authorization

- Execution Mode: `EXECUTION_ENABLED`
- Human authorization: current Codex conversation, 2026-07-12, "I agree proceed"
- Downstream fan-out: not approved

## Required Read

- `pack/VEH-V1-001_ENVELOPE.md`
- `pack/micro_sprints.md`
- `pack/verification_plan.md`
- `pack/traceability_matrix.md`
- `pack/PACK_AUDIT_REPORT.md`

## Constraints

- Preserve the eight-file non-run budget and all no-touch paths.
- Do not change runtime code, schemas, object seeds, Factory Core, dependencies, APIs, UI, providers, or portfolio ownership.
- Stop on any envelope stop condition.
- Run every verification-manifest command and produce `VALIDATION_CLOSEOUT_REPORT.md`.
