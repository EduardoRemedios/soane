# Intent: Coding Proof Harness v0

## Version

v2

## Change Log

- v1 (2026-07-01): Initial Stage A intent.
- v2 (2026-07-01): Hardened after Red/Blue review.

## Purpose

Plan the smallest implementation slice that proves Soane can coordinate a coding workflow through Project Memory, Intake, Socratic Discovery, adapter-twin invocation records, and Candidate Review and Promotion without live provider calls or product UI.

## Goal

Produce a Factory V2 planning pack for `CPH-V0-001`, a mock-first Coding Proof Harness v0 implementation slice.

The future slice should define deterministic local behavior for:

- accepting a Greenfield or Brownfield coding project brief fixture
- running Thinking Engine Intake v0
- running Socratic Discovery v0 when intake reveals gaps
- assembling a task-specific Project Memory context package
- selecting a mocked provider surface from Codex CLI, Cursor CLI, Cursor SDK, OpenAI SDK, or OpenAI Agents SDK
- creating deterministic Provider Invocation records through existing adapter-twin semantics
- capturing proposed provider outputs as Project Memory candidates
- routing proposed outputs through Candidate Review and Promotion before any accepted truth exists
- reporting harness state without mutating an external repository

## Non-Goals

- no implementation in this run
- no live Codex, Cursor, OpenAI, or other provider call
- no live CLI, SDK, repository, analytics, CRM, ads, design, or external connector integration
- no external repository mutation
- no product web UI
- no Workspace Shell implementation
- no database or persistence selection
- no mission execution
- no Factory V3, Temper, Aegis, Sentinel, or Harmony responsibility import

## Principles

- Thinking and discovery precede planning and delegation.
- Coding is the first proof path, not the only Workspace use case.
- Provider surfaces are capabilities, not authority.
- Provider output is candidate material until reviewed.
- The harness should compose existing local primitives instead of duplicating them.
- Greenfield and Brownfield coding starts require different context baselines.
- Brownfield work must respect repo/workspace audit needs before feature planning.
- Mock-first proof should preserve deterministic tests before any live CLI or SDK integration.

## Roles

- Workspace: owns the human-facing coding proof workflow.
- Thinking Engine: owns intake and discovery semantics.
- Project Memory: owns context assembly, candidate objects, provenance, and review/promotion.
- Adapter twins: own deterministic provider invocation records for coding surfaces.
- Factory V2: structures this planning pack only.
- External coding tools: remain future adapter providers and are not called by this slice.

## Requirements

- REQ-001: define a local deterministic Coding Proof Harness v0 contract.
- REQ-002: support Greenfield and Brownfield coding project fixture inputs.
- REQ-003: compose existing Intake v0 and Socratic Discovery v0 services rather than duplicating their logic.
- REQ-004: assemble task-specific Project Memory context for the coding task.
- REQ-005: select a mocked provider surface from the existing adapter-twin vocabulary.
- REQ-006: create deterministic Provider Invocation records with input references, output references, policy context, confidence, cost, latency, capability, and authority separation.
- REQ-007: capture proposed provider output as Project Memory candidates, not accepted truth.
- REQ-008: route proposed output through Candidate Review and Promotion as the only promotion path.
- REQ-009: preserve Greenfield/Brownfield differences, including Brownfield audit/readiness gates.
- REQ-010: require no live models, live CLIs, live SDKs, databases, product shell, or external connectors.
- REQ-011: expose a small headless service surface; optional CLI wrapper may be added only if it delegates to shared service functions.

## Acceptance Criteria

- The pack defines bounded implementation scope for `CPH-V0-001`.
- Verification covers each critical harness requirement.
- Fixtures prove Greenfield and Brownfield coding behavior.
- Verification proves no live provider call, repository mutation, database, or product shell is required.
- Verification proves proposed outputs remain Project Memory candidates until Candidate Review and Promotion accepts them.
- Stop gates prevent live integrations, authority drift, product shell scope creep, and external repository mutation.
- Future implementation can proceed only after Stage I2 PASS and explicit human Go.

## Open Questions

### BLOCKING

- None.

### NON-BLOCKING

- Whether a thin CLI wrapper should be included in the first implementation slice or deferred until service semantics pass.
- Whether the first Brownfield fixture should model a single repository only or include a multi-repository fixture as a stretch case.

## Go Or No-Go Rule

Go to future implementation only if this pack passes Stage I2 and a human explicitly authorizes execution.
