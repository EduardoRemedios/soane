# Handoff Stage D

## Version

v2

## Change Log

- v1 (2026-07-23): Locked the hardened intent through Purple adjudication.
- v2 (2026-07-23): Re-locked intent v3 after second-cycle credential review.

## Stage

STAGE_D Purple Intent Lock

## Inputs (LOAD)

- `pack/intent.md`
- `pack/intent_redteam.md`
- `pack/intent_synthesis.md`

## Inputs (DISK)

- `pack/external_source_review.md`
- `KNOWLEDGE_LINT.txt`

## Skill Routing Contract

- Skill used (or `NONE`): `factory-purple-gate`

## Outputs Produced (paths)

- `pack/intent_lock_report.md`

## Verification Steps Recommended

- `./scripts/factoryctl stage-lint --run RUN_20260723_0805_codex_cli_read_only_proof_plan --stage D`

## Exit Criteria Status

- PASS

## Notes

- Verdict: PASS.
- Isolation is locked as a proof precondition, not a general platform deliverable.
- Direct-key auth is blocked without parent-process isolation evidence; the
  preferred route is an external single-run credential-isolating proxy.
- No unresolved Critical finding or unapproved scope expansion remains.
