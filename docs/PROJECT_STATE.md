# Project State

> Purpose: Current source of truth for the Soane repository state.
>
> Last updated: 2026-06-30

## Current Identity

Soane is the working codename for the Workspace.

The Workspace is a new product: the primary human-facing environment for governed AI work. It is project-centric. It helps humans think, preserve Project Memory, collaborate, plan, supervise missions, and coordinate neighbouring portfolio systems.

## What Exists

Constitutional documents:

- `docs/VISION.md`
- `docs/CORE_CONCEPTS.md`
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

## Current Architectural Posture

The Workspace is separate from Factory V2, Factory V3, Temper, Aegis, Sentinel, and Harmony.

Factory V2 is available locally as process discipline for planning and review. It is not a Workspace subsystem.

In this repository, `docs/Factory/` means the Factory V2 starter-kit scaffold. It does not mean Factory V3.

Factory V3 remains separate in its own repository and should continue to own mission governance.

## What Does Not Exist Yet

- application code
- product UI
- Project Memory implementation
- Thinking Engine implementation
- Workspace Shell implementation
- integration clients for Factory V3, Temper, Aegis, Sentinel, or Harmony
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
