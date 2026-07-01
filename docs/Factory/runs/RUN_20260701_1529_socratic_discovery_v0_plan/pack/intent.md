# Intent: Socratic Discovery v0

## Version

v2

## Change Log

- v1 (2026-07-01): Initial Stage A intent.
- v2 (2026-07-01): Hardened after Red/Blue review.

## Purpose

Plan the smallest implementation slice that lets Soane conduct a local deterministic guided discovery loop after intake and before planning or delegation.

## Goal

Produce a Factory V2 planning pack for `SD-V0-001`, a Socratic Discovery v0 implementation slice.

The future slice should define deterministic local behavior for:

- discovery session state
- question generation from Context Baseline gaps
- answer capture as Project Memory candidates
- hypothesis generation from answers, assumptions, constraints, and evidence gaps
- stop conditions for blocked, needs evidence, needs authority, and ready for planning
- provenance and candidate-review handoff

## Non-Goals

- no implementation in this run
- no product web UI
- no live LLM calls
- no live Cursor, Codex, OpenAI, analytics, CRM, ads, design, repository, or external connector integration
- no database selection
- no Workspace Shell implementation
- no mission execution
- no Factory V3, Temper, Aegis, Sentinel, or Harmony responsibility import

## Principles

- Thinking precedes planning.
- Discovery should reduce uncertainty without pretending uncertainty is gone.
- Questions, answers, hypotheses, evidence gaps, assumptions, and authority needs remain distinct.
- Answers and hypotheses are candidates until reviewed through Candidate Review and Promotion.
- Generated questions must be traceable to a baseline gap, assumption, constraint, missing context item, or playbook prompt.
- Discovery states must preserve uncertainty rather than presenting hypotheses as conclusions.
- The first discovery loop should be deterministic and fixture-backed before any model, adapter, UI, or persistence choices.
- Discovery must support greenfield, brownfield single-repo, brownfield multi-repo, non-repository, and blocked contexts.

## Roles

- Workspace: owns human-facing thinking and discovery.
- Thinking Engine: owns local discovery session semantics.
- Project Memory: owns candidate objects, provenance, and review/promotion semantics.
- Factory V2: structures this planning pack only.
- External systems: remain source owners for repositories, analytics, CRM, ads, design, authority, proof, and mission execution.

## Requirements

- REQ-001: define a local deterministic Discovery Session v0 contract.
- REQ-002: generate discovery questions from Context Baseline goals, assumptions, constraints, open questions, missing context, and readiness state.
- REQ-003: capture answers as Project Memory candidate objects with provenance.
- REQ-004: generate hypotheses from answers and evidence gaps without promoting them to accepted truth.
- REQ-005: represent discovery state transitions and stop conditions: blocked, needs evidence, needs authority, ready for planning.
- REQ-006: select or reference Discovery Playbook prompts without implementing a generic process engine.
- REQ-007: create fixtures for greenfield, brownfield single-repo, brownfield multi-repo, non-repository, and blocked discovery.
- REQ-008: future CLI/TUI changes must wrap shared service functions.
- REQ-009: no live adapters, product shell, database, or live model calls should be introduced by this slice.
- REQ-010: every generated question must include a source reason.
- REQ-011: every hypothesis must retain uncertainty state and evidence-gap links.

## Acceptance Criteria

- The pack defines bounded implementation scope for `SD-V0-001`.
- Verification covers each critical discovery requirement.
- Fixtures prove category-specific discovery behavior and blocked states.
- Verification proves no live model calls are required or invoked.
- Verification proves generated questions and hypotheses preserve traceability.
- Stop gates prevent model calls, product shell, database, live integration, authority drift, or mission execution.
- Future implementation can proceed only after Stage I2 PASS and explicit human Go.

## Open Questions

### BLOCKING

- None.

### NON-BLOCKING

- Whether the optional wrapper should be CLI-only or include a minimal TUI view after service semantics pass.

## Go Or No-Go Rule

Go to future implementation only if this pack passes Stage I2 and a human explicitly authorizes execution.
