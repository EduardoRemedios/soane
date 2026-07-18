# Verification Plan: GCT-V0-001

## Version

v1

## Change Log

- v1 (2026-07-18): Stage F verification design.

## Strategy

Use fixed in-memory Project Memory graphs and subprocess CLI tests. Prove graph semantics at the service boundary first, then command integration, then full regression and no-touch constraints.

## Checks

| ID | Tier | Check | Expected Evidence |
| --- | --- | --- | --- |
| VC-01 | V2 | Validate empty seeds, empty allowlist, invalid limits, and depth greater than two. | Focused service tests fail closed with stable errors/results. |
| VC-02 | V2 | Traverse the same asymmetric edge inbound and outbound. | Different destinations and directional path steps. |
| VC-03 | V2 | Compare current-only and explicit non-current traversal. | Current-first order; proposed/superseded only when enabled. |
| VC-04 | V2 | Seed and traverse toward restricted/suppressed nodes. | No hidden content, no hidden bridge, opaque exclusion only. |
| VC-05 | V2 | Traverse a cycle with repeated edges. | Termination, unique selection, bounded alternate paths. |
| VC-06 | V2 | Exhaust object, path, examined-edge, exclusion, and explanation budgets. | Deterministic structured truncations and omitted counts. |
| VC-07 | V2 | Shuffle object/edge insertion order and repeat traversal. | Byte-stable semantic JSON after serialization. |
| VC-08 | V3 | Run existing and new agent-context tests. | Fail-closed recall, separate budgets, selection states, and reasons preserved. |
| VC-09 | V2 | Exercise trace CLI defaults and explicit controls. | Existing fields plus paths, exclusions, and truncations. |
| VC-10 | V2 | Exercise exact source affected-by propagation. | Direct Claim plus only allowlisted directional dependents; unmatched path is empty. |
| VC-11 | V2 | Use fixed realistic MMI-style Claim graph. | Source-to-Claim-to-dependent path; no review or lifecycle mutation. |
| VC-12 | V2 | Include external, missing local, inaccessible, disallowed, and depth-bound edges. | Distinct reasons with no inaccessible metadata. |
| VC-13 | V1 | Scan diff/imports for persistence, query DSL, dependencies, semantic inference, and code graph work. | No forbidden files, dependencies, or concepts. |
| VC-14 | V2 | Test public package exports and CLI help. | Traversal API and controls are discoverable and bounded. |
| VC-15 | V3 | Run full repository tests, knowledge lint, pack lint, and diff check. | All pass at closeout. |

## Critical And High Coverage

- R-01: VC-04
- R-02: VC-05, VC-06
- R-03: VC-02, VC-10
- R-04: VC-03, VC-11
- R-05: VC-07
- R-06: VC-08
- R-07: VC-09
- R-08: VC-10
- R-09: VC-11
- R-14: VC-15

## Execution Commands

Planned commands after human Go:

```bash
python3 -m unittest tests.test_project_memory_graph_traversal tests.test_project_memory_agent_context
python3 -m unittest discover -s tests
bash scripts/knowledge_lint.sh
./scripts/factoryctl pack-lint --run RUN_20260718_0721_graph_aware_context_trace_plan
git diff --check
```

## Stop Conditions

- Hidden content appears anywhere in output.
- Traversal exceeds a declared work budget.
- Any command retains independent relationship expansion.
- A proposed Claim changes lifecycle or epistemic status.
- Implementation requires a dependency, persistence, semantic inference, new relationship type, code graph, or depth greater than two.
