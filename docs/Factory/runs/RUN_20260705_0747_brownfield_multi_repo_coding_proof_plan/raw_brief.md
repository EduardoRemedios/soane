# Raw Brief: BMR-CPH-V0-001 Brownfield Multi-Repo Coding Proof Planning

## Request

Create a Factory V2 planning pack for the next Soane roadmap slice: a Brownfield multi-repository coding proof.

## Background

Soane has already proven:

- Project Memory v0 local contract, fixture corpus, semantics, context assembly, Markdown mapping, adapter twins, CLI, TUI, and candidate review/promotion.
- Thinking Engine Intake v0.
- Socratic Discovery v0.
- Coding Proof Harness v0 for Greenfield and Brownfield single-repository coding cases.
- Coding Harness Workflow v0 as a CLI-first operator surface over the coding proof harness.

The next complexity to address is Brownfield systems that are not monorepos. A real Brownfield system may span multiple repositories, shared libraries, service boundaries, deployment surfaces, generated clients, API contracts, CI pipelines, ownership boundaries, and documentation locations.

## Goal

Plan the smallest implementation slice that extends the existing mock-first coding proof from Brownfield single-repo fixtures to Brownfield multi-repo system-boundary fixtures.

The future implementation should prove that Soane can represent and inspect a multi-repository Brownfield coding task without collapsing the project into a single repository or skipping context readiness checks.

## Required Posture

- Execution Mode: PLANNING_ONLY
- No implementation is authorized by this run.
- No live Cursor, Codex, OpenAI, SDK, CLI, connector, database, external repository, or repository mutation is in scope.
- Future implementation should remain deterministic and fixture-backed.

## Candidate Sprint ID

`BMR-CPH-V0-001`

## In Scope For Planning

- Define a bounded implementation plan for multi-repo Brownfield coding proof fixtures.
- Define expected fixture shape for repository map, in-scope repositories, out-of-scope repositories, service boundaries, integration contracts, ownership, build/test commands, documentation gaps, and readiness blockers.
- Define how existing Intake, Discovery, Context Assembly, Coding Harness, Coding Workflow, adapter twins, and Candidate Review services should be extended or reused.
- Define verification that task-specific context crosses repository boundaries only when relevant and allowed.
- Define blocked and ready paths for multi-repo Brownfield cases.
- Define CLI workflow expectations for listing and running the new multi-repo fixtures.
- Preserve capability and authority separation.
- Preserve candidate review/promotion semantics.

## Out Of Scope

- Live provider calls.
- Real repository cloning, scanning, mutation, or command execution.
- Database or persistence selection.
- Product UI or Workspace Shell.
- Mission execution.
- Factory V3, Temper, Aegis, Sentinel, or Harmony responsibilities.
- Full non-coding external context support.
- Live multi-agent orchestration.

## Key Evidence To Consume

- `docs/PROJECT_MEMORY_ARCHITECTURE.md`
- `docs/THINKING_ENGINE_ARCHITECTURE.md`
- `docs/ROADMAP.md`
- `docs/PROJECT_STATE.md`
- `docs/Factory/runs/RUN_20260701_1548_coding_proof_harness_v0_plan/VALIDATION_CLOSEOUT_REPORT.md`
- `docs/Factory/runs/RUN_20260702_0617_coding_harness_workflow_v0_plan/VALIDATION_CLOSEOUT_REPORT.md`
- `soane/thinking_engine/intake.py`
- `soane/thinking_engine/coding_harness.py`
- `soane/thinking_engine/coding_workflow.py`
- `tests/fixtures/coding_proof_harness/`
- `tests/test_thinking_engine_coding_harness.py`
- `tests/test_thinking_engine_coding_workflow.py`

## Go Or No-Go Rule

The pack should be ready for human Go only if it gives a small, testable implementation envelope that:

- extends the existing proof rather than replacing it
- keeps the workflow mock-first and deterministic
- makes multi-repo system boundaries explicit
- blocks provider invocation when system-boundary context is insufficient
- avoids product-shell, live-provider, persistence, and repository-mutation scope
