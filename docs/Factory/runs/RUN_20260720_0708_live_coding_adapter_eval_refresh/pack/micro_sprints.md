# Micro-Sprints: LCAE-V0-001

## Version

v2

## Change Log

- v1 (2026-07-05): Initial Stage G sequence in the upstream planning run.
- v2 (2026-07-20): Sequenced current-source profiles, hard gates, context reuse, and no-touch proofs.

## Sprint Sequence

### MS-00 Verification Scaffold

- Objective: Add failing tests and fixtures for profile validation, hard blockers, deterministic recommendation, context payload reuse, no-touch behavior, and CLI output.
- Inputs: `verification_plan.md`, `traceability_matrix.md`, fixture contract.
- Outputs: focused tests and negative fixtures covering VC-001 through VC-012.
- Entry Criteria: Explicit human Go for implementation and current official-source revalidation.
- Exit Criteria: Tests fail for missing implementation and do not invoke providers, credentials, network, or external repositories.
- Stop/Go Gate: Stop if any test requires installed provider tooling, auth state, dependency installation, or evaluated-surface execution.

### MS-01 Source Profile Contract

- Objective: Implement typed profile parsing and exactly five source-backed profile fixtures.
- Inputs: refreshed `external_source_review.md`.
- Outputs: profile types, loader, validation, and five fixtures under `tests/fixtures/live_adapter_evaluation/`.
- Entry Criteria: MS-00 complete and source access dates confirmed.
- Exit Criteria: Valid profiles preserve every required dimension; invalid, unknown, duplicate, contradictory, and stale-without-review cases fail closed or carry hard blockers as specified.
- Stop/Go Gate: Stop if implementation discovers providers or reads environment/config/session state.

### MS-02 Hard Gates, Context Input, And Recommendation

- Objective: Implement pure hard-gate and scoring functions over validated profiles plus existing agent-context payloads.
- Inputs: profile loader, fixed criteria, existing `agent-context` JSON contract.
- Outputs: evaluation result with eligibility, reason codes, evidence refs, ranked recommendation or no recommendation, and preserved context explanations.
- Entry Criteria: MS-01 complete.
- Exit Criteria: Hard blockers precede scoring; results are order-independent; no scanner, retrieval, graph, persistence, or memory-write path exists.
- Stop/Go Gate: Stop if a score can override a blocker or context semantics are duplicated.

### MS-03 Thin CLI Workflow

- Objective: Add a service-delegating text/JSON command for explicit profile and context inputs.
- Inputs: evaluator service.
- Outputs: `python3 -m soane.thinking_engine.adapter_evaluation_workflow`.
- Entry Criteria: MS-02 complete.
- Exit Criteria: CLI emits deterministic recommendation, alternatives, blockers, sources, and context status with no provider side effects.
- Stop/Go Gate: Stop if CLI owns evaluation rules or implicitly discovers provider/user state.

### MS-04 Regression And No-Touch Proof

- Objective: Run focused and repository regressions plus static/no-touch checks.
- Inputs: implementation diff and verification plan.
- Outputs: VC-001 through VC-014 evidence.
- Entry Criteria: MS-03 complete.
- Exit Criteria: Focused/full tests, compile, knowledge lint, context refresh, pack lint, scope scan, and diff hygiene pass.
- Stop/Go Gate: Stop on any side-effect, scope, compatibility, or hard-gate failure.

### MS-05 Validation Closeout

- Objective: Reconcile evidence and canonical repository state without authorizing live use.
- Inputs: verification output, implementation diff, pack.
- Outputs: `VALIDATION_CLOSEOUT_REPORT.md`, state docs, and bounded next-proof recommendation.
- Entry Criteria: MS-04 complete.
- Exit Criteria: Every check maps to evidence; residual uncertainty and separate live-proof requirements are explicit.
- Stop/Go Gate: Stop if closeout implies deterministic documentation evaluation proves live safety.

## Bounded Deferrals

- Live provider behavior, credentials, sandbox, network, mutation, cost, latency, and traces: MS-05 records requirements for a separate live-proof pack.
- Codex SDK evaluation: MS-05 records a backlog candidate only.
- Persistence and Project Memory profile promotion: no implementation in this sprint; reconsider after persistence access patterns are approved.
- Product UI and Workspace Shell: remain outside this sprint.
