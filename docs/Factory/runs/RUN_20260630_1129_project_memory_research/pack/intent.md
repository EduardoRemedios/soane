# Intent: Project Memory Research Spike

## Version

v1

## Change Log

- v1 (2026-06-30): Initial planning-only research intent.

## Purpose

Use a bounded research spike to inform the future Workspace Project Memory architecture.

## Goal

Produce `docs/research/PROJECT_MEMORY_RESEARCH_SYNTHESIS.md` as an architecture input, not as the final architecture.

## Non-Goals

- Do not choose a database.
- Do not design final schemas.
- Do not implement Project Memory.
- Do not design UI.
- Do not import Factory V3 mission governance into Soane.
- Do not treat adjacent memory products as the Workspace source of truth.

## Principles

- Memory is infrastructure, not chat history.
- Conversation is an input to memory, not memory itself.
- Evidence, Decision, Authority, Capability, Hypothesis, and Mission must remain distinct.
- Semantic retrieval and execution state must be separated.
- Generated Markdown is a view over memory, not the memory substrate.

## Acceptance Criteria

- The synthesis exists at `docs/research/PROJECT_MEMORY_RESEARCH_SYNTHESIS.md`.
- It records reviewed sources, implications, anti-patterns, open questions, and a recommendation.
- It remains conceptual and implementation-neutral.
- It aligns with the constitutional documents.

## Go Or No-Go Rule

Go to Project Memory architecture only if the synthesis can clearly identify the minimum conceptual decisions the architecture must make.
