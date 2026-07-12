# Micro-Sprints: MMI-V0-001

## Version
v1

## Change Log
- v1 (2026-07-12): Stage G sequence.

## MS-00 Verification Scaffold And Claim Contract
- Objective: Add fixtures and failing tests, then extend the contract with Claim and candidate-only metadata validation.
- Inputs: verification assets, existing contract/review tests, fixed architecture excerpt.
- Outputs: Claim type, validation rules, malformed fixtures, executable VC-001/VC-002/VC-008 coverage.
- Entry Criteria: Human Go and execution-enabled handoff exist.
- Exit Criteria: Valid proposed/asserted Claim candidates pass; invalid combinations fail; no existing object behavior regresses.
- Stop/Go Gate: Stop if Claim requires changing the generic MemoryObject shape or implementing wider epistemic workflow.

## MS-01 Markdown Vocabulary And Parser
- Objective: Move shared role vocabulary if necessary and implement repository-bounded, prose-only parsing with exclusions.
- Inputs: MS-00 contract, role classifier, parser/path fixtures.
- Outputs: product-owned Markdown vocabulary and ingestion parser primitives.
- Entry Criteria: MS-00 passes focused tests.
- Exit Criteria: VC-003 through VC-005 and role portions of VC-009 pass.
- Stop/Go Gate: Stop if a dependency, Factory private-helper import, or broad Markdown parser is required.

## MS-02 Candidate Construction And Snapshot
- Objective: Build deterministic source snapshots and proposed Claim candidates with exact anchors, hashes, occurrence identities, metadata, budgets, and reasons.
- Inputs: MS-01 parser and Claim contract.
- Outputs: ingestion request/result service API and candidate interchange serialization.
- Entry Criteria: Parser and path boundaries pass.
- Exit Criteria: VC-001, VC-004, VC-006, VC-008, and VC-011 pass.
- Stop/Go Gate: Stop if candidate construction invokes review, assigns Authority, or needs persistence.

## MS-03 Source Comparison
- Objective: Compare immutable snapshots and report every bounded change state without mutating memory.
- Inputs: before/after fixture pairs and MS-02 snapshots.
- Outputs: deterministic comparison events and explanations.
- Entry Criteria: Candidate identity/fingerprint tests pass.
- Exit Criteria: VC-007 and comparison portions of VC-008 pass.
- Stop/Go Gate: Stop if duplicate matching requires semantic inference or guessed lineage.

## MS-04 Headless CLI
- Objective: Add thin `ingest-markdown` and `compare-markdown` commands over service functions.
- Inputs: MS-02/MS-03 APIs and existing CLI conventions.
- Outputs: stable JSON output and optional candidate interchange export.
- Entry Criteria: Service tests pass.
- Exit Criteria: VC-010 passes and exported candidates can be consumed by existing `review-candidate` without hidden promotion.
- Stop/Go Gate: Stop if CLI begins owning parser, review, or persistence semantics.

## MS-05 Real-Source Proof And Regression
- Objective: Prove the fixed canonical excerpt, compatibility, no-touch constraints, and full regression.
- Inputs: all implementation and fixture assets.
- Outputs: passing focused/full suites and scope evidence.
- Entry Criteria: CLI proof passes.
- Exit Criteria: VC-009, VC-011, VC-012, and VC-013 pass.
- Stop/Go Gate: Stop on candidate noise outside the reviewability bound, regression, dependency, persistence, provider, UI, or Factory-index change.

## MS-06 Validation Closeout
- Objective: Compare implementation to the locked pack and update repository truth.
- Inputs: complete diff, verification output, state docs, and pack.
- Outputs: validation closeout report and truthful roadmap/state/changelog updates.
- Entry Criteria: MS-05 complete.
- Exit Criteria: VC-001 through VC-014 pass and Factory execution-closeout finds no scope drift.
- Stop/Go Gate: Stop if evidence is incomplete or any pack change requires intent unlock.

## Bounded Deferral Hooks

- Graph-aware context may consume realistic Claim relationships only after this ingestion slice closes.
- Persistent source tracking and automatic staleness propagation remain part of later persistence architecture.
- Constitutional ingestion and curated round trips require a separate authority/write-back pack.
- Wider Knowledge Scope and cross-project promotion require identity and policy contracts.
