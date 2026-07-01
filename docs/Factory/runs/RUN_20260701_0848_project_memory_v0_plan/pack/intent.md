# Intent: Project Memory v0 Object Model Prototype Plan

## Version

v2

## Change Log

- v1 (2026-07-01): Initial Stage A planning intent.
- v2 (2026-07-01): Hardened after Stage B red-team review.

## Purpose

Produce a Factory V2 planning-only implementation pack for the first local Project Memory v0 object-model prototype.

## Goal

Define a bounded, reviewable implementation plan that can safely guide the first Project Memory v0 prototype, headless CLI, thin TUI scope, golden fixtures, and mock-first coding adapter proof path.

## Non-Goals

- Do not implement application code.
- Do not choose a final database.
- Do not build the CLI or TUI.
- Do not create live Cursor, Codex, or OpenAI integrations.
- Do not create Factory V3 mission governance, Aegis proof semantics, or Temper runtime behavior.
- Do not treat generated Markdown as the Project Memory substrate.
- Do not narrow the Workspace to coding-only use cases.

## Principles

- Project Memory is the durable substrate; Markdown is a view.
- Conversation and model output are inputs to memory, not authoritative memory.
- Evidence, Proof, Authority, Capability, Decision, Hypothesis, and Mission must remain distinct.
- The v0 contract must precede implementation.
- The CLI should wrap the contract, not become the architecture.
- Adapter proof should be mock-first, then CLI-backed, then SDK-backed.
- Coding is the first proof path, not the Workspace product boundary.

## Roles

- Root Planner: maintain Factory V2 run discipline and `PLANNING_ONLY` posture.
- Intent Contractor: define bounded implementation intent.
- Red Team: challenge scope drift, missing gates, and false authority.
- Blue Team: synthesize corrections without expanding scope.
- Purple Gate: lock or reject intent.
- Risk Analyst: define pre-mortem and risk register.
- Verification Specialist: define golden fixtures and validation strategy.
- Sprint Planner: sequence implementation micro-sprints.
- Envelope Author: produce the planning envelope.
- Pack Auditor: verify final review readiness.

## Acceptance Criteria

- The pack defines a Project Memory v0 object contract and implementation slice.
- The pack defines governed memory invariants and golden fixtures.
- The pack defines context assembly v0, capture/review/promotion, source mapping, and persistence guardrails.
- The pack defines mock-first Cursor/Codex/OpenAI adapter behavior without live integration.
- The pack defines headless CLI command surface and thin TUI navigation scope.
- The pack remains `PLANNING_ONLY` and does not execute implementation.
- Stage A through I2 lint and final pack lint pass.

## Contract Constraints

- The v0 contract must prove memory semantics, not only object persistence.
- Golden fixtures must cover decisions, assumptions, contradictions, staleness, source mapping, provider invocation, capability versus authority, visibility, supersession, provenance lineage, and context assembly propagation.
- Context assembly v0 must be rule-driven and must not treat semantic retrieval rank as truth.
- Adapter behavior must be mock-first. Live CLI-backed and SDK-backed adapters are deferred until the Provider Invocation contract is stable.
- Storage must remain local, portable, deterministic for fixtures, and reversible enough to support migrations or rewrites.
- Domain language must remain Workspace-general even when the first proof path uses coding.

## Go Or No-Go Rule

Go to implementation planning review only if the pack proves that v0 can be implemented locally, deterministically, and reversibly without collapsing Project Memory into CRUD, RAG, generated Markdown, live SDK behavior, or coding-only scope.

## Open Questions

### BLOCKING

- None.

### NON-BLOCKING

- Exact file/module names may be adjusted by the implementation pack as long as the v0 contract remains explicit.
- Final storage engine remains intentionally deferred.
