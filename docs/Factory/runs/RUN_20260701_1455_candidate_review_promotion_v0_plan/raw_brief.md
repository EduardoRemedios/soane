# Raw Brief

## Request

Review the completed Thinking Engine Intake v0 proof and prepare the next bounded Factory V2 planning pack.

## Recommended Next Slice

Plan `CRP-V0-001`, a local deterministic Candidate Review and Promotion v0 slice.

## Reason

Thinking Engine Intake v0 now emits Project Memory write-back candidates with provenance, but Soane does not yet have a governed local flow for reviewing, accepting, rejecting, deferring, or amending those candidates.

That gap should be closed before Socratic discovery flow, live adapters, product shell work, or broader delegation features, because those later features will create more candidate claims and decisions.

## Scope

The planning pack should define a small implementation slice for:

- reviewing Project Memory candidates produced by Thinking Engine Intake v0
- preserving candidate provenance
- requiring explicit status transitions before accepted truth
- recording reviewer decisions and rationale
- separating accepted, rejected, deferred, amended, and still-open candidates
- exposing the flow through local service functions and deterministic tests
- optionally exposing a thin CLI command over the shared service

## Non-goals

- no product web UI
- no database selection
- no live Cursor, Codex, OpenAI, analytics, CRM, ads, design, or repository integrations
- no Factory V3, Temper, Aegis, Sentinel, or Harmony responsibilities
- no broad Workspace Shell implementation
- no Socratic dialogue implementation in this slice

## Execution Mode

Execution Mode: PLANNING_ONLY

No implementation is authorized by this run. Implementation requires a future explicit human Go after pack review.
