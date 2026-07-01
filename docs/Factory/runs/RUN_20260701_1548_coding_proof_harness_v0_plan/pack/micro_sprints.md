# Micro-Sprints

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage G micro-sprint sequence.

## Sprint Sequence

### MS-00 Verification Scaffold

- Objective: Create deterministic coding harness fixture and test skeletons.
- Inputs: `verification_plan.md`, `fixtures/README.md`
- Outputs: future focused test file and fixture directory.
- Entry Criteria: Human Go for `CPH-V0-001`.
- Exit Criteria: Test skeleton names cover VC-001 through VC-011.
- Stop/Go Gate: Stop if tests require live provider calls, repository mutation, or persistence.

### MS-01 Harness Contract

- Objective: Define local harness request, result, provider selection, and output-candidate objects.
- Inputs: Intake, Discovery, Project Memory context, adapter twin, and review modules.
- Outputs: future coding harness contract module.
- Entry Criteria: MS-00 complete.
- Exit Criteria: Contract supports Greenfield/Brownfield inputs, task context, provider selection, invocation record, candidate output, and review state.
- Stop/Go Gate: Stop if contract collapses capability, authority, evidence, and candidate truth.

### MS-02 Service Composition

- Objective: Compose existing Intake v0, Socratic Discovery v0, Project Memory context assembly, adapter twins, and Candidate Review services.
- Inputs: MS-01 contract and existing local primitives.
- Outputs: shared service functions for running the mock coding proof path.
- Entry Criteria: MS-01 complete.
- Exit Criteria: Harness does not duplicate service logic and focused tests pass.
- Stop/Go Gate: Stop if implementation reimplements existing primitives.

### MS-03 Provider Output Candidate Flow

- Objective: Capture proposed provider output as Project Memory candidates and prove review-gated promotion.
- Inputs: MS-01 and MS-02.
- Outputs: candidate output generation and review path tests.
- Entry Criteria: MS-02 complete.
- Exit Criteria: Proposed output remains non-current until Candidate Review and Promotion accepts it.
- Stop/Go Gate: Stop if proposed output bypasses review.

### MS-04 Greenfield/Brownfield Fixtures

- Objective: Prove distinct Greenfield and Brownfield coding behavior.
- Inputs: MS-02 and MS-03.
- Outputs: fixtures and tests for Greenfield, Brownfield ready, and Brownfield blocked states.
- Entry Criteria: MS-03 complete.
- Exit Criteria: Brownfield audit/authority gaps block ready-for-planning when required.
- Stop/Go Gate: Stop if Brownfield becomes a generic coding path.

### MS-05 Optional Thin CLI/TUI Wrapper

- Objective: Add a small wrapper only if service semantics are stable and file budget remains.
- Inputs: shared coding harness service functions.
- Outputs: optional CLI command or TUI screen.
- Entry Criteria: MS-04 complete and file budget available.
- Exit Criteria: Wrapper delegates to shared service and adds no harness logic.
- Stop/Go Gate: Skip if it risks becoming Workspace Shell or product UX.

### MS-06 Validation Closeout

- Objective: Validate implementation against the pack.
- Inputs: verification plan, traceability matrix, tests, implementation diff.
- Outputs: future validation closeout report.
- Entry Criteria: Earlier micro-sprints complete or explicitly skipped.
- Exit Criteria: Required tests, lint, pack reference checks, and diff hygiene pass.
- Stop/Go Gate: Stop if any critical verification check fails.

## Bounded Deferrals

- Product UI is deferred.
- Workspace Shell is deferred.
- Database persistence is deferred.
- Live provider adapters are deferred.
- External repository mutation is deferred.
