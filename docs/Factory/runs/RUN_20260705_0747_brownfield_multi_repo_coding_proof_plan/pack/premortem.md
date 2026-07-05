# Premortem: Brownfield Multi-Repo Coding Proof

## Version

v1

## Change Log

- v1 (2026-07-05): Initial Stage E premortem.

## Failure Scenarios

### FS-001: Multi-Repo Means Only Multiple URLs

The implementation adds two repository entries but does not model service boundaries, integration contracts, or ownership.

Mitigation: Require fixture fields and tests for repository map, service boundary, integration contract, ownership, and build/test responsibility.

### FS-002: Provider Invoked With Incomplete Boundary

The harness treats a multi-repo fixture as ready even when boundary, owner, authority, or contract evidence is missing.

Mitigation: Include a blocked fixture where repositories exist but provider invocation is unavailable.

### FS-003: Workflow Owns Readiness Logic

The CLI workflow starts deciding readiness rather than summarizing the harness result.

Mitigation: Tests should show workflow delegates to shared service functions and only renders summary state.

### FS-004: Live Repo Audit Sneaks In

Implementation starts cloning repos, running commands, or inspecting real filesystem paths.

Mitigation: Keep all sources fixture-backed and assert no live side effects.

### FS-005: Candidate Output Becomes Truth

Provider output for ready multi-repo fixtures becomes current truth without review.

Mitigation: Reuse Candidate Review and Promotion tests and add multi-repo candidate-only assertions.
