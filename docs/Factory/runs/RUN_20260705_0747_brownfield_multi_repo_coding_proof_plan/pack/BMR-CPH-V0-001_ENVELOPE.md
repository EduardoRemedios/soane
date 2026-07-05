# Sprint Envelope: BMR-CPH-V0-001 Brownfield Multi-Repo Coding Proof

## Version

v1

## Change Log

- v1 (2026-07-05): Initial Stage H sprint envelope.

## Sprint ID

`BMR-CPH-V0-001`

## Execution Mode

`PLANNING_ONLY`

Implementation is not authorized by this pack. A future explicit human Go is required.

## Objective

Implement the smallest deterministic extension to Coding Proof Harness v0 that proves Brownfield multi-repository system-boundary handling.

## In Scope

- Multi-repo Brownfield ready fixture.
- Multi-repo Brownfield blocked fixture.
- Fixture fields for repository map, relevant repositories, out-of-scope repositories, service boundaries, integration contracts, ownership, build/test responsibility, documentation gaps, and authority path.
- Local service behavior for multi-repo readiness and context summary.
- Coding Harness and Workflow summaries that expose multi-repo system boundary state.
- Candidate-only and reviewed-state behavior for ready multi-repo provider output.
- Regression coverage for existing Greenfield and single-repo Brownfield fixtures.
- Validation closeout report.

## Out of Scope

- product web UI
- Workspace Shell implementation
- database or persistence selection
- live LLM calls
- live Cursor, Codex, OpenAI, analytics, CRM, ads, design, repository, or external connector integration
- external repository cloning, scanning, command execution, or mutation
- mission execution
- Factory V3, Temper, Aegis, Sentinel, or Harmony responsibilities

## File-Touch Budget

| Area | Budget |
| --- | --- |
| Fixture schema and service helpers | up to 5 files |
| Fixtures and tests | up to 8 files |
| Workflow summary updates | up to 2 files |
| Validation closeout and state docs | up to 3 files |
| Total | up to 18 files |

## Required Micro-Sprints

- MS-00 Verification Scaffold
- MS-01 Multi-Repo Fixture Contract
- MS-02 Intake And Context Semantics
- MS-03 Harness Multi-Repo Execution Path
- MS-04 Workflow Summary
- MS-05 Validation Closeout

## Implementation Constraints

- Apply SIMPLE-CODE-GATE v2.
- Preserve existing fixture behavior.
- Keep workflow service-delegating.
- Preserve Project Memory and generated Markdown distinction.
- Preserve capability and authority separation.
- Do not call live models, live CLIs, live SDKs, external connectors, databases, real repositories, or mutate repositories.
- Do not treat proposed provider output as accepted truth.
- Keep Workspace Shell and product UI out of scope.

## Required Verification

Run at minimum:

```bash
python3 -m unittest tests/test_thinking_engine_coding_harness.py tests/test_thinking_engine_coding_workflow.py
python3 -m unittest tests/test_project_memory_contract.py tests/test_project_memory_fixtures.py tests/test_project_memory_semantics.py tests/test_project_memory_context.py tests/test_project_memory_adapter_twins.py tests/test_project_memory_cli.py tests/test_project_memory_tui.py tests/test_project_memory_review.py tests/test_thinking_engine_intake.py tests/test_thinking_engine_discovery.py tests/test_thinking_engine_coding_harness.py tests/test_thinking_engine_coding_workflow.py tests/test_context_recall_repair.py
bash scripts/knowledge_lint.sh
./scripts/factoryctl pack-lint --run RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan
git diff --check
```

Add and run focused Brownfield multi-repo tests created during implementation.

## Stop Gates

- Stop if multi-repo support is only multiple URLs without system-boundary semantics.
- Stop if provider invocation occurs while boundary, owner, contract, build/test, or authority context is missing.
- Stop if implementation calls a live model, CLI, SDK, connector, database, real repository, or mutates a repository.
- Stop if proposed provider output bypasses Candidate Review and Promotion.
- Stop if workflow becomes product shell or owns readiness decisions.

## Review Handoff

Future implementation should produce a validation closeout report mapping VC-001 through VC-010 to test and artifact evidence.
