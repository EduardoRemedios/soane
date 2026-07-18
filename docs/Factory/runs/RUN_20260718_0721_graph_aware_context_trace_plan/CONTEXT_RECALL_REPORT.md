# Context Recall Report

## Version
v1

## Change Log
- v1 (2026-07-18): Generated recall report for profile `stage-a`.

## Report Metadata
- Profile: stage-a (Factory Stage A Preflight)
- Requested Scope: RUN_20260718_0721_graph_aware_context_trace_plan
- Effective Scope: RUN_20260718_0721_graph_aware_context_trace_plan
- Attempted Scopes: RUN_20260718_0721_graph_aware_context_trace_plan, docs/Factory/runs, docs/Factory/ProductOwner/phases, docs
- Fallback Applied: NO
- Coverage Verdict: SUFFICIENT
- Generated At (UTC): 2026-07-18T06:26:53Z
- Source Index: /private/tmp/factory_starter_kit_context/context.sqlite3

## Purpose
- Use this before Stage A to surface binding constraints, unresolved blockers, prior human checkpoints, and recent scope decisions tied to the new run.

## Coverage Snapshot
- Indexed sources in effective scope: 1
- Artifact types: {"factory_run_root_artifact": 1}
- Focus terms: None
- Trace IDs: None
- Required refs: None
- Unresolved required refs: None

## Recall Queries
### Q1. `BLOCKING`
- Result count: 0
- Evidence: None

### Q2. `Critical`
- Result count: 1
- Evidence:
  - `docs/Factory/runs/RUN_20260718_0721_graph_aware_context_trace_plan/raw_brief.md:38` [Raw Brief: GCT-V0-001 Graph-Aware Context And Trace > Non-Goals]

### Q3. `deferral`
- Result count: 0
- Evidence: None

### Q4. `human GO`
- Result count: 1
- Evidence:
  - `docs/Factory/runs/RUN_20260718_0721_graph_aware_context_trace_plan/raw_brief.md:20` [Raw Brief: GCT-V0-001 Graph-Aware Context And Trace > Execution Contract]

### Q5. `scope expansion`
- Result count: 0
- Evidence: None

## Trace Queries
## Required Reference Checks
## Operator Notes
- Carry forward any blockers, approvals, descopes, and human checkpoint references recovered above before the next stage proceeds.
