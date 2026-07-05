# Micro-Sprints

## Version

v1

## Change Log

- v1 (2026-07-05): Initial Stage G micro-sprint sequence.

## Sprint Sequence

### MS-00 Verification Scaffold

- Objective: Add focused tests for multi-repo fixture loading, readiness, blocked behavior, workflow summary, and regression coverage.
- Inputs: `verification_plan.md`, `fixtures/README.md`
- Outputs: future focused tests.
- Entry Criteria: Human Go for `BMR-CPH-V0-001`.
- Exit Criteria: Tests cover VC-001 through VC-010.
- Stop/Go Gate: Stop if tests require live repositories, providers, or command execution.

### MS-01 Multi-Repo Fixture Contract

- Objective: Add deterministic ready and blocked multi-repo Brownfield fixtures.
- Inputs: existing coding proof fixtures and Intake fixture schema.
- Outputs: fixture files and fixture loader compatibility.
- Entry Criteria: MS-00 complete.
- Exit Criteria: Fixtures express repository map, service boundary, integration contracts, ownership, build/test responsibility, authority path, and expected ready state.
- Stop/Go Gate: Stop if fixture format requires live repo access.

### MS-02 Intake And Context Semantics

- Objective: Preserve multi-repo intake classification and expose repository-boundary context to the harness.
- Inputs: `soane.thinking_engine.intake`, `soane.project_memory.context`
- Outputs: local service behavior and tests.
- Entry Criteria: MS-01 complete.
- Exit Criteria: Ready fixture is `brownfield_multi_repo`; blocked fixture is blocked; task-relevant context is inspectable.
- Stop/Go Gate: Stop if readiness logic becomes duplicated across modules.

### MS-03 Harness Multi-Repo Execution Path

- Objective: Extend Coding Proof Harness summary and mocked provider path for multi-repo Brownfield fixtures.
- Inputs: existing `run_coding_proof` behavior.
- Outputs: ready and blocked harness behavior.
- Entry Criteria: MS-02 complete.
- Exit Criteria: Ready fixture creates mocked Provider Invocation and candidate output; blocked fixture creates neither.
- Stop/Go Gate: Stop if live provider or repo mutation is introduced.

### MS-04 Workflow Summary

- Objective: Extend Coding Harness Workflow output for multi-repo repository map, relevant repositories, and blocked state.
- Inputs: shared harness result.
- Outputs: text and JSON summary behavior.
- Entry Criteria: MS-03 complete.
- Exit Criteria: CLI lists and runs multi-repo fixtures and exposes system-boundary state without owning readiness logic.
- Stop/Go Gate: Stop if CLI duplicates harness semantics.

### MS-05 Validation Closeout

- Objective: Validate implementation against this pack.
- Inputs: verification plan, traceability matrix, tests, implementation diff.
- Outputs: validation closeout report and state docs.
- Entry Criteria: Earlier micro-sprints complete.
- Exit Criteria: Required tests, lint, pack checks, and diff hygiene pass.
- Stop/Go Gate: Stop if any critical verification check fails.

## Bounded Deferrals

- Live providers are deferred.
- Live repository audit and command execution are deferred.
- Persistence is deferred.
- Workspace Shell and product UI are deferred.
