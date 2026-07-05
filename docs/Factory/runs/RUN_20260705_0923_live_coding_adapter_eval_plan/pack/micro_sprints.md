# Micro-Sprints: LCAE-V0-001

## Version

v1

## Change Log

- v1 (2026-07-05): Initial Stage G micro-sprint sequence.

## Sprint Sequence

### MS-00 Verification Scaffold

- Objective: Add tests for adapter profile loading, safety gates, recommendation output, no-live-call behavior, and regression coverage.
- Inputs: `verification_plan.md`, `fixtures/README.md`
- Outputs: focused future tests.
- Entry Criteria: Human Go for `LCAE-V0-001`.
- Exit Criteria: Tests cover VC-001 through VC-010.
- Stop/Go Gate: Stop if tests require credentials, network, dependency installs, live CLIs, SDKs, APIs, or external repositories.

### MS-01 Source-Backed Adapter Profiles

- Objective: Add deterministic profiles for Codex CLI, Cursor CLI, Cursor SDK, OpenAI SDK, and OpenAI Agents SDK.
- Inputs: `external_source_review.md`, existing adapter twins.
- Outputs: profile fixtures and loader.
- Entry Criteria: MS-00 complete.
- Exit Criteria: Profiles include source refs, modes, auth, mutation controls, structured output, traceability, and limitations.
- Stop/Go Gate: Stop if a profile depends on a live provider probe.

### MS-02 Safety And Authority Gates

- Objective: Implement deterministic evaluation rules for auth, authority, mutation controls, repository scope, traceability, output capture, and candidate review.
- Inputs: Project Memory adapter twin contract and coding harness behavior.
- Outputs: evaluator service and blocked cases.
- Entry Criteria: MS-01 complete.
- Exit Criteria: Unsafe or under-specified surfaces are blocked with reason codes.
- Stop/Go Gate: Stop if capability is treated as authority.

### MS-03 Recommendation Matrix

- Objective: Produce deterministic recommendation output for first live proof surface and rejected alternatives.
- Inputs: evaluated profiles and safety gates.
- Outputs: text/JSON matrix or report.
- Entry Criteria: MS-02 complete.
- Exit Criteria: Recommendation is explainable and does not call live surfaces.
- Stop/Go Gate: Stop if recommendation requires credential access.

### MS-04 CLI Wrapper

- Objective: Add a thin local CLI command to inspect evaluation profiles and recommendations.
- Inputs: evaluator service.
- Outputs: service-delegating command.
- Entry Criteria: MS-03 complete.
- Exit Criteria: CLI emits readable text and JSON without live side effects.
- Stop/Go Gate: Stop if CLI owns evaluation semantics.

### MS-05 Validation Closeout

- Objective: Validate implementation against this pack.
- Inputs: verification plan, traceability matrix, tests, implementation diff.
- Outputs: validation closeout report and state docs.
- Entry Criteria: Earlier micro-sprints complete.
- Exit Criteria: Required tests, lint, pack checks, and diff hygiene pass.
- Stop/Go Gate: Stop if any critical verification check fails.

## Bounded Deferrals

- Live invocation is deferred.
- Credential provisioning is deferred.
- Dependency installation is deferred.
- Product UI and Workspace Shell are deferred.
