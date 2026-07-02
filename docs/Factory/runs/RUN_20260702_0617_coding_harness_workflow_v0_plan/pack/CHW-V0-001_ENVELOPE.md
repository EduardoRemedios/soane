# Sprint Envelope: CHW-V0-001 Coding Harness Workflow v0

## Version

v1

## Change Log

- v1 (2026-07-02): Initial Stage H sprint envelope.

## Sprint ID

`CHW-V0-001`

## Execution Mode

`PLANNING_ONLY`

Implementation is not authorized by this pack. A future explicit human Go is required.

## Objective

Implement the smallest CLI-first workflow wrapper over Coding Proof Harness v0 so the existing coding proof can be navigated and inspected from the terminal.

## In Scope

- Thin CLI command surface for fixture listing and fixture execution.
- Text summary of readiness, discovery, context, provider invocation, output candidate, review status, live-call status, and repository-mutation status.
- Optional JSON summary for machine-readable inspection.
- Deterministic tests over existing coding harness fixtures.
- Candidate-only and reviewed-state summary behavior.
- Brownfield blocked workflow summary.
- Optional thin TUI wrapper only if it delegates to shared summary/service functions.
- Validation closeout report.

## Out of Scope

- product web UI
- Workspace Shell implementation
- database or persistence selection
- live LLM calls
- live Cursor, Codex, OpenAI, analytics, CRM, ads, design, repository, or external connector integration
- external repository mutation
- mission execution
- Factory V3, Temper, Aegis, Sentinel, or Harmony responsibilities

## File-Touch Budget

| Area | Budget |
| --- | --- |
| CLI workflow and summary helpers | up to 4 files |
| Fixtures and tests | up to 8 files |
| Optional TUI wrapper | up to 3 files |
| Validation closeout and state docs | up to 3 files |
| Total | up to 18 files |

## Required Micro-Sprints

- MS-00 Verification Scaffold
- MS-01 CLI Command Surface
- MS-02 Text And JSON Summary
- MS-03 Candidate Review Status
- MS-04 Brownfield Blocked Workflow
- MS-06 Validation Closeout

## Optional Micro-Sprints

- MS-05 Optional Thin TUI Wrapper

MS-05 should be skipped if it causes product-workflow drift or duplicates service logic.

## Implementation Constraints

- Apply SIMPLE-CODE-GATE v2.
- CLI must delegate to existing coding harness service functions.
- Preserve Project Memory and generated Markdown distinction.
- Preserve Thinking, Evidence, Decisions, Authority, Capabilities, Missions, and Proof as distinct concepts.
- Preserve capability and authority separation.
- Do not call live models, live CLIs, live SDKs, external connectors, databases, or mutate repositories.
- Do not treat proposed provider output as accepted truth.
- Keep Workspace Shell and product UI out of scope.

## Required Verification

Run at minimum:

```bash
python3 -m unittest tests/test_project_memory_contract.py tests/test_project_memory_fixtures.py tests/test_project_memory_semantics.py tests/test_project_memory_context.py tests/test_project_memory_adapter_twins.py tests/test_project_memory_cli.py tests/test_project_memory_tui.py tests/test_project_memory_review.py tests/test_thinking_engine_intake.py tests/test_thinking_engine_discovery.py tests/test_thinking_engine_coding_harness.py
bash scripts/knowledge_lint.sh
./scripts/factoryctl pack-lint --run RUN_20260702_0617_coding_harness_workflow_v0_plan
git diff --check
```

Add and run focused Coding Harness Workflow tests created during implementation.

## Stop Gates

- Stop if CLI duplicates harness semantics.
- Stop if implementation calls a live model, CLI, SDK, connector, database, or mutates a repository.
- Stop if proposed provider output bypasses Candidate Review and Promotion.
- Stop if optional TUI becomes Workspace Shell or product UX.

## Review Handoff

Future implementation should produce a validation closeout report mapping VC-001 through VC-010 to test and artifact evidence.
