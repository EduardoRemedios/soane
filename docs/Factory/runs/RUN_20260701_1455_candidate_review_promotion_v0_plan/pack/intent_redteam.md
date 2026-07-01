# Intent Red Team

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage B red-team review.

## Iteration

Iteration: 1 of max 2

## Findings

### RT-001 Candidate Promotion Could Smuggle Authority

- Severity: High
- Why it matters: Accepting a candidate claim could be mistaken for permission to execute work or call an adapter.
- Recommendation: The future slice must preserve the authority boundary and explicitly test that accepted memory does not grant authority unless an Authority Reference exists.

### RT-002 Amended Candidates Need Lineage

- Severity: High
- Why it matters: An amended candidate could overwrite the original claim and lose why the reviewer changed it.
- Recommendation: Require amended outcomes to retain derivation from the original candidate and reviewer rationale.

### RT-003 Rejected Candidates Must Stay Inspectable

- Severity: Medium
- Why it matters: If rejected candidates disappear, future contradictions and repeated bad claims cannot be audited.
- Recommendation: Rejected candidates should remain inspectable and excluded from current truth.

### RT-004 CLI Wrapper Could Become Architecture

- Severity: Medium
- Why it matters: A command shape built before service semantics stabilize could become accidental architecture.
- Recommendation: Keep CLI optional and require it to wrap the shared service only.

### RT-005 Fixture Coverage Needs Negative Cases

- Severity: High
- Why it matters: Only happy-path acceptance would miss the highest-risk governance failures.
- Recommendation: Require fixtures for unauthorized promotion, conflicting candidates, rejected candidates, deferred candidates, and amended candidates.

## Agent Failure Modes

- Treating `LifecycleStatus.ACCEPTED` as equivalent to authority.
- Mutating candidate objects in place instead of creating review outcomes with provenance.
- Adding persistence or UI because review sounds workflow-like.
- Treating rejected or deferred candidates as current truth through retrieval shortcuts.

## Verification Holes

- The current intent does not explicitly require unauthorized promotion tests.
- The current intent should tie amended outcomes to provenance lineage.
- The current intent should make CLI wrapper optional, not required.

## Summary

The intent is directionally sound. It should be hardened to make authority separation, lineage, negative fixtures, and optional CLI boundaries explicit.
