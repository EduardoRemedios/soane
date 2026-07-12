# Risk Register: VEH-V1-001

## Version
v1

## Change Log
- v1 (2026-07-12): Stage E risk register.

| ID | Severity | Risk | Mitigation | Verification Hook |
| --- | --- | --- | --- | --- |
| R-001 | Critical | Workspace understanding overrides external authority. | Define source authority and portfolio ownership explicitly. | VC-001, VC-008 |
| R-002 | High | Agent judgement implies permission. | Bind delegation to explicit external authority and accountability. | VC-002 |
| R-003 | High | Cross-project knowledge leaks restrictions or identity. | Fail closed; propagate scope, provenance, and restrictions. | VC-003 |
| R-004 | High | Markdown generation overwrites authored meaning. | Three modes and reviewed promotion/write-back. | VC-004 |
| R-005 | High | Docs claim runtime types that do not exist. | Explicit deferred implementation boundary. | VC-005 |
| R-006 | Medium | Decision review does not feed learning. | Define traceable expected-versus-observed review. | VC-006 |
| R-007 | Medium | Measures reward artifact volume. | Outcome and attention measures with anti-metric rule. | VC-007 |
| R-008 | Medium | Broad edits create unrelated doctrine drift. | File budget and scoped diff review. | VC-008 |

## Residual Risk

Doctrine will precede runtime enforcement. The roadmap must retain a bounded implementation candidate rather than representing the new concepts as operational today.
