# Micro-Sprints

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage G sequence.

## Sprint Sequence

### MS-00 Roadmap Evidence Review

- Objective: Review current roadmap, project state, and completed proof evidence.
- Inputs: `docs/ROADMAP.md`, `docs/PROJECT_STATE.md`
- Outputs: sequencing findings.
- Entry Criteria: Stage D PASS.
- Exit Criteria: Current fork and downstream risks are explicit.
- Stop/Go Gate: Stop if implementation work is required.

### MS-01 Sequence Update

- Objective: Update roadmap/state docs with a clearer near-term order.
- Inputs: MS-00 findings.
- Outputs: updated `docs/ROADMAP.md`, `docs/PROJECT_STATE.md`, `docs/CHANGELOG.md`.
- Entry Criteria: MS-00 complete.
- Exit Criteria: next immediate slice and deferred tracks are explicit.
- Stop/Go Gate: Stop if constitutional docs would need rewriting.

### MS-02 Validation Closeout

- Objective: Validate roadmap review artifacts.
- Inputs: verification plan and diff.
- Outputs: review closeout evidence.
- Entry Criteria: MS-01 complete.
- Exit Criteria: Factory stage lint, pack lint, knowledge lint, and diff hygiene pass.
- Stop/Go Gate: Stop if lint fails.

## Bounded Deferrals

- Workflow wrapper implementation is deferred.
- Workspace Shell architecture is deferred.
- Live adapters are deferred.
- Persistence architecture is deferred.
