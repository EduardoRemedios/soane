# Envelope Red Team: GCT-V0-001

## Version

v1

## Change Log

- v1 (2026-07-18): Stage I adversarial review.

## Iteration

Iteration: 1 of max 2

## Findings

### ER-01 Critical: Caller Limits Had No Hard Ceiling

- Why it matters: A positive object or edge limit can still be millions and defeat the bounded-system requirement.
- Resolution: Envelope v2 defines service maxima and rejects requests above them.

### ER-02 High: Command Defaults Were Not Numerically Reproducible

- Why it matters: Implementers could select materially different depth and work budgets.
- Resolution: Envelope v2 sets defaults for context, trace, and affected workflows.

### ER-03 High: Duplicate Edge And Path Identity Was Ambiguous

- Why it matters: Repeated authored edges could consume path budgets or alter deterministic output.
- Resolution: Complete ordered step tuples identify paths; duplicate edges do not create duplicate paths.

### ER-04 High: Naive Inbound Traversal Could Repeatedly Scan All Objects

- Why it matters: The edge budget would not account for repeated full-memory scans, making work scale poorly.
- Resolution: Build one inbound index per traversal from safe edge records.

### ER-05 Medium: Explanation Cap And Truncation Cap Were Conflated

- Why it matters: Unbounded structured truncations can replace unbounded paths as the output problem.
- Resolution: Envelope v2 caps exclusions and truncation/explanation records separately.

### ER-06 Medium: Silent Clamping Would Hide Caller Error

- Why it matters: A caller could believe a requested proof was complete when the service quietly reduced limits.
- Resolution: Above-ceiling requests fail validation; runtime budget exhaustion remains explicit.

## Scope Review

- No `[SCOPE EXPANSION]` was introduced.
- Hard ceilings and defaults refine the locked boundedness requirement.
- No persistence, dependency, graph query language, new relationship, semantic inference, or code graph appears.

## Verification Impact

- VC-01 must cover above-ceiling validation.
- VC-05/VC-06 must cover duplicate edges and capped explanation records.
- VC-07 must include inbound index determinism.
- VC-09/VC-10 must assert command defaults.

## Residual Findings

- Critical: None.
- High: None.
- NON-BLOCKING: Exact class and field names remain implementation choices within the locked semantic API.

## Result

Envelope v2 is ready for Stage J consolidation.
