# Context Recall Report

## Version
v1

## Change Log
- v1 (2026-07-20): Generated recall report for profile `stage-a`.

## Report Metadata
- Profile: stage-a (Factory Stage A Preflight)
- Requested Scope: RUN_20260720_0708_live_coding_adapter_eval_refresh
- Effective Scope: docs
- Attempted Scopes: RUN_20260720_0708_live_coding_adapter_eval_refresh, docs/Factory/runs, docs/Factory/ProductOwner/phases, docs
- Fallback Applied: YES
- Coverage Verdict: WEAK
- Generated At (UTC): 2026-07-20T06:09:56Z
- Source Index: /private/tmp/factory_starter_kit_context/context.sqlite3

## Purpose
- Use this before Stage A to surface binding constraints, unresolved blockers, prior human checkpoints, and recent scope decisions tied to the new run.

## Coverage Snapshot
- Indexed sources in effective scope: 517
- Artifact types: {"canonical_doc": 54, "factory_run_pack_artifact": 407, "factory_run_root_artifact": 56}
- Focus terms: LCAE-V0-001 live coding adapter evaluation refresh context graph markdown candidate Provider Invocation Codex CLI Cursor CLI Cursor SDK OpenAI SDK Agents SDK
- Trace IDs: None
- Required refs: docs/Factory/runs/RUN_20260705_0923_live_coding_adapter_eval_plan/pack/PACK_AUDIT_REPORT.md, docs/Factory/runs/RUN_20260718_0721_graph_aware_context_trace_plan/VALIDATION_CLOSEOUT_REPORT.md, docs/Factory/runs/RUN_20260712_0909_agent_context_relevance_v1_plan/VALIDATION_CLOSEOUT_REPORT.md, docs/Factory/runs/RUN_20260712_1030_markdown_memory_ingestion_v0_plan/VALIDATION_CLOSEOUT_REPORT.md, docs/INTEGRATION_ARCHITECTURE.md, docs/PROJECT_MEMORY_ARCHITECTURE.md, docs/THINKING_ENGINE_ARCHITECTURE.md, soane/project_memory/adapters.py, soane/project_memory/agent_context.py, soane/project_memory/graph.py, soane/thinking_engine/coding_harness.py, soane/thinking_engine/coding_workflow.py
- Unresolved required refs: soane/project_memory/adapters.py, soane/project_memory/agent_context.py, soane/project_memory/graph.py, soane/thinking_engine/coding_harness.py, soane/thinking_engine/coding_workflow.py

## Recall Queries
### Q1. `BLOCKING`
- Result count: 420
- Evidence:
  - `docs/Factory/runs/RUN_20260701_1604_roadmap_sequence_review/CONTEXT_RECALL_REPORT.md:31` [Context Recall Report > Recall Queries > Q1. `BLOCKING`]
  - `docs/Factory/runs/RUN_20260712_1030_markdown_memory_ingestion_v0_plan/CONTEXT_RECALL_REPORT.md:31` [Context Recall Report > Recall Queries > Q1. `BLOCKING`]
  - `docs/Factory/runs/RUN_20260712_1011_vision_epistemic_hardening/CONTEXT_RECALL_REPORT.md:31` [Context Recall Report > Recall Queries > Q1. `BLOCKING`]
  - `docs/Factory/runs/RUN_20260705_0923_live_coding_adapter_eval_plan/pack/intent.md:52` [Intent: LCAE-V0-001 Live Coding Adapter Evaluation Plan > Open Questions]
  - `docs/Factory/runs/RUN_20260712_0909_agent_context_relevance_v1_plan/CONTEXT_RECALL_REPORT.md:31` [Context Recall Report > Recall Queries > Q1. `BLOCKING`]

### Q2. `Critical`
- Result count: 170
- Evidence:
  - `docs/Factory/runs/RUN_20260712_0909_agent_context_relevance_v1_plan/CONTEXT_RECALL_REPORT.md:43` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/runs/RUN_20260701_1604_roadmap_sequence_review/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/runs/RUN_20260630_1129_project_memory_research/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/runs/RUN_20260712_1011_vision_epistemic_hardening/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/runs/RUN_20260712_1030_markdown_memory_ingestion_v0_plan/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]

### Q3. `deferral`
- Result count: 122
- Evidence:
  - `docs/Factory/runs/RUN_20260712_0909_agent_context_relevance_v1_plan/CONTEXT_RECALL_REPORT.md:55` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260705_0923_live_coding_adapter_eval_plan/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260712_1011_vision_epistemic_hardening/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260712_1030_markdown_memory_ingestion_v0_plan/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]

### Q4. `human GO`
- Result count: 239
- Evidence:
  - `docs/PROJECT_STATE.md:257` [Project State > Current Implementation State]
  - `docs/Factory/Harnesses/CODEX.md:216` [Codex Harness Adapter > Mission Goal Continuity (Experimental)]
  - `docs/PORTFOLIO_CONTEXT.md:207` [Portfolio Context > How Humans Experience The Portfolio]
  - `docs/CORE_CONCEPTS.md:150` [Core Concepts > Canonical Document]
  - `docs/CORE_CONCEPTS.md:685` [Core Concepts > Negotiation]

### Q5. `scope expansion`
- Result count: 162
- Evidence:
  - `docs/Factory/runs/RUN_20260712_0909_agent_context_relevance_v1_plan/CONTEXT_RECALL_REPORT.md:79` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260701_1604_roadmap_sequence_review/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260705_0923_live_coding_adapter_eval_plan/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260712_1011_vision_epistemic_hardening/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260712_1030_markdown_memory_ingestion_v0_plan/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]

### Q6. `LCAE-V0-001 live coding adapter evaluation refresh context graph markdown candidate Provider Invocation Codex CLI Cursor CLI Cursor SDK OpenAI SDK Agents SDK`
- Result count: 1
- Evidence:
  - `docs/ROADMAP.md:138` [Roadmap > Current Candidates]

## Trace Queries
## Required Reference Checks
### R1. `docs/Factory/runs/RUN_20260705_0923_live_coding_adapter_eval_plan/pack/PACK_AUDIT_REPORT.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/Factory/runs/RUN_20260705_0923_live_coding_adapter_eval_plan/pack/PACK_AUDIT_REPORT.md` (factory_run_pack_artifact)

### R2. `docs/Factory/runs/RUN_20260718_0721_graph_aware_context_trace_plan/VALIDATION_CLOSEOUT_REPORT.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/Factory/runs/RUN_20260718_0721_graph_aware_context_trace_plan/VALIDATION_CLOSEOUT_REPORT.md` (factory_run_root_artifact)

### R3. `docs/Factory/runs/RUN_20260712_0909_agent_context_relevance_v1_plan/VALIDATION_CLOSEOUT_REPORT.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/Factory/runs/RUN_20260712_0909_agent_context_relevance_v1_plan/VALIDATION_CLOSEOUT_REPORT.md` (factory_run_root_artifact)

### R4. `docs/Factory/runs/RUN_20260712_1030_markdown_memory_ingestion_v0_plan/VALIDATION_CLOSEOUT_REPORT.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/Factory/runs/RUN_20260712_1030_markdown_memory_ingestion_v0_plan/VALIDATION_CLOSEOUT_REPORT.md` (factory_run_root_artifact)

### R5. `docs/INTEGRATION_ARCHITECTURE.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/INTEGRATION_ARCHITECTURE.md` (canonical_doc)

### R6. `docs/PROJECT_MEMORY_ARCHITECTURE.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/PROJECT_MEMORY_ARCHITECTURE.md` (canonical_doc)

### R7. `docs/THINKING_ENGINE_ARCHITECTURE.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/THINKING_ENGINE_ARCHITECTURE.md` (canonical_doc)

### R8. `soane/project_memory/adapters.py`
- Status: UNRESOLVED
- Resolution Type: path
- Evidence: None

### R9. `soane/project_memory/agent_context.py`
- Status: UNRESOLVED
- Resolution Type: path
- Evidence: None

### R10. `soane/project_memory/graph.py`
- Status: UNRESOLVED
- Resolution Type: path
- Evidence: None

### R11. `soane/thinking_engine/coding_harness.py`
- Status: UNRESOLVED
- Resolution Type: path
- Evidence: None

### R12. `soane/thinking_engine/coding_workflow.py`
- Status: UNRESOLVED
- Resolution Type: path
- Evidence: None

## Operator Notes
- Carry forward any blockers, approvals, descopes, and human checkpoint references recovered above before the next stage proceeds.

## Direct-Source Repair

- Original Generated Verdict: WEAK
- Direct-Source Repair Status: APPLIED
- Context Index Refreshed: YES
- Fallback Scopes Attempted: YES
- Unresolved Generated Refs: `soane/project_memory/adapters.py`, `soane/project_memory/agent_context.py`, `soane/project_memory/graph.py`, `soane/thinking_engine/coding_harness.py`, `soane/thinking_engine/coding_workflow.py`
- Remaining Unresolved Generated Refs: None
- Remaining Material Unresolved Refs: None
- Materiality Check: PASS
- Final Repaired Verdict: REPAIRED_DIRECT_SOURCE_CHECK

## Direct Sources Read

- `soane/project_memory/adapters.py`
- `soane/project_memory/agent_context.py`
- `soane/project_memory/graph.py`
- `soane/thinking_engine/coding_harness.py`
- `soane/thinking_engine/coding_workflow.py`

## Source Summaries

### `soane/project_memory/adapters.py`

- Summary: Defines the five in-scope deterministic adapter twins and Provider Invocation metadata. Results always default to `live_call_performed=False`; capability and optional authority are separate relationships. This is the existing adapter contract the evaluator must inspect rather than replace.
- Covers refs: `soane/project_memory/adapters.py`
- Remaining unresolved refs: None

### `soane/project_memory/agent_context.py`

- Summary: Builds bounded agent-facing bundles through the Factory context index, Project Memory provenance refs, explicit selection and refresh states, separate document and memory budgets, and shared typed graph traversal. It fails closed to `no_relevant_context` instead of broadening an unmatched task.
- Covers refs: `soane/project_memory/agent_context.py`
- Remaining unresolved refs: None

### `soane/project_memory/graph.py`

- Summary: Owns storage-neutral typed inbound/outbound traversal with hard depth, object, path, edge, exclusion, and truncation ceilings. It enforces per-hop visibility and lifecycle policy and explains missing, external, inaccessible, disallowed, and cyclic relationships without inference.
- Covers refs: `soane/project_memory/graph.py`
- Remaining unresolved refs: None

### `soane/thinking_engine/coding_harness.py`

- Summary: Composes intake, discovery, local context, adapter twins, Provider Invocation objects, and proposed output candidates for deterministic coding proofs. Provider readiness is explicit, live calls remain false, and output review delegates to Candidate Review and Promotion.
- Covers refs: `soane/thinking_engine/coding_harness.py`
- Remaining unresolved refs: None

### `soane/thinking_engine/coding_workflow.py`

- Summary: Provides the thin CLI workflow over the coding harness. Its output keeps provider readiness, mocked invocation, candidate state, review state, current-truth status, and live-call status inspectable; it does not call live providers, mutate repositories, persist state, or create product UI.
- Covers refs: `soane/thinking_engine/coding_workflow.py`
- Remaining unresolved refs: None
