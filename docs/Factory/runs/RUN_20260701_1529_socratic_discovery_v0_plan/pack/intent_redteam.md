# Intent Red Team

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage B red-team review.

## Iteration

Iteration: 1 of max 2

## Findings

### RT-001 Discovery Could Manufacture Certainty

- Severity: High
- Why it matters: A discovery loop that produces hypotheses may make unresolved assumptions look settled.
- Recommendation: Require discovery outputs to preserve uncertainty state and remain candidates until review.

### RT-002 Question Generation Could Become Generic

- Severity: High
- Why it matters: Generic questions would not differentiate greenfield, brownfield, multi-repo, non-repo, or blocked contexts.
- Recommendation: Require category-specific fixture coverage and question source traceability.

### RT-003 Hidden Model Dependency Risk

- Severity: Critical
- Why it matters: Socratic discovery sounds like an LLM-driven workflow, but the slice is supposed to prove deterministic local semantics first.
- Recommendation: Add explicit no-live-model and no-model-call verification checks.

### RT-004 Evidence And Authority Could Blur

- Severity: High
- Why it matters: A user answer might provide evidence, but it does not necessarily provide authority to proceed.
- Recommendation: Require separate discovery states for needs evidence and needs authority.

### RT-005 Optional Wrapper Could Become Product UX

- Severity: Medium
- Why it matters: Discovery is conversational, so CLI/TUI work could drift into product shell design.
- Recommendation: Keep wrappers optional and require service-first implementation.

## Agent Failure Modes

- Generating questions that are plausible but not traceable to baseline gaps.
- Treating user answers as accepted facts instead of candidates.
- Producing hypotheses without evidence-gap links.
- Collapsing blocked, needs-evidence, and needs-authority into one vague not-ready state.
- Adding live LLM calls or UI because Socratic discovery sounds interactive.

## Verification Holes

- Intent should explicitly require question provenance or source reason.
- Intent should explicitly test no model calls.
- Intent should require stop-condition fixtures.

## Summary

The intent is sound but should be hardened around uncertainty preservation, question traceability, and no-model-call enforcement.
