# Verification Plan: ACR-V1-001

## Version

v1

## Change Log

- v1 (2026-07-12): Initial Stage F verification plan.

## Strategy

Use deterministic fixtures and focused unit/process tests around the existing context index, agent-context service, lower-level context assembly, and CLI. Run the complete repository suite after focused checks.

## Required Checks

| Check | Tier | Required Proof |
| --- | --- | --- |
| VC-001 | V2 | Natural multi-term tasks use bounded fallback and retrieve relevant slices with stable order. |
| VC-002 | V2 | Zero document and memory matches return explicit degraded empty context, never all visible memory. |
| VC-003 | V2 | Explicit broad inspection remains available only through labeled, access-controlled semantics. |
| VC-004 | V2 | Query attempts, document count, and memory count obey separate hard budgets and deterministic deduplication. |
| VC-005 | V2 | One-hop allowlisted traversal dedupes cycles, obeys lifecycle policy and budget, and records inclusion/truncation reasons. |
| VC-006 | V2 | Restricted, suppressed, propagation-blocked, and ineligible lifecycle targets are excluded with reasons. |
| VC-007 | V2 | Markdown role affects precedence only and cannot grant authority or change memory status/evidence. |
| VC-008 | V2 | Concurrent refresh contention publishes one complete valid index without uniqueness or partial-state errors. |
| VC-009 | V2 | Refresh failure preserves the prior valid index and reports `failed`; deliberate reuse reports `reused`. |
| VC-010 | V3 | `python3 -m unittest discover -s tests` passes, including intentional lower-level broad inspection cases. |
| VC-011 | V1 | Freshness output is observational and no memory lifecycle state is mutated. |
| VC-012 | V1 | Diff introduces no persistence, external provider, embedding, ingestion, UI, live adapter, dependency, or portfolio-boundary change. |
| VC-013 | V2 | CLI JSON and Markdown outputs expose selection mode, refresh state, budgets, and explanations deterministically. |

## Failure Injection

- Force an isolated rebuild failure before publication and confirm the prior index remains queryable.
- Run concurrent rebuild callers against the same temporary destination and confirm deterministic completion or explicit failure.

## Acceptance Standard

VC-001 through VC-013 pass. Any failure in VC-002, VC-006, VC-008, VC-009, or VC-012 blocks acceptance.
