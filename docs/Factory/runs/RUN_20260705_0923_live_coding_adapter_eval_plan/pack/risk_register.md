# Risk Register: LCAE-V0-001

## Version

v1

## Change Log

- v1 (2026-07-05): Initial Stage E risk register.

| ID | Severity | Risk | Mitigation | Verification Hook |
| --- | --- | --- | --- | --- |
| R-001 | Critical | Live invocation occurs during evaluation. | Keep implementation source-backed and deterministic. | VC-001, VC-008 |
| R-002 | Critical | Repository mutation occurs through CLI/SDK surface. | Model mutation controls and blocked unsafe surfaces. | VC-004, VC-008 |
| R-003 | High | Auth, capability, and authority are collapsed. | Separate matrix dimensions and fixtures. | VC-003 |
| R-004 | High | SDK orchestration expands Soane scope. | Keep SDKs evaluation-only and behind adapter contracts. | VC-005, VC-010 |
| R-005 | High | Output bypasses Candidate Review. | Require candidate-only output capture criteria. | VC-006 |
| R-006 | Medium | Evaluation lacks current source provenance. | Include source review metadata and source refs in profiles. | VC-002 |
| R-007 | Medium | Existing mock proofs regress. | Run focused regression suite. | VC-009 |
