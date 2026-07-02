# Execution Prompt: CHW-V0-001 Coding Harness Workflow v0

## Version
v1

## Change Log
- v1 (2026-07-02): Execution prompt generated after human Go.

## Run Metadata
- RUN_ID: RUN_20260702_0617_coding_harness_workflow_v0_plan
- Sprint ID: CHW-V0-001
- Created: 2026-07-02 06:17 local
- Source Pack: `docs/Factory/runs/RUN_20260702_0617_coding_harness_workflow_v0_plan/pack/`

## Purpose
Implement the smallest CLI-first workflow wrapper over Coding Proof Harness v0 so the existing coding proof can be listed, run, and inspected from the terminal. Do not introduce live providers, repository mutation, persistence, product UI, Workspace Shell, mission execution, or neighbouring portfolio responsibilities.

## Required Read Order
1. `docs/PROJECT_STATE.md`
2. `docs/ROADMAP.md`
3. `docs/Factory/ORCHESTRATION.md`
4. `docs/Factory/SCRATCHPAD.md` (read only `## Active Pitfalls (Mandatory)`)
5. `docs/Factory/runs/RUN_20260702_0617_coding_harness_workflow_v0_plan/pack/intent.md`
6. `docs/Factory/runs/RUN_20260702_0617_coding_harness_workflow_v0_plan/pack/intent_lock_report.md`
7. `docs/Factory/runs/RUN_20260702_0617_coding_harness_workflow_v0_plan/pack/risk_register.md`
8. `docs/Factory/runs/RUN_20260702_0617_coding_harness_workflow_v0_plan/pack/verification_plan.md`
9. `docs/Factory/runs/RUN_20260702_0617_coding_harness_workflow_v0_plan/pack/traceability_matrix.md`
10. `docs/Factory/runs/RUN_20260702_0617_coding_harness_workflow_v0_plan/pack/verification_manifest.yaml`
11. `docs/Factory/runs/RUN_20260702_0617_coding_harness_workflow_v0_plan/pack/micro_sprints.md`
12. `docs/Factory/runs/RUN_20260702_0617_coding_harness_workflow_v0_plan/pack/CHW-V0-001_ENVELOPE.md`
13. `docs/Factory/runs/RUN_20260702_0617_coding_harness_workflow_v0_plan/pack/PACK_AUDIT_REPORT.md`

## Skill Routing Contract
- Use the factory-execution-closeout skill for implementation closeout and verification evidence.
- No dedicated skill applies to the local CLI implementation itself; execute via the approved envelope and stage contract.

## Hard Guardrails
- CLI must delegate to existing Coding Proof Harness v0 service functions.
- Do not duplicate harness semantics in the workflow wrapper.
- Preserve Project Memory and generated Markdown distinction.
- Preserve capability and authority separation.
- Do not call live models, live CLIs, live SDKs, databases, external connectors, or mutate repositories.
- Do not treat proposed provider output as accepted truth.
- Keep Workspace Shell and product UI out of scope.

## SIMPLE-CODE-GATE v2
- Implement the smallest clear change.
- Prefer direct, local, readable code.
- Do not add dependencies.
- Do not add generic plugin, strategy, registry, or product-shell abstractions.
- Fail clearly for invalid fixture IDs or invalid review requests.

## Micro-sprint Execution Sequence
0. MS-00 Verification Scaffold: add focused workflow tests for VC-001 through VC-010.
1. MS-01 CLI Command Surface: add fixture list and fixture run commands over existing service functions.
2. MS-02 Text And JSON Summary: render workflow summaries for humans and machines.
3. MS-03 Candidate Review Status: expose candidate-only and explicit reviewed states without implicit promotion.
4. MS-04 Brownfield Blocked Workflow: show blocked readiness without provider invocation.
5. MS-05 Optional Thin TUI Wrapper: skip unless it remains service-delegating and clearly useful.
6. MS-06 Validation Closeout: run verification and record evidence.

## Verification Contract
- `/opt/homebrew/bin/python3.13 -m unittest tests/test_thinking_engine_coding_workflow.py`
- `/opt/homebrew/bin/python3.13 -m unittest tests/test_project_memory_contract.py tests/test_project_memory_fixtures.py tests/test_project_memory_semantics.py tests/test_project_memory_context.py tests/test_project_memory_adapter_twins.py tests/test_project_memory_cli.py tests/test_project_memory_tui.py tests/test_project_memory_review.py tests/test_thinking_engine_intake.py tests/test_thinking_engine_discovery.py tests/test_thinking_engine_coding_harness.py tests/test_thinking_engine_coding_workflow.py`
- `bash scripts/knowledge_lint.sh`
- `./scripts/factoryctl pack-lint --run RUN_20260702_0617_coding_harness_workflow_v0_plan`
- `git diff --check`

## Failure Policy
- Stop if any verification command fails.
- Stop if implementation calls live providers or mutates a repository.
- Stop if provider output bypasses Candidate Review and Promotion.
- Stop if the optional TUI grows into product UX or Workspace Shell.

## Final Exit Checklist
- [x] Scope delivered per envelope and micro-sprints.
- [x] SIMPLE-CODE-GATE v2 satisfied.
- [x] Verification commands pass.
- [x] Evidence artifacts and validation closeout updated.
- [x] Required state docs updated.
- [x] Outstanding risks and deferrals listed.
