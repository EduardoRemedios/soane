# Micro-Sprints

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage G micro-sprint sequence.

## Sprint Sequence

### MS-00 Verification Scaffold

- Objective: Create deterministic candidate review fixture and test skeletons.
- Inputs: `verification_plan.md`, `fixtures/README.md`
- Outputs: future test file and fixture directory.
- Entry Criteria: Human Go for `CRP-V0-001`.
- Exit Criteria: Test skeleton names cover VC-001 through VC-010.
- Stop/Go Gate: Stop if tests require live integrations or persistence.

### MS-01 Review Contract

- Objective: Define local review decision objects, allowed outcomes, and validation errors.
- Inputs: `soane/project_memory/contract.py`, `soane/project_memory/semantics.py`
- Outputs: future candidate review contract module or focused extension.
- Entry Criteria: MS-00 complete.
- Exit Criteria: Review outcomes support accept, reject, defer, amend, and keep open.
- Stop/Go Gate: Stop if implementation embeds authority into capability or accepted memory.

### MS-02 Promotion Service

- Objective: Implement deterministic local service functions for reviewing candidates.
- Inputs: MS-01 contract.
- Outputs: shared service functions that preserve provenance and produce reviewed outputs.
- Entry Criteria: MS-01 complete.
- Exit Criteria: Service tests pass for accepted, rejected, deferred, amended, unauthorized, and conflicting cases.
- Stop/Go Gate: Stop if service mutates source candidates in place or drops lineage.

### MS-03 Current Truth Semantics

- Objective: Ensure reviewed outcomes interact correctly with current-truth retrieval.
- Inputs: Project Memory semantics and MS-02 service outputs.
- Outputs: tests proving candidate-only, rejected, deferred, stale, and superseded records stay out of current truth.
- Entry Criteria: MS-02 complete.
- Exit Criteria: Current-truth tests pass.
- Stop/Go Gate: Stop if retrieval behavior diverges between direct lookup and context assembly.

### MS-04 Optional Thin CLI Wrapper

- Objective: Add a small CLI command only if service semantics are stable and file budget remains.
- Inputs: shared service functions.
- Outputs: optional CLI command over the service.
- Entry Criteria: MS-03 complete and file budget available.
- Exit Criteria: CLI delegates to shared service and adds no review logic of its own.
- Stop/Go Gate: Skip this micro-sprint if it risks becoming product workflow or accidental architecture.

### MS-05 Validation Closeout

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
- Socratic discovery is deferred.
- Workspace Shell architecture is deferred.
