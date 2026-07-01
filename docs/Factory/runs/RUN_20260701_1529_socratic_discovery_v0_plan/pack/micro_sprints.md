# Micro-Sprints

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage G micro-sprint sequence.

## Sprint Sequence

### MS-00 Verification Scaffold

- Objective: Create deterministic Socratic Discovery fixture and test skeletons.
- Inputs: `verification_plan.md`, `fixtures/README.md`
- Outputs: future test file and fixture directory.
- Entry Criteria: Human Go for `SD-V0-001`.
- Exit Criteria: Test skeleton names cover VC-001 through VC-011.
- Stop/Go Gate: Stop if tests require live model calls, live integrations, or persistence.

### MS-01 Discovery Session Contract

- Objective: Define local session, question, answer, hypothesis, and stop-condition objects.
- Inputs: `soane/thinking_engine/intake.py`, `soane/project_memory/review.py`
- Outputs: future discovery contract module or focused extension.
- Entry Criteria: MS-00 complete.
- Exit Criteria: Contract supports session state, question source reasons, candidate answers, candidate hypotheses, and stop conditions.
- Stop/Go Gate: Stop if implementation collapses evidence, authority, and readiness into one vague state.

### MS-02 Question Generation Service

- Objective: Generate deterministic questions from Context Baseline gaps and playbook references.
- Inputs: MS-01 contract and Thinking Engine Intake v0 baseline objects.
- Outputs: shared service functions for question generation.
- Entry Criteria: MS-01 complete.
- Exit Criteria: Category-specific fixtures pass and every question has a source reason.
- Stop/Go Gate: Stop if questions are generic or untraceable.

### MS-03 Answer Capture And Hypothesis Service

- Objective: Capture answers and derive hypotheses as Project Memory candidates.
- Inputs: MS-01 and MS-02 service functions.
- Outputs: shared service functions for answer and hypothesis candidate generation.
- Entry Criteria: MS-02 complete.
- Exit Criteria: Answers and hypotheses remain candidates with provenance, uncertainty state, and evidence-gap links.
- Stop/Go Gate: Stop if outputs bypass Candidate Review and Promotion.

### MS-04 Stop Conditions

- Objective: Implement deterministic discovery state transitions.
- Inputs: MS-01 through MS-03 outputs.
- Outputs: service logic and tests for blocked, needs evidence, needs authority, and ready for planning.
- Entry Criteria: MS-03 complete.
- Exit Criteria: Stop-condition tests pass for all required states.
- Stop/Go Gate: Stop if ready for planning implies execution authority.

### MS-05 Optional Thin CLI/TUI Wrapper

- Objective: Add a small wrapper only if service semantics are stable and file budget remains.
- Inputs: shared discovery service functions.
- Outputs: optional CLI command or thin TUI screen over the service.
- Entry Criteria: MS-04 complete and file budget available.
- Exit Criteria: Wrapper delegates to shared service and adds no discovery logic of its own.
- Stop/Go Gate: Skip this micro-sprint if it risks becoming product workflow or Workspace Shell.

### MS-06 Validation Closeout

- Objective: Validate the implementation against the pack.
- Inputs: verification plan, traceability matrix, tests, implementation diff.
- Outputs: future validation closeout report.
- Entry Criteria: Earlier micro-sprints complete or explicitly skipped.
- Exit Criteria: Required tests, lint, pack reference checks, and diff hygiene pass.
- Stop/Go Gate: Stop if any critical verification check fails.

## Bounded Deferrals

- Product UI is deferred.
- Database persistence is deferred.
- Live adapters and connectors are deferred.
- Live model calls are deferred.
- Workspace Shell architecture is deferred.
