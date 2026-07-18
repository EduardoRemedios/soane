# Pre-mortem: GCT-V0-001

## Version

v1

## Change Log

- v1 (2026-07-18): Stage E failure analysis.

## Failure Scenarios

### PM-01 Hidden Bridge Leakage

Traversal suppresses a restricted intermediate object in output but still reaches and returns a visible dependent through it.

- Mitigation: Stop expansion at every inaccessible node; test that the visible downstream object is absent.

### PM-02 Directional Impact Inversion

`agent-affected` follows outbound `depends_on` when it needs inbound dependents and reports prerequisites as impacted.

- Mitigation: Encode direction with each allowed impact relationship and assert asymmetric fixtures.

### PM-03 Dense Graph Work Explosion

A two-hop cyclic graph remains expensive because thousands of edges and path variants are examined before output limits apply.

- Mitigation: Enforce examined-edge and path budgets during traversal, not during serialization.

### PM-04 Proposed Claim Becomes Current Context

An MMI-generated proposed Claim ranks above accepted memory or is described as current truth because graph proximity overrides lifecycle.

- Mitigation: Reuse lifecycle semantics, rank current first, and require explicit non-current inclusion.

### PM-05 Competing Traversal Logic

`agent-context`, `agent-trace`, and `agent-affected` each retain subtly different direction and visibility behavior.

- Mitigation: One traversal module owns graph mechanics; command code owns only policies and presentation.

### PM-06 Nondeterministic Paths

Fixture load order or object insertion order changes which equal-length path survives the path budget.

- Mitigation: Canonically sort neighbors and complete paths before budget admission; compare repeated JSON results.

### PM-07 Explanation Leaks Metadata

An inaccessible exclusion includes a target title or object type obtained through audit lookup.

- Mitigation: Use opaque target IDs and source-edge facts only; adversarial JSON assertions forbid hidden strings.

### PM-08 CLI Regression

Existing users lose `outgoing`, `incoming`, object summaries, or context reason fields when graph output is introduced.

- Mitigation: Add graph output fields and retain prior fields with focused regression tests.

### PM-09 Overbroad Impact

References, evidence, capability, or authority links are traversed indiscriminately, turning proximity into unsupported causal impact.

- Mitigation: Start with a narrow documented `(relationship, direction)` policy and include excluded unrelated edges.

### PM-10 Platform Drift

Implementation introduces a graph repository, query DSL, generic predicate framework, or persistence abstraction before access patterns justify it.

- Mitigation: File budget, no-dependency rule, two-hop maximum, fixed dataclasses, and no-touch scans.

## Residual Risk

Authored relationships may be incomplete or directionally inconsistent in real memory. The slice can explain only the graph that exists; it must not infer missing edges. Real-source proof should report useful paths and omissions without claiming graph completeness.
