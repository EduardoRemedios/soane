# Execution Prompt: GCT-V0-001

## Version

v1

## Change Log

- v1 (2026-07-18): Generated after Stage I2 PASS and human Go.

## Run Metadata

- RUN_ID: `RUN_20260718_0721_graph_aware_context_trace_plan`
- Sprint ID: `SPRINT_20260718_001`
- Created: 2026-07-18 07:50 WEST
- Source Pack: `docs/Factory/runs/RUN_20260718_0721_graph_aware_context_trace_plan/pack/`

## Purpose

Implement the locked storage-neutral graph traversal service and integrate it with existing agent context, trace, and affected-by workflows. Do not introduce persistence, inferred edges, code graphs, new relationship types, external providers, UI, or automatic memory mutation.

## Required Read Order

1. `docs/PROJECT_STATE.md`
2. `docs/ROADMAP.md`
3. `docs/Factory/ORCHESTRATION.md`
4. `docs/Factory/SCRATCHPAD.md` `## Active Pitfalls (Mandatory)`
5. `pack/intent.md`
6. `pack/intent_lock_report.md`
7. `pack/risk_register.md`
8. `pack/verification_plan.md`
9. `pack/traceability_matrix.md`
10. `pack/verification_manifest.yaml`
11. `pack/micro_sprints.md`
12. `pack/SPRINT_20260718_001_ENVELOPE.md`
13. `pack/PACK_AUDIT_REPORT.md`

## Skill Routing Contract

- No dedicated implementation skill applies; execute via the locked envelope and repository engineering contract.
- Use the `factory-execution-closeout` skill for validation and closeout.

## Hard Guardrails

- Apply SIMPLE-CODE-GATE v2.
- Use existing Project Memory types and relationships only.
- Enforce access policy at seeds and every hop; inaccessible nodes never bridge traversal.
- Enforce hard depth, object, path, examined-edge, exclusion, and explanation ceilings.
- Preserve existing CLI fields and agent-context fail-closed behavior.
- Do not expand scope implicitly; any net-new requirement is `[SCOPE EXPANSION]` and BLOCKING.

## Micro-sprint Sequence

1. MS-00: Add realistic Claim graph and failing traversal tests.
2. MS-01: Implement the storage-neutral traversal service and public exports.
3. MS-02: Delegate agent-context graph expansion to the service.
4. MS-03: Add bounded trace and affected-by integrations.
5. MS-04: Prove realistic Claim propagation without mutation.
6. MS-05: Run regression and scope gates.
7. MS-06: Reconcile canonical docs and produce execution closeout.

Each micro-sprint uses its entry, exit, and stop/go gate from `pack/micro_sprints.md`.

## Verification Contract

- `python3 -m unittest tests.test_project_memory_graph_traversal tests.test_project_memory_agent_context`
- `python3 -m unittest discover -s tests`
- `bash scripts/knowledge_lint.sh`
- `./scripts/factoryctl context-index`
- `./scripts/factoryctl pack-lint --run RUN_20260718_0721_graph_aware_context_trace_plan`
- `git diff --check`

Run every check in `pack/verification_manifest.yaml` in order. A `halt_on_failure: true` failure blocks closeout.

## Troubleshooting

- Stop and reconcile contract drift before further feature work.
- Do not bypass policy or budget failures with silent filtering.
- If a command compatibility test fails, preserve the prior field and add graph detail additively.
- If the realistic Claim graph needs inferred relationships, report the missing authored edge and stop.

## Final Exit Checklist

- Scope delivered within file budgets.
- SIMPLE-CODE-GATE v2 satisfied.
- Verification manifest checks pass.
- Realistic graph evidence records selected objects, examined edges, exclusions, and truncations.
- Project State, Roadmap, Changelog, and validation closeout are updated truthfully.
- Residual risks and bounded deferrals remain explicit.
