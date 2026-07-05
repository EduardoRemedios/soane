# Context Recall Report

## Version
v1

## Change Log
- v1 (2026-07-05): Generated recall report for profile `stage-a`.

## Report Metadata
- Profile: stage-a (Factory Stage A Preflight)
- Requested Scope: RUN_20260705_0923_live_coding_adapter_eval_plan
- Effective Scope: docs
- Attempted Scopes: RUN_20260705_0923_live_coding_adapter_eval_plan, docs/Factory/runs, docs/Factory/ProductOwner/phases, docs
- Fallback Applied: YES
- Coverage Verdict: WEAK
- Generated At (UTC): 2026-07-05T08:25:56Z
- Source Index: /private/tmp/factory_starter_kit_context/context.sqlite3

## Purpose
- Use this before Stage A to surface binding constraints, unresolved blockers, prior human checkpoints, and recent scope decisions tied to the new run.

## Coverage Snapshot
- Indexed sources in effective scope: 327
- Artifact types: {"canonical_doc": 46, "factory_run_pack_artifact": 244, "factory_run_root_artifact": 37}
- Focus terms: live coding adapter evaluation plan Codex CLI Cursor CLI Cursor SDK OpenAI SDK Agents SDK Provider Invocation Capability authority evidence
- Trace IDs: None
- Required refs: docs/ROADMAP.md, docs/PROJECT_STATE.md, docs/INTEGRATION_ARCHITECTURE.md, docs/PROJECT_MEMORY_ARCHITECTURE.md, docs/THINKING_ENGINE_ARCHITECTURE.md, soane/project_memory/adapters.py, soane/thinking_engine/coding_harness.py, soane/thinking_engine/coding_workflow.py, docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/VALIDATION_CLOSEOUT_REPORT.md
- Unresolved required refs: docs/INTEGRATION_ARCHITECTURE.md, docs/PROJECT_MEMORY_ARCHITECTURE.md, docs/THINKING_ENGINE_ARCHITECTURE.md, soane/project_memory/adapters.py, soane/thinking_engine/coding_harness.py, soane/thinking_engine/coding_workflow.py

## Recall Queries
### Q1. `BLOCKING`
- Result count: 300
- Evidence:
  - `docs/Factory/runs/RUN_20260701_1604_roadmap_sequence_review/CONTEXT_RECALL_REPORT.md:31` [Context Recall Report > Recall Queries > Q1. `BLOCKING`]
  - `docs/Factory/Harnesses/AGENT_LOOP_BRIDGE.md:139` [Agent Loop Bridge > Review Result Schema]
  - `docs/Factory/Harnesses/AGENT_LOOP_BRIDGE_MANUAL_RUNBOOK.md:56` [Agent Loop Bridge Manual Runbook > Verdict Rules]
  - `docs/Factory/Spec/DEFINITIONS.md:115` [docs/Factory/Spec/DEFINITIONS.md — Doc Factory (v3.5) > 8. Contract-grade intent]
  - `docs/Factory/Spec/STAGE_CONTRACTS.md:23` [docs/Factory/Spec/STAGE_CONTRACTS.md — Factory Stage Contracts (v4.14) > Global rules (HARD)]

### Q2. `Critical`
- Result count: 91
- Evidence:
  - `docs/Factory/runs/RUN_20260701_1604_roadmap_sequence_review/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/runs/RUN_20260630_1129_project_memory_research/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/Spec/STAGE_CONTRACTS.md:214` [docs/Factory/Spec/STAGE_CONTRACTS.md — Factory Stage Contracts (v4.14) > STAGE_F — Verification Assets]
  - `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/Spec/DEFINITIONS.md:61` [docs/Factory/Spec/DEFINITIONS.md — Doc Factory (v3.5) > 4. Impact rubric (verification obligations)]

### Q3. `deferral`
- Result count: 73
- Evidence:
  - `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/templates/PACK_AUDIT_REPORT_TEMPLATE.md:44` [docs/Factory/templates/PACK_AUDIT_REPORT_TEMPLATE.md > Deferrals Summary]
  - `docs/Factory/runs/RUN_20260630_1129_project_memory_research/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260701_1604_roadmap_sequence_review/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/templates/INTENT_LOCK_REPORT_TEMPLATE.md:42` [docs/Factory/templates/INTENT_LOCK_REPORT_TEMPLATE.md > Deferrals]

### Q4. `human GO`
- Result count: 122
- Evidence:
  - `docs/Factory/Harnesses/CODEX.md:216` [Codex Harness Adapter > Mission Goal Continuity (Experimental)]
  - `docs/PROJECT_STATE.md:207` [Project State > Current Implementation State]
  - `docs/Factory/Harnesses/AGENT_LOOP_BRIDGE.md:55` [Agent Loop Bridge > Handoff Event Schema]
  - `docs/Factory/ProductOwner/PO_PROCESS.md:40` [Product Owner Pre-Factory Process > 0.2 Separation of Concerns (HARD)]
  - `docs/Factory/runs/RUN_20260701_1438_thinking_engine_intake_v0_plan/raw_brief.md:138` [Raw Brief: Thinking Engine Intake v0 Planning > Go Or No-Go Rule]

### Q5. `scope expansion`
- Result count: 91
- Evidence:
  - `docs/Factory/runs/RUN_20260701_1604_roadmap_sequence_review/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260630_1129_project_memory_research/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/templates/INTENT_LOCK_REPORT_TEMPLATE.md:51` [docs/Factory/templates/INTENT_LOCK_REPORT_TEMPLATE.md > Scope Expansion Check]
  - `docs/Factory/templates/PACK_AUDIT_REPORT_TEMPLATE.md:55` [docs/Factory/templates/PACK_AUDIT_REPORT_TEMPLATE.md > Scope Expansion Summary]

### Q6. `live coding adapter evaluation plan Codex CLI Cursor CLI Cursor SDK OpenAI SDK Agents SDK Provider Invocation Capability authority evidence`
- Result count: 1
- Evidence:
  - `docs/ROADMAP.md:107` [Roadmap > Current Candidates]

## Trace Queries
## Required Reference Checks
### R1. `docs/ROADMAP.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/ROADMAP.md` (canonical_doc)

### R2. `docs/PROJECT_STATE.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/PROJECT_STATE.md` (canonical_doc)

### R3. `docs/INTEGRATION_ARCHITECTURE.md`
- Status: UNRESOLVED
- Resolution Type: path
- Evidence: None

### R4. `docs/PROJECT_MEMORY_ARCHITECTURE.md`
- Status: UNRESOLVED
- Resolution Type: path
- Evidence: None

### R5. `docs/THINKING_ENGINE_ARCHITECTURE.md`
- Status: UNRESOLVED
- Resolution Type: path
- Evidence: None

### R6. `soane/project_memory/adapters.py`
- Status: UNRESOLVED
- Resolution Type: path
- Evidence: None

### R7. `soane/thinking_engine/coding_harness.py`
- Status: UNRESOLVED
- Resolution Type: path
- Evidence: None

### R8. `soane/thinking_engine/coding_workflow.py`
- Status: UNRESOLVED
- Resolution Type: path
- Evidence: None

### R9. `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/VALIDATION_CLOSEOUT_REPORT.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/VALIDATION_CLOSEOUT_REPORT.md` (factory_run_root_artifact)

## Operator Notes
- Carry forward any blockers, approvals, descopes, and human checkpoint references recovered above before the next stage proceeds.

## Direct-Source Repair

- Original Generated Verdict: WEAK
- Direct-Source Repair Status: APPLIED
- Context Index Refreshed: YES
- Fallback Scopes Attempted: YES
- Unresolved Generated Refs: `docs/INTEGRATION_ARCHITECTURE.md`, `docs/PROJECT_MEMORY_ARCHITECTURE.md`, `docs/THINKING_ENGINE_ARCHITECTURE.md`, `soane/project_memory/adapters.py`, `soane/thinking_engine/coding_harness.py`, `soane/thinking_engine/coding_workflow.py`
- Remaining Unresolved Generated Refs: None
- Remaining Material Unresolved Refs: None
- Materiality Check: PASS
- Final Repaired Verdict: REPAIRED_DIRECT_SOURCE_CHECK

## Direct Sources Read

- `docs/INTEGRATION_ARCHITECTURE.md`
- `docs/PROJECT_MEMORY_ARCHITECTURE.md`
- `docs/THINKING_ENGINE_ARCHITECTURE.md`
- `soane/project_memory/adapters.py`
- `soane/thinking_engine/coding_harness.py`
- `soane/thinking_engine/coding_workflow.py`
- `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/VALIDATION_CLOSEOUT_REPORT.md`

## Source Summaries

### `docs/INTEGRATION_ARCHITECTURE.md`
- Summary: Defines Provider Invocation as a cross-portfolio contract carrying purpose, Inference Strategy, policy context, privacy classification, input/output refs, cost, latency, confidence, and evidence or trace refs. It explicitly lists Codex CLI, Cursor CLI, Cursor SDK, OpenAI SDK, and OpenAI Agents SDK as candidate coding adapter surfaces, behind Provider Invocation, Capability Reference, Inference Strategy, and governed work contracts.
- Covers refs: `docs/INTEGRATION_ARCHITECTURE.md`
- Remaining unresolved refs: None

### `docs/PROJECT_MEMORY_ARCHITECTURE.md`
- Summary: Defines Project Memory as structured, inspectable, amendable, model-independent substrate. It requires facts, assumptions, hypotheses, decisions, constraints, evidence, authority, provenance, lifecycle, context assembly, and generated Markdown views to remain distinct.
- Covers refs: `docs/PROJECT_MEMORY_ARCHITECTURE.md`
- Remaining unresolved refs: None

### `docs/THINKING_ENGINE_ARCHITECTURE.md`
- Summary: Defines the Thinking Engine as a reasoning aid that reduces uncertainty before planning or delegation. It states that the Thinking Engine does not own live Cursor, Codex, OpenAI, or other provider integrations and must not decide work may proceed without human or policy authority.
- Covers refs: `docs/THINKING_ENGINE_ARCHITECTURE.md`
- Remaining unresolved refs: None

### `soane/project_memory/adapters.py`
- Summary: Implements deterministic adapter twins for `cursor_cli`, `codex_cli`, `cursor_sdk`, `openai_sdk`, and `openai_agents_sdk`. The current adapter contract records capability, optional authority, input/output refs, policy, privacy, evidence, confidence, cost, latency, status, and `live_call_performed=False`.
- Covers refs: `soane/project_memory/adapters.py`
- Remaining unresolved refs: None

### `soane/thinking_engine/coding_harness.py`
- Summary: Composes intake, discovery, context assembly, adapter twins, provider invocation records, output candidates, and review-gated promotion. It now includes deterministic multi-repo system-boundary readiness while keeping live calls and repository mutation disabled.
- Covers refs: `soane/thinking_engine/coding_harness.py`
- Remaining unresolved refs: None

### `soane/thinking_engine/coding_workflow.py`
- Summary: Provides the CLI-first workflow wrapper over the shared harness. It lists and runs fixtures, emits text/JSON summaries, exposes provider/candidate/review state, and remains service-delegating.
- Covers refs: `soane/thinking_engine/coding_workflow.py`
- Remaining unresolved refs: None

### `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/VALIDATION_CLOSEOUT_REPORT.md`
- Summary: Records that Brownfield multi-repo proof implementation is complete, mock-first, fixture-backed, no live providers, no repository mutation, and that live Codex/Cursor/OpenAI adapter evaluation remains the next roadmap slice.
- Covers refs: `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/VALIDATION_CLOSEOUT_REPORT.md`
- Remaining unresolved refs: None
