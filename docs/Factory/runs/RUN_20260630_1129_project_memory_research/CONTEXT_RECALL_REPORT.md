# Context Recall Report

## Version
v1

## Change Log
- v1 (2026-06-30): Generated recall report for profile `stage-a`.

## Report Metadata
- Profile: stage-a (Factory Stage A Preflight)
- Requested Scope: RUN_20260630_1129_project_memory_research
- Effective Scope: docs
- Attempted Scopes: RUN_20260630_1129_project_memory_research, docs/Factory/runs, docs/Factory/ProductOwner/phases, docs
- Fallback Applied: YES
- Coverage Verdict: SUFFICIENT
- Generated At (UTC): 2026-06-30T10:30:21Z
- Source Index: /private/tmp/factory_starter_kit_context/context.sqlite3

## Purpose
- Use this before Stage A to surface binding constraints, unresolved blockers, prior human checkpoints, and recent scope decisions tied to the new run.

## Coverage Snapshot
- Indexed sources in effective scope: 46
- Artifact types: {"canonical_doc": 46}
- Focus terms: None
- Trace IDs: None
- Required refs: None
- Unresolved required refs: None

## Recall Queries
### Q1. `BLOCKING`
- Result count: 51
- Evidence:
  - `docs/Factory/Harnesses/AGENT_LOOP_BRIDGE.md:139` [Agent Loop Bridge > Review Result Schema]
  - `docs/Factory/Harnesses/AGENT_LOOP_BRIDGE_MANUAL_RUNBOOK.md:56` [Agent Loop Bridge Manual Runbook > Verdict Rules]
  - `docs/Factory/Spec/DEFINITIONS.md:115` [docs/Factory/Spec/DEFINITIONS.md — Doc Factory (v3.5) > 8. Contract-grade intent]
  - `docs/Factory/Spec/STAGE_CONTRACTS.md:22` [docs/Factory/Spec/STAGE_CONTRACTS.md — Factory Stage Contracts (v4.13) > Global rules (HARD)]
  - `docs/Factory/Spec/STAGE_CONTRACTS.md:131` [docs/Factory/Spec/STAGE_CONTRACTS.md — Factory Stage Contracts (v4.13) > STAGE_A — Intent Contracting]

### Q2. `Critical`
- Result count: 26
- Evidence:
  - `docs/Factory/Spec/STAGE_CONTRACTS.md:209` [docs/Factory/Spec/STAGE_CONTRACTS.md — Factory Stage Contracts (v4.13) > STAGE_F — Verification Assets]
  - `docs/Factory/Spec/DEFINITIONS.md:61` [docs/Factory/Spec/DEFINITIONS.md — Doc Factory (v3.5) > 4. Impact rubric (verification obligations)]
  - `docs/Factory/Spec/PURPLE_GATE_CHECKLIST.md:15` [docs/Factory/Spec/PURPLE_GATE_CHECKLIST.md — v3.3 > Critical (must all be YES for PASS or CONDITIONAL PASS)]
  - `docs/Factory/templates/PACK_AUDIT_REPORT_TEMPLATE.md:40` [docs/Factory/templates/PACK_AUDIT_REPORT_TEMPLATE.md > Critical Failures (only if any Critical item is NO)]
  - `docs/Factory/templates/PACK_CHECKLIST_TEMPLATE.md:26` [docs/Factory/templates/PACK_CHECKLIST_TEMPLATE.md > Critical (must all be YES for PASS/CONDITIONAL PASS)]

### Q3. `deferral`
- Result count: 15
- Evidence:
  - `docs/Factory/templates/PACK_AUDIT_REPORT_TEMPLATE.md:44` [docs/Factory/templates/PACK_AUDIT_REPORT_TEMPLATE.md > Deferrals Summary]
  - `docs/Factory/templates/INTENT_LOCK_REPORT_TEMPLATE.md:42` [docs/Factory/templates/INTENT_LOCK_REPORT_TEMPLATE.md > Deferrals]
  - `docs/Factory/Spec/DEFINITIONS.md:84` [docs/Factory/Spec/DEFINITIONS.md — Doc Factory (v3.5) > 5. Bounded deferral (HARD)]
  - `docs/Factory/Spec/DEFINITIONS.md:93` [docs/Factory/Spec/DEFINITIONS.md — Doc Factory (v3.5) > 6. Conditional Pass]
  - `docs/Factory/Spec/PURPLE_GATE_CHECKLIST.md:26` [docs/Factory/Spec/PURPLE_GATE_CHECKLIST.md — v3.3 > Conditional (required for CONDITIONAL PASS)]

### Q4. `human GO`
- Result count: 44
- Evidence:
  - `docs/Factory/Harnesses/CODEX.md:216` [Codex Harness Adapter > Mission Goal Continuity (Experimental)]
  - `docs/Factory/Harnesses/AGENT_LOOP_BRIDGE.md:55` [Agent Loop Bridge > Handoff Event Schema]
  - `docs/Factory/ProductOwner/PO_PROCESS.md:40` [Product Owner Pre-Factory Process > 0.2 Separation of Concerns (HARD)]
  - `docs/Factory/MISSION_MODE.md:214` [docs/Factory/MISSION_MODE.md — Mission Mode (Factory Extension) > 11. Mission artifacts (minimum) > 11.3 Codex Mission Goal Continuity adapter (experimental)]
  - `docs/Factory/Harnesses/KILO.md:122` [Kilo Code CLI Harness Adapter > Permission Posture]

### Q5. `scope expansion`
- Result count: 32
- Evidence:
  - `docs/Factory/templates/INTENT_LOCK_REPORT_TEMPLATE.md:51` [docs/Factory/templates/INTENT_LOCK_REPORT_TEMPLATE.md > Scope Expansion Check]
  - `docs/Factory/templates/PACK_AUDIT_REPORT_TEMPLATE.md:55` [docs/Factory/templates/PACK_AUDIT_REPORT_TEMPLATE.md > Scope Expansion Summary]
  - `docs/Factory/Harnesses/CODEX.md:216` [Codex Harness Adapter > Mission Goal Continuity (Experimental)]
  - `docs/Factory/SCRATCHPAD.md:11` [Factory Scratchpad — Cross-Run Pitfalls Index > Active Pitfalls (Mandatory)]
  - `docs/Factory/templates/INTENT_LOCK_REPORT_TEMPLATE.md:1` [docs/Factory/templates/INTENT_LOCK_REPORT_TEMPLATE.md]

## Trace Queries
## Required Reference Checks
## Operator Notes
- Carry forward any blockers, approvals, descopes, and human checkpoint references recovered above before the next stage proceeds.
