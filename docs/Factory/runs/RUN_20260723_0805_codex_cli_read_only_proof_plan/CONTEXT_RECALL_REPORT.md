# Context Recall Report

## Version
v1

## Change Log
- v1 (2026-07-23): Generated recall report for profile `stage-a`.

## Report Metadata
- Profile: stage-a (Factory Stage A Preflight)
- Requested Scope: RUN_20260723_0805_codex_cli_read_only_proof_plan
- Effective Scope: docs
- Attempted Scopes: RUN_20260723_0805_codex_cli_read_only_proof_plan, docs/Factory/runs, docs, docs/Factory/ProductOwner/phases
- Fallback Applied: YES
- Coverage Verdict: WEAK
- Generated At (UTC): 2026-07-23T07:06:29Z
- Source Index: /private/tmp/factory_starter_kit_context/context.sqlite3

## Purpose
- Use this before Stage A to surface binding constraints, unresolved blockers, prior human checkpoints, and recent scope decisions tied to the new run.

## Coverage Snapshot
- Indexed sources in effective scope: 522
- Artifact types: {"canonical_doc": 54, "factory_run_pack_artifact": 407, "factory_run_root_artifact": 61}
- Focus terms: Codex CLI read-only proof, live coding proof
- Trace IDs: LCAE-V0-001, RUN_20260720_0708_live_coding_adapter_eval_refresh
- Required refs: RUN_20260720_0708_live_coding_adapter_eval_refresh, LCAE-V0-001, docs/ROADMAP.md
- Unresolved required refs: LCAE-V0-001

## Recall Queries
### Q1. `BLOCKING`
- Result count: 421
- Evidence:
  - `docs/Factory/runs/RUN_20260701_1604_roadmap_sequence_review/CONTEXT_RECALL_REPORT.md:31` [Context Recall Report > Recall Queries > Q1. `BLOCKING`]
  - `docs/Factory/runs/RUN_20260712_1030_markdown_memory_ingestion_v0_plan/CONTEXT_RECALL_REPORT.md:31` [Context Recall Report > Recall Queries > Q1. `BLOCKING`]
  - `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/CONTEXT_RECALL_REPORT.md:31` [Context Recall Report > Recall Queries > Q1. `BLOCKING`]
  - `docs/Factory/runs/RUN_20260712_1011_vision_epistemic_hardening/CONTEXT_RECALL_REPORT.md:31` [Context Recall Report > Recall Queries > Q1. `BLOCKING`]
  - `docs/Factory/runs/RUN_20260705_0923_live_coding_adapter_eval_plan/pack/intent.md:52` [Intent: LCAE-V0-001 Live Coding Adapter Evaluation Plan > Open Questions]
  - `docs/Factory/runs/RUN_20260712_0909_agent_context_relevance_v1_plan/CONTEXT_RECALL_REPORT.md:31` [Context Recall Report > Recall Queries > Q1. `BLOCKING`]
  - `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/pack/intent.md:63` [Intent: LCAE-V0-001 Live Coding Adapter Evaluation > Open Questions]
  - `docs/INTEGRATION_ARCHITECTURE.md:741` [Integration Architecture > Failure And Blocking States]

### Q2. `Critical`
- Result count: 173
- Evidence:
  - `docs/Factory/runs/RUN_20260712_0909_agent_context_relevance_v1_plan/CONTEXT_RECALL_REPORT.md:43` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/runs/RUN_20260701_1604_roadmap_sequence_review/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/runs/RUN_20260630_1129_project_memory_research/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/runs/RUN_20260712_1011_vision_epistemic_hardening/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/runs/RUN_20260712_1030_markdown_memory_ingestion_v0_plan/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/Spec/STAGE_CONTRACTS.md:214` [docs/Factory/Spec/STAGE_CONTRACTS.md — Factory Stage Contracts (v4.14) > STAGE_F — Verification Assets]
  - `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]

### Q3. `deferral`
- Result count: 132
- Evidence:
  - `docs/Factory/runs/RUN_20260712_0909_agent_context_relevance_v1_plan/CONTEXT_RECALL_REPORT.md:55` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260705_0923_live_coding_adapter_eval_plan/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260712_1011_vision_epistemic_hardening/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260712_1030_markdown_memory_ingestion_v0_plan/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/templates/PACK_AUDIT_REPORT_TEMPLATE.md:44` [docs/Factory/templates/PACK_AUDIT_REPORT_TEMPLATE.md > Deferrals Summary]
  - `docs/Factory/runs/RUN_20260630_1129_project_memory_research/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]

### Q4. `human GO`
- Result count: 249
- Evidence:
  - `docs/PROJECT_STATE.md:270` [Project State > Current Implementation State]
  - `docs/Factory/Harnesses/CODEX.md:216` [Codex Harness Adapter > Mission Goal Continuity (Experimental)]
  - `docs/PORTFOLIO_CONTEXT.md:207` [Portfolio Context > How Humans Experience The Portfolio]
  - `docs/CORE_CONCEPTS.md:150` [Core Concepts > Canonical Document]
  - `docs/CORE_CONCEPTS.md:685` [Core Concepts > Negotiation]
  - `docs/Factory/Harnesses/AGENT_LOOP_BRIDGE.md:55` [Agent Loop Bridge > Handoff Event Schema]
  - `docs/Factory/ProductOwner/PO_PROCESS.md:40` [Product Owner Pre-Factory Process > 0.2 Separation of Concerns (HARD)]
  - `docs/Factory/runs/RUN_20260712_1011_vision_epistemic_hardening/pack/intent.md:20` [Intent: VEH-V1-001 Vision And Epistemic Model Hardening > Requirements]

### Q5. `scope expansion`
- Result count: 166
- Evidence:
  - `docs/Factory/runs/RUN_20260712_0909_agent_context_relevance_v1_plan/CONTEXT_RECALL_REPORT.md:79` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260701_1604_roadmap_sequence_review/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260705_0923_live_coding_adapter_eval_plan/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260712_1011_vision_epistemic_hardening/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260712_1030_markdown_memory_ingestion_v0_plan/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/PROJECT_STATE.md:270` [Project State > Current Implementation State]
  - `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]

### Q6. `Codex CLI read-only proof`
- Result count: 18
- Evidence:
  - `docs/ROADMAP.md:43` [Roadmap > Sequence]
  - `docs/ROADMAP.md:143` [Roadmap > Current Candidates]
  - `docs/ROADMAP.md:192` [Roadmap > Process Guidance]
  - `docs/PROJECT_STATE.md:270` [Project State > Current Implementation State]
  - `docs/CHANGELOG.md:3` [Changelog > 2026-07-23]
  - `docs/ROADMAP.md:100` [Roadmap > Immediate Next Move]
  - `docs/CHANGELOG.md:58` [Changelog > 2026-07-05]
  - `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/pack/external_source_review.md:42` [External Source Review: Live Coding Adapter Surfaces > Refresh Conclusions]

### Q7. `live coding proof`
- Result count: 67
- Evidence:
  - `docs/ROADMAP.md:43` [Roadmap > Sequence]
  - `docs/ROADMAP.md:143` [Roadmap > Current Candidates]
  - `docs/ROADMAP.md:7` [Roadmap > Completed]
  - `docs/PROJECT_STATE.md:270` [Project State > Current Implementation State]
  - `docs/CHANGELOG.md:58` [Changelog > 2026-07-05]
  - `docs/Factory/runs/RUN_20260702_0617_coding_harness_workflow_v0_plan/VALIDATION_CLOSEOUT_REPORT.md:25` [Validation Closeout Report: CHW-V0-001 Coding Harness Workflow v0 > Verification Evidence]
  - `docs/PROJECT_STATE.md:93` [Project State > What Exists]
  - `docs/CHANGELOG.md:71` [Changelog > 2026-07-01]

## Trace Queries
### T1. `LCAE-V0-001`
- Match count: 0
- Evidence: None

### T2. `RUN_20260720_0708_live_coding_adapter_eval_refresh`
- Match count: 24
- Evidence:
  - `docs/CHANGELOG.md:13` [run_id]
  - `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/CONTEXT_RECALL_REPORT.md:9` [run_id]
  - `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/EXECUTION_PROMPT.md:11` [run_id]
  - `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/RETRO.md:1` [run_id]
  - `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/pack/HANDOFF/HANDOFF_STAGE_A.md:28` [run_id]
  - `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/pack/HANDOFF/HANDOFF_STAGE_B.md:25` [run_id]
  - `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/pack/HANDOFF/HANDOFF_STAGE_C.md:27` [run_id]
  - `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/pack/HANDOFF/HANDOFF_STAGE_D.md:27` [run_id]
  - `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/pack/HANDOFF/HANDOFF_STAGE_E.md:26` [run_id]
  - `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/pack/HANDOFF/HANDOFF_STAGE_F.md:29` [run_id]
  - `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/pack/HANDOFF/HANDOFF_STAGE_G.md:27` [run_id]
  - `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/pack/HANDOFF/HANDOFF_STAGE_H.md:28` [run_id]
  - `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/pack/HANDOFF/HANDOFF_STAGE_I.md:28` [run_id]
  - `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/pack/HANDOFF/HANDOFF_STAGE_I2.md:31` [run_id]
  - `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/pack/HANDOFF/HANDOFF_STAGE_J.md:30` [run_id]
  - `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/pack/PACK_MANIFEST.md:13` [run_id]
  - `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/pack/verification_plan.md:43` [run_id]
  - `docs/Factory/runs/RUN_20260723_0805_codex_cli_read_only_proof_plan/raw_brief.md:20` [run_id]
  - `docs/PROJECT_STATE.md:93` [run_id]
  - `docs/PROJECT_STATE.md:238` [run_id]
  - `docs/PROJECT_STATE.md:270` [run_id]
  - `docs/ROADMAP.md:7` [run_id]
  - `docs/ROADMAP.md:43` [run_id]
  - `docs/ROADMAP.md:143` [run_id]

## Required Reference Checks
### R1. `RUN_20260720_0708_live_coding_adapter_eval_refresh`
- Status: RESOLVED
- Resolution Type: identifier
- Evidence:
  - `docs/CHANGELOG.md` (canonical_doc)
  - `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/CONTEXT_RECALL_REPORT.md` (factory_run_root_artifact)
  - `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/EXECUTION_PROMPT.md` (factory_run_root_artifact)

### R2. `LCAE-V0-001`
- Status: UNRESOLVED
- Resolution Type: path
- Evidence: None

### R3. `docs/ROADMAP.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/ROADMAP.md` (canonical_doc)

## Operator Notes
- Carry forward any blockers, approvals, descopes, and human checkpoint references recovered above before the next stage proceeds.

## Direct-Source Repair

- Original Generated Verdict: WEAK
- Direct-Source Repair Status: APPLIED
- Final Repaired Verdict: REPAIRED_DIRECT_SOURCE_CHECK
- Unresolved Generated Refs: `LCAE-V0-001`
- Context Index Refreshed: YES
- Fallback Scopes Attempted: YES
- Remaining Unresolved Generated Refs: None
- Remaining Material Unresolved Refs: None
- Materiality Check: PASS

## Direct Sources Read

- `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/VALIDATION_CLOSEOUT_REPORT.md`
- `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/pack/LCAE-V0-001_ENVELOPE.md`
- `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/pack/external_source_review.md`
- `soane/thinking_engine/adapter_evaluation.py`
- `tests/fixtures/live_adapter_evaluation/profiles/codex_cli.json`
- `docs/ROADMAP.md`

## Source Summaries

### `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/VALIDATION_CLOSEOUT_REPORT.md`

- Summary: Records a READY deterministic evaluator, Codex CLI as a documentation-level recommendation, no live authorization, and explicit uncertainty around installed behavior, auth, network, hooks, filesystem writes, cost, latency, and traces.
- Covers refs: `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/VALIDATION_CLOSEOUT_REPORT.md`
- Remaining unresolved refs: None

### `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/pack/LCAE-V0-001_ENVELOPE.md`

- Summary: Requires any first live read-only proof to use a separate Factory run and separate human authorization.
- Covers refs: `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/pack/LCAE-V0-001_ENVELOPE.md`
- Remaining unresolved refs: None

### `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/pack/external_source_review.md`

- Summary: Records Codex CLI working-directory control, JSONL, output schemas, ephemeral mode, and read-only sandbox documentation while refusing to treat those claims as measured live behavior.
- Covers refs: `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/pack/external_source_review.md`
- Remaining unresolved refs: None

### `soane/thinking_engine/adapter_evaluation.py`

- Summary: Implements hard gates and emits `authorizes_live_use: false`; it contains no provider invocation path.
- Covers refs: `soane/thinking_engine/adapter_evaluation.py`
- Remaining unresolved refs: None

### `tests/fixtures/live_adapter_evaluation/profiles/codex_cli.json`

- Summary: Preserves documentation-only evidence, authority and project-permission preconditions, explicit read-only sandbox state, candidate review, and residual network and hook uncertainty.
- Covers refs: `tests/fixtures/live_adapter_evaluation/profiles/codex_cli.json`
- Remaining unresolved refs: None

### `docs/ROADMAP.md`

- Summary: Names this bounded planning run as the next gate and keeps execution behind a later human-approved proof pack.
- Covers refs: `docs/ROADMAP.md`
- Remaining unresolved refs: None
