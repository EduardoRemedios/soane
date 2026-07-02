# Raw Brief: CHW-V0-001 Coding Harness Workflow v0

## Request

Plan the next bounded Soane implementation slice: a thin CLI-first workflow over the existing Coding Proof Harness v0.

## Context

The roadmap sequencing review selected this as the next step before Workspace Shell architecture.

Soane already has:

- Project Memory v0 contract, semantics, context assembly, CLI, TUI, adapter twins, and review/promotion.
- Thinking Engine Intake v0.
- Socratic Discovery v0.
- Coding Proof Harness v0.

The coding harness service proves the end-to-end path locally, but it is not yet conveniently navigable as a workflow.

## Goal

Define a Factory pack for a small implementation slice that adds a CLI-first workflow over `soane.thinking_engine.coding_harness`.

The future implementation should let a user:

- list or select deterministic coding harness fixtures
- run the existing coding harness service
- see intake readiness and discovery stop condition
- see task-specific context package summary
- see mocked provider invocation summary
- see proposed output candidate summary
- see candidate review/promotion status
- optionally export a JSON summary

## Non-goals

- Do not call live Codex, Cursor, OpenAI, or other providers.
- Do not mutate repositories.
- Do not add persistence or database selection.
- Do not build product web UI or Workspace Shell.
- Do not duplicate coding harness, intake, discovery, context, adapter, or review logic.
- Do not treat proposed provider output as accepted truth.

## Required Posture

Execution Mode: PLANNING_ONLY

This run should produce a Factory pack for human Go/No-go review before implementation.
