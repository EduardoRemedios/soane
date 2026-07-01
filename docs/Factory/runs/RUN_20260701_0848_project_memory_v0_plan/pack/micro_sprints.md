# Micro-sprints: Project Memory v0

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage G micro-sprint plan.

## MS-00 Contract Scaffold

- Objective: Define Project Memory v0 object contract, invariants, lifecycle transitions, relationship types, evidence handling, and deterministic fixture IDs.
- Inputs: `intent.md`, `verification_plan.md`, `traceability_matrix.md`.
- Outputs: contract module or schema definitions, fixture ID conventions, validation entry point.
- Entry Criteria: planning pack accepted by human review.
- Exit Criteria: V1 static checks for contract shape and deterministic fixture IDs pass.
- Stop or Go Gate: Stop if object model cannot represent required fixtures without special cases.

## MS-01 Golden Fixture Corpus

- Objective: Create fixture data for all twelve required golden fixtures.
- Inputs: `pack/fixtures/golden_fixtures.md`.
- Outputs: local fixture files and fixture loader.
- Entry Criteria: MS-00 complete.
- Exit Criteria: fixture loader validates each fixture and preserves deterministic IDs.
- Stop or Go Gate: Stop if any required fixture cannot be represented by the contract.

## MS-02 Memory Semantics

- Objective: Implement lifecycle, provenance, relationships, evidence levels, scope, visibility, supersession, redaction, and contradiction semantics.
- Inputs: MS-00 contract and MS-01 fixtures.
- Outputs: local Project Memory service functions and invariant tests.
- Entry Criteria: MS-01 complete.
- Exit Criteria: VC-001 through VC-012 pass against fixtures.
- Stop or Go Gate: Stop if direct lookup, search, and context assembly cannot share enforcement rules.

## MS-03 Context Assembly And Markdown Mapping

- Objective: Implement context assembly v0 and canonical Markdown source mapping.
- Inputs: memory semantics and fixture corpus.
- Outputs: context package builder and Markdown mapping proof.
- Entry Criteria: MS-02 complete.
- Exit Criteria: context assembly respects lifecycle, evidence, scope, visibility, and propagation rules.
- Stop or Go Gate: Stop if context assembly hides contradictions or treats stale records as current truth.

## MS-04 Mock Coding Adapter Contract

- Objective: Implement mocked Provider Invocation for Cursor/Codex/OpenAI adapter surfaces.
- Inputs: Integration Architecture and verification fixtures.
- Outputs: mock adapter invocation record and provider invocation fixture test.
- Entry Criteria: MS-02 complete.
- Exit Criteria: Provider Invocation fixture passes without live CLI or SDK calls.
- Stop or Go Gate: Stop if adapter metadata changes Project Memory semantics.

## MS-05 Headless CLI

- Objective: Add a small command surface over the Project Memory v0 service functions.
- Inputs: MS-00 through MS-04.
- Outputs: commands for validate, fixture-test, context-build, export-markdown, and inspect.
- Entry Criteria: contract and core fixture tests pass.
- Exit Criteria: CLI commands call shared service functions and do not duplicate logic.
- Stop or Go Gate: Stop if CLI behavior diverges from contract tests.

## MS-06 Thin TUI Scope

- Objective: Add or plan a thin TUI navigation layer over CLI/service primitives.
- Inputs: CLI command model and memory service outputs.
- Outputs: project navigation, memory browser, evidence/decision/hypothesis views, adapter invocation view, validation status, unresolved questions.
- Entry Criteria: headless CLI is stable.
- Exit Criteria: TUI remains navigational and does not introduce separate memory semantics.
- Stop or Go Gate: Stop if TUI starts driving architecture rather than wrapping it.

## MS-07 Validation Closeout

- Objective: Run the full v0 validation pass and update canonical docs if implementation teaches durable lessons.
- Inputs: all prior micro-sprints.
- Outputs: validation report and any required doc updates.
- Entry Criteria: MS-00 through MS-06 complete.
- Exit Criteria: all required checks pass or blockers are recorded as Questions, Constraints, or Decision needs.
- Stop or Go Gate: Stop if new architecture decisions are required before proceeding to Thinking Engine architecture.

