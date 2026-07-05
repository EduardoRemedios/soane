# Sprint Envelope: LCAE-V0-001 Live Coding Adapter Evaluation

## Version

v1

## Change Log

- v1 (2026-07-05): Initial Stage H sprint envelope.

## Sprint ID

`LCAE-V0-001`

## Execution Mode

`PLANNING_ONLY`

Implementation is not authorized by this pack. A future explicit human Go is required.

## Objective

Implement the smallest deterministic source-backed evaluation contract for live coding adapter surfaces, without invoking live providers.

## In Scope

- Source-backed adapter profiles for Codex CLI, Cursor CLI, Cursor SDK, OpenAI SDK, and OpenAI Agents SDK.
- Deterministic safety gates for auth, authority, mutation controls, repository scope, traceability, structured output, cost/latency metadata path, and candidate review.
- Recommendation matrix for first live proof surface.
- Blocked cases for unsafe or under-specified surfaces.
- Thin CLI wrapper over shared evaluator functions.
- Validation closeout and state docs.

## Out of Scope

- live Codex, Cursor, OpenAI, SDK, CLI, API, or cloud-agent invocation
- credential reads or auth flows
- dependency installation
- external repository access
- repository mutation
- product UI or Workspace Shell
- persistence
- mission execution
- portfolio product responsibility expansion

## File-Touch Budget

| Area | Budget |
| --- | --- |
| Evaluation profiles and fixtures | up to 8 files |
| Evaluator service and CLI wrapper | up to 4 files |
| Tests | up to 4 files |
| Validation closeout and state docs | up to 4 files |
| Total | up to 20 files |

## Required Micro-Sprints

- MS-00 Verification Scaffold
- MS-01 Source-Backed Adapter Profiles
- MS-02 Safety And Authority Gates
- MS-03 Recommendation Matrix
- MS-04 CLI Wrapper
- MS-05 Validation Closeout

## Required Verification

Run at minimum:

```bash
python3 -m unittest tests/test_project_memory_adapter_twins.py tests/test_thinking_engine_coding_harness.py tests/test_thinking_engine_coding_workflow.py
python3 -m unittest tests/test_project_memory_contract.py tests/test_project_memory_fixtures.py tests/test_project_memory_semantics.py tests/test_project_memory_context.py tests/test_project_memory_adapter_twins.py tests/test_project_memory_cli.py tests/test_project_memory_tui.py tests/test_project_memory_review.py tests/test_thinking_engine_intake.py tests/test_thinking_engine_discovery.py tests/test_thinking_engine_coding_harness.py tests/test_thinking_engine_coding_workflow.py tests/test_context_recall_repair.py
bash scripts/knowledge_lint.sh
./scripts/factoryctl pack-lint --run RUN_20260705_0923_live_coding_adapter_eval_plan
git diff --check
```

Add and run focused live-adapter-evaluation tests created during implementation.

## Stop Gates

- Stop if any implementation calls a live provider, CLI, SDK, API, model, cloud agent, network, or external repository.
- Stop if any implementation reads credentials or requires installed provider tooling.
- Stop if capability, auth, authority, and project permission are collapsed.
- Stop if unsafe mutation controls do not block a surface.
- Stop if provider output can bypass Candidate Review and Promotion.
- Stop if product UI, Workspace Shell, persistence, or mission execution appears.

## Review Handoff

Future implementation should produce a validation closeout report mapping VC-001 through VC-010 to tests and artifact evidence.
