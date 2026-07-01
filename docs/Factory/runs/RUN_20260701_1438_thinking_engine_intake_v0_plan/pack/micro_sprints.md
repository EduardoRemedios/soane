# Micro-Sprints

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage G micro-sprint plan.

## MS-00 Intake Contract Scaffold

- Objective: Define intake categories, Context Baseline, and Readiness Assessment dataclasses or equivalent local objects.
- Inputs: architecture doc, fixtures plan.
- Outputs: local contract module and tests.
- Entry Criteria: human Go after pack review.
- Exit Criteria: static tests validate object shapes and readiness states.
- Stop or Go Gate: Stop if schema starts modeling product UI or live connectors.

## MS-01 Golden Intake Fixtures

- Objective: Add fixtures for Greenfield, Brownfield single-repo, Brownfield multi-repo, non-repository context, and missing-context blocker.
- Inputs: verification plan.
- Outputs: fixture files and loader tests.
- Entry Criteria: MS-00 complete.
- Exit Criteria: fixtures validate deterministically.
- Stop or Go Gate: Stop if fixture requires live external access.

## MS-02 Intake Semantics

- Objective: Implement deterministic intake classification, context baseline assessment, and readiness state derivation.
- Inputs: MS-00 and MS-01.
- Outputs: local service functions and focused tests.
- Entry Criteria: fixture suite passing.
- Exit Criteria: VC-002 through VC-008 pass.
- Stop or Go Gate: Stop if readiness becomes numeric scoring.

## MS-03 Discovery Playbook Selection

- Objective: Implement local selection of Discovery Playbook stubs based on intake category and missing context.
- Inputs: MS-02.
- Outputs: playbook selection functions and tests.
- Entry Criteria: intake semantics passing.
- Exit Criteria: each fixture maps to expected playbook candidates.
- Stop or Go Gate: Stop if playbooks become rigid full workflows.

## MS-04 CLI And TUI Wrappers

- Objective: Expose intake validation through existing CLI/TUI proof surfaces if useful.
- Inputs: MS-00 through MS-03.
- Outputs: wrapper commands or screens and subprocess tests.
- Entry Criteria: shared services stable.
- Exit Criteria: wrappers call shared service functions.
- Stop or Go Gate: Stop if CLI/TUI duplicates intake logic.

## MS-05 Validation Closeout

- Objective: Run full validation and update canonical docs if implementation teaches durable lessons.
- Inputs: all prior micro-sprints.
- Outputs: closeout report and doc updates.
- Entry Criteria: implementation checks pass.
- Exit Criteria: all required checks pass or blockers are recorded.
- Stop or Go Gate: Stop if new architecture decisions are required.
