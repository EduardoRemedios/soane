# Traceability Matrix: GCT-V0-001

## Version

v1

## Change Log

- v1 (2026-07-18): Stage F traceability.

| Requirement Area | Risk IDs | Verification | Planned Test Surface |
| --- | --- | --- | --- |
| Fail-closed request contract | R-02, R-11 | VC-01 | `tests/test_project_memory_graph_traversal.py` |
| Directional typed paths | R-03, R-08 | VC-02, VC-10 | traversal and affected fixtures |
| Lifecycle-aware selection | R-04, R-09 | VC-03, VC-11 | current/non-current Claim graph cases |
| Per-hop access policy | R-01 | VC-04 | restricted and suppressed bridge cases |
| Cycle and duplicate handling | R-02, R-05 | VC-05, VC-07 | cyclic graph and shuffled input |
| Work and output budgets | R-02 | VC-06 | dense fan-out fixture |
| Agent context integration | R-06 | VC-08 | existing plus new agent-context tests |
| Trace compatibility | R-07, R-13 | VC-09, VC-14 | CLI subprocess/help tests |
| Source impact propagation | R-03, R-08, R-12 | VC-10 | exact provenance graph |
| Realistic MMI Claim proof | R-04, R-09 | VC-11 | fixed Claim metadata fixture |
| Exclusion taxonomy | R-01, R-10 | VC-12 | external/missing/hidden/depth cases |
| Scope and regression | R-11, R-14 | VC-13, VC-15 | diff scan and full suite |

## Domain Area

- `verification/graph_traversal_cases` is the approved Stage F fixture area for this pack.
