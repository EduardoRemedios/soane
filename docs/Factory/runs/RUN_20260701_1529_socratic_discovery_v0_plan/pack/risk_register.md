# Risk Register

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage E risk register.

| ID | Risk | Severity | Mitigation | Verification Hook |
| --- | --- | --- | --- | --- |
| R-001 | Discovery produces false certainty. | Critical | Preserve uncertainty state and candidate-only hypotheses. | VC-004, VC-008 |
| R-002 | Questions are generic and not traceable. | High | Require source reason for every generated question. | VC-002 |
| R-003 | Hidden model dependency enters local semantics. | Critical | Prove no live model calls are required or invoked. | VC-009 |
| R-004 | Answers bypass Candidate Review and Promotion. | Critical | Emit Project Memory candidates only. | VC-003, VC-005 |
| R-005 | Evidence and authority blur. | High | Separate needs-evidence and needs-authority stop conditions. | VC-006 |
| R-006 | Category coverage misses brownfield or non-repo contexts. | High | Require fixtures for all intake categories. | VC-001, VC-007 |
| R-007 | Wrapper becomes product shell. | Medium | Keep wrappers optional and service-backed. | VC-010 |
| R-008 | Live integration, database, or adapter scope creeps in. | High | Keep the slice fixture-backed and local. | VC-009, VC-011 |
