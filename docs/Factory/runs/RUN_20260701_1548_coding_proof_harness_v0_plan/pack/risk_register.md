# Risk Register: Coding Proof Harness v0

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage E risk register.

| Risk ID | Severity | Risk | Mitigation | Verification Hook |
| --- | --- | --- | --- | --- |
| R-001 | High | Harness duplicates existing service logic. | Require composition of Intake, Discovery, Context, Adapter, and Review services. | VC-001, VC-003 |
| R-002 | High | Proposed provider output bypasses candidate review. | Keep output candidate-only and require review path tests. | VC-006, VC-007 |
| R-003 | High | Live provider call or repository mutation enters v0. | Forbid live CLIs, SDKs, databases, connectors, and repo mutation. | VC-008 |
| R-004 | High | Capability is treated as authority. | Preserve capability/authority separation in invocation records. | VC-005 |
| R-005 | Medium | Brownfield and Greenfield paths are flattened. | Require separate fixtures and readiness expectations. | VC-002, VC-009 |
| R-006 | Medium | Wrapper work becomes product shell. | Make wrapper optional and service-delegating only. | VC-010 |
| R-007 | Medium | The proof becomes too broad for one slice. | Keep file-touch budget and out-of-scope list strict. | Envelope stop gates |
