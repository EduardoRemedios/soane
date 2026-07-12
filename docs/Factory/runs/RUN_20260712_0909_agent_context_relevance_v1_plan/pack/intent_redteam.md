# Intent Red Team: ACR-V1-001

## Version

v1

## Change Log

- v1 (2026-07-12): Initial Stage B red-team review.

Iteration: 1 of max 2

## Findings

### RT-001 - Critical - Broad inspection ambiguity

Why it matters: An explicit broad-memory option could accidentally become an agent-context default or bypass visibility, suppression, lifecycle, and propagation rules.

Fix: Keep agent context fail-closed; preserve broad inspection only in the lower-level context command or behind an explicit mode that still applies access controls and reports selection mode.

### RT-002 - High - Query fallback can become unbounded

Why it matters: Decomposing long tasks into every token could flood recall, destabilize ordering, and recreate repo-wide rereading.

Fix: Define deterministic normalization, stop terms, a bounded number of fallback queries, stable scoring, deduplication, and a hard document budget.

### RT-003 - High - Memory expansion semantics are underspecified

Why it matters: One-hop traversal can still exceed budget, follow inverse or contradictory edges unexpectedly, or include non-current records without explanation.

Fix: Require an allowlist, deterministic edge ordering, cycle deduplication, lifecycle policy, budget truncation reason, and per-object inclusion reason.

### RT-004 - High - Refresh correctness needs a failure contract

Why it matters: Serialization alone does not define stale-index behavior after a failed rebuild or whether a caller may consume the previous valid index.

Fix: Build into an isolated temporary database, publish atomically after success, preserve the prior valid index on failure, and report `refreshed`, `reused`, or `failed` truthfully.

### RT-005 - Medium - Source freshness could expand into persistence

Why it matters: Marking Project Memory objects stale mutates durable state and belongs to later ingestion/persistence work.

Fix: Limit this slice to reporting available source/index freshness metadata and selection warnings; do not mutate memory status.

### RT-006 - Medium - Existing lower-level broad behavior may be intentional

Why it matters: Changing `build_context_package` globally could break fixtures and audit workflows that intentionally inspect all visible memory.

Fix: Introduce explicit selection semantics at the agent-context boundary or make broad selection explicit while preserving a documented lower-level path.

### RT-007 - Medium - Tests can miss real contention

Why it matters: Thread-only tests may not cover separate agent processes sharing the default SQLite path.

Fix: Include deterministic process-level contention coverage or an equivalent isolated lock/publication test, plus failure injection.

## Verdict

Proceed to synthesis after incorporating RT-001 through RT-007. No scope expansion is required.
