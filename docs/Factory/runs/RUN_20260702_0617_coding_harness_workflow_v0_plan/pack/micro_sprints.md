# Micro-Sprints

## Version

v1

## Change Log

- v1 (2026-07-02): Initial Stage G micro-sprint sequence.

## Sprint Sequence

### MS-00 Verification Scaffold

- Objective: Create focused CLI workflow test skeletons.
- Inputs: `verification_plan.md`, `fixtures/README.md`
- Outputs: future focused test file.
- Entry Criteria: Human Go for `CHW-V0-001`.
- Exit Criteria: Test skeleton covers VC-001 through VC-010.
- Stop/Go Gate: Stop if tests require live providers, persistence, or repository mutation.

### MS-01 CLI Command Surface

- Objective: Add a thin CLI entry point or subcommand for the coding harness workflow.
- Inputs: `soane.thinking_engine.coding_harness`.
- Outputs: fixture list and fixture run commands.
- Entry Criteria: MS-00 complete.
- Exit Criteria: CLI lists fixtures and runs a selected fixture through shared service functions.
- Stop/Go Gate: Stop if CLI duplicates harness logic.

### MS-02 Text And JSON Summary

- Objective: Summarize harness results in human-readable text and optional JSON.
- Inputs: MS-01 command surface and `CodingHarnessResult`.
- Outputs: summary renderer or CLI output helpers.
- Entry Criteria: MS-01 complete.
- Exit Criteria: Summary includes readiness, discovery, context, provider, candidate, review, live-call, and repository-mutation fields.
- Stop/Go Gate: Stop if summary hides candidate/review state.

### MS-03 Candidate Review Status

- Objective: Prove proposed output remains candidate-only unless reviewed.
- Inputs: MS-02 summary and Candidate Review service.
- Outputs: tests for candidate-only and reviewed states.
- Entry Criteria: MS-02 complete.
- Exit Criteria: CLI or summary exposes review status without promoting output implicitly.
- Stop/Go Gate: Stop if output bypasses Candidate Review and Promotion.

### MS-04 Brownfield Blocked Workflow

- Objective: Prove blocked Brownfield fixture remains inspectable without provider invocation.
- Inputs: existing Brownfield blocked coding harness fixture.
- Outputs: focused test and summary behavior.
- Entry Criteria: MS-03 complete.
- Exit Criteria: blocked summary shows no provider invocation or output candidate.
- Stop/Go Gate: Stop if blocked flow appears ready for provider execution.

### MS-05 Optional Thin TUI Wrapper

- Objective: Add a minimal TUI screen only if CLI semantics are stable and file budget remains.
- Inputs: shared workflow summary functions.
- Outputs: optional service-delegating TUI navigation.
- Entry Criteria: MS-04 complete and file budget available.
- Exit Criteria: TUI adds no workflow logic.
- Stop/Go Gate: Skip if it risks becoming product shell or UX design.

### MS-06 Validation Closeout

- Objective: Validate implementation against the pack.
- Inputs: verification plan, traceability matrix, tests, implementation diff.
- Outputs: future validation closeout report.
- Entry Criteria: Earlier micro-sprints complete or explicitly skipped.
- Exit Criteria: Required tests, lint, pack checks, and diff hygiene pass.
- Stop/Go Gate: Stop if any critical verification check fails.

## Bounded Deferrals

- TUI may be deferred.
- Live providers are deferred.
- Repository mutation is deferred.
- Persistence is deferred.
- Workspace Shell and product UI are deferred.
