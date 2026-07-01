# Intent: Roadmap Sequencing Review

## Version

v2

## Change Log

- v1 (2026-07-01): Initial Stage A intent.
- v2 (2026-07-01): Hardened after sequencing red team.

## Purpose

Review the Soane roadmap after Coding Proof Harness v0 and convert the current fork into a clearer near-term sequence.

## Goal

Produce `ROADMAP-SEQ-001`, a planning-only sequencing review that decides the next immediate slice and updates roadmap/state documentation if needed.

## Non-Goals

- no product implementation
- no Workspace Shell architecture deliverable
- no live provider integration
- no persistence or database decision
- no constitutional document rewrite
- no Factory V3, Temper, Aegis, Sentinel, or Harmony responsibility import

## Principles

- Roadmap updates should reflect implementation evidence, not speculative polish.
- A thin workflow should prove usability before Workspace Shell architecture.
- Live adapters should wait until deterministic workflow boundaries are inspectable.
- Persistence should wait until the memory/write paths to persist are stable enough.
- Brownfield complexity should be introduced deliberately, not hidden inside a generic coding path.

## Roles

- Roadmap: owns the near-term sequence and next bounded slice.
- Factory V2: structures the review evidence.
- Project Memory and Thinking Engine: provide current implementation evidence.
- Workspace Shell: remains future architecture work, not this run's output.

## Requirements

- REQ-001: decide whether the roadmap is detailed enough after Coding Proof Harness v0.
- REQ-002: decide the next immediate bounded slice.
- REQ-003: identify sequencing for workflow wrapper, Brownfield multi-repo, live adapters, memory provider evaluation, persistence, Workspace Shell, and product surface.
- REQ-004: update state docs if the sequence changes.
- REQ-005: avoid product implementation or architecture expansion in this run.

## Acceptance Criteria

- A sequencing review artifact exists and records recommendations.
- `docs/ROADMAP.md` names the next immediate slice and near-term sequence.
- `docs/PROJECT_STATE.md` and `docs/CHANGELOG.md` reflect the review.
- Factory stage lint and pack lint pass.

## Open Questions

### BLOCKING

- None.

### NON-BLOCKING

- Exact scope of the future workflow wrapper should be decided in its own Factory pack.

## Go Or No-Go Rule

Go if the review produces a clearer roadmap sequence without starting implementation.
