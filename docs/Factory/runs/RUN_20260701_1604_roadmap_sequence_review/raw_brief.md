# Raw Brief: ROADMAP-SEQ-001 Roadmap Sequencing Review

## Request

Review the Soane roadmap after completing Coding Proof Harness v0 and decide whether the roadmap is detailed enough or needs a sequencing update.

## Context

Soane now has:

- Project Memory v0 local primitives, CLI, TUI, context assembly, adapter twins, and review/promotion.
- Thinking Engine Intake v0.
- Socratic Discovery v0.
- Coding Proof Harness v0.

The current roadmap names the next step as a choice between a thin CLI/TUI workflow over the coding harness and Workspace Shell architecture.

## Goal

Produce a bounded sequencing review that:

- evaluates whether the roadmap is still detailed enough
- checks whether the next slices are in the right order
- recommends the next immediate slice
- identifies near-term deferred tracks such as live adapters, persistence, Brownfield multi-repo proof, memory-provider evaluation, and Workspace Shell architecture
- updates `docs/ROADMAP.md`, `docs/PROJECT_STATE.md`, and `docs/CHANGELOG.md` if the review changes the roadmap sequence

## Non-goals

- Do not implement new product behavior.
- Do not start Workspace Shell architecture in this run.
- Do not call live providers or SDKs.
- Do not choose persistence or database technology.
- Do not rewrite constitutional documents.

## Required Posture

Execution Mode: PLANNING_ONLY

This run may update roadmap/state documentation, but it must not implement a product feature.
