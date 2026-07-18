# Risk Register: GCT-V0-001

## Version

v1

## Change Log

- v1 (2026-07-18): Stage E risk register.

| ID | Severity | Risk | Mitigation | Verification Hook |
| --- | --- | --- | --- | --- |
| R-01 | Critical | Inaccessible object content or topology leaks through traversal output. | Per-hop access checks, opaque exclusions, no hidden bridges. | VC-04 |
| R-02 | Critical | Traversal is computationally or serially unbounded on dense cycles. | Depth, object, path, edge, exclusion, and explanation caps enforced during work. | VC-05, VC-06 |
| R-03 | Critical | Relationship direction is lost and affected-by results invert dependency meaning. | Direction on every path step and direction-aware impact policy. | VC-02, VC-10 |
| R-04 | High | Proposed, stale, or superseded memory displaces current truth. | Explicit non-current inclusion and current-first ordering. | VC-03 |
| R-05 | High | Path results vary with input order. | Canonical neighbor/path ordering before budgets. | VC-07 |
| R-06 | High | Existing agent-context fail-closed and budget behavior regresses. | Delegate expansion while retaining current document and memory selection contracts. | VC-08 |
| R-07 | High | Trace CLI breaks existing output consumers. | Preserve existing fields and add traversal output. | VC-09 |
| R-08 | High | Affected-by propagation overstates impact through unrelated relationship types. | Narrow command-owned relationship/direction allowlist. | VC-10 |
| R-09 | High | MMI-style Claim is promoted or treated as accepted by traversal. | Read-only service and explicit lifecycle assertions. | VC-11 |
| R-10 | Medium | External and missing local targets are conflated with inaccessible objects. | Distinct exclusion reasons and fixtures. | VC-12 |
| R-11 | Medium | New abstraction expands into query DSL or persistence. | Fixed request/result API, no dependencies, no-touch scans. | VC-13 |
| R-12 | Medium | Source matching becomes fuzzy and nondeterministic. | Exact normalized provenance and derivation refs only. | VC-10 |
| R-13 | Medium | Public package exports or help text omit the supported service. | Explicit API/CLI surface test. | VC-14 |
| R-14 | High | Unrelated Project Memory behavior regresses. | Full repository regression and knowledge lint. | VC-15 |
