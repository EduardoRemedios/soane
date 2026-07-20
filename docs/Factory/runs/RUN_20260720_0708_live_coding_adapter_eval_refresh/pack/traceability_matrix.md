# Traceability Matrix: LCAE-V0-001

## Version

v2

## Change Log

- v1 (2026-07-05): Initial Stage F traceability matrix in the upstream planning run.
- v2 (2026-07-20): Mapped refreshed risks to current verification checks.

| Requirement | Risk | Verification |
| --- | --- | --- |
| Cover exactly five supported surfaces with valid profiles. | R-010 | VC-001, VC-002 |
| Prevent provider, credential, config, session, network, install, and external-repo side effects. | R-001 | VC-001, VC-011 |
| Prevent evaluated-surface repository mutation. | R-002 | VC-004, VC-011 |
| Fail closed on source contradiction and unproven read-only behavior. | R-003 | VC-003, VC-006 |
| Keep auth, capability, authority, permission, sandbox, privacy, and review distinct. | R-004, R-008 | VC-002, VC-005 |
| Reuse existing bounded context and graph explanations. | R-005 | VC-007, VC-012 |
| Distinguish documentation from measured behavior. | R-006, R-012 | VC-008, VC-013 |
| Produce unbiased deterministic recommendations or no recommendation. | R-007 | VC-005, VC-006 |
| Keep outputs local and candidate-only where applicable. | R-009 | VC-009 |
| Provide a thin inspectable CLI. | R-011 | VC-010, VC-014 |
| Preserve existing behavior and boundaries. | R-010, R-011 | VC-012, VC-014 |

## Coverage Assessment

Every Critical and High risk has V1, V2, or V3 coverage. V4 live behavior is explicitly deferred and cannot be used to claim this deterministic slice proves operational safety.
