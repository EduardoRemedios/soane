# Raw Brief: Thinking Engine Intake v0 Planning

## Request

Plan the first bounded implementation slice for the Thinking Engine after the canonical architecture document was accepted.

The implementation target should be `Thinking Engine Intake v0`.

## Execution Mode

PLANNING_ONLY.

This run must not implement code. It should produce a reviewable Factory V2 pack for future human Go or No-go.

## Background

Project Memory v0 has been implemented and validated.

The validation closeout is ready at:

- `docs/Factory/runs/RUN_20260701_0848_project_memory_v0_plan/VALIDATION_CLOSEOUT_REPORT.md`

The next canonical architecture document is complete at:

- `docs/THINKING_ENGINE_ARCHITECTURE.md`

The roadmap now calls for a Factory V2 planning run before implementing the first Thinking Engine slice.

## Proposed Implementation Slice

Plan `Thinking Engine Intake v0`.

The slice should focus on:

- intake classification
- context baseline assessment
- Discovery Playbook selection
- readiness assessment
- Project Memory write-back shape

## Required Intake Categories

The planned implementation should distinguish at least:

- Greenfield project
- Brownfield single-repository coding project
- Brownfield multi-repository coding or system project
- Non-repository context project

## Required Context Concerns

The planned implementation must not assume every project is a repository.

Brownfield systems may involve:

- one repository
- multiple repositories
- deployed services
- build and test commands
- issue trackers
- CI or deployment systems
- architecture documentation
- undocumented decisions and assumptions

Non-coding projects may involve:

- analytics dashboards
- advertising platform reports
- campaign briefs
- creative assets
- spreadsheets
- CRM records
- customer interviews
- research notes
- product analytics
- design files
- operations runbooks
- support tickets
- sales notes
- compliance documents
- screenshots
- data exports

## In Scope For Planning

- define the smallest useful intake object shape
- define Context Baseline v0 shape
- define Readiness Assessment v0 shape
- define Discovery Playbook selection shape
- define fixture cases for Greenfield, Brownfield single repo, Brownfield multi repo, and non-repository context
- define service functions to be implemented later
- define CLI/TUI extension points if useful
- define verification requirements
- define Project Memory integration boundaries

## Out Of Scope

- implementation during this run
- product web UI
- database selection
- live Cursor, Codex, OpenAI, Google Analytics, CRM, advertising platform, or design-tool integrations
- live repository scanning
- live model routing
- final readiness score
- Factory V3 mission governance
- Temper runtime behavior
- Aegis authority or proof semantics
- Harmony regulated conversational runtime

## Inputs

Use these sources:

- `docs/VISION.md`
- `docs/CORE_CONCEPTS.md`
- `docs/GOVERNANCE_MODEL.md`
- `docs/PROJECT_MEMORY_ARCHITECTURE.md`
- `docs/THINKING_ENGINE_ARCHITECTURE.md`
- `docs/ROADMAP.md`
- `docs/PROJECT_STATE.md`
- `docs/INTEGRATION_ARCHITECTURE.md`
- `docs/Factory/runs/RUN_20260701_0848_project_memory_v0_plan/VALIDATION_CLOSEOUT_REPORT.md`

## Acceptance Standard

The pack is review-ready when it:

- preserves Soane portfolio boundaries
- plans only the smallest useful Thinking Engine Intake v0 implementation slice
- includes fixtures for the required intake categories
- keeps Project Memory as the source substrate
- keeps Context Baseline and Readiness Assessment separate from Project Memory truth
- avoids live integrations
- avoids premature readiness scoring
- defines verification before implementation
- includes clear stop/go gates

## Go Or No-Go Rule

Go to future implementation only after the Factory pack passes I2, pack-lint passes, and a human explicitly gives Go.
