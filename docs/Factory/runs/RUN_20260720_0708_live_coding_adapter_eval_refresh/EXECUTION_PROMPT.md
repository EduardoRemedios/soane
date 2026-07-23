# Execution Prompt: LCAE-V0-001

## Version

v1

## Change Log

- v1 (2026-07-23): Generated after Stage I2 PASS and human Go.

## Run Metadata

- RUN_ID: `RUN_20260720_0708_live_coding_adapter_eval_refresh`
- Sprint ID: `LCAE-V0-001`
- Source Pack: `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/pack/`

## Purpose

Implement the locked fixture-only, source-backed Thinking Engine evaluator for the
five approved adapter surfaces. The evaluator recommends, blocks, or defers
surfaces from committed evidence without invoking any provider.

## Required Read Order

1. `docs/PROJECT_STATE.md`
2. `docs/ROADMAP.md`
3. `pack/intent.md`
4. `pack/risk_register.md`
5. `pack/verification_plan.md`
6. `pack/traceability_matrix.md`
7. `pack/verification_manifest.yaml`
8. `pack/micro_sprints.md`
9. `pack/LCAE-V0-001_ENVELOPE.md`
10. `pack/PACK_AUDIT_REPORT.md`

## Hard Guardrails

- Apply SIMPLE-CODE-GATE v2.
- Evaluate exactly Codex CLI, Cursor CLI, Cursor SDK, OpenAI SDK, and OpenAI Agents SDK.
- Use committed profiles and explicit existing agent-context JSON only.
- Run hard gates before scoring; a score never compensates for a blocker.
- Do not invoke providers, inspect provider/user state, install dependencies, access
  external repositories, or mutate the repository through an evaluated surface.
- Do not add persistence, a context or graph engine, UI, mission execution, or Codex SDK.
- Keep outputs local and explicitly documentation-level, unmeasured, and non-authorizing.

## Micro-Sprint Sequence

1. MS-00: Add focused fixtures and failing verification.
2. MS-01: Implement typed source profiles and validation.
3. MS-02: Implement hard gates, context preservation, scoring, and recommendation.
4. MS-03: Add the thin text/JSON CLI.
5. MS-04: Run regression and no-touch proofs.
6. MS-05: Reconcile canonical state and produce closeout.

## Verification Contract

Run every check in `pack/verification_manifest.yaml` in order. Any
`halt_on_failure: true` failure blocks closeout.

## Final Exit Checklist

- Scope delivered within the file budget.
- VC-001 through VC-014 mapped to exact evidence.
- Source access dates match the 2026-07-23 revalidation.
- No provider or repository side effect path exists.
- Canonical state and validation closeout are updated truthfully.
- Any live read-only proof remains a separate human-authorized Factory run.
