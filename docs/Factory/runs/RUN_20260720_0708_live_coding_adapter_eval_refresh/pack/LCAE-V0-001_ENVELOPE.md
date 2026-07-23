# Sprint Envelope: LCAE-V0-001 Live Coding Adapter Evaluation

## Version

v3

## Change Log

- v1 (2026-07-05): Initial Stage H envelope in the upstream planning run.
- v2 (2026-07-20): Refreshed implementation boundary, context reuse, hard gates, files, and verification.
- v3 (2026-07-23): Recorded human Go for the locked deterministic implementation.

## Sprint ID

`LCAE-V0-001`

## Execution Mode

`EXECUTION_ENABLED`

Human Go was recorded in the current Codex task on 2026-07-23. Authorization is
limited to this fixture-only deterministic implementation; live adapter use and
downstream fan-out remain unapproved.

## Objective

Implement a fixture-only, source-backed Thinking Engine evaluator that recommends, blocks, or defers five candidate live coding adapter surfaces without invoking them.

## In Scope

- Typed profiles for Codex CLI, Cursor CLI, Cursor SDK, OpenAI SDK, and OpenAI Agents SDK.
- Official source URLs, access dates, evidence kinds, contradiction states, limitations, and source revalidation checks.
- Non-compensable gates for contradiction, read-only containment, repository scope, authority/permission, trace privacy, and candidate review.
- Versioned deterministic scoring and tie behavior for gate-passing surfaces only.
- Existing agent-context text/JSON payload as the bounded repository-context evidence input.
- Explainable local text/JSON recommendation or no-recommendation output.
- Thin service-delegating CLI workflow.
- Focused, regression, no-touch, and closeout evidence.

## Out Of Scope

- provider, model, CLI, SDK, API, cloud-agent, shell-through-provider, or external-repository invocation
- credentials, environment keys, auth state, provider config, installed provider version, or session inspection
- dependency installation
- evaluated-surface repository mutation
- live behavior, sandbox, network, cost, latency, or trace measurement
- Codex SDK as an evaluated surface
- alternate repository scanner, context ranker, graph traversal, or semantic code intelligence
- automatic Project Memory write, promotion, or lifecycle change
- persistence, product UI, Workspace Shell, mission execution, or neighbouring-product implementation

## Expected Files

- `soane/thinking_engine/adapter_evaluation.py`
- `soane/thinking_engine/adapter_evaluation_workflow.py`
- `tests/fixtures/live_adapter_evaluation/*.json`
- `tests/test_thinking_engine_adapter_evaluation.py`
- `tests/test_thinking_engine_adapter_evaluation_workflow.py`
- bounded updates to `soane/thinking_engine/__init__.py` only if public exports are necessary
- `VALIDATION_CLOSEOUT_REPORT.md`, `docs/PROJECT_STATE.md`, `docs/ROADMAP.md`, `docs/CHANGELOG.md`

## File-Touch Budget

| Area | Budget |
| --- | --- |
| Evaluator service, workflow, optional exports | up to 3 files |
| Source profiles and negative fixtures | up to 8 files |
| Focused tests | up to 2 files |
| Closeout and canonical state | up to 4 files |
| Total non-pack files | up to 17 files |
| Deletes | 0 |

## Required Micro-Sprints

- MS-00 Verification Scaffold
- MS-01 Source Profile Contract
- MS-02 Hard Gates, Context Input, And Recommendation
- MS-03 Thin CLI Workflow
- MS-04 Regression And No-Touch Proof
- MS-05 Validation Closeout

## SIMPLE-CODE-GATE V2

- Keep profile parsing, gates, scoring, and rendering in their named owners.
- Prefer immutable dataclasses, enums, pure functions, and stable reason codes.
- Add no provider abstraction, plugin registry, query language, persistence seam, or generic scoring framework.
- Use standard-library JSON and argparse only.
- Fail explicitly; do not normalize malformed or contradictory evidence.

## Required Verification

Run every command in `verification_plan.md`, including focused evaluator/workflow tests, existing context/graph/adapter/review/coding regressions, the full suite, compileall, knowledge lint, context refresh, this run's pack lint, and diff hygiene.

Before closeout, confirm:

- no provider package or subprocess invocation path
- no access to credential-bearing environment names, provider config roots, login status, or session stores
- no network client or external repository operation
- no alternate scan, retrieval, graph, persistence, or memory mutation path
- no Codex SDK profile
- no hard blocker can be score-compensated

## Stop Gates

- Stop on any provider/user-state discovery or side effect.
- Stop if Cursor's source contradiction is silently resolved.
- Stop if Codex CLI is hard-coded as winner.
- Stop if context selection or graph semantics are duplicated.
- Stop if output is promoted or treated as live authorization.
- Stop if implementation exceeds the budget or requires a dependency.

## Review Handoff

Implementation must produce a validation closeout mapping VC-001 through VC-014 to exact tests and measured artifacts. Any first live read-only proof remains a separate Factory run with separate human authorization.
