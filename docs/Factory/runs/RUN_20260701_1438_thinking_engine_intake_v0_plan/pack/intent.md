# Intent: Thinking Engine Intake v0

## Version

v2

## Change Log

- v1 (2026-07-01): Initial Stage A intent.
- v2 (2026-07-01): Hardened after Red/Blue review.

## Purpose

Plan the smallest implementation slice that lets Soane assess a Project starting point before planning, decisions, or delegated work.

## Goal

Produce a Factory V2 planning pack for `TEI-V0-001`, the Thinking Engine Intake v0 implementation slice.

The future slice should define deterministic local behavior for:

- intake classification
- Context Baseline v0
- Discovery Playbook selection
- Readiness Assessment v0
- Project Memory write-back candidates

## Non-Goals

- no implementation in this run
- no product web UI
- no database selection
- no live repository scanning
- no live Cursor, Codex, OpenAI, analytics, CRM, advertising, or design-tool integration
- no final readiness score
- no Factory V3, Temper, Aegis, Sentinel, or Harmony responsibility import

## Principles

- Project Memory remains the durable substrate.
- Context Baseline is a starting view, not permanent truth.
- Readiness Assessment is explainable criteria, not a confidence feeling.
- Greenfield, Brownfield single-repo, Brownfield multi-repo, and non-repository contexts must be distinct.
- Missing context should block feature delegation unless the delegated work is explicitly discovery.
- Live adapters and connectors wait until deterministic local semantics are proven.

## Roles

- Workspace: owns human-facing thinking, intake, context, readiness, and Project Memory views.
- Project Memory: stores structured outputs and provenance.
- Factory V2: structures this planning pack only.
- External systems: remain source owners for repositories, analytics, CRM, ads, design, authority, proof, and mission execution.

## Requirements

- REQ-001: classify intake as Greenfield, Brownfield single-repo, Brownfield multi-repo, or non-repository context.
- REQ-002: define Context Baseline v0 with goals, boundaries, sources, assumptions, questions, constraints, evidence gaps, and readiness state.
- REQ-003: define Readiness Assessment v0 using explainable dimensions and states, not a numeric score.
- REQ-004: define Discovery Playbook selection for software, Brownfield audit, Greenfield definition, and non-coding campaign or operations context.
- REQ-005: create golden fixtures for all intake categories and missing-context blockers.
- REQ-006: future CLI/TUI changes must wrap shared service functions.
- REQ-007: Project Memory write-back must produce candidate objects, not silently promote model output to truth.

## Acceptance Criteria

- The pack defines bounded implementation scope.
- Verification covers each critical requirement.
- Fixtures prove category handling and blockers.
- Stop gates prevent product shell, database, live integration, scoring, or authority drift.
- Future implementation can proceed only after human Go.

## Open Questions

### BLOCKING

- None.

### NON-BLOCKING

- Whether the first future proof should include both coding and marketing fixtures, or implement one first and keep the other as fixture-only coverage.

## Go Or No-Go Rule

Go to future implementation only if this pack passes Stage I2 and a human explicitly authorizes execution.
