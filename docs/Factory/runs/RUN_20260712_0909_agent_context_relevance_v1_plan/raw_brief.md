# Raw Brief: Agent Context Relevance And Fail-Closed Assembly V1

## Request

Review the canonical Soane documents for staleness, determine the next bounded slices, and proceed with the recommended sequence.

The approved priority is to harden the agent-facing context slice before live adapter evaluation or persistence work.

## Observed Evidence

- Natural multi-term task queries can produce zero Factory context-index document matches because recall requires all parsed terms to occur in a chunk.
- When agent context produces no memory seed IDs, the underlying context package currently falls back to every visible memory object.
- Concurrent context-index refresh attempts can collide in SQLite; sequential refresh succeeds, but atomicity and truthful refresh reporting are not contractually verified.
- Existing focused tests pass but use constrained queries and do not cover realistic task text, zero-match fail-closed behavior, or concurrent refresh contention.

## Requested Planning Scope

- deterministic query decomposition and bounded fallback for natural agent tasks
- explicit empty or degraded context results instead of implicit all-memory fallback
- separate document and memory budgets
- constitutional and canonical document precedence without treating role as authority
- lifecycle, visibility, propagation, and source-freshness constraints
- bounded one-hop typed relationship expansion with selection and exclusion reasons
- atomic or serialized context-index refresh behavior and truthful refresh status
- natural-task, zero-match, concurrency, visibility, lifecycle, cycle, and regression verification

## Non-Goals

- no implementation during this Factory run
- no persistence architecture or database selection
- no semantic embeddings or external retrieval provider
- no automatic Markdown-to-memory extraction or promotion
- no product UI or Workspace Shell
- no live coding adapter or provider invocation
- no Factory V3, Temper, Aegis, Sentinel, or Harmony responsibility expansion

## Follow-On Sequence

After this slice is planned and separately authorized for implementation:

1. Markdown-to-memory candidate ingestion with review-gated promotion
2. graph-aware context and trace over realistic memory density
3. existing `LCAE-V0-001` implementation after source-evidence refresh
4. first live read-only coding proof
5. second non-coding domain proof
6. persistence architecture after access and mutation patterns are proven

## Execution Posture

Execution Mode: PLANNING_ONLY

No implementation authority is granted by this brief. Human Go/No-go is required after Stage I2 and pack lint.

## Execution Authorization Update

- Execution Mode: EXECUTION_ENABLED
- Execution Authorization: Human `Go` recorded in the Soane repository collaboration thread on 2026-07-12 after Stage I2 PASS and final pack-lint PASS.
- Authorized Scope: Implement `ACR-V1-001` only within the locked envelope and verification plan.
- Downstream Fan-Out: NOT_APPROVED
