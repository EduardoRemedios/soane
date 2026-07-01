# Raw Brief

## Request

Prepare the next bounded Factory V2 planning pack after Candidate Review and Promotion v0.

## Recommended Next Slice

Plan `SD-V0-001`, a local deterministic Socratic Discovery v0 slice.

## Reason

Soane now has the supporting sequence needed for a first guided thinking loop:

- Project Memory v0 local contract and semantics
- Thinking Engine Intake v0
- Project Memory candidate review and promotion
- thin CLI proof paths over local services

The next missing Thinking Engine layer is a deterministic discovery loop that turns Context Baseline gaps into questions, records answers as candidates, derives hypotheses, tracks evidence gaps, and decides whether the project is blocked, needs more evidence, is ready for planning, or needs authority review.

## Scope

The planning pack should define a small implementation slice for:

- local deterministic discovery session model
- question generation from Context Baseline gaps, assumptions, constraints, open questions, and missing context
- answer capture as candidate Project Memory objects
- hypothesis generation from answers and available evidence
- discovery state transitions
- stop conditions: blocked, needs evidence, needs authority, ready for planning
- fixtures for greenfield, brownfield single-repo, brownfield multi-repo, non-repository, and blocked discovery
- optional thin CLI or TUI wrapper only after service tests pass

## Non-goals

- no implementation in this run
- no product web UI
- no live LLM calls
- no live Cursor, Codex, OpenAI, analytics, CRM, ads, design, repository, or external connectors
- no database selection
- no Workspace Shell implementation
- no Factory V3, Temper, Aegis, Sentinel, or Harmony responsibilities

## Execution Mode

Execution Mode: PLANNING_ONLY

No implementation is authorized by this run. Implementation requires a future explicit human Go after pack review.
