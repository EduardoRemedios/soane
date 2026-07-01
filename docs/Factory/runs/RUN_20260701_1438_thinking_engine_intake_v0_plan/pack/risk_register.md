# Risk Register

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage E risk register.

| Risk ID | Severity | Risk | Mitigation | Verification Hook |
| --- | --- | --- | --- | --- |
| R-001 | Critical | Future slice expands into product shell. | Restrict scope to local services and optional CLI/TUI wrappers. | VC-001, VC-009 |
| R-002 | High | Brownfield model assumes a monorepo. | Require single-repo and multi-repo fixtures. | VC-003, VC-004 |
| R-003 | High | Non-coding context is ignored. | Require non-repository context fixture. | VC-005 |
| R-004 | High | Readiness score creates false certainty. | Use explainable states and dimensions only. | VC-007 |
| R-005 | High | Thinking output silently becomes accepted memory. | Write candidate objects with provenance and review status. | VC-008 |
| R-006 | Medium | CLI/TUI duplicate logic. | Require wrappers over service functions. | VC-010 |
| R-007 | Medium | Live integrations leak into v0. | Defer all live providers and connectors. | VC-011 |
| R-008 | Medium | Context Baseline becomes permanent truth. | Treat baseline as current starting view. | VC-006 |
