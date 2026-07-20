# Verification Plan: LCAE-V0-001

## Version

v2

## Change Log

- v1 (2026-07-05): Initial Stage F verification plan in the upstream planning run.
- v2 (2026-07-20): Added current-source, context-reuse, hard-blocker, and no-touch verification.

## Strategy

Future implementation is verified entirely with committed source-profile fixtures, pure evaluator functions, fixed agent-context payloads, and deterministic text/JSON output. V4 live behavior remains deferred.

## Verification Tiers

- V0 artifact proof
- V1 static or mechanical check
- V2 focused fixture or unit test
- V3 regression suite
- V4 live or external proof

## Required Checks

| Check ID | Tier | Required Proof |
| --- | --- | --- |
| VC-001 | V2 | Exactly five supported surfaces load; unknown, duplicate, malformed, incomplete, and path-escaping profiles fail closed. |
| VC-002 | V2 | Profiles preserve source URL, access date, evidence kind, contradiction state, invocation/auth/capability/authority/permission/sandbox fields, output/trace/session/cost/latency paths, privacy controls, and limitations. |
| VC-003 | V2 | Contradictory official claims, stale-without-review profiles, and missing hard read-only guarantees emit stable non-compensable blockers. |
| VC-004 | V2 | Mutation-capable or externally hosted modes cannot qualify for a first read-only proof. |
| VC-005 | V2 | Hard gates run before scoring; auth, capability, authority, permission, sandbox, trace privacy, and candidate review remain independent. |
| VC-006 | V2 | Recommendation, no-recommendation, tie, blocked-high-score, rejected-alternative, and reversed-input-order cases are deterministic and explained. |
| VC-007 | V2 | Evaluation accepts existing agent-context output, preserves its selection/refresh states, source freshness, graph paths/exclusions, and budgets, and adds no alternate scanner or traversal. |
| VC-008 | V2 | Reports distinguish documentation evidence from measured evidence, show source access dates, and require future source revalidation. |
| VC-009 | V2 | Output is a local report; any simulated Provider Invocation or provider output remains proposed/candidate-only and cannot become current truth without existing Candidate Review. |
| VC-010 | V2 | Thin CLI delegates to evaluator functions and emits stable text and JSON for explicit profile/context inputs. |
| VC-011 | V1/V2 | Static imports plus guarded tests prove no provider command/import, credential/config/session read, network call, dependency install, external repository access, or evaluated-surface mutation path. |
| VC-012 | V1 | Scope scan finds no persistence, new graph/context/retrieval engine, UI, mission execution, Codex SDK profile, or neighbouring-product implementation. |
| VC-013 | V0/V1 | `external_source_review.md` is revalidated at implementation start; profile source dates match reviewed evidence or execution stops. |
| VC-014 | V3 | Focused Project Memory agent-context, graph, adapter twin, review, coding harness, coding workflow, and full repository tests pass. |

## Required Commands

```bash
python3 -m unittest tests/test_thinking_engine_adapter_evaluation.py tests/test_thinking_engine_adapter_evaluation_workflow.py
python3 -m unittest tests/test_project_memory_agent_context.py tests/test_project_memory_graph_traversal.py tests/test_project_memory_adapter_twins.py tests/test_project_memory_review.py tests/test_thinking_engine_coding_harness.py tests/test_thinking_engine_coding_workflow.py
python3 -m unittest discover -s tests
python3 -m compileall -q soane tests
bash scripts/knowledge_lint.sh
./scripts/factoryctl context-index
./scripts/factoryctl pack-lint --run RUN_20260720_0708_live_coding_adapter_eval_refresh
git diff --check
```

## Deferred Verification

- V4 provider invocation, auth, sandbox, network, mutation, cost, latency, and trace capture is deferred to a separate human-authorized live-proof pack.
- Credential provisioning and installed-version probes are deferred.
- Codex SDK evaluation is deferred.

## Acceptance Standard

VC-001 through VC-014 pass, no hard blocker is score-compensable, no side effect occurs, and a reviewer can explain every recommendation, rejection, and deferral from exact profile and context evidence.
