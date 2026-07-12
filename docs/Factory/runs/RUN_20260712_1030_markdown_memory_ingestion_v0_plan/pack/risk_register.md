# Risk Register: MMI-V0-001

## Version
v1

## Change Log
- v1 (2026-07-12): Stage E risk register.

| ID | Severity | Risk | Mitigation | Verification Hook |
| --- | --- | --- | --- | --- |
| R-001 | Critical | Ingestion creates accepted truth or authority. | Fixed candidate invariants; no review calls. | VC-001, VC-008 |
| R-002 | Critical | Path or symlink escapes repository root. | Resolve containment and validate input before reading. | VC-003 |
| R-003 | High | Role is treated as authority mode. | Shared role vocabulary; explicit mode and source authority. | VC-004 |
| R-004 | High | Parser creates low-quality Claims from structured Markdown. | Exact prose paragraphs only with exclusions and budget. | VC-005, VC-011 |
| R-005 | High | IDs or fingerprints are unstable or collide. | Canonical hashing rules and occurrence identity. | VC-006 |
| R-006 | High | Move/duplicate matching invents lineage. | Ordered comparison rules and ambiguous fail-closed state. | VC-007 |
| R-007 | High | Comparison mutates accepted-memory lifecycle. | Immutable observational snapshots/events. | VC-008 |
| R-008 | High | Claim metadata can be incomplete or inconsistent. | Contract-level required-key and value validation. | VC-001, VC-002 |
| R-009 | Medium | Role-module refactor regresses context recall. | Preserve public imports and run focused/full regressions. | VC-009, VC-012 |
| R-010 | Medium | CLI output is nondeterministic or unusable by review. | Stable JSON schema and candidate interchange export. | VC-010 |
| R-011 | Medium | Scope expands into persistence or semantic extraction. | Static no-touch/dependency checks. | VC-013 |
| R-012 | Medium | State docs claim more than implemented. | Closeout reconciliation. | VC-014 |

## Residual Risk

Prose-block extraction will miss Claims expressed in lists, tables, and implicit narrative. This is accepted because review precision and source fidelity are more important than coverage in v0.
