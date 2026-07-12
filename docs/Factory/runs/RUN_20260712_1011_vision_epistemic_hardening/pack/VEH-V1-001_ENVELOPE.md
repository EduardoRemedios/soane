# Sprint Envelope: VEH-V1-001

## Version
v3

## Change Log
- v1 (2026-07-12): Stage H envelope.
- v2 (2026-07-12): Added explicit no-touch and semantic consistency checks after Stage I.
- v3 (2026-07-12): Corrected the constitutional file set to include Governance Model within the existing total budget.

## Objective

Apply the locked vision and epistemic-model amendments without changing runtime behavior or portfolio ownership.

## Allowed Files

- `docs/VISION.md`
- `docs/CORE_CONCEPTS.md`
- `docs/GOVERNANCE_MODEL.md`
- `docs/PROJECT_MEMORY_ARCHITECTURE.md`
- `docs/THINKING_ENGINE_ARCHITECTURE.md`
- `docs/INTEGRATION_ARCHITECTURE.md`
- `docs/PROJECT_STATE.md`
- `docs/ROADMAP.md`
- `docs/CHANGELOG.md`
- this run root

## File-Touch Budget

- MS-01: at most 3 constitutional files.
- MS-02: at most 3 architecture files.
- MS-03: exactly the 3 state-hygiene files when relevant.
- MS-04: this run's closeout only.
- Total non-run implementation budget: at most 8 files.

## Required Changes

- Implement every locked requirement using concise additions or precise wording changes.
- Preserve external source authority and all portfolio ownership boundaries.
- State runtime deferrals wherever new doctrine could be mistaken for implementation.
- Keep cross-project promotion fail-closed and Markdown write-back review-gated.

## No-Touch Constraints

- No changes under `soane/`, `scripts/`, `tests/`, dependencies, or `docs/project_memory/objects/`.
- No Factory Core doctrine changes.
- No database, schema, API, UI, provider, or live integration work.

## Verification

- Follow `verification_plan.md`, `traceability_matrix.md`, and `verification_manifest.yaml`.
- Run exact-term and contradiction scans for Claim, source authority, delegation, Knowledge Scope, Markdown modes, Decision Review, and success measures.
- Run knowledge lint, context-index refresh, full tests, pack lint, and `git diff --check` before closeout.

## Stop Conditions

- Any wording makes Soane the owner of external authority, proof, missions, runtime, or source-system records.
- A concept requires an unapproved runtime change.
- Cross-project access or generated write-back becomes implicit.
- Changed paths exceed the budget.

## Completion

Completion requires all verification checks to pass and execution-closeout evidence to find no scope drift.
