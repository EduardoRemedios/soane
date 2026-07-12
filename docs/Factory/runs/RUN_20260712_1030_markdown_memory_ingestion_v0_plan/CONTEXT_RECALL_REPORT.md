# Context Recall Report

## Version
v1

## Change Log
- v1 (2026-07-12): Generated recall report for profile `stage-a`.

## Report Metadata
- Profile: stage-a (Factory Stage A Preflight)
- Requested Scope: RUN_20260712_1030_markdown_memory_ingestion_v0_plan
- Effective Scope: docs
- Attempted Scopes: RUN_20260712_1030_markdown_memory_ingestion_v0_plan, docs/Factory/runs, docs/Factory/ProductOwner/phases, docs
- Fallback Applied: YES
- Coverage Verdict: WEAK
- Generated At (UTC): 2026-07-12T09:31:26Z
- Source Index: /private/tmp/factory_starter_kit_context/context.sqlite3

## Purpose
- Use this before Stage A to surface binding constraints, unresolved blockers, prior human checkpoints, and recent scope decisions tied to the new run.

## Coverage Snapshot
- Indexed sources in effective scope: 427
- Artifact types: {"canonical_doc": 54, "factory_run_pack_artifact": 326, "factory_run_root_artifact": 47}
- Focus terms: Markdown memory ingestion Claim candidate provenance source authority authority mode Knowledge Scope fingerprint freshness review promotion
- Trace IDs: None
- Required refs: docs/PROJECT_MEMORY_ARCHITECTURE.md, docs/GOVERNANCE_MODEL.md, soane/project_memory/contract.py, soane/project_memory/review.py, soane/project_memory/agent_context.py
- Unresolved required refs: soane/project_memory/contract.py, soane/project_memory/review.py, soane/project_memory/agent_context.py

## Recall Queries
### Q1. `BLOCKING`
- Result count: 363
- Evidence:
  - `docs/Factory/runs/RUN_20260701_1604_roadmap_sequence_review/CONTEXT_RECALL_REPORT.md:31` [Context Recall Report > Recall Queries > Q1. `BLOCKING`]
  - `docs/Factory/runs/RUN_20260712_1011_vision_epistemic_hardening/CONTEXT_RECALL_REPORT.md:31` [Context Recall Report > Recall Queries > Q1. `BLOCKING`]
  - `docs/Factory/runs/RUN_20260705_0923_live_coding_adapter_eval_plan/pack/intent.md:52` [Intent: LCAE-V0-001 Live Coding Adapter Evaluation Plan > Open Questions]
  - `docs/Factory/runs/RUN_20260712_0909_agent_context_relevance_v1_plan/CONTEXT_RECALL_REPORT.md:31` [Context Recall Report > Recall Queries > Q1. `BLOCKING`]
  - `docs/INTEGRATION_ARCHITECTURE.md:741` [Integration Architecture > Failure And Blocking States]

### Q2. `Critical`
- Result count: 130
- Evidence:
  - `docs/Factory/runs/RUN_20260712_0909_agent_context_relevance_v1_plan/CONTEXT_RECALL_REPORT.md:43` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/runs/RUN_20260701_1604_roadmap_sequence_review/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/runs/RUN_20260630_1129_project_memory_research/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/runs/RUN_20260712_1011_vision_epistemic_hardening/CONTEXT_RECALL_REPORT.md:40` [Context Recall Report > Recall Queries > Q2. `Critical`]
  - `docs/Factory/Spec/STAGE_CONTRACTS.md:214` [docs/Factory/Spec/STAGE_CONTRACTS.md — Factory Stage Contracts (v4.14) > STAGE_F — Verification Assets]

### Q3. `deferral`
- Result count: 100
- Evidence:
  - `docs/Factory/runs/RUN_20260712_0909_agent_context_relevance_v1_plan/CONTEXT_RECALL_REPORT.md:55` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260705_0923_live_coding_adapter_eval_plan/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/runs/RUN_20260712_1011_vision_epistemic_hardening/CONTEXT_RECALL_REPORT.md:49` [Context Recall Report > Recall Queries > Q3. `deferral`]
  - `docs/Factory/templates/PACK_AUDIT_REPORT_TEMPLATE.md:44` [docs/Factory/templates/PACK_AUDIT_REPORT_TEMPLATE.md > Deferrals Summary]

### Q4. `human GO`
- Result count: 198
- Evidence:
  - `docs/PROJECT_STATE.md:241` [Project State > Current Implementation State]
  - `docs/Factory/Harnesses/CODEX.md:216` [Codex Harness Adapter > Mission Goal Continuity (Experimental)]
  - `docs/PORTFOLIO_CONTEXT.md:207` [Portfolio Context > How Humans Experience The Portfolio]
  - `docs/CORE_CONCEPTS.md:150` [Core Concepts > Canonical Document]
  - `docs/CORE_CONCEPTS.md:685` [Core Concepts > Negotiation]

### Q5. `scope expansion`
- Result count: 134
- Evidence:
  - `docs/Factory/runs/RUN_20260712_0909_agent_context_relevance_v1_plan/CONTEXT_RECALL_REPORT.md:79` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260701_1604_roadmap_sequence_review/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260705_0923_live_coding_adapter_eval_plan/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260712_1011_vision_epistemic_hardening/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]
  - `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/CONTEXT_RECALL_REPORT.md:67` [Context Recall Report > Recall Queries > Q5. `scope expansion`]

### Q6. `Markdown memory ingestion Claim candidate provenance source authority authority mode Knowledge Scope fingerprint freshness review promotion`
- Result count: 0
- Evidence: None

## Trace Queries
## Required Reference Checks
### R1. `docs/PROJECT_MEMORY_ARCHITECTURE.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/PROJECT_MEMORY_ARCHITECTURE.md` (canonical_doc)

### R2. `docs/GOVERNANCE_MODEL.md`
- Status: RESOLVED
- Resolution Type: path
- Evidence:
  - `docs/GOVERNANCE_MODEL.md` (canonical_doc)

### R3. `soane/project_memory/contract.py`
- Status: UNRESOLVED
- Resolution Type: path
- Evidence: None

### R4. `soane/project_memory/review.py`
- Status: UNRESOLVED
- Resolution Type: path
- Evidence: None

### R5. `soane/project_memory/agent_context.py`
- Status: UNRESOLVED
- Resolution Type: path
- Evidence: None

## Operator Notes
- Carry forward any blockers, approvals, descopes, and human checkpoint references recovered above before the next stage proceeds.

## Direct-Source Repair

- Original Generated Verdict: WEAK
- Direct-Source Repair Status: APPLIED
- Unresolved Generated Refs: `soane/project_memory/contract.py`, `soane/project_memory/review.py`, `soane/project_memory/agent_context.py`
- Context Index Refreshed: YES
- Fallback Scopes Attempted: YES
- Remaining Unresolved Generated Refs: None
- Remaining Material Unresolved Refs: None
- Materiality Check: PASS
- Final Repaired Verdict: REPAIRED_DIRECT_SOURCE_CHECK

## Direct Sources Read

- `docs/PROJECT_MEMORY_ARCHITECTURE.md`
- `docs/GOVERNANCE_MODEL.md`
- `docs/CORE_CONCEPTS.md`
- `docs/ROADMAP.md`
- `soane/project_memory/contract.py`
- `soane/project_memory/review.py`
- `soane/project_memory/context.py`
- `soane/project_memory/agent_context.py`
- `soane/project_memory/cli.py`
- `scripts/factory_context_index.py`
- `tests/test_project_memory_contract.py`
- `tests/test_project_memory_review.py`
- `tests/test_project_memory_agent_context.py`

## Source Summaries

### `docs/PROJECT_MEMORY_ARCHITECTURE.md`
- Summary: Accepts Claim, Knowledge Scope, and Markdown modes as doctrine but records them as unimplemented runtime extensions; import must create reviewable candidates without silent promotion.
### `docs/GOVERNANCE_MODEL.md`
- Summary: Distinguishes Markdown document status and authority mode and keeps Project Memory subordinate to external source authority.
### `docs/CORE_CONCEPTS.md`
- Summary: Defines Claim as an assertion with revisable epistemic status rather than automatic fact and defines Project Knowledge Scope and memory rights.
### `docs/ROADMAP.md`
- Summary: Names MMI-V0-001 as the immediate planning slice and forbids automatic Claim promotion or persistence selection.
### `soane/project_memory/contract.py`
- Summary: Provides a storage-neutral generic MemoryObject and lifecycle model but has no Claim type or Claim metadata validation.
### `soane/project_memory/review.py`
- Summary: Provides deterministic review outcomes for any valid candidate while retaining lineage and requiring Authority when marked.
### `soane/project_memory/context.py`
- Summary: Renders Markdown views from memory and is not an ingestion path.
### `soane/project_memory/agent_context.py`
- Summary: Classifies Markdown roles and carries heading and line data, but role is not authority mode and no candidates are created.
### `soane/project_memory/cli.py`
- Summary: Loads and reviews candidate JSON but has no ingest or source-comparison command.
### `scripts/factory_context_index.py`
- Summary: Provides deterministic chunks, line bounds, paths, and document SHA values, but remains an advisory retrieval index rather than Project Memory.
### `tests/test_project_memory_contract.py`
- Summary: Protects the object-type registry, deterministic identifiers, lifecycle, and common contract behavior.
### `tests/test_project_memory_review.py`
- Summary: Proves candidate-only promotion, lineage, explicit outcomes, contradiction retention, and Authority-gated acceptance.
### `tests/test_project_memory_agent_context.py`
- Summary: Protects Markdown role classification, source freshness, bounded recall, and role-without-authority behavior.
