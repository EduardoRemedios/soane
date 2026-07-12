# Intent Synthesis: ACR-V1-001

## Version

v1

## Change Log

- v1 (2026-07-12): Initial Stage C synthesis.

Iteration: 1 of max 2

## Resolutions

- RT-001: Agent context is fail-closed; broad inspection is explicit, labeled, and remains access-controlled.
- RT-002: Query fallback is bounded by attempt count, normalization policy, stable scoring, deduplication, and document budget.
- RT-003: Traversal is one hop with allowlisted types, deterministic ordering, lifecycle policy, cycle deduplication, memory budget, and inclusion/truncation reasons.
- RT-004: Refresh builds in isolation, publishes atomically after success, preserves the prior valid index on failure, and reports `refreshed`, `reused`, or `failed`.
- RT-005: Freshness is observational only; no memory lifecycle mutation is allowed.
- RT-006: Lower-level broad inspection remains an explicit documented path with regression coverage.
- RT-007: Verification includes contention and failure-injection evidence, preferably process-level where practical.

## Scope Check

- No new product surface, persistence layer, external provider, embedding system, ingestion workflow, or live adapter was introduced.
- No `[SCOPE EXPANSION]` item exists.
- All requirements remain sourced from the raw brief or canonical documents.

## Remaining Questions

- NON-BLOCKING: The implementation may choose the simplest deterministic query normalization and explicit broad-mode representation that satisfy fixtures and acceptance criteria.

## Recommendation

Advance the hardened v2 intent to Purple intent lock.
