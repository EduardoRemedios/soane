# Intent: LCAE-V0-001 Live Coding Adapter Evaluation

## Version

v2

## Change Log

- v1 (2026-07-05): Initial Stage A intent in the upstream planning run.
- v2 (2026-07-20): Refreshed after ACR-V1-001, MMI-V0-001, and GCT-V0-001; removed recommendation bias and locked context reuse, source contradiction, and no-touch requirements.

## Purpose

Implement the smallest deterministic, source-backed evaluator that can compare five candidate live coding adapter surfaces without invoking them.

## Goal

Produce an explainable recommendation, blocked status, or deferral for Codex CLI, Cursor CLI, Cursor SDK, OpenAI SDK, and OpenAI Agents SDK using typed local profiles, current official-source evidence, explicit safety gates, and Soane's existing Project Memory and Thinking Engine contracts.

## Non-Goals

- Do not implement or invoke live adapters.
- Do not execute provider CLIs, SDKs, APIs, models, cloud agents, shell commands through evaluated surfaces, or external repository operations.
- Do not inspect credentials, authentication state, provider configuration, installed provider versions, or user sessions.
- Do not install dependencies.
- Do not add Codex SDK as a sixth evaluated surface.
- Do not introduce product UI, Workspace Shell, persistence, mission execution, embeddings, semantic code intelligence, or a new graph/context system.
- Do not promote source profiles, recommendations, simulated outputs, or Provider Invocation candidates into Project Memory automatically.
- Do not decide the permanent provider strategy for Soane.

## Principles

- Capability does not imply authentication, authority, project permission, sandbox containment, or review approval.
- Official-source contradictions and missing hard guarantees fail closed.
- Documentation evidence is not locally measured behavior.
- Recommendation criteria are fixed before profile scores are evaluated.
- Existing `agent-context`, Markdown provenance, graph traversal, adapter twins, coding harness, and Candidate Review services remain the owners of their current semantics.
- CLI-first remains a sequencing preference, not a scoring override.
- A future live proof requires a separate Factory pack and explicit human authorization.

## Roles

- Thinking Engine: owns deterministic profile evaluation and recommendation as uncertainty-reduction work.
- Project Memory: supplies adapter twin, Provider Invocation, provenance, context, graph, and Candidate Review contracts; this slice does not write accepted memory.
- Factory context index and `agent-context`: supply the bounded, explained repository-context evidence used by the evaluator.
- Adapter profiles: immutable local evidence snapshots with official source refs, access dates, contradiction state, and limitations.
- Human reviewer: decides whether the deterministic implementation may proceed and later whether a separate live proof may proceed.

## Acceptance Criteria

- Five typed profile fixtures cover the in-scope surfaces and reject unknown, duplicate, malformed, stale-without-review, or incomplete profiles.
- Every profile separates source provenance, invocation mode, auth, capability, authority need, project permission, repository scope, mutation controls, structured output, traceability, session identity, cost/latency metadata path, and limitations.
- Source contradiction and missing hard read-only guarantees produce blocked reason codes; scoring cannot offset a hard blocker.
- Criteria and weights are deterministic, versioned, bounded, and independent of surface order.
- Evaluation produces one ranked recommendation only when a surface passes all hard gates; otherwise it returns an explicit no-recommendation result.
- Rejected and deferred alternatives include evidence refs and reason codes.
- The evaluator consumes a bounded current `agent-context` bundle or its shared service output and preserves selection, freshness, graph, visibility, lifecycle, and budget explanations without implementing parallel retrieval.
- Evaluation output is a local text/JSON report. Simulated Provider Invocation output, if included in tests, remains proposed/candidate-only and requires existing Candidate Review for promotion.
- A thin CLI delegates to pure evaluator functions and emits deterministic text and JSON.
- Tests prove no provider invocation, credential read, dependency install, network access, external repository access, or evaluated-surface repository mutation occurs.
- Existing Project Memory, context, graph, adapter twin, coding harness, and workflow behavior remains compatible.

## Open Questions

- NON-BLOCKING: Should a later bounded run evaluate Codex SDK now that official TypeScript and Python surfaces expose thread and sandbox controls?
- NON-BLOCKING: Should source profile refresh eventually become a reviewed Project Memory candidate workflow after persistence exists?
- NON-BLOCKING: Which evidence threshold should a separate live-proof pack require before a documentation-level blocker can be replaced by measured behavior?

## Go Or No-Go Rule

Go only if the pack passes Stage A through I2 and final pack lint, locks contradiction handling and existing-context reuse, covers every Critical and High risk, and permits implementation without live calls, credential inspection, dependency installation, external repository access, or evaluated-surface mutation.
