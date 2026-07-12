# Execution Prompt: ACR-V1-001

## Version

v1

## Change Log

- v1 (2026-07-12): Instantiated after Stage I2 PASS, pack-lint PASS, and explicit human Go.

## Run Metadata

- RUN_ID: `RUN_20260712_0909_agent_context_relevance_v1_plan`
- Sprint ID: `ACR-V1-001`
- Created: 2026-07-12 10:45 WEST
- Source Pack: `docs/Factory/runs/RUN_20260712_0909_agent_context_relevance_v1_plan/pack/`
- Execution Mode: `EXECUTION_ENABLED`
- Execution Authorization: Human `Go` recorded 2026-07-12

## Purpose

Implement bounded natural-task recall, fail-closed zero-match agent context, explicit selection and refresh states, one-hop governed relationship expansion, and atomic local context-index publication. Do not add persistence, embeddings, external providers, ingestion, product UI, live adapters, or portfolio responsibilities.

## Required Read Order

1. `docs/PROJECT_STATE.md`
2. `docs/ROADMAP.md`
3. `docs/Factory/ORCHESTRATION.md`
4. `docs/Factory/SCRATCHPAD.md`, only `## Active Pitfalls (Mandatory)`
5. `pack/intent.md`
6. `pack/intent_lock_report.md`
7. `pack/risk_register.md`
8. `pack/verification_plan.md`
9. `pack/traceability_matrix.md`
10. `pack/micro_sprints.md`
11. `pack/ACR-V1-001_ENVELOPE.md`
12. `pack/PACK_AUDIT_REPORT.md`

## Skill Routing Contract

- Use the `factory-execution-closeout` skill for final pack-alignment review and execution completion evidence.
- No dedicated skill applies to implementation micro-sprints; execute via the locked envelope and repository engineering rules.

## Execution Sequence

1. MS-00: establish focused failing verification cases.
2. MS-01: implement bounded deterministic query planning.
3. MS-02: implement fail-closed selection state and separate budgets.
4. MS-03: implement one-hop allowlisted relationship expansion.
5. MS-04: implement isolated, ownership-aware, atomic refresh publication.
6. MS-05: complete output contracts, focused tests, full regression, lint, and scope audit.
7. MS-06: prepare validation closeout and update state documents.

## Hard Guardrails

- Do not infer broad memory selection from empty seeds.
- Do not weaken visibility, suppression, lifecycle, propagation, contradiction, evidence, or authority distinctions.
- Do not issue unbounded recall queries per task token.
- Preserve the previous valid index until a complete replacement is ready.
- Report only `refreshed`, `reused`, or `failed` refresh states.
- Keep traversal one hop and within the allowlist and memory budget.
- Keep source freshness observational; do not mutate lifecycle status.
- Any persistence, external retrieval, ingestion, UI, live adapter, dependency, or portfolio-boundary change is blocking scope expansion.

## SIMPLE-CODE-GATE V2

- Implement the smallest clear local change in existing owner modules.
- Add no dependency, framework, registry, strategy layer, plugin seam, daemon, or service.
- Do not swallow refresh or selection errors.
- Add helpers only when they name stable behavior and reduce branching in current call paths.

## Verification Contract

- Focused agent-context and context-index tests prove VC-001 through VC-009 and VC-013.
- `python3 -m unittest discover -s tests`
- `bash scripts/knowledge_lint.sh`
- `./scripts/factoryctl context-index`
- `./scripts/factoryctl pack-lint --run RUN_20260712_0909_agent_context_relevance_v1_plan`
- `git diff --check`
- Factory execution closeout records VC-010 through VC-012, file-budget alignment, and residual lexical-relevance risk.

## Exit Checklist

- All thirteen verification checks pass.
- No Critical or High risk remains unverified.
- Actual files stay within the twelve-modified, four-created, zero-deleted implementation envelope.
- SIMPLE-CODE-GATE v2 review accepts the final complexity.
- `VALIDATION_CLOSEOUT_REPORT.md` records commands, results, deviations, and residual risk.
- Project state, roadmap, changelog, and reviewed Project Memory evidence reflect the implementation truthfully.
