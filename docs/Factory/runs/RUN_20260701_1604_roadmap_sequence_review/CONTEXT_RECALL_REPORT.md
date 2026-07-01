# Context Recall Report

## Version
v1

## Change Log
- v1 (2026-07-01): Generated recall report for profile `stage-a`.

## Report Metadata
- Profile: stage-a (Factory Stage A Preflight)
- Requested Scope: RUN_20260701_1604_roadmap_sequence_review
- Effective Scope: docs/Factory/runs
- Attempted Scopes: RUN_20260701_1604_roadmap_sequence_review, docs/Factory/runs, docs/Factory/ProductOwner/phases, docs
- Fallback Applied: YES
- Coverage Verdict: SUFFICIENT
- Generated At (UTC): 2026-07-01T15:04:51Z
- Source Index: /private/tmp/factory_starter_kit_context/context.sqlite3

## Purpose
- Use this before Stage A to surface binding constraints, unresolved blockers, prior human checkpoints, and recent scope decisions tied to the new run.

## Coverage Snapshot
- Indexed sources in effective scope: 186
- Artifact types: {"factory_run_pack_artifact": 162, "factory_run_root_artifact": 24}
- Focus terms: None
- Trace IDs: None
- Required refs: None
- Unresolved required refs: None

## Recall Queries
### Q1. `BLOCKING`
- Result count: 160
- Evidence:
  - `docs/Factory/runs/RUN_20260630_1129_project_memory_research/CONTEXT_RECALL_REPORT.md:31` [Context Recall Report > Recall Queries > Q1. `BLOCKING`]
  - `docs/Factory/runs/RUN_20260630_1129_project_memory_research/pack/HANDOFF/HANDOFF_STAGE_A.md:51` [Handoff Stage A > Open Issues > BLOCKING]
  - `docs/Factory/runs/RUN_20260630_1129_project_memory_research/pack/HANDOFF/HANDOFF_STAGE_A.md:55` [Handoff Stage A > Open Issues > NON-BLOCKING]
  - `docs/Factory/runs/RUN_20260630_1129_project_memory_research/pack/HANDOFF/HANDOFF_STAGE_I2.md:53` [Handoff Stage I2 > Open Issues > BLOCKING]
  - `docs/Factory/runs/RUN_20260630_1129_project_memory_research/pack/HANDOFF/HANDOFF_STAGE_I2.md:57` [Handoff Stage I2 > Open Issues > NON-BLOCKING]

### Q2. `Critical`
- Result count: 45
- Evidence:
  - `docs/Factory/runs/RUN_20260630_1129_project_memory_research/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/runs/RUN_20260701_0848_project_memory_v0_plan/pack/PACK_CHECKLIST.md:11` [Pack Checklist > Critical]
  - `docs/Factory/runs/RUN_20260701_1438_thinking_engine_intake_v0_plan/pack/PACK_CHECKLIST.md:16` [Pack Checklist > Critical]
  - `docs/Factory/runs/RUN_20260701_1455_candidate_review_promotion_v0_plan/pack/PACK_CHECKLIST.md:16` [Pack Checklist > Critical]
  - `docs/Factory/runs/RUN_20260701_1529_socratic_discovery_v0_plan/pack/PACK_CHECKLIST.md:16` [Pack Checklist > Critical]

### Q3. `deferral`
- Result count: 37
- Evidence:
  - `docs/Factory/runs/RUN_20260630_1129_project_memory_research/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260630_1129_project_memory_research/pack/PACK_AUDIT_REPORT.md:36` [Pack Audit Report > Deferrals Summary]
  - `docs/Factory/runs/RUN_20260701_0848_project_memory_v0_plan/pack/PACK_CHECKLIST.md:23` [Pack Checklist > Conditional]
  - `docs/Factory/runs/RUN_20260701_1438_thinking_engine_intake_v0_plan/pack/PACK_CHECKLIST.md:28` [Pack Checklist > Conditional]
  - `docs/Factory/runs/RUN_20260701_1455_candidate_review_promotion_v0_plan/pack/PACK_CHECKLIST.md:28` [Pack Checklist > Conditional]

### Q4. `human GO`
- Result count: 54
- Evidence:
  - `docs/Factory/runs/RUN_20260701_1438_thinking_engine_intake_v0_plan/raw_brief.md:138` [Raw Brief: Thinking Engine Intake v0 Planning > Go Or No-Go Rule]
  - `docs/Factory/runs/RUN_20260701_1438_thinking_engine_intake_v0_plan/pack/intent.md:82` [Intent: Thinking Engine Intake v0 > Go Or No-Go Rule]
  - `docs/Factory/runs/RUN_20260701_1455_candidate_review_promotion_v0_plan/pack/intent.md:91` [Intent: Candidate Review and Promotion v0 > Go Or No-Go Rule]
  - `docs/Factory/runs/RUN_20260701_1529_socratic_discovery_v0_plan/pack/intent.md:93` [Intent: Socratic Discovery v0 > Go Or No-Go Rule]
  - `docs/Factory/runs/RUN_20260701_1548_coding_proof_harness_v0_plan/pack/intent.md:99` [Intent: Coding Proof Harness v0 > Go Or No-Go Rule]

### Q5. `scope expansion`
- Result count: 42
- Evidence:
  - `docs/Factory/runs/RUN_20260630_1129_project_memory_research/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260630_1129_project_memory_research/pack/PACK_AUDIT_REPORT.md:43` [Pack Audit Report > Scope Expansion Summary]
  - `docs/Factory/runs/RUN_20260701_0848_project_memory_v0_plan/pack/intent_lock_report.md:33` [Intent Lock Report > Scope Expansion Review]
  - `docs/Factory/runs/RUN_20260701_0848_project_memory_v0_plan/pack/intent_synthesis.md:26` [Intent Synthesis: Project Memory v0 Plan > Scope Expansion Review]
  - `docs/Factory/runs/RUN_20260701_1438_thinking_engine_intake_v0_plan/pack/intent_synthesis.md:28` [Intent Synthesis > Scope Expansion Review]

## Trace Queries
## Required Reference Checks
## Operator Notes
- Carry forward any blockers, approvals, descopes, and human checkpoint references recovered above before the next stage proceeds.
