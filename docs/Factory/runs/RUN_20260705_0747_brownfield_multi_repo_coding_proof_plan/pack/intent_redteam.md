# Intent Red Team: Brownfield Multi-Repo Coding Proof

## Version

v1

## Change Log

- v1 (2026-07-05): Initial Stage B red-team review.

## Findings

### RT-001

- Severity: High
- Finding: A multi-repo fixture can become a superficial list of repositories unless it models system boundaries, ownership, integration contracts, and cross-repo build/test responsibility.
- Why It Matters: The proof would claim multi-repo support while still behaving like a single-repo proof with extra metadata.
- Recommendation: Require fixture fields and tests for in-scope repos, out-of-scope repos, service boundaries, integration contracts, and per-repo build/test responsibility.

### RT-002

- Severity: High
- Finding: Provider invocation may become ready too early if readiness only checks that repositories exist.
- Why It Matters: Multi-repo Brownfield systems often fail because the relevant boundary, authority, or dependent service is missing, not because no repo is listed.
- Recommendation: Verification must include a blocked fixture where repository URLs exist but boundary, contract, owner, or authority context is missing.

### RT-003

- Severity: Medium
- Finding: Extending Intake, Harness, and Workflow at the same time could create duplicated multi-repo semantics.
- Why It Matters: Duplicated readiness logic would drift between services and CLI output.
- Recommendation: Keep readiness decisions in intake/discovery/harness service behavior and make the workflow summarize rather than decide.

### RT-004

- Severity: Medium
- Finding: The implementation could drift into real repo audit or scanning.
- Why It Matters: Live repository inspection would add external side effects and broaden the proof beyond deterministic fixtures.
- Recommendation: Explicitly forbid cloning, scanning, command execution, or mutation. Use fixture-backed source references only.

## Agent Failure Modes

- Treating repository count as system understanding.
- Treating provider capability as authority.
- Hiding blocked readiness behind a successful CLI run.
- Promoting proposed output without Candidate Review.
- Starting product-shell UX before proof semantics are stable.

## Verification Holes To Close

- Fixture-level tests for multi-repo ready and blocked paths.
- Summary tests proving repository map and service boundary are visible.
- Negative test proving blocked multi-repo context produces no provider invocation.
- Regression tests proving existing Greenfield and single-repo Brownfield fixtures remain unchanged.

## Open Issues

### BLOCKING

- None if the recommendations above are incorporated.

### NON-BLOCKING

- Future live adapter evaluation remains deferred.
