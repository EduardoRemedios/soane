# Risk Register: Brownfield Multi-Repo Coding Proof

## Version

v1

## Change Log

- v1 (2026-07-05): Initial Stage E risk register.

| ID | Risk | Severity | Mitigation | Verification Hook |
| --- | --- | --- | --- | --- |
| R-001 | Multi-repo support is superficial metadata. | High | Require service boundary, integration contract, ownership, and build/test fields. | VC-001, VC-002 |
| R-002 | Provider invocation occurs despite missing boundary or authority context. | High | Add blocked multi-repo fixture and assert no provider invocation. | VC-004, VC-006 |
| R-003 | CLI workflow duplicates readiness logic. | Medium | Keep workflow service-delegating and summarize harness results only. | VC-007 |
| R-004 | Implementation performs live repo scanning or command execution. | High | Keep all repo data in fixtures and assert no side effects. | VC-008 |
| R-005 | Candidate review semantics regress. | High | Assert candidate output is not current truth and promotion requires review. | VC-005 |
| R-006 | Existing single-repo proof regresses. | Medium | Run existing harness and workflow regression tests. | VC-009 |
