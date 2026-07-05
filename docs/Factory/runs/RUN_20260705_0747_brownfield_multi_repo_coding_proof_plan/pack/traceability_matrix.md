# Traceability Matrix

## Version

v1

## Change Log

- v1 (2026-07-05): Initial Stage F traceability matrix.

| Requirement | Risk | Verification |
| --- | --- | --- |
| Model multi-repo system boundary explicitly. | R-001 | VC-001, VC-003 |
| Classify Brownfield multi-repo intake correctly. | R-001 | VC-002 |
| Expose task-relevant repositories without over-including all repos. | R-001 | VC-003 |
| Block provider invocation when boundary or authority context is missing. | R-002 | VC-004, VC-006 |
| Preserve candidate-only provider output until review. | R-005 | VC-005 |
| Keep CLI workflow service-delegating. | R-003 | VC-007 |
| Avoid live side effects. | R-004 | VC-008 |
| Preserve existing proof behavior. | R-006 | VC-009 |
| Avoid product shell scope. | R-004 | VC-010 |

## Coverage Assessment

- Critical and High risks have V1, V2, or V3 coverage.
- No V4 live verification is needed for this mock-first proof.
