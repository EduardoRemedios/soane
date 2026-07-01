# Sprint Envelope: PM-V0-001

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage H sprint envelope.

## Sprint Identity

- Sprint ID: `PM-V0-001`
- Sprint Name: Project Memory v0 Object Model Prototype
- Execution Mode: `PLANNING_ONLY` in this Factory run
- Future Execution Requires: explicit human Go after pack review

## Objective

Implement the smallest local Project Memory v0 prototype after human approval, beginning with the v0 contract and golden fixtures, then memory semantics, context assembly, mock adapter invocation, headless CLI, and thin TUI navigation.

## Scope

In scope for future execution:

- Project Memory v0 object contract
- deterministic local fixture corpus
- local memory service functions
- governed memory invariant tests
- context assembly v0
- canonical Markdown source mapping proof
- mock Cursor/Codex/OpenAI adapter invocation records
- headless CLI commands over shared service functions
- thin TUI navigation scope after CLI stabilization

Out of scope:

- final database selection
- live Cursor, Codex, or OpenAI integrations
- product web, desktop, mobile, or voice shell
- Factory V3 mission governance
- Aegis authority or proof semantics
- Temper runtime behavior
- implementation during this Factory run

## File-Touch Budget

Total future implementation budget: up to 24 files before renewed planning review.

Indicative budget by area:

- contract and schemas: up to 4 files
- local storage and service functions: up to 5 files
- fixtures and tests: up to 8 files
- CLI: up to 3 files
- TUI: up to 2 files
- docs or validation report: up to 2 files

No existing constitutional document should be edited during implementation unless implementation teaches a durable architectural lesson and the change is explicitly reviewed.

## Micro-sprints

Follow `pack/micro_sprints.md`:

- MS-00 Contract Scaffold
- MS-01 Golden Fixture Corpus
- MS-02 Memory Semantics
- MS-03 Context Assembly And Markdown Mapping
- MS-04 Mock Coding Adapter Contract
- MS-05 Headless CLI
- MS-06 Thin TUI Scope
- MS-07 Validation Closeout

## Verification Requirements

Future implementation must satisfy `pack/verification_plan.md` and `pack/traceability_matrix.md`.

Minimum required before TUI:

- VC-001 through VC-015 pass locally.
- Fixture IDs are deterministic.
- Storage is portable and inspectable.
- Context assembly respects lifecycle, evidence, scope, visibility, and propagation rules.
- Mock adapter invocation works without live CLI or SDK calls.

Minimum required before product shell:

- Project Memory v0 validation pass complete.
- CLI/TUI proof path complete.
- Durable architecture lessons recorded in canonical docs if needed.

## SIMPLE-CODE-GATE v2 Constraint

Future code-changing execution must:

- prefer the smallest clear behavior-preserving change
- avoid code bloat and speculative abstraction
- avoid dependency creep
- avoid silent failures
- bind accepted complexity to fixtures, validation, or explicit deferred decisions

## Stop Gates

Stop implementation if:

- object contract cannot represent required fixtures
- context assembly hides contradictions
- direct lookup bypasses visibility enforcement
- live adapter behavior becomes necessary before mock adapter contract is stable
- CLI duplicates memory logic instead of calling service functions
- TUI starts defining memory semantics
- a database choice becomes necessary before the contract proves itself

## Handoff State

This envelope is `REVIEW_READY` as planning evidence only after Stage I2 and pack lint pass.

