# Context Recall Report

## Version
v1

## Change Log
- v1 (2026-07-12): Generated recall report for profile `stage-a`.

## Report Metadata
- Profile: stage-a (Factory Stage A Preflight)
- Requested Scope: RUN_20260712_1011_vision_epistemic_hardening
- Effective Scope: docs
- Attempted Scopes: RUN_20260712_1011_vision_epistemic_hardening, docs/Factory/runs, docs/Factory/ProductOwner/phases, docs
- Fallback Applied: YES
- Coverage Verdict: SUFFICIENT
- Generated At (UTC): 2026-07-12T09:11:58Z
- Source Index: /private/tmp/factory_starter_kit_context/context.sqlite3

## Purpose
- Use this before Stage A to surface binding constraints, unresolved blockers, prior human checkpoints, and recent scope decisions tied to the new run.

## Coverage Snapshot
- Indexed sources in effective scope: 396
- Artifact types: {"canonical_doc": 54, "factory_run_pack_artifact": 299, "factory_run_root_artifact": 43}
- Focus terms: Project Memory claims source of truth delegated judgement decision outcomes memory rights knowledge scope Markdown authority success measures
- Trace IDs: None
- Required refs: docs/VISION.md, docs/CORE_CONCEPTS.md, docs/PROJECT_MEMORY_ARCHITECTURE.md, docs/THINKING_ENGINE_ARCHITECTURE.md
- Unresolved required refs: None

## Recall Queries
### Q1. `BLOCKING`
- Result count: 337
- Evidence:
  - `docs/Factory/runs/RUN_20260701_1604_roadmap_sequence_review/CONTEXT_RECALL_REPORT.md:31` [Context Recall Report > Recall Queries > Q1. `BLOCKING`]
  - `docs/Factory/runs/RUN_20260705_0923_live_coding_adapter_eval_plan/pack/intent.md:52` [Intent: LCAE-V0-001 Live Coding Adapter Evaluation Plan > Open Questions]
  - `docs/Factory/runs/RUN_20260712_0909_agent_context_relevance_v1_plan/CONTEXT_RECALL_REPORT.md:31` [Context Recall Report > Recall Queries > Q1. `BLOCKING`]
  - `docs/INTEGRATION_ARCHITECTURE.md:741` [Integration Architecture > Failure And Blocking States]
  - `docs/Factory/Harnesses/AGENT_LOOP_BRIDGE.md:139` [Agent Loop Bridge > Review Result Schema]

### Q2. `Critical`
- Result count: 117
- Evidence:
  - `docs/Factory/runs/RUN_20260712_0909_agent_context_relevance_v1_plan/CONTEXT_RECALL_REPORT.md:43` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/runs/RUN_20260701_1604_roadmap_sequence_review/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/runs/RUN_20260630_1129_project_memory_research/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/Spec/STAGE_CONTRACTS.md:214` [docs/Factory/Spec/STAGE_CONTRACTS.md — Factory Stage Contracts (v4.14) > STAGE_F — Verification Assets]
  - `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]

### Q3. `deferral`
- Result count: 86
- Evidence:
  - `docs/Factory/runs/RUN_20260712_0909_agent_context_relevance_v1_plan/CONTEXT_RECALL_REPORT.md:55` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260705_0923_live_coding_adapter_eval_plan/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/templates/PACK_AUDIT_REPORT_TEMPLATE.md:44` [docs/Factory/templates/PACK_AUDIT_REPORT_TEMPLATE.md > Deferrals Summary]
  - `docs/Factory/runs/RUN_20260630_1129_project_memory_research/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]

### Q4. `human GO`
- Result count: 188
- Evidence:
  - `docs/PROJECT_STATE.md:235` [Project State > Current Implementation State]
  - `docs/Factory/Harnesses/CODEX.md:216` [Codex Harness Adapter > Mission Goal Continuity (Experimental)]
  - `docs/PORTFOLIO_CONTEXT.md:207` [Portfolio Context > How Humans Experience The Portfolio]
  - `docs/CORE_CONCEPTS.md:603` [Core Concepts > Negotiation]
  - `docs/Factory/Harnesses/AGENT_LOOP_BRIDGE.md:55` [Agent Loop Bridge > Handoff Event Schema]

### Q5. `scope expansion`
- Result count: 124
- Evidence:
  - `docs/Factory/runs/RUN_20260712_0909_agent_context_relevance_v1_plan/CONTEXT_RECALL_REPORT.md:79` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260701_1604_roadmap_sequence_review/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260705_0923_live_coding_adapter_eval_plan/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260630_1129_project_memory_research/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]

### Q6. `Project Memory claims source of truth delegated judgement decision outcomes memory rights knowledge scope Markdown authority success measures`
- Result count: 0
- Evidence: None

## Trace Queries
## Required Reference Checks
### R1. `docs/VISION.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/VISION.md` (canonical_doc)

### R2. `docs/CORE_CONCEPTS.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/CORE_CONCEPTS.md` (canonical_doc)

### R3. `docs/PROJECT_MEMORY_ARCHITECTURE.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/PROJECT_MEMORY_ARCHITECTURE.md` (canonical_doc)

### R4. `docs/THINKING_ENGINE_ARCHITECTURE.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/THINKING_ENGINE_ARCHITECTURE.md` (canonical_doc)

## Operator Notes
- Carry forward any blockers, approvals, descopes, and human checkpoint references recovered above before the next stage proceeds.
