# Intent: Candidate Review and Promotion v0

## Version

v2

## Change Log

- v1 (2026-07-01): Initial Stage A intent.
- v2 (2026-07-01): Hardened after Red/Blue review.

## Purpose

Plan the smallest implementation slice that lets Soane review Project Memory candidates before any candidate becomes accepted Project Memory truth.

## Goal

Produce a Factory V2 planning pack for `CRP-V0-001`, a local deterministic Candidate Review and Promotion v0 implementation slice.

The future slice should define deterministic local behavior for:

- reviewing Project Memory candidate objects
- accepting, rejecting, deferring, or amending candidates
- preserving provenance and reviewer rationale
- preventing silent promotion of raw conversation, model output, or intake output into accepted truth
- exposing the flow through shared service functions and tests
- optionally exposing a thin CLI command over the shared service

## Non-Goals

- no implementation in this run
- no product web UI
- no database selection
- no live repository scanning
- no live Cursor, Codex, OpenAI, analytics, CRM, advertising, design-tool, or external source integration
- no Socratic dialogue implementation
- no Workspace Shell implementation
- no Factory V3, Temper, Aegis, Sentinel, or Harmony responsibility import

## Principles

- Project Memory candidate output is not accepted truth.
- Promotion requires explicit review action, status transition, provenance retention, and rationale.
- Capability does not imply authority; review flow must not grant execution permission.
- Review outcomes must remain inspectable, including rejected, deferred, amended, stale, and superseded records.
- Amended outcomes must preserve lineage to the original candidate and record what changed.
- Local deterministic semantics should be proven before persistence, product UI, or live integrations.
- CLI or TUI affordances, if included, must wrap shared service functions.

## Roles

- Workspace: owns the human-facing review experience and candidate presentation.
- Project Memory: owns object contracts, status transitions, provenance, and current-truth semantics.
- Thinking Engine: may produce candidates but does not promote them by itself.
- Factory V2: structures this planning pack only.
- External systems: remain source owners for repositories, analytics, CRM, ads, design, authority, proof, and mission execution.

## Requirements

- REQ-001: define a Candidate Review v0 contract for Project Memory candidate objects.
- REQ-002: define allowed review decisions: accept, reject, defer, amend, and keep open.
- REQ-003: preserve original candidate provenance when creating promoted or reviewed objects.
- REQ-004: require reviewer rationale and review provenance for accepted, rejected, deferred, or amended outcomes.
- REQ-005: keep accepted current truth distinct from rejected, deferred, stale, superseded, or candidate-only records.
- REQ-006: create deterministic fixtures for accepted, rejected, deferred, amended, conflicting, and unauthorized promotion cases.
- REQ-007: future CLI/TUI changes must wrap shared service functions.
- REQ-008: no live adapters, product shell, database, or external connector should be introduced by this slice.
- REQ-009: accepted memory must not imply authority unless an explicit Authority Reference or authority relationship exists.
- REQ-010: amended outcomes must retain derivation lineage from the original candidate.

## Acceptance Criteria

- The pack defines bounded implementation scope for `CRP-V0-001`.
- Verification covers each critical review and promotion requirement.
- Fixtures prove accepted, rejected, deferred, amended, conflicting, and unauthorized promotion cases.
- Verification proves accepted memory remains separate from authority.
- Verification proves amended outcomes preserve lineage to the original candidate.
- Stop gates prevent product shell, database, live integration, authority drift, or Socratic discovery expansion.
- Future implementation can proceed only after Stage I2 PASS and explicit human Go.

## Open Questions

### BLOCKING

- None.

### NON-BLOCKING

- Whether the optional CLI wrapper should land in the same implementation slice or remain a follow-up after service tests pass.

## Go Or No-Go Rule

Go to future implementation only if this pack passes Stage I2 and a human explicitly authorizes execution.
