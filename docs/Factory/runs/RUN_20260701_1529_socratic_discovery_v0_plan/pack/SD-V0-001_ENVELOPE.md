# Sprint Envelope: SD-V0-001 Socratic Discovery v0

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage H sprint envelope.

## Sprint ID

`SD-V0-001`

## Execution Mode

`PLANNING_ONLY`

Implementation is not authorized by this pack. A future explicit human Go is required.

## Objective

Implement the smallest local deterministic Socratic Discovery v0 layer so Soane can turn intake gaps into traceable questions, capture answers as candidates, derive uncertainty-preserving hypotheses, and decide the next discovery state before planning or delegation.

## In Scope

- Discovery session contract and validation errors.
- Deterministic question generation from Context Baseline gaps and playbook references.
- Answer capture as Project Memory candidates.
- Hypothesis generation as Project Memory candidates with uncertainty state and evidence-gap links.
- Stop conditions: blocked, needs evidence, needs authority, ready for planning.
- Deterministic fixtures and tests for greenfield, brownfield single-repo, brownfield multi-repo, non-repository, and blocked discovery.
- Optional thin CLI or TUI wrapper only if it delegates to shared service functions.
- Validation closeout report for the implementation.

## Out of Scope

- product web UI
- database or persistence selection
- live LLM calls
- live Cursor, Codex, OpenAI, analytics, CRM, ads, design, repository, or external connectors
- Workspace Shell implementation
- mission execution
- Factory V3, Temper, Aegis, Sentinel, or Harmony responsibilities

## File-Touch Budget

| Area | Budget |
| --- | --- |
| Socratic Discovery contract and service | up to 4 files |
| Fixtures and tests | up to 10 files |
| Optional CLI/TUI wrapper | up to 3 files |
| Validation closeout and state docs | up to 3 files |
| Total | up to 20 files |

## Required Micro-Sprints

- MS-00 Verification Scaffold
- MS-01 Discovery Session Contract
- MS-02 Question Generation Service
- MS-03 Answer Capture And Hypothesis Service
- MS-04 Stop Conditions
- MS-06 Validation Closeout

## Optional Micro-Sprints

- MS-05 Optional Thin CLI/TUI Wrapper

MS-05 should be skipped if it causes service duplication, product-workflow drift, or Workspace Shell scope creep.

## Implementation Constraints

- Apply SIMPLE-CODE-GATE v2.
- Preserve Project Memory and generated Markdown distinction.
- Preserve Thinking, Evidence, Decisions, Authority, Capabilities, Missions, and Proof as distinct concepts.
- Preserve capability and authority separation.
- Do not call live models, adapters, external connectors, or databases.
- Do not treat answers or hypotheses as accepted truth.
- Route answers and hypotheses through Project Memory candidate semantics and Candidate Review and Promotion.
- Require source reasons for generated questions.
- Require uncertainty state and evidence-gap links for generated hypotheses.
- Keep ready for planning distinct from execution authority.

## Required Verification

Run at minimum:

```bash
python3 -m unittest tests/test_project_memory_contract.py tests/test_project_memory_fixtures.py tests/test_project_memory_semantics.py tests/test_project_memory_context.py tests/test_project_memory_adapter_twins.py tests/test_project_memory_cli.py tests/test_project_memory_tui.py tests/test_project_memory_review.py tests/test_thinking_engine_intake.py
bash scripts/knowledge_lint.sh
./scripts/factoryctl pack-lint --run RUN_20260701_1529_socratic_discovery_v0_plan
git diff --check
```

Add and run focused Socratic Discovery tests created during implementation.

## Stop Gates

- Stop if implementation calls a live model or hides a model dependency.
- Stop if generated questions lack source reasons.
- Stop if answers or hypotheses bypass Candidate Review and Promotion.
- Stop if hypotheses lose uncertainty state or evidence-gap links.
- Stop if ready for planning implies authority to execute.
- Stop if wrapper work becomes Workspace Shell or product UX.

## Review Handoff

Future implementation should produce a validation closeout report mapping VC-001 through VC-011 to test and artifact evidence.
