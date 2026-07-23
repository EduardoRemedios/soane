# Traceability Matrix: CLR-V0-001

## Version

v2

## Change Log

- v1 (2026-07-23): Initial Stage F traceability matrix.
- v2 (2026-07-23): Added parent-process and proxy credential-isolation semantics.

## Risk Coverage

| Risk | Verification |
| --- | --- |
| R-001 host-read exposure | VC-001, VC-002, VC-021 |
| R-002 credential exposure | VC-003, VC-004, VC-005, VC-022 |
| R-003 hidden state/tool surfaces | VC-006, VC-007, VC-008, VC-016, VC-025 |
| R-004 repository mutation | VC-009, VC-010, VC-023 |
| R-005 evidence visibility/attribution | VC-011, VC-012, VC-026 |
| R-006 invocation ceiling breach | VC-013, VC-024 |
| R-007 source/runtime drift | VC-014, VC-015, VC-026 |
| R-008 unknown or external events | VC-016, VC-025 |
| R-009 false favorable outcome | VC-017, VC-018, VC-026 |
| R-010 premature/unauthorized live call | VC-019, VC-024, VC-026 |
| R-011 broad authorization/promotion | VC-020, VC-026 |
| R-012 incomplete teardown/retention | VC-012, VC-021, VC-026 |

## Acceptance Coverage

| Acceptance Criterion | Verification |
| --- | --- |
| AC-001 planning-only, no inspection | VC-027 and run-root execution evidence |
| AC-002 exact command, no passthrough | VC-007 |
| AC-003 offline control coverage | VC-001 through VC-020, including parent-process and credential-route proof in VC-003/VC-004 |
| AC-004 isolated non-writable fixture | VC-001, VC-002, VC-009, VC-021, VC-023 |
| AC-005 explicit authority inputs | VC-019, VC-026 |
| AC-006 one invocation, no retry/resume | VC-013, VC-024 |
| AC-007 mandatory CLI/config controls | VC-003, VC-004, VC-007, VC-015 |
| AC-008 fail-closed outcomes | VC-005, VC-008, VC-010, VC-016, VC-017 |
| AC-009 bounded invisible evidence | VC-005, VC-011, VC-012, VC-026 |
| AC-010 no automatic promotion | VC-020, VC-026 |
| AC-011 repository and pack checks | VC-027 |
| AC-012 exact closeout/residual risk | VC-026 |

## Coverage Assessment

- Every Critical and High risk has V1 or V2 prevention/detection coverage before
  provider use and V4 observation where live behavior is material.
- No Critical or High item relies only on V0 artifact assertion.
- The optional verification manifest is omitted because this run is
  `PLANNING_ONLY`.
