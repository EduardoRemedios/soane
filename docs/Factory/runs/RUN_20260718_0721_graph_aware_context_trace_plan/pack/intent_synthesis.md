# Intent Synthesis: GCT-V0-001

## Version

v1

## Change Log

- v1 (2026-07-18): Stage C synthesis.

## Iteration

Iteration: 1 of max 2

## Accepted Findings

- RT-01: Direction is explicit in requests, paths, and command policies.
- RT-02 and RT-06: Visibility applies to seeds and every hop; inaccessible details remain opaque and cannot bridge traversal.
- RT-03: An examined-edge limit and bounded exclusion/explanation output complement depth, object, and path budgets.
- RT-04: Non-current inclusion is explicit and current-first at equal depth.
- RT-05: Canonical neighbor and alternate-path ordering precedes budget application.
- RT-07: `agent-context` delegates graph expansion to one shared traversal service.
- RT-08: `agent-affected` owns a narrow direction-aware impact policy.
- RT-09: The Claim proof preserves proposed status and prohibits promotion.
- RT-10: Existing trace JSON fields are preserved additively.
- RT-11: External, missing, inaccessible, disallowed, depth, and budget outcomes remain distinct.
- RT-12: Two-hop maximum, existing enums, and no predicate language bound the abstraction.

## Rejected Findings

- None.

## Scope Review

- No `[SCOPE EXPANSION]` was introduced.
- The new edge-work bound and opaque exclusions clarify the raw brief's bounded-policy requirement.
- No object type, relationship type, persistence layer, semantic inference, or code graph was added.

## Assumptions

- Existing fixture and repo-local memory loaders preserve enough stable object identity for deterministic graph tests.
- The first affected-by policy can be represented as command-owned sets of `(relationship type, direction)`.

## Open Issues

- BLOCKING: None.
- NON-BLOCKING: Canonical single-path versus bounded alternate-path presentation remains an implementation choice with explicit verification.

## Synthesis Result

Intent v2 is contract-grade and ready for Purple lock review.
