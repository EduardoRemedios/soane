# Risk Register

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage E risk register.

| ID | Risk | Severity | Mitigation | Verification Hook |
| --- | --- | --- | --- | --- |
| R-001 | Silent candidate promotion bypasses review. | Critical | Require explicit review action and reviewer provenance. | VC-001, VC-002 |
| R-002 | Accepted memory is treated as execution authority. | Critical | Keep authority separate and test absence of authority linkage. | VC-006 |
| R-003 | Amended candidates lose lineage. | High | Preserve derivation references to original candidates. | VC-004 |
| R-004 | Rejected or deferred candidates pollute current truth. | High | Filter current-truth retrieval by status and review outcome. | VC-003, VC-005 |
| R-005 | Conflicting candidates are flattened too early. | High | Preserve contradictions or challenged status for review. | VC-007 |
| R-006 | CLI wrapper duplicates service logic. | Medium | Make CLI optional and require service delegation. | VC-008 |
| R-007 | Live integration or database scope creeps in. | High | Keep implementation fixture-backed and local. | VC-009, VC-010 |
| R-008 | Review rationale is optional or empty. | High | Require non-empty rationale for terminal review outcomes. | VC-002 |
