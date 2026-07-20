# Risk Register: LCAE-V0-001

## Version

v2

## Change Log

- v1 (2026-07-05): Initial Stage E risk register in the upstream planning run.
- v2 (2026-07-20): Added contradiction, parallel-context, privacy, and recommendation-bias risks.

| ID | Severity | Risk | Mitigation | Verification Hook |
| --- | --- | --- | --- | --- |
| R-001 | Critical | Evaluation executes a provider, reads credential/config/session state, accesses network, or installs a dependency. | Committed fixtures and explicit inputs only; no subprocess/provider imports/environment credential access. | VC-001, VC-011 |
| R-002 | Critical | Evaluated surface or harness mutates repository content. | No evaluated-surface execution; explicit report destination contract; pre/post worktree proof. | VC-004, VC-011 |
| R-003 | Critical | Contradictory or missing hard read-only evidence is treated as safe. | Non-compensable `source_contradiction` and `hard_read_only_unproven` gates. | VC-003, VC-006 |
| R-004 | High | Capability, auth, authority, permission, and sandbox are collapsed. | Typed separate fields and independent hard-gate tests. | VC-002, VC-005 |
| R-005 | High | Adapter evaluator reimplements repository context or graph semantics. | Consume existing agent-context bundle only; static and behavioral integration checks. | VC-007, VC-012 |
| R-006 | High | Source recency is mistaken for measured behavior. | Evidence-kind and access-date fields; V4 behavior explicitly deferred. | VC-002, VC-008 |
| R-007 | High | Recommendation is biased or order-dependent. | Versioned fixed criteria, hard gates before scores, stable tie handling. | VC-005, VC-006 |
| R-008 | High | Trace or serialized state captures sensitive project data. | Separate privacy fields and blockers for unclear sensitive-data controls. | VC-002, VC-005 |
| R-009 | High | Evaluation or simulated output bypasses Candidate Review. | Local report only; simulated Provider Invocation remains proposed/candidate-only. | VC-009 |
| R-010 | Medium | Codex SDK or another surface expands scope. | Exact surface enum and unknown-surface rejection. | VC-001, VC-012 |
| R-011 | Medium | Existing context, graph, adapter, or coding proof behavior regresses. | Focused and full repository regression. | VC-010, VC-014 |
| R-012 | Medium | Official source snapshot becomes stale before implementation. | Source revalidation at implementation start and profile access-date reporting. | VC-008, VC-013 |
