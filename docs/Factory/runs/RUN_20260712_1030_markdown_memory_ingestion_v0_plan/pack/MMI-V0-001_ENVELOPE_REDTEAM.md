# Envelope Red Team: MMI-V0-001

## Version
v1

## Change Log
- v1 (2026-07-12): Stage I envelope review.

Iteration: 1 of max 2

## Findings

### ER-001 - Critical - No candidate limit was explicit
Why it matters: A long architecture document could create an unreviewable output even with prose-only extraction.
Fix: Require a positive hard candidate limit, deterministic truncation, and warnings.

### ER-002 - High - Comparison precedence could produce conflicting events
Why it matters: The same block might be reported moved and modified depending on iteration order.
Fix: Lock an ordered rule boundary and one primary state per occurrence.

### ER-003 - High - Export was not proven compatible with review
Why it matters: A bundle format might not be consumable by existing `review-candidate` semantics.
Fix: Export individual ordinary MemoryObject JSON artifacts or add a tested explicit conversion without changing review ownership.

### ER-004 - High - Role vocabulary extraction could become an unnecessary refactor
Why it matters: Moving shared code may introduce churn unrelated to ingestion.
Fix: Make `markdown_roles.py` optional and require behavior-preserving tests; choose the smallest cycle-free dependency shape.

### ER-005 - Medium - Accepted Claim lifecycle could be confused with accepted fact status
Why it matters: Existing review acceptance admits an object to current memory but does not verify its proposition.
Fix: Preserve epistemic status separately; review compatibility must not promote `asserted` to `verified`.

## Resolutions

- Envelope v2 adds candidate budgets, ordered comparison rules, review-compatible export, optional role refactor, and explicit no-epistemic-elevation constraints.
- No Critical finding or `[SCOPE EXPANSION]` remains.

## Verdict

PASS for Stage J consolidation.
