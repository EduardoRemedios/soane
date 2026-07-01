# Project State

> Purpose: Current source of truth for the Soane repository state.
>
> Last updated: 2026-07-01

## Current Identity

Soane is the working codename for the Workspace.

The Workspace is a new product: the primary human-facing environment for governed AI work. It is project-centric. It helps humans think, preserve Project Memory, collaborate, plan, supervise missions, and coordinate neighbouring portfolio systems.

## What Exists

Implementation:

- Project Memory v0 contract scaffold at `soane/project_memory/contract.py`
- Project Memory deterministic adapter twins at `soane/project_memory/adapters.py`
- Project Memory headless CLI at `soane/project_memory/cli.py`
- Project Memory thin TUI at `soane/project_memory/tui.py`
- Project Memory context assembly and Markdown mapping at `soane/project_memory/context.py`
- Project Memory golden fixture loader at `soane/project_memory/fixtures.py`
- Project Memory local semantics layer at `soane/project_memory/semantics.py`
- Project Memory golden fixture corpus at `tests/fixtures/project_memory/golden/`
- static contract tests at `tests/test_project_memory_contract.py`
- adapter twin tests at `tests/test_project_memory_adapter_twins.py`
- headless CLI tests at `tests/test_project_memory_cli.py`
- thin TUI tests at `tests/test_project_memory_tui.py`
- context assembly and Markdown mapping tests at `tests/test_project_memory_context.py`
- golden fixture tests at `tests/test_project_memory_fixtures.py`
- memory semantics tests at `tests/test_project_memory_semantics.py`

Constitutional documents:

- `docs/VISION.md`
- `docs/CORE_CONCEPTS.md`
- `docs/GOVERNANCE_MODEL.md`
- `docs/PROJECT_MEMORY_ARCHITECTURE.md`
- `docs/THINKING_ENGINE_ARCHITECTURE.md`
- `docs/PORTFOLIO_CONTEXT.md`
- `docs/PORTFOLIO_ASSUMPTIONS.md`
- `docs/INTEGRATION_ARCHITECTURE.md`

Factory V2 process scaffold:

- `docs/Factory/README.md`
- `docs/Factory/SOANE_FACTORY_V2_ADAPTER.md`
- `docs/Factory/`
- `docs/onboarding/`
- `scripts/factoryctl`
- `scripts/knowledge_lint.sh`
- `scripts/factory_stage_lint.py`
- `scripts/factory_pack_lint.py`
- `scripts/factory_context_index.py`
- `scripts/mission_lint.sh`
- `scripts/mission_cursor_lint.sh`
- `tools/repo_cartographer/`
- `requirements.txt`

Repository adapter:

- `AGENTS.md`
- `docs/PROJECT_STATE.md`
- `docs/ROADMAP.md`
- `docs/CHANGELOG.md`

Research outputs:

- `docs/research/PROJECT_MEMORY_RESEARCH_SYNTHESIS.md`
- `docs/Factory/runs/RUN_20260630_1129_project_memory_research/`

Planning outputs:

- `docs/Factory/runs/RUN_20260701_0848_project_memory_v0_plan/`
- `docs/Factory/runs/RUN_20260701_0848_project_memory_v0_plan/VALIDATION_CLOSEOUT_REPORT.md`
- `docs/Factory/runs/RUN_20260701_1438_thinking_engine_intake_v0_plan/`

## Current Architectural Posture

The Workspace is separate from Factory V2, Factory V3, Temper, Aegis, Sentinel, and Harmony.

Factory V2 is available locally as process discipline for planning and review. It is not a Workspace subsystem.

In this repository, `docs/Factory/` means the Factory V2 starter-kit scaffold. It does not mean Factory V3.

Factory V3 remains separate in its own repository and should continue to own mission governance.

## What Does Not Exist Yet

- product UI
- full Project Memory implementation
- Thinking Engine implementation
- Workspace Shell implementation
- integration clients for Factory V3, Temper, Aegis, Sentinel, or Harmony
- live Cursor CLI, Codex CLI, Cursor SDK, OpenAI SDK, or OpenAI Agents SDK adapters
- concrete API schemas
- runnable application tests
- active implementation runs
- active Workspace missions

## Current Verification

Process scaffold verification:

```bash
bash scripts/knowledge_lint.sh
./scripts/factoryctl context-index
./scripts/factoryctl pack-lint --run RUN_20260701_0848_project_memory_v0_plan
python3 -m unittest tests/test_project_memory_contract.py tests/test_project_memory_fixtures.py tests/test_project_memory_semantics.py tests/test_project_memory_context.py
python3 -m unittest tests/test_project_memory_adapter_twins.py
python3 -m unittest tests/test_project_memory_cli.py
python3 -m unittest tests/test_project_memory_tui.py
python3 scripts/agent_loop_bridge_validate.py tests/fixtures/agent_loop_bridge/valid_handoff.json --json
```

There is no product build yet.

Headless CLI entry point:

```bash
python3 -m soane.project_memory.cli --help
```

Thin TUI entry point:

```bash
python3 -m soane.project_memory.tui --help
```

Validation closeout:

```bash
cat docs/Factory/runs/RUN_20260701_0848_project_memory_v0_plan/VALIDATION_CLOSEOUT_REPORT.md
```

## Active Boundary Decisions

- Use Factory V2 locally for planning discipline.
- Treat `docs/Factory/` as Factory V2 starter-kit process only.
- Keep Factory V3 work in `/Users/eduardodosremedios/Factory_V3`.
- Use `/Users/eduardodosremedios/Eduardo_Product_Stack` as the portfolio context source.
- Do not duplicate neighbouring product responsibilities inside the Workspace.
- Treat `docs/GOVERNANCE_MODEL.md` as the repository-level rule for document status, amendments, decisions, evidence levels, and implementation blockers.
- Use `docs/research/PROJECT_MEMORY_RESEARCH_SYNTHESIS.md` as the research input behind the Project Memory architecture.
- Treat `docs/PROJECT_MEMORY_ARCHITECTURE.md` as the conceptual architecture for Project Memory. It intentionally defers storage, API, UI, and implementation choices.
- Treat `docs/THINKING_ENGINE_ARCHITECTURE.md` as the conceptual architecture for the Thinking Engine. It defines intake, discovery, Socratic dialogue, hypotheses, evidence review, synthesis, inference strategy, readiness states, and boundaries without defining implementation APIs or UI.
- Use coding as an acceptable first proof path for Workspace primitives, while keeping the Workspace domain-general and treating Cursor CLI, Codex CLI, Cursor SDK, and OpenAI SDK integrations as adapters.
- Use a headless CLI first, then a thin TUI, before starting the broader Workspace product shell.
- Define the Project Memory v0 contract, golden fixtures, context assembly v0, capture/review/promotion flow, and mock-first adapter contract before implementation.
- Include governed memory invariants in the Project Memory v0 contract: scope and visibility, temporal supersession, provenance lineage, controlled propagation, contradiction handling, and equivalent enforcement across retrieval paths.
- Prefer mock-first, then CLI-backed coding harness adapters, then SDK-backed integrations once the adapter contract is stable.
- Treat Greenfield and Brownfield project intake differently. Brownfield coding work may involve one repository, multiple repositories, or a wider workspace/system boundary. Intake requires repo/workspace audit, existing application context, build/test discovery, architecture/documentation gap analysis, ownership and integration mapping, and agreed starting-context files before feature planning or coding delegation.
- Do not assume all project context lives in Git. Non-coding work may depend on external artifacts such as analytics dashboards, campaign assets, research notes, briefs, spreadsheets, design files, CRM records, ad accounts, and other operational systems. Soane must be able to identify and govern those sources as context inputs.

## Current Implementation State

- `RUN_20260701_0848_project_memory_v0_plan`: Factory V2 `PLANNING_ONLY` pack for Project Memory v0 object-model prototype. Status: `PASS`; final pack lint passed.
- Human Go for `PM-V0-001` was given on 2026-07-01.
- MS-00 Contract Scaffold is implemented.
- MS-01 Golden Fixture Corpus is implemented.
- MS-02 Memory Semantics is implemented.
- MS-03 Context Assembly And Markdown Mapping is implemented.
- MS-04 Mock Coding Adapter Contract is implemented.
- MS-05 Headless CLI is implemented.
- MS-06 Thin TUI Scope is implemented.
- MS-07 Validation Closeout is complete.
- Thinking Engine architecture is complete.
- `RUN_20260701_1438_thinking_engine_intake_v0_plan`: Factory V2 `PLANNING_ONLY` pack for `TEI-V0-001` Thinking Engine Intake v0. Status: `PASS`; pack lint passed.
- Next roadmap step: human Go/No-go review for `TEI-V0-001` before implementation.
