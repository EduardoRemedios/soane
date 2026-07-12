# Execution Prompt: MMI-V0-001

Execute only the locked `MMI-V0-001` envelope.

## Authorization

- Execution Mode: `EXECUTION_ENABLED`
- Human authorization: current Codex conversation, 2026-07-12, `Go`
- Downstream fan-out: not approved

## Required Read

- `pack/MMI-V0-001_ENVELOPE.md`
- `pack/micro_sprints.md`
- `pack/verification_plan.md`
- `pack/traceability_matrix.md`
- `pack/PACK_AUDIT_REPORT.md`

## Constraints

- Preserve proposed/asserted Claim candidates and the existing review boundary.
- Enforce repository path containment and fail-closed ambiguity.
- Do not add persistence, dependencies, semantic/model extraction, write-back, wider Knowledge Scope, UI, providers, live adapters, or portfolio integration.
- Stop on any envelope stop condition.
- Run every verification-manifest command and produce `VALIDATION_CLOSEOUT_REPORT.md`.
