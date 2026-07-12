# Context Recall Report

## Version
v1

## Change Log
- v1 (2026-07-12): Generated recall report for profile `stage-a`.

## Report Metadata
- Profile: stage-a (Factory Stage A Preflight)
- Requested Scope: RUN_20260712_0909_agent_context_relevance_v1_plan
- Effective Scope: docs
- Attempted Scopes: RUN_20260712_0909_agent_context_relevance_v1_plan, docs/Factory/runs, docs/Factory/ProductOwner/phases, docs
- Fallback Applied: YES
- Coverage Verdict: WEAK
- Generated At (UTC): 2026-07-12T08:11:17Z
- Source Index: /private/tmp/factory_starter_kit_context/context.sqlite3

## Purpose
- Use this before Stage A to surface binding constraints, unresolved blockers, prior human checkpoints, and recent scope decisions tied to the new run.

## Coverage Snapshot
- Indexed sources in effective scope: 365
- Artifact types: {"canonical_doc": 54, "factory_run_pack_artifact": 272, "factory_run_root_artifact": 39}
- Focus terms: agent context, fail closed
- Trace IDs: RUN_20260712_0909_agent_context_relevance_v1_plan
- Required refs: docs/ROADMAP.md, docs/PROJECT_STATE.md, soane/project_memory/agent_context.py, soane/project_memory/context.py, scripts/factory_context_index.py, tests/test_project_memory_agent_context.py
- Unresolved required refs: soane/project_memory/agent_context.py, soane/project_memory/context.py, scripts/factory_context_index.py, tests/test_project_memory_agent_context.py

## Recall Queries
### Q1. `BLOCKING`
- Result count: 309
- Evidence:
  - `docs/Factory/runs/RUN_20260701_1604_roadmap_sequence_review/CONTEXT_RECALL_REPORT.md:31` [Context Recall Report > Recall Queries > Q1. `BLOCKING`]
  - `docs/Factory/runs/RUN_20260705_0923_live_coding_adapter_eval_plan/pack/intent.md:52` [Intent: LCAE-V0-001 Live Coding Adapter Evaluation Plan > Open Questions]
  - `docs/INTEGRATION_ARCHITECTURE.md:741` [Integration Architecture > Failure And Blocking States]
  - `docs/Factory/Harnesses/AGENT_LOOP_BRIDGE.md:139` [Agent Loop Bridge > Review Result Schema]
  - `docs/Factory/Harnesses/AGENT_LOOP_BRIDGE_MANUAL_RUNBOOK.md:56` [Agent Loop Bridge Manual Runbook > Verdict Rules]
  - `docs/Factory/Spec/DEFINITIONS.md:115` [docs/Factory/Spec/DEFINITIONS.md — Doc Factory (v3.5) > 8. Contract-grade intent]
  - `docs/Factory/Spec/STAGE_CONTRACTS.md:23` [docs/Factory/Spec/STAGE_CONTRACTS.md — Factory Stage Contracts (v4.14) > Global rules (HARD)]
  - `docs/Factory/Spec/STAGE_CONTRACTS.md:136` [docs/Factory/Spec/STAGE_CONTRACTS.md — Factory Stage Contracts (v4.14) > STAGE_A — Intent Contracting]

### Q2. `Critical`
- Result count: 103
- Evidence:
  - `docs/Factory/runs/RUN_20260701_1604_roadmap_sequence_review/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/runs/RUN_20260630_1129_project_memory_research/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/Spec/STAGE_CONTRACTS.md:214` [docs/Factory/Spec/STAGE_CONTRACTS.md — Factory Stage Contracts (v4.14) > STAGE_F — Verification Assets]
  - `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/runs/RUN_20260705_0923_live_coding_adapter_eval_plan/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/Spec/DEFINITIONS.md:61` [docs/Factory/Spec/DEFINITIONS.md — Doc Factory (v3.5) > 4. Impact rubric (verification obligations)]
  - `docs/Factory/Spec/PURPLE_GATE_CHECKLIST.md:15` [docs/Factory/Spec/PURPLE_GATE_CHECKLIST.md — v3.3 > Critical (must all be YES for PASS or CONDITIONAL PASS)]
  - `docs/Factory/runs/RUN_20260701_0848_project_memory_v0_plan/pack/PACK_CHECKLIST.md:11` [Pack Checklist > Critical]

### Q3. `deferral`
- Result count: 80
- Evidence:
  - `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260705_0923_live_coding_adapter_eval_plan/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/templates/PACK_AUDIT_REPORT_TEMPLATE.md:44` [docs/Factory/templates/PACK_AUDIT_REPORT_TEMPLATE.md > Deferrals Summary]
  - `docs/Factory/runs/RUN_20260630_1129_project_memory_research/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260701_1604_roadmap_sequence_review/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/templates/INTENT_LOCK_REPORT_TEMPLATE.md:42` [docs/Factory/templates/INTENT_LOCK_REPORT_TEMPLATE.md > Deferrals]
  - `docs/Factory/Spec/DEFINITIONS.md:84` [docs/Factory/Spec/DEFINITIONS.md — Doc Factory (v3.5) > 5. Bounded deferral (HARD)]
  - `docs/Factory/Spec/DEFINITIONS.md:93` [docs/Factory/Spec/DEFINITIONS.md — Doc Factory (v3.5) > 6. Conditional Pass]

### Q4. `human GO`
- Result count: 173
- Evidence:
  - `docs/PROJECT_STATE.md:229` [Project State > Current Implementation State]
  - `docs/Factory/Harnesses/CODEX.md:216` [Codex Harness Adapter > Mission Goal Continuity (Experimental)]
  - `docs/PORTFOLIO_CONTEXT.md:207` [Portfolio Context > How Humans Experience The Portfolio]
  - `docs/CORE_CONCEPTS.md:603` [Core Concepts > Negotiation]
  - `docs/Factory/Harnesses/AGENT_LOOP_BRIDGE.md:55` [Agent Loop Bridge > Handoff Event Schema]
  - `docs/Factory/ProductOwner/PO_PROCESS.md:40` [Product Owner Pre-Factory Process > 0.2 Separation of Concerns (HARD)]
  - `docs/VISION.md:47` [The Workspace Vision > Human and AI Responsibilities]
  - `docs/CORE_CONCEPTS.md:46` [Core Concepts > Workspace]

### Q5. `scope expansion`
- Result count: 102
- Evidence:
  - `docs/Factory/runs/RUN_20260701_1604_roadmap_sequence_review/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260705_0923_live_coding_adapter_eval_plan/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260630_1129_project_memory_research/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/templates/INTENT_LOCK_REPORT_TEMPLATE.md:51` [docs/Factory/templates/INTENT_LOCK_REPORT_TEMPLATE.md > Scope Expansion Check]
  - `docs/Factory/templates/PACK_AUDIT_REPORT_TEMPLATE.md:55` [docs/Factory/templates/PACK_AUDIT_REPORT_TEMPLATE.md > Scope Expansion Summary]
  - `docs/ROADMAP.md:109` [Roadmap > Backlog Notes]
  - `docs/Factory/Harnesses/CODEX.md:216` [Codex Harness Adapter > Mission Goal Continuity (Experimental)]

### Q6. `agent context`
- Result count: 60
- Evidence:
  - `docs/PROJECT_STATE.md:13` [Project State > What Exists]
  - `docs/PROJECT_STATE.md:138` [Project State > Current Verification]
  - `docs/ROADMAP.md:7` [Roadmap > Completed]
  - `docs/CHANGELOG.md:32` [Changelog > 2026-07-01]
  - `docs/Factory/ORCHESTRATION.md:191` [docs/Factory/ORCHESTRATION.md — Factory Pipeline Runner Guide (Starter Kit) > 2. Run Initialization > 2.1 Stage A Direct-Source Repair For WEAK Recall]
  - `docs/Factory/ProductOwner/PO_PROCESS.md:102` [Product Owner Pre-Factory Process > 2. Sprint Brief Cycle (repeats per sprint, within budget) > 2.2 PO writes Sprint Brief]
  - `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/CONTEXT_RECALL_REPORT.md:31` [Context Recall Report > Recall Queries > Q1. `BLOCKING`]
  - `docs/Factory/runs/RUN_20260705_0923_live_coding_adapter_eval_plan/CONTEXT_RECALL_REPORT.md:31` [Context Recall Report > Recall Queries > Q1. `BLOCKING`]

### Q7. `context assembly`
- Result count: 72
- Evidence:
  - `docs/ROADMAP.md:88` [Roadmap > Immediate Next Move]
  - `docs/CHANGELOG.md:3` [Changelog > 2026-07-12]
  - `docs/Factory/runs/RUN_20260701_0848_project_memory_v0_plan/pack/risk_register.md:7` [Risk Register: Project Memory v0 Plan > Change Log]
  - `docs/Factory/runs/RUN_20260701_0848_project_memory_v0_plan/VALIDATION_CLOSEOUT_REPORT.md:35` [Project Memory v0 Validation Closeout Report > Files Changed Since Planning Pack]
  - `docs/Factory/runs/RUN_20260701_0848_project_memory_v0_plan/pack/micro_sprints.md:38` [Micro-sprints: Project Memory v0 > MS-03 Context Assembly And Markdown Mapping]
  - `docs/PROJECT_MEMORY_ARCHITECTURE.md:620` [Project Memory Architecture > Context Assembly]
  - `docs/CHANGELOG.md:32` [Changelog > 2026-07-01]
  - `docs/CHANGELOG.md:59` [Changelog > 2026-06-30]

### Q8. `fail closed`
- Result count: 43
- Evidence:
  - `docs/ROADMAP.md:123` [Roadmap > Current Candidates]
  - `docs/Factory/SIMPLE_CODE_GATE_SEVERITY_POLICY.md:25` [Factory SIMPLE-CODE-GATE Severity Policy > Severity Classes > BLOCKER]
  - `docs/ROADMAP.md:35` [Roadmap > Sequence]
  - `docs/Factory/MISSION_MODE.md:55` [docs/Factory/MISSION_MODE.md — Mission Mode (Factory Extension) > 2. Mission object model > 2.2.1 Mission unit status semantics]
  - `docs/Factory/runs/RUN_20260705_0923_live_coding_adapter_eval_plan/raw_brief.md:36` [Raw Brief: Live Coding Adapter Evaluation Plan > Required Evaluation Dimensions]
  - `docs/Factory/templates/MISSION_MANIFEST_TEMPLATE.md:35` [docs/Factory/templates/MISSION_MANIFEST_TEMPLATE.md > Ordered Mission Units]
  - `docs/Factory/templates/PACK_AUDIT_REPORT_TEMPLATE.md:44` [docs/Factory/templates/PACK_AUDIT_REPORT_TEMPLATE.md > Deferrals Summary]
  - `docs/onboarding/NON_TECHNICAL_STARTER_GUIDE.md:178` [Non-Technical Starter Guide > 7. Setup Prompt To Paste Into An Agent]

## Trace Queries
### T1. `RUN_20260712_0909_agent_context_relevance_v1_plan`
- Match count: 3
- Evidence:
  - `docs/ROADMAP.md:35` [run_id]
  - `docs/ROADMAP.md:123` [run_id]
  - `docs/ROADMAP.md:169` [run_id]

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

### R3. `soane/project_memory/agent_context.py`
- Status: UNRESOLVED
- Resolution Type: path
- Evidence: None

### R4. `soane/project_memory/context.py`
- Status: UNRESOLVED
- Resolution Type: path
- Evidence: None

### R5. `scripts/factory_context_index.py`
- Status: UNRESOLVED
- Resolution Type: path
- Evidence: None

### R6. `tests/test_project_memory_agent_context.py`
- Status: UNRESOLVED
- Resolution Type: path
- Evidence: None

## Operator Notes
- Carry forward any blockers, approvals, descopes, and human checkpoint references recovered above before the next stage proceeds.

## Direct-Source Repair

- Original Generated Verdict: WEAK
- Direct-Source Repair Status: APPLIED
- Final Repaired Verdict: REPAIRED_DIRECT_SOURCE_CHECK
- Unresolved Generated Refs: `soane/project_memory/agent_context.py`, `soane/project_memory/context.py`, `scripts/factory_context_index.py`, `tests/test_project_memory_agent_context.py`
- Context Index Refreshed: YES
- Fallback Scopes Attempted: YES
- Remaining Unresolved Generated Refs: None
- Remaining Material Unresolved Refs: None
- Materiality Check: PASS

## Direct Sources Read

- `soane/project_memory/agent_context.py`
- `soane/project_memory/context.py`
- `scripts/factory_context_index.py`
- `tests/test_project_memory_agent_context.py`

## Source Summaries

### `soane/project_memory/agent_context.py`
- Summary: Refreshes the shared Factory index, sends the full task and optional queries to recall, maps recalled document paths to memory provenance refs, and delegates seeded memory selection to `build_context_package`.

### `soane/project_memory/context.py`
- Summary: Returns all visible objects when `ContextRequest.seed_object_ids` is empty, which is acceptable for explicit broad inspection but unsafe as an implicit agent-context zero-match fallback.

### `scripts/factory_context_index.py`
- Summary: Tokenizes recall queries and requires every parsed term to occur when the full phrase is absent; index rebuild uses a shared SQLite path without an explicit concurrent-refresh contract.

### `tests/test_project_memory_agent_context.py`
- Summary: Proves constrained query and source-scope cases but does not cover natural task text, zero document matches, empty memory seeds, concurrent refresh contention, traversal budgets, or truthful degraded status.
