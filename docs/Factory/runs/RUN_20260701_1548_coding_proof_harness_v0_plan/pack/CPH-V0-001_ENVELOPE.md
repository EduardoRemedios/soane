# Sprint Envelope: CPH-V0-001 Coding Proof Harness v0

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage H sprint envelope.

## Sprint ID

`CPH-V0-001`

## Execution Mode

`PLANNING_ONLY`

Implementation is not authorized by this pack. A future explicit human Go is required.

## Objective

Implement the smallest local deterministic Coding Proof Harness v0 so Soane can demonstrate a coding workflow through intake, discovery, context assembly, mocked provider invocation, candidate output capture, and review-gated promotion.

## In Scope

- Coding harness contract and validation errors.
- Greenfield and Brownfield coding fixture inputs.
- Service composition over existing Intake, Socratic Discovery, Project Memory context, adapter twin, and Candidate Review semantics.
- Deterministic provider surface selection from existing mock coding adapter vocabulary.
- Deterministic Provider Invocation records.
- Proposed provider output captured as Project Memory candidates.
- Candidate Review and Promotion as the only promotion path.
- Deterministic tests for Greenfield, Brownfield ready, Brownfield blocked, provider invocation, candidate output, and review promotion.
- Optional thin CLI or TUI wrapper only if it delegates to shared service functions.
- Validation closeout report for the implementation.

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
| Coding harness contract and service | up to 4 files |
| Fixtures and tests | up to 10 files |
| Optional CLI/TUI wrapper | up to 3 files |
| Validation closeout and state docs | up to 3 files |
| Total | up to 20 files |

## Required Micro-Sprints

- MS-00 Verification Scaffold
- MS-01 Harness Contract
- MS-02 Service Composition
- MS-03 Provider Output Candidate Flow
- MS-04 Greenfield/Brownfield Fixtures
- MS-06 Validation Closeout

## Optional Micro-Sprints

- MS-05 Optional Thin CLI/TUI Wrapper

MS-05 should be skipped if it causes service duplication, product-workflow drift, or Workspace Shell scope creep.

## Implementation Constraints

- Apply SIMPLE-CODE-GATE v2.
- Preserve Project Memory and generated Markdown distinction.
- Preserve Thinking, Evidence, Decisions, Authority, Capabilities, Missions, and Proof as distinct concepts.
- Preserve capability and authority separation.
- Do not call live models, live CLIs, live SDKs, external connectors, databases, or mutate repositories.
- Do not treat proposed provider output as accepted truth.
- Route proposed output through Project Memory candidate semantics and Candidate Review and Promotion.
- Keep ready for planning distinct from execution authority.

## Required Verification

Run at minimum:

```bash
python3 -m unittest tests/test_project_memory_contract.py tests/test_project_memory_fixtures.py tests/test_project_memory_semantics.py tests/test_project_memory_context.py tests/test_project_memory_adapter_twins.py tests/test_project_memory_cli.py tests/test_project_memory_tui.py tests/test_project_memory_review.py tests/test_thinking_engine_intake.py tests/test_thinking_engine_discovery.py
bash scripts/knowledge_lint.sh
./scripts/factoryctl pack-lint --run RUN_20260701_1548_coding_proof_harness_v0_plan
git diff --check
```

Add and run focused Coding Proof Harness tests created during implementation.

## Stop Gates

- Stop if implementation calls a live model, CLI, SDK, connector, database, or mutates a repository.
- Stop if proposed provider output bypasses Candidate Review and Promotion.
- Stop if Provider Invocation records lose capability and authority separation.
- Stop if Brownfield readiness gates are flattened into Greenfield behavior.
- Stop if wrapper work becomes Workspace Shell or product UX.

## Review Handoff

Future implementation should produce a validation closeout report mapping VC-001 through VC-011 to test and artifact evidence.
