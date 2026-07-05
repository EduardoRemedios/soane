# Execution Prompt: BMR-CPH-V0-001 Brownfield Multi-Repo Coding Proof

## Version

v1

## Change Log

- v1 (2026-07-05): Execution prompt generated after explicit human Go.

## Run Metadata

- RUN_ID: `RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan`
- Sprint ID: `BMR-CPH-V0-001`
- Created: 2026-07-05
- Source Pack: `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/pack/`

## Purpose

Implement the smallest deterministic extension to Coding Proof Harness v0 that proves Brownfield multi-repository system-boundary handling. Keep the proof local, fixture-backed, and mock-first. Do not introduce live providers, real repository access, persistence, product UI, Workspace Shell, or neighbouring portfolio responsibilities.

## Required Read Order

1. `docs/PROJECT_STATE.md`
2. `docs/ROADMAP.md`
3. `docs/Factory/ORCHESTRATION.md`
4. `docs/Factory/SCRATCHPAD.md` only `## Active Pitfalls (Mandatory)`
5. `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/pack/intent.md`
6. `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/pack/verification_plan.md`
7. `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/pack/traceability_matrix.md`
8. `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/pack/verification_manifest.yaml`
9. `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/pack/micro_sprints.md`
10. `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/pack/BMR-CPH-V0-001_ENVELOPE.md`
11. `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/pack/PACK_AUDIT_REPORT.md`

## Skill Routing Contract

- Use the `factory-execution-closeout` skill for implementation closeout against the approved pack.
- No dedicated skill applies to the local fixture and service edits; execute via stage contract and repository tests.

## Hard Guardrails

- Apply SIMPLE-CODE-GATE v2.
- Preserve existing Greenfield and single-repo Brownfield fixture behavior.
- Keep workflow service-delegating.
- Preserve Project Memory versus generated Markdown separation.
- Preserve capability and authority separation.
- Do not call live models, live CLIs, live SDKs, external connectors, databases, real repositories, or mutate repositories.
- Do not treat proposed provider output as accepted truth.
- Keep Workspace Shell and product UI out of scope.

## Verification Contract

Run every check in `pack/verification_manifest.yaml` plus any focused tests added during implementation. A failed check marked `halt_on_failure: true` blocks closeout.

## Final Exit Checklist

- [x] Scope delivered per envelope and micro-sprints.
- [x] Verification commands passed.
- [x] Evidence artifacts and validation closeout updated.
- [x] `PROJECT_STATE.md`, `ROADMAP.md`, and `CHANGELOG.md` updated.
- [x] Residual risks and deferrals listed.
