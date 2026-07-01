# Sprint Envelope: TEI-V0-001

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage H envelope.

## Sprint Identity

- Sprint ID: `TEI-V0-001`
- Sprint Name: Thinking Engine Intake v0
- Execution Mode: `PLANNING_ONLY` in this Factory run
- Future Execution Requires: explicit human Go after pack review

## Objective

Implement the smallest local Thinking Engine intake proof after human approval.

## Scope

In scope for future execution:

- intake category contract
- Context Baseline v0 contract
- Readiness Assessment v0 contract
- Discovery Playbook selection stubs
- deterministic fixtures
- local service functions
- optional CLI/TUI wrappers over shared services

Out of scope:

- product web UI
- database selection
- live repository scanning
- live analytics, CRM, advertising, or design-tool integrations
- live Cursor, Codex, OpenAI, or agent SDK calls
- final readiness score
- Factory V3, Temper, Aegis, Sentinel, or Harmony responsibilities

## File-Touch Budget

Total future implementation budget: up to 18 files.

- contracts and services: up to 4 files
- fixtures and tests: up to 9 files
- CLI/TUI wrappers: up to 3 files
- docs or closeout: up to 2 files

## Micro-Sprints

Follow `pack/micro_sprints.md`:

- MS-00 Intake Contract Scaffold
- MS-01 Golden Intake Fixtures
- MS-02 Intake Semantics
- MS-03 Discovery Playbook Selection
- MS-04 CLI And TUI Wrappers
- MS-05 Validation Closeout

## Verification Requirements

Future implementation must satisfy `pack/verification_plan.md` and `pack/traceability_matrix.md`.

Minimum required:

- fixtures cover Greenfield, Brownfield single-repo, Brownfield multi-repo, non-repository context, and blocked missing context
- readiness uses explainable states and dimensions
- outputs are Project Memory candidates with provenance
- no live integrations are required
- wrappers call shared service functions

## SIMPLE-CODE-GATE v2 Constraint

Future code-changing execution must prefer the smallest clear behavior-preserving change, avoid dependency creep, avoid speculative abstraction, avoid silent failures, and bind complexity to fixtures or verification.

## Stop Gates

Stop future implementation if:

- product shell work becomes necessary
- live integration becomes necessary
- readiness scoring becomes necessary
- Project Memory promotion bypasses review
- multi-repo or non-repository fixtures cannot be represented
- CLI/TUI duplicates service logic

## Handoff State

This envelope is review-ready planning evidence only after Stage I2 and pack lint pass.
