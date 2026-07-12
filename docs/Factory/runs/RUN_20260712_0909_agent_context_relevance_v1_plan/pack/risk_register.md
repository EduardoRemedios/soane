# Risk Register: ACR-V1-001

## Version

v1

## Change Log

- v1 (2026-07-12): Initial Stage E risk register.

| ID | Severity | Risk | Mitigation | Verification Hook |
| --- | --- | --- | --- | --- |
| R-001 | Critical | Zero matches implicitly select all visible memory. | Explicit fail-closed agent selection mode. | VC-002, VC-003 |
| R-002 | Critical | Visibility, suppression, lifecycle, propagation, or authority distinctions are weakened. | Reuse governed semantics and test exclusions. | VC-006, VC-007 |
| R-003 | High | Natural-task fallback is unstable or unbounded. | Bounded deterministic query plan and budgets. | VC-001, VC-004 |
| R-004 | High | Relationship expansion exceeds depth/budget or loops. | One-hop allowlist, stable ordering, cycle dedupe, truncation reasons. | VC-005, VC-006 |
| R-005 | High | Concurrent refresh corrupts index state or reports false success. | Isolated rebuild, serialized/atomic publication, previous-index preservation. | VC-008, VC-009 |
| R-006 | High | Global empty-seed change breaks intentional broad inspection. | Explicit broad path and regression coverage. | VC-003, VC-010 |
| R-007 | Medium | Markdown role becomes authority or memory status. | Keep role as selection metadata only. | VC-007 |
| R-008 | Medium | Freshness reporting mutates durable memory. | Observational metadata only. | VC-011 |
| R-009 | Medium | Scope expands into persistence, ingestion, providers, or UI. | Static no-touch and dependency checks. | VC-012 |

## Residual Risk

Deterministic lexical recall will remain less semantically capable than future retrieval systems. This is accepted for v1 because inspectable bounded behavior is more important than retrieval sophistication.
