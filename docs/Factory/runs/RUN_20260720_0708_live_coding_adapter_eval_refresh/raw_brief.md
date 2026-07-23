# Raw Brief: LCAE-V0-001 Planning Pack Refresh

## Request

Refresh the passed `LCAE-V0-001` planning pack against current repository architecture, implementation evidence, and official adapter documentation before asking for human Go or No-go.

## Upstream Pack

- Run: `RUN_20260705_0923_live_coding_adapter_eval_plan`
- Sprint: `LCAE-V0-001`
- Prior verdict: `PASS`
- Prior mode: `PLANNING_ONLY`

The upstream pack remains historical evidence. This run is the review-ready replacement for any future deterministic adapter-evaluation implementation.

## Current Repository Evidence

Since the upstream pack passed, Soane has implemented:

- `ACR-V1-001` bounded relevant agent context with fail-closed zero-match behavior and atomic Factory context-index refresh
- `MMI-V0-001` deterministic Markdown-to-Claim candidate ingestion with exact provenance and no automatic promotion
- `GCT-V0-001` bounded typed graph traversal shared by `agent-context`, `agent-trace`, and `agent-affected`

The refresh must prevent live-adapter evaluation from creating a second context, graph, provenance, or candidate-promotion path.

## Goal

Produce a current, bounded implementation pack for a deterministic source-backed evaluator covering:

- Codex CLI
- Cursor CLI
- Cursor SDK
- OpenAI SDK
- OpenAI Agents SDK

The evaluator must recommend, block, or defer candidate surfaces using explicit evidence and reason codes. It must not invoke those surfaces.

## Required Constraints

- Keep this run `PLANNING_ONLY`.
- Do not invoke a live provider, model, CLI, SDK, API, cloud agent, or external repository.
- Do not inspect credentials, authentication state, provider configuration, installed provider versions, or user sessions.
- Do not install dependencies.
- Do not mutate product code or repository content outside this planning pack and canonical status reconciliation.
- Reuse existing Project Memory adapter twins, agent context assembly, Markdown provenance, graph traversal, Candidate Review, and coding proof contracts.
- Keep capability, authentication, authority, project permission, sandbox policy, and review state distinct.
- Treat official-source contradictions or missing read-only guarantees as blocked, not as a favorable score.
- Keep every evaluated or simulated Provider Invocation output candidate-only until explicit review.
- Do not add persistence, product UI, Workspace Shell, mission execution, full code graphing, or portfolio-product responsibilities.
- Treat Codex SDK as adjacent source evidence only; adding it as a sixth evaluated surface is out of scope.

## Source Refresh Requirements

- Record exact official source URLs and an access date.
- Record source recency and contradiction status per surface.
- Preserve claims only when current official material supports them.
- Require a future implementation-time source revalidation because provider behavior and documentation are mutable.
- Distinguish documentation evidence from locally measured evidence; this slice permits documentation evidence only.

## Context-System Integration Requirements

- Use existing `agent-context` output or its shared service as the bounded repository-context input to evaluation.
- Preserve document and memory selection states, source freshness, graph explanations, visibility, lifecycle, and hard budgets.
- Do not infer missing relationships or silently broaden zero-match context.
- Store source and evaluation outputs as deterministic local fixtures or reports only; do not promote them into Project Memory automatically.

## Expected Output

A refreshed Factory pack for `LCAE-V0-001`, ready for explicit human Go or No-go before deterministic implementation. No `EXECUTION_PROMPT.md` is allowed in this planning-only run.

## Go Or No-Go Rule

Go only if Stage A through I2 and final pack lint pass, current source contradictions fail closed, current context-system reuse is explicit, and the implementation envelope can be executed without live calls, credential reads, dependency installs, external repository access, or repository mutation by evaluated surfaces.

## Execution Authorization Addendum

- Execution Mode: EXECUTION_ENABLED
- Execution Authorization: Human Go recorded in the current Codex task on 2026-07-23: "GO I approve the implementation"
- Authorized Envelope: `LCAE-V0-001`
- Downstream Fan-Out: NOT_APPROVED
- Live Adapter Use: NOT_APPROVED

This later explicit authorization supersedes the planning-only execution restriction for the
locked deterministic implementation only. It does not authorize a provider invocation,
credential or user-state inspection, evaluated-surface repository mutation, or any deferred
live-proof work.
