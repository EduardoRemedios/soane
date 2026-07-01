# Intent Red Team

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage B red-team review.

## Iteration

Iteration: 1 of max 2.

## Findings

### R1: Intake could become hidden product shell work

- Severity: Critical.
- Why it matters: A broad intake experience could pull in UI, connectors, accounts, dashboards, and workflow design before the core semantics are proven.
- Fix recommendation: Restrict future implementation to local deterministic service functions plus optional CLI/TUI wrappers.

### R2: Brownfield could be treated as one repository only

- Severity: High.
- Why it matters: Many real systems span multiple repositories and external operational artifacts.
- Fix recommendation: Require fixtures and schema fields for multi-repo and non-repository context sources.

### R3: Readiness scoring may be premature

- Severity: High.
- Why it matters: A score can hide missing context and weak evidence behind false precision.
- Fix recommendation: Use explainable readiness states and dimensions only.

### R4: Model output could silently become memory

- Severity: High.
- Why it matters: Thinking Engine synthesis must not bypass review or provenance.
- Fix recommendation: Require write-back candidates and explicit promotion boundaries.

### R5: Verification could be too document-heavy

- Severity: Medium.
- Why it matters: Architecture prose alone will not prove intake behavior.
- Fix recommendation: Require deterministic fixtures and tests for each intake category.

## Verification Holes

- Missing fixture coverage for non-repository context would leave the architecture coding-biased.
- Missing blocker fixtures would fail to prove readiness restraint.

## Recommendation

Proceed only after the intent explicitly locks local deterministic scope, category fixtures, no scoring, and no live integrations.
