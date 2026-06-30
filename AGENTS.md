# AGENTS.md - Soane Repository Context Map

Purpose:
- Give future humans and agents the shortest reliable path into this repository.
- Keep Factory V2 process use aligned with the Workspace constitutional documents.

## 1) Read Order

Read these first:

1. `docs/VISION.md`
2. `docs/CORE_CONCEPTS.md`
3. `docs/PORTFOLIO_CONTEXT.md`
4. `docs/PORTFOLIO_ASSUMPTIONS.md`
5. `docs/INTEGRATION_ARCHITECTURE.md`
6. `docs/PROJECT_STATE.md`
7. `docs/ROADMAP.md`

When using Factory V2 process, also read:

8. `docs/Factory/README.md`
9. `docs/Factory/SOANE_FACTORY_V2_ADAPTER.md`
10. `docs/Factory/ARCHITECTURE.md`
11. `docs/Factory/ORCHESTRATION.md`
12. `docs/Factory/MISSION_MODE.md` if using Mission Mode
13. `docs/Factory/ProductOwner/PO_PROCESS.md` if working on phase planning or PO-authored briefs
14. `docs/Factory/SCRATCHPAD.md`, only `## Active Pitfalls (Mandatory)`

## 2) Repository Boundary

Soane is the working codename for the Workspace.

The Workspace is the primary human-facing environment for governed AI work. It owns project-centric thinking, Project Memory, discovery, synthesis, decision support, mission planning UI, mission monitoring, collaboration, voice, desktop, cloud, mobile, and cross-project knowledge.

The Workspace does not own:

- Factory V2 process doctrine
- Factory V3 mission governance
- Temper agent-team runtime
- Aegis authority or proof
- Sentinel boundary discovery
- Harmony regulated conversational runtime

Use portfolio integrations through explicit contracts. Do not collapse neighbouring products into this repository.

## 3) Factory V2 Use In This Repository

This repository includes a local Factory V2 scaffold from:

`/Users/eduardodosremedios/factory-starter-kit`

Factory V2 is used here as the current planning-first process discipline. It helps turn rough intent into bounded, reviewable, evidence-backed work before implementation.

Factory V2 in this repository is a process scaffold, not the product architecture of the Workspace.

Factory V3 work continues separately in:

`/Users/eduardodosremedios/Factory_V3`

Do not import Factory V3 responsibilities into this repo unless a future architectural decision explicitly changes the boundary.

In `docs/Factory/`, the unqualified word "Factory" refers to the Factory V2 starter-kit process unless a document explicitly says otherwise. It does not refer to Factory V3.

## 4) Canonical Commands

Factory preflight:

```bash
bash scripts/knowledge_lint.sh
./scripts/factoryctl context-index
```

Factory run setup:

```bash
./scripts/factoryctl context-report --profile stage-a --scope <RUN_ID> --output docs/Factory/runs/<RUN_ID>/CONTEXT_RECALL_REPORT.md
./scripts/factoryctl stage-lint --run <RUN_ID> --stage <STAGE>
./scripts/factoryctl pack-lint --run <RUN_ID>
```

Optional Factory helpers:

```bash
./scripts/factoryctl metrics-init --run <RUN_ID>
./scripts/factoryctl memory-init
./scripts/factoryctl kilo-stage --run <RUN_ID> --stage <STAGE> --model <KILO_MODEL_ID> --variant high --auto --timeout-seconds 900
./scripts/cartographer
bash scripts/mission_lint.sh <MISSION_ID>
bash scripts/mission_cursor_lint.sh <MISSION_ID>
python3 scripts/agent_loop_bridge_validate.py tests/fixtures/agent_loop_bridge/valid_handoff.json --json
```

Dependencies:

```bash
python3 -m pip install -r requirements.txt
```

No application build or test command exists yet. Add one only when implementation introduces runnable code.

## 5) Hard Guardrails

- Do not rewrite constitutional documents unless explicitly asked.
- Preserve the distinction between Project Memory and generated Markdown views.
- Keep Thinking, Evidence, Decisions, Authority, Capabilities, Missions, and Proof distinct.
- Treat assumptions as assumptions until evidence or authority changes their status.
- Keep authority explicit. Capability does not imply permission.
- Keep integration contracts conceptual until implementation requires concrete APIs.
- Do not duplicate Factory V3, Temper, Aegis, Sentinel, or Harmony responsibilities inside the Workspace.
- Do not treat `docs/Factory/` as Factory V3. It is the Factory V2 starter-kit scaffold.
- Prefer small, auditable changes with clear evidence paths.

## 6) Factory Run Preconditions

Before Stage A:

- create a run root under `docs/Factory/runs/<RUN_ID>/`
- persist `raw_brief.md`
- run `bash scripts/knowledge_lint.sh`
- persist output as `KNOWLEDGE_LINT.txt`
- refresh the context index
- generate `CONTEXT_RECALL_REPORT.md`
- persist `EXECUTION_MODE.txt`

Runs default to `PLANNING_ONLY`.

Execution is allowed only when the run explicitly records:

- `Execution Mode: EXECUTION_ENABLED`
- `Execution Authorization: <human-approved reference>`

After each stage, run stage lint before proceeding.

After Stage I2, run pack lint before asking for Go or No-go.

## 7) Change Hygiene

When a material repository change lands, update these in the same cycle when relevant:

- `docs/PROJECT_STATE.md`
- `docs/ROADMAP.md`
- `docs/CHANGELOG.md`

Factory Core improvements should be promoted back to `/Users/eduardodosremedios/factory-starter-kit` rather than silently forked here.

## 8) When Uncertain

Stop and clarify intent, constraints, evidence, and authority before implementation.

If the uncertainty concerns portfolio ownership or architectural direction, consult `/Users/eduardodosremedios/Eduardo_Product_Stack` before making assumptions.
