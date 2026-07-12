# Micro-Sprints: ACR-V1-001

## Version

v1

## Change Log

- v1 (2026-07-12): Initial Stage G sequence.

## MS-00 Verification Scaffold

- Objective: Add natural-task, zero-match, explicit broad, traversal, refresh contention, and failure-injection fixtures/tests before behavior changes.
- Inputs: `verification_plan.md`, `fixtures/`, existing agent-context tests.
- Outputs: focused failing tests and final fixture data shapes.
- Entry Criteria: Human Go and execution-enabled handoff exist.
- Exit Criteria: VC-001 through VC-009 and VC-013 have executable focused coverage; failures represent intended gaps.
- Stop/Go Gate: Stop if tests require network, credentials, nondeterministic timing, or external providers.

## MS-01 Bounded Query Planning

- Objective: Convert natural task text into a small deterministic recall plan with stable ranking, deduplication, and document budget.
- Inputs: MS-00 fixtures, Factory recall API.
- Outputs: query-planning helper and document-selection updates.
- Entry Criteria: MS-00 complete.
- Exit Criteria: VC-001 and VC-004 pass without an unbounded per-token query loop.
- Stop/Go Gate: Stop if implementation requires embeddings, external retrieval, or a new dependency.

## MS-02 Fail-Closed Selection State

- Objective: Prevent implicit all-memory fallback and expose explicit selection mode, degraded reason, and separate budgets.
- Inputs: MS-00 zero-match and broad-inspection fixtures.
- Outputs: agent-context and lower-level selection semantics with JSON/Markdown summaries.
- Entry Criteria: MS-01 complete.
- Exit Criteria: VC-002, VC-003, VC-004, and relevant VC-013 assertions pass.
- Stop/Go Gate: Stop if broad mode bypasses visibility, lifecycle, suppression, or propagation rules.

## MS-03 Bounded Relationship Expansion

- Objective: Add deterministic one-hop allowlisted expansion with cycle deduplication, lifecycle policy, budget truncation, and reasons.
- Inputs: MS-00 traversal fixtures and Project Memory semantics.
- Outputs: bounded expansion service behavior and explanations.
- Entry Criteria: MS-02 complete.
- Exit Criteria: VC-005, VC-006, and VC-007 pass.
- Stop/Go Gate: Stop if traversal exceeds one hop or becomes a general graph query API.

## MS-04 Atomic Refresh Publication

- Objective: Isolate index builds, serialize or atomically publish valid results, preserve prior valid state on failure, and report refresh state truthfully.
- Inputs: MS-00 contention and failure fixtures, existing SQLite index implementation.
- Outputs: refresh coordination and failure contract.
- Entry Criteria: MS-03 complete.
- Exit Criteria: VC-008, VC-009, and refresh portions of VC-013 pass.
- Stop/Go Gate: Stop if the solution requires a service, daemon, non-standard dependency, or persistent schema redesign.

## MS-05 Regression And Scope Gate

- Objective: Complete CLI Markdown/JSON explanations, observational freshness, no-scope checks, and full regression.
- Inputs: all prior changes and verification assets.
- Outputs: passing focused and full tests plus diff audit.
- Entry Criteria: MS-04 complete.
- Exit Criteria: VC-010 through VC-013 pass; knowledge lint and diff hygiene pass.
- Stop/Go Gate: Stop on any Critical check failure or unintended persistence/provider/UI scope.

## MS-06 Validation Closeout

- Objective: Compare implementation with the locked pack and update repository state evidence.
- Inputs: implementation diff, test output, pack, roadmap, project state, changelog.
- Outputs: validation closeout report and truthful state-doc updates.
- Entry Criteria: MS-05 complete.
- Exit Criteria: Factory execution-closeout review finds no scope drift and residual risks are recorded.
- Stop/Go Gate: Stop if implementation evidence is incomplete or the pack requires intent unlock.

## Roadmap Non-Goals

- Markdown candidate ingestion remains a separate future Factory run owned by Project Memory.
- Deeper graph query and traversal remain outside this slice until ingestion creates realistic graph density.
- `LCAE-V0-001`, live proof, persistence, and product shell remain separate roadmap gates and are not incomplete requirements of ACR-V1-001.
