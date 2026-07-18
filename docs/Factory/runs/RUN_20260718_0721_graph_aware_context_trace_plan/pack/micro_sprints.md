# Micro-Sprints: GCT-V0-001

## Version

v1

## Change Log

- v1 (2026-07-18): Stage G implementation sequence.

## MS-00 Verification Scaffold

- Objective: Add the realistic Claim graph and failing tests for request validation, direction, policy, lifecycle, cycles, and budgets.
- Inputs: Stage F fixtures, current contract and semantics tests.
- Outputs: `tests/test_project_memory_graph_traversal.py` and fixed fixture helpers.
- Entry Criteria: Human Go and execution-enabled handoff exist.
- Exit Criteria: VC-01 through VC-07 and VC-11/VC-12 have failing assertions against the absent service.
- Stop/Go Gate: Stop if the fixture needs a new object or relationship type.

## MS-01 Traversal Service

- Objective: Implement one storage-neutral traversal request/result API with directional typed paths and bounded work.
- Inputs: MS-00 tests, `contract.py`, `semantics.py`.
- Outputs: `soane/project_memory/graph.py` and public exports.
- Entry Criteria: Verification scaffold accurately represents the locked contract.
- Exit Criteria: VC-01 through VC-07 and VC-12 pass; no hidden bridge or unbounded work remains.
- Stop/Go Gate: Stop if persistence, a query DSL, semantic inference, or depth greater than two is required.

## MS-02 Agent Context Integration

- Objective: Replace private one-hop relationship expansion with the shared traversal service.
- Inputs: MS-01 service and existing `agent_context.py` tests.
- Outputs: delegated graph expansion, preserved reasons/states/budgets, path-aware explanations.
- Entry Criteria: Service tests pass.
- Exit Criteria: VC-08 passes and no duplicate graph-expansion implementation remains.
- Stop/Go Gate: Stop if document recall or fail-closed zero-match behavior must be weakened.

## MS-03 Trace And Affected Integration

- Objective: Add bounded trace controls and direction-aware source impact propagation to existing CLI commands.
- Inputs: MS-01 service, existing CLI output contracts.
- Outputs: additive trace graph details and direct/propagated affected explanations.
- Entry Criteria: Service API and context integration are stable.
- Exit Criteria: VC-09, VC-10, and VC-14 pass.
- Stop/Go Gate: Stop if existing fields must be removed or affected-by requires inferred edges.

## MS-04 Realistic Claim Proof

- Objective: Prove source-to-proposed-Claim-to-dependent-object paths with lifecycle, visibility, cycle, and unrelated-object controls.
- Inputs: Stage F graph and completed integrations.
- Outputs: passing VC-11 proof and example command evidence.
- Entry Criteria: Service and CLI tests pass.
- Exit Criteria: Proposed Claim remains unchanged; every propagated result has a typed path; hidden/unrelated nodes are absent.
- Stop/Go Gate: Stop if traversal calls review, mutates memory, or describes proposed content as accepted truth.

## MS-05 Regression And Scope Gate

- Objective: Run focused/full tests, deterministic repeats, no-touch scans, knowledge lint, and diff checks.
- Inputs: complete implementation.
- Outputs: VC-13 and VC-15 evidence.
- Entry Criteria: VC-01 through VC-14 pass.
- Exit Criteria: Full suite passes with no persistence, dependency, semantic graph, code graph, provider, UI, or relationship-vocabulary change.
- Stop/Go Gate: Stop on any regression, unbounded output, scope drift, or environment-dependent result.

## MS-06 Validation Closeout

- Objective: Compare implementation to the locked pack and update repository truth.
- Inputs: complete diff, verification evidence, canonical state docs, and pack.
- Outputs: validation closeout report and truthful Project State, Roadmap, and Changelog updates.
- Entry Criteria: MS-05 passes.
- Exit Criteria: VC-01 through VC-15 pass and Factory execution closeout finds no scope drift.
- Stop/Go Gate: Stop if evidence is incomplete or intent unlock is required.

## Bounded Deferral Hooks

- `MS-06` records that durable graph storage remains deferred to the persistence gate; Project Memory architecture owns the later decision and no storage work is permitted here.
- `MS-06` records that semantic edge discovery and code graphs require separate approved packs; repository architecture owns those later decisions and v0 uses authored relationships only.
- `MS-06` records observed two-hop usefulness and truncation data; agent-context ownership may propose deeper traversal later, but v0 rejects it.
