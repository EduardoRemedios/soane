# Project State

> Purpose: Current source of truth for the Soane repository state.
>
> Last updated: 2026-07-01

## Current Identity

Soane is the working codename for the Workspace.

The Workspace is a new product: the primary human-facing environment for governed AI work. It is project-centric. It helps humans think, preserve Project Memory, collaborate, plan, supervise missions, and coordinate neighbouring portfolio systems.

## What Exists

Constitutional documents:

- `docs/VISION.md`
- `docs/CORE_CONCEPTS.md`
- `docs/GOVERNANCE_MODEL.md`
- `docs/PROJECT_MEMORY_ARCHITECTURE.md`
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

## Current Architectural Posture

The Workspace is separate from Factory V2, Factory V3, Temper, Aegis, Sentinel, and Harmony.

Factory V2 is available locally as process discipline for planning and review. It is not a Workspace subsystem.

In this repository, `docs/Factory/` means the Factory V2 starter-kit scaffold. It does not mean Factory V3.

Factory V3 remains separate in its own repository and should continue to own mission governance.

## What Does Not Exist Yet

- application code
- product UI
- Project Memory implementation
- headless CLI
- TUI
- Thinking Engine implementation
- Workspace Shell implementation
- integration clients for Factory V3, Temper, Aegis, Sentinel, or Harmony
- Cursor CLI, Codex CLI, Cursor SDK, or OpenAI SDK adapters
- concrete API schemas
- runnable application tests
- active Factory runs
- active Workspace missions

## Current Verification

Process scaffold verification:

```bash
bash scripts/knowledge_lint.sh
./scripts/factoryctl context-index
python3 scripts/agent_loop_bridge_validate.py tests/fixtures/agent_loop_bridge/valid_handoff.json --json
```

There is no product build or application test suite yet.

## Active Boundary Decisions

- Use Factory V2 locally for planning discipline.
- Treat `docs/Factory/` as Factory V2 starter-kit process only.
- Keep Factory V3 work in `/Users/eduardodosremedios/Factory_V3`.
- Use `/Users/eduardodosremedios/Eduardo_Product_Stack` as the portfolio context source.
- Do not duplicate neighbouring product responsibilities inside the Workspace.
- Treat `docs/GOVERNANCE_MODEL.md` as the repository-level rule for document status, amendments, decisions, evidence levels, and implementation blockers.
- Use `docs/research/PROJECT_MEMORY_RESEARCH_SYNTHESIS.md` as the research input behind the Project Memory architecture.
- Treat `docs/PROJECT_MEMORY_ARCHITECTURE.md` as the conceptual architecture for Project Memory. It intentionally defers storage, API, UI, and implementation choices.
- Use coding as an acceptable first proof path for Workspace primitives, while keeping the Workspace domain-general and treating Cursor CLI, Codex CLI, Cursor SDK, and OpenAI SDK integrations as adapters.
- Use a headless CLI first, then a thin TUI, before starting the broader Workspace product shell.
- Define the Project Memory v0 contract, golden fixtures, context assembly v0, capture/review/promotion flow, and mock-first adapter contract before implementation.
- Include governed memory invariants in the Project Memory v0 contract: scope and visibility, temporal supersession, provenance lineage, controlled propagation, contradiction handling, and equivalent enforcement across retrieval paths.
- Prefer mock-first, then CLI-backed coding harness adapters, then SDK-backed integrations once the adapter contract is stable.
