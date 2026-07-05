# Intent: Brownfield Multi-Repo Coding Proof

## Version

v1

## Change Log

- v1 (2026-07-05): Initial Stage A intent.

## Purpose

Plan `BMR-CPH-V0-001`, a bounded implementation slice that extends Soane's existing mock-first Coding Proof Harness from Brownfield single-repository fixtures to Brownfield multi-repository system fixtures.

## Goal

Produce a small, reviewable implementation plan that proves Soane can represent, inspect, and gate a Brownfield coding task whose relevant context spans multiple repositories and service boundaries.

The future implementation should make multi-repository system context explicit before provider invocation is considered.

## Non-Goals

- No implementation in this planning run.
- No live Cursor, Codex, OpenAI, SDK, CLI, connector, database, external repository, or repository mutation.
- No real repository cloning, scanning, command execution, or CI integration.
- No product UI, Workspace Shell, mission execution, or persistence design.
- No Factory V3, Temper, Aegis, Sentinel, or Harmony responsibility.
- No general non-coding external context implementation.

## Principles

- Extend the existing proof instead of replacing it.
- Keep fixtures deterministic and local.
- Treat Project, system boundary, and repository as different concepts.
- A multi-repo Brownfield system is not ready merely because multiple repo URLs exist.
- Context crossing repository boundaries must be explicit, relevant, and governed.
- Capability does not imply authority.
- Provider output remains a candidate until reviewed.
- Missing system-boundary context must block provider invocation.

## Roles

- Project Memory: records structured project context, evidence, relationships, candidates, provenance, and review state.
- Thinking Engine Intake: classifies multi-repository Brownfield starting context and readiness.
- Socratic Discovery: surfaces questions and missing context before planning.
- Coding Proof Harness: composes existing services into a deterministic mock coding proof.
- Coding Harness Workflow: lists and runs fixtures and summarizes readiness and provider state.
- Candidate Review and Promotion: remains the only promotion path for proposed provider output.
- Human reviewer: authorizes future implementation and any eventual provider use.

## Scope

Future implementation should add:

- at least one ready Brownfield multi-repo fixture
- at least one blocked Brownfield multi-repo fixture
- fixture fields for repository map, in-scope repositories, out-of-scope repositories, service boundaries, integration contracts, ownership, build/test responsibility, documentation gaps, and authority path
- service behavior that preserves multi-repo context in intake, context assembly, harness summary, and workflow summary
- focused tests proving ready and blocked multi-repo paths
- validation closeout and state docs

## Acceptance Criteria

- The implementation plan has explicit verification coverage for ready and blocked multi-repo Brownfield paths.
- The plan reuses existing Intake, Discovery, Context Assembly, Coding Harness, Coding Workflow, adapter-twin, and Candidate Review services where practical.
- The plan identifies which fixture fields are required before a multi-repo Brownfield task is ready for provider invocation.
- The plan blocks provider invocation when repository map, service boundary, ownership, build/test, integration contract, or authority context is insufficient.
- The plan preserves mocked provider invocation only; no live integrations are introduced.
- The plan includes CLI workflow expectations for listing and running multi-repo fixtures.
- The plan includes no unapproved scope expansion.

## Go Or No-Go Rule

Go only if the pack defines a small deterministic implementation slice with clear tests, strict non-goals, and no unresolved critical findings.

No-go if the pack depends on live repositories, live providers, persistence, product UI, or undefined authority semantics.

## Open Questions

### BLOCKING

- None.

### NON-BLOCKING

- Whether multi-repo fixture IDs should keep the `CPH-GF-*` prefix or move to a clearer `CPH-BMR-*` prefix can be resolved during implementation as long as tests remain deterministic.
