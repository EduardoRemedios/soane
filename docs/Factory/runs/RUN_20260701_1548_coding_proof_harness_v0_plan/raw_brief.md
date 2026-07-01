# Raw Brief: CPH-V0-001 Coding Proof Harness v0

## Request

Plan the next bounded Soane implementation slice: a mock-first Coding Proof Harness v0.

## Context

Soane now has local deterministic proofs for:

- Project Memory v0 contract, semantics, context assembly, Markdown mapping, CLI, TUI, and adapter twins.
- Thinking Engine Intake v0.
- Candidate Review and Promotion v0.
- Socratic Discovery v0.

The next proof should show how these primitives combine for a coding workflow without yet building the Workspace Shell or calling live external tools.

## Goal

Define a small implementation plan for a coding proof harness that can:

- accept a Greenfield or Brownfield coding project brief
- run the existing intake and Socratic discovery primitives
- assemble task-specific Project Memory context
- select a mocked provider surface such as Codex CLI, Cursor CLI, Cursor SDK, OpenAI SDK, or OpenAI Agents SDK
- create deterministic Provider Invocation records
- capture proposed provider outputs as Project Memory candidates
- route proposed outputs through Candidate Review and Promotion
- prove the workflow without live model, live CLI, live SDK, repository mutation, database, or product UI dependencies

## Non-goals

- Do not execute live Codex, Cursor, OpenAI, or other provider calls.
- Do not build a product web UI or Workspace Shell.
- Do not introduce persistence or database selection.
- Do not mutate an external repository.
- Do not treat generated output as accepted Project Memory truth.
- Do not collapse capability into authority.
- Do not add Factory V3, Temper, Aegis, Sentinel, or Harmony responsibilities.

## Required Posture

Execution Mode: PLANNING_ONLY

This run should produce a Factory pack for human Go/No-go review before implementation.
