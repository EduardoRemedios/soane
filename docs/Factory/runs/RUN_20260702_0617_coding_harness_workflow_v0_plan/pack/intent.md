# Intent: Coding Harness Workflow v0

## Version

v2

## Change Log

- v1 (2026-07-02): Initial Stage A intent.
- v2 (2026-07-02): Hardened after Red/Blue review.

## Purpose

Plan the smallest implementation slice that makes the existing Coding Proof Harness v0 navigable from the command line without starting Workspace Shell, product UI, live providers, persistence, or repository mutation.

## Goal

Produce a Factory V2 planning pack for `CHW-V0-001`, a CLI-first Coding Harness Workflow v0 implementation slice.

The future slice should provide a thin workflow over `soane.thinking_engine.coding_harness` that can:

- list available deterministic coding harness fixtures
- run a selected fixture through the existing harness service
- summarize intake readiness and discovery stop condition
- summarize task-specific context package output
- summarize mocked provider invocation metadata
- summarize proposed output candidate metadata
- summarize whether provider output is still candidate-only or reviewed
- optionally emit a JSON summary for downstream inspection

## Non-Goals

- no implementation in this run
- no live Codex, Cursor, OpenAI, or other provider calls
- no live CLI, SDK, repository, analytics, CRM, ads, design, or external connector integration
- no external repository mutation
- no persistence or database selection
- no Workspace Shell or product web UI
- no duplication of coding harness, intake, discovery, context, adapter, or review logic
- no acceptance of proposed provider output as truth without Candidate Review and Promotion

## Principles

- The workflow wraps the harness; it does not become the harness.
- CLI comes before TUI, and TUI comes before product shell.
- The workflow should make state inspectable, not hide it behind a conversational abstraction.
- Proposed output remains candidate-only unless explicitly reviewed.
- Provider invocation is a trace record, not execution authority.
- The workflow should stay deterministic and fixture-backed.

## Roles

- Coding Harness Workflow: owns command/navigation shape only.
- Coding Proof Harness: owns workflow semantics and result construction.
- Project Memory: owns context, candidates, provenance, and review/promotion.
- Adapter Twins: own deterministic provider invocation records.
- Factory V2: structures this planning pack only.

## Requirements

- REQ-001: define a CLI-first workflow command surface over the existing coding harness service.
- REQ-002: list deterministic coding harness fixtures.
- REQ-003: run a selected fixture through `run_coding_proof`.
- REQ-004: summarize readiness, discovery, context, provider invocation, output candidate, and review status.
- REQ-005: provide optional JSON output for machine-readable inspection.
- REQ-006: keep proposed provider output candidate-only unless review is explicitly invoked through Candidate Review and Promotion.
- REQ-007: avoid duplicating intake, discovery, context assembly, adapter twin, coding harness, or review logic.
- REQ-008: require no live provider calls, live CLIs, live SDKs, persistence, repository mutation, product shell, or Workspace Shell.
- REQ-009: keep optional TUI as a bounded deferral unless implementation has spare budget and service semantics are stable.

## Acceptance Criteria

- The pack defines bounded implementation scope for `CHW-V0-001`.
- Verification covers all critical workflow requirements.
- Future implementation can prove CLI fixture listing, fixture execution, text summary, JSON summary, and candidate-only output behavior.
- Verification proves no live provider call, repository mutation, persistence, product UI, or Workspace Shell is required.
- Future implementation can proceed only after Stage I2 PASS and explicit human Go.

## Open Questions

### BLOCKING

- None.

### NON-BLOCKING

- Whether a minimal TUI wrapper should be included after CLI tests pass, or deferred to a later slice.

## Go Or No-Go Rule

Go to future implementation only if this pack passes Stage I2 and a human explicitly authorizes execution.
