# Intent: ACR-V1-001 Agent Context Relevance And Fail-Closed Assembly

## Version

v2

## Change Log

- v1 (2026-07-12): Initial Stage A intent.
- v2 (2026-07-12): Hardened broad-selection, query budget, traversal, refresh publication, freshness, and compatibility rules after Stage B.

## Purpose

Plan the smallest safe implementation slice that makes Soane's existing agent-context front door relevant, bounded, explainable, and fail-closed before further memory ingestion or live adapter work. [SOURCE:RAW]

## Goal

Define deterministic behavior for natural-task recall, zero-match handling, memory selection, bounded relationship expansion, and context-index refresh so agents receive a small explained bundle rather than accidental broad memory. [SOURCE:RAW]

## Definitions

- `zero-match`: no document slice or explicit memory seed is selected for the request. [SOURCE:RAW]
- `fail-closed context`: a zero-match request returns an explicit empty or degraded result and never silently expands to all visible memory. [SOURCE:RAW]
- `bounded expansion`: relationship traversal constrained by allowlisted type, depth, visibility, lifecycle, and output budget. [SOURCE:RAW]
- `refresh truthfulness`: reported refresh state matches the actual completed index state. [SOURCE:RAW]

## Requirements

- Natural task text must use deterministic query decomposition or bounded fallback rather than requiring every task term in one chunk. [SOURCE:RAW]
- Document and memory budgets must be separate, positive, and visible in output. [SOURCE:RAW]
- Zero-match agent context must return explicit empty or degraded state; broad all-memory inspection requires an explicit separate request. [SOURCE:RAW]
- Document role may affect selection precedence but must not imply authority or Project Memory lifecycle status. [SOURCE:REF:docs/GOVERNANCE_MODEL.md]
- Visibility, propagation, lifecycle, contradiction, and suppression semantics must remain enforced. [SOURCE:REF:docs/PROJECT_MEMORY_ARCHITECTURE.md]
- Relationship expansion must be one hop in this slice, use an explicit type allowlist, avoid cycles, obey the memory budget, and explain each included object. [SOURCE:RAW]
- Index refresh must be serialized or atomic for concurrent callers, and failures must not report success. [SOURCE:RAW]
- Existing CLI JSON and Markdown modes must remain deterministic and backward compatible except where unsafe broad fallback is intentionally corrected. [SOURCE:RAW]
- Focused and full regression tests must cover natural task text, zero matches, explicit broad inspection, role precedence, visibility, lifecycle, traversal cycles and budgets, refresh contention, and failure reporting. [SOURCE:RAW]

## Hardened Behavior

- Agent context never performs broad all-memory selection implicitly; any broad inspection remains explicit, access-controlled, and labeled in output. [SOURCE:RAW]
- Query planning uses bounded normalization and fallback attempts, stable scoring and deduplication, and a hard document budget; it must not issue an unbounded query per task token. [SOURCE:RAW]
- One-hop traversal uses deterministic edge ordering, an explicit relationship allowlist, cycle deduplication, lifecycle handling, and a concrete truncation reason when the memory budget is reached. [SOURCE:RAW]
- Index rebuild occurs in isolation and publishes only after success; failed refresh preserves the previous valid index and reports `failed`, while deliberate reuse reports `reused`. [SOURCE:RAW]
- Source freshness in this slice is observational metadata or a warning only; it does not mutate Project Memory lifecycle state. [SOURCE:RAW]
- Lower-level intentional broad inspection remains available through documented explicit semantics and is covered by regression tests. [SOURCE:RAW]

## Non-Goals

- persistence architecture, migrations, or database selection
- embeddings, vector retrieval, external memory providers, or network calls
- Markdown extraction, automatic candidate creation, or automatic promotion
- traversal deeper than one hop or a general graph query language
- product UI, Workspace Shell, live coding adapters, or provider invocation
- changes to Factory V2 doctrine or neighbouring portfolio ownership

## Principles

- Context is a selected task view; it is not all memory. [SOURCE:REF:docs/CORE_CONCEPTS.md]
- Empty evidence is preferable to unexplained broad context. [SOURCE:RAW]
- Capability does not imply authority. [SOURCE:REF:docs/VISION.md]
- Selection and exclusion must be inspectable. [SOURCE:REF:docs/PROJECT_MEMORY_ARCHITECTURE.md]
- Keep the implementation local, deterministic, and dependency-free. [SOURCE:RAW]

## Roles

- Workspace Project Memory: owns context selection and memory semantics.
- Factory context index: supplies local document recall evidence; it is not authority.
- Agent caller: supplies task, access scope, optional explicit seeds, and budgets.
- Human reviewer: grants or denies later implementation Go.

## Acceptance Criteria

- A realistic multi-term task retrieves bounded relevant document slices through deterministic fallback.
- A zero-match request returns no implicit all-memory context and records a concrete degraded reason.
- Explicit seeds and explicit broad-inspection mode remain possible and distinguishable.
- One-hop allowlisted expansion includes only visible, lifecycle-eligible objects within budget and records relationship reasons.
- Concurrent refresh attempts complete deterministically or one returns an explicit failure; no successful status is fabricated.
- Existing Project Memory and Thinking Engine regression tests pass.
- No dependency, persistence, UI, external provider, or neighbouring-product scope is introduced.

## Open Questions

- NON-BLOCKING: Exact query normalization and minimum-match policy, bounded by the hardened behavior and fixtures.
- NON-BLOCKING: Exact API representation of explicit broad inspection, bounded by access controls and labeled selection mode.

## Go Or No-Go Rule

Go only if the final pack proves fail-closed zero-match behavior, bounded relevance and traversal, truthful refresh behavior, preserved governance invariants, and no scope expansion into persistence, external retrieval, or live adapters.
