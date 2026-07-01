# Sprint Envelope: CRP-V0-001 Candidate Review and Promotion v0

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage H sprint envelope.

## Sprint ID

`CRP-V0-001`

## Execution Mode

`PLANNING_ONLY`

Implementation is not authorized by this pack. A future explicit human Go is required.

## Objective

Implement the smallest local deterministic Candidate Review and Promotion v0 layer so Project Memory candidates can be reviewed before they become accepted truth.

## In Scope

- Review decision contract and validation errors.
- Allowed outcomes: accept, reject, defer, amend, keep open.
- Local service functions for candidate review and promotion.
- Deterministic fixtures and tests for accepted, rejected, deferred, amended, unauthorized, and conflicting cases.
- Current-truth behavior tests for candidate-only and non-current outcomes.
- Optional thin CLI wrapper only if it delegates to shared service functions.
- Validation closeout report for the implementation.

## Out of Scope

- product web UI
- database or persistence selection
- live Cursor, Codex, OpenAI, analytics, CRM, ads, design, repository, or external connectors
- Socratic discovery implementation
- Workspace Shell implementation
- Factory V3, Temper, Aegis, Sentinel, or Harmony responsibilities

## File-Touch Budget

| Area | Budget |
| --- | --- |
| Candidate review contract and service | up to 3 files |
| Fixtures and tests | up to 8 files |
| Optional CLI wrapper | up to 2 files |
| Validation closeout and state docs | up to 3 files |
| Total | up to 16 files |

## Required Micro-Sprints

- MS-00 Verification Scaffold
- MS-01 Review Contract
- MS-02 Promotion Service
- MS-03 Current Truth Semantics
- MS-05 Validation Closeout

## Optional Micro-Sprints

- MS-04 Optional Thin CLI Wrapper

MS-04 should be skipped if it causes CLI logic duplication, product-workflow drift, or file-budget pressure.

## Implementation Constraints

- Apply SIMPLE-CODE-GATE v2.
- Preserve Project Memory and generated Markdown distinction.
- Preserve capability and authority separation.
- Do not mutate source candidates in place.
- Preserve original candidate provenance and add reviewer provenance.
- Require rationale for terminal review outcomes.
- Keep rejected, deferred, stale, superseded, and candidate-only records inspectable but out of current truth.
- Do not introduce live integrations, database selection, or product shell.

## Required Verification

Run at minimum:

```bash
python3 -m unittest tests/test_project_memory_contract.py tests/test_project_memory_fixtures.py tests/test_project_memory_semantics.py tests/test_project_memory_context.py tests/test_project_memory_adapter_twins.py tests/test_project_memory_cli.py tests/test_project_memory_tui.py tests/test_thinking_engine_intake.py
bash scripts/knowledge_lint.sh
./scripts/factoryctl pack-lint --run RUN_20260701_1455_candidate_review_promotion_v0_plan
git diff --check
```

Add and run focused Candidate Review and Promotion tests created during implementation.

## Stop Gates

- Stop if accepted memory implies authority without an Authority Reference.
- Stop if candidate review requires persistence or live connectors.
- Stop if amended outcomes lose lineage.
- Stop if current-truth retrieval includes rejected, deferred, stale, superseded, or candidate-only records.
- Stop if CLI/TUI work duplicates service logic or becomes product shell.

## Review Handoff

Future implementation should produce a validation closeout report mapping VC-001 through VC-010 to test and artifact evidence.
