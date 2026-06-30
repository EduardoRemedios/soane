# Roadmap

> Purpose: Track near-term Soane repository work.
>
> Last updated: 2026-06-30

## Completed

| Item | Status | Evidence |
| --- | --- | --- |
| Founding vision | Done | `docs/VISION.md` |
| Core concepts v1.1 | Done | `docs/CORE_CONCEPTS.md` |
| Governance model | Done | `docs/GOVERNANCE_MODEL.md` |
| Portfolio context documents | Done | `docs/PORTFOLIO_CONTEXT.md`, `docs/PORTFOLIO_ASSUMPTIONS.md`, `docs/INTEGRATION_ARCHITECTURE.md` |
| Factory V2 process scaffold | Done | `docs/Factory/`, `docs/Factory/SOANE_FACTORY_V2_ADAPTER.md`, `scripts/`, `AGENTS.md`, `docs/PROJECT_STATE.md` |
| Project Memory research synthesis | Done | `docs/research/PROJECT_MEMORY_RESEARCH_SYNTHESIS.md`, `docs/Factory/runs/RUN_20260630_1129_project_memory_research/` |
| Project Memory architecture | Done | `docs/PROJECT_MEMORY_ARCHITECTURE.md` |

## Sequence

| Order | Work | Status | Notes |
| --- | --- | --- |
| 1 | Foundation documents | Done | Vision, core concepts, governance, portfolio context, integration architecture, Factory V2 scaffold, Project Memory research, and Project Memory architecture are complete. |
| 2 | Project Memory implementation planning | Next | Run a Factory V2 `PLANNING_ONLY` pack for the first local Project Memory object-model prototype. |
| 3 | Project Memory v0 prototype | Pending | Implement the smallest local prototype for object types, lifecycle states, provenance, relationships, and traceability. Use a coding workflow as the first proof path if the planning pack supports it. No database choice unless the planning pack proves it is needed. |
| 4 | Project Memory validation pass | Pending | Validate the prototype against existing canonical docs and the research synthesis. Prove import, traceability, amendment, supersession, Markdown source mapping, and adapter-backed provider invocation fixtures. |
| 5 | Thinking Engine architecture | Pending | Define discovery, Thinking, Socratic dialogue, hypotheses, inference strategies, Discovery Playbooks, and readiness assessment. |
| 6 | Thinking Engine planning run | Pending | Use Factory V2 to plan the first Thinking Engine implementation slice after the architecture is accepted. |
| 7 | Workspace Shell architecture | Pending | Define desktop, web, mobile, voice, collaboration, dashboards, notifications, mission monitoring, and portfolio views. |
| 8 | First product surface prototype | Pending | Build only after Project Memory and Thinking Engine primitives are coherent enough to support a real workflow. |

## Immediate Next Move

Run a Factory V2 `PLANNING_ONLY` implementation-planning pack for:

`Project Memory v0 Object Model Prototype`

The pack should consume:

- `docs/VISION.md`
- `docs/CORE_CONCEPTS.md`
- `docs/GOVERNANCE_MODEL.md`
- `docs/research/PROJECT_MEMORY_RESEARCH_SYNTHESIS.md`
- `docs/PROJECT_MEMORY_ARCHITECTURE.md`

The output should define:

- first implementation slice
- non-goals
- file/module layout
- minimal object model
- lifecycle states
- provenance representation
- relationship representation
- validation strategy
- fixtures
- commands/tests to add
- coding-first proof path using Cursor SDK or OpenAI SDK as candidate adapters, without narrowing the Workspace to coding

It should not implement during the planning run.

## Current Candidates

| Candidate | Status | Notes |
| --- | --- | --- |
| Decision Record format | Candidate | Useful once the Project Memory prototype needs durable Decision fixtures. |
| Evidence Artifact format | Candidate | Useful once the Project Memory prototype needs traceability fixtures. |
| Canonical Markdown generation rules | Candidate | Useful after object model and provenance are proven locally. |
| Cursor/OpenAI adapter fixtures | Candidate | Useful as the first coding proof path for Provider Invocation and Capability Reference semantics. |
| Thinking Engine architecture | Candidate | Next major architecture document after Project Memory implementation planning starts. |
| Workspace Shell architecture | Candidate | Defer until Project Memory and Thinking Engine shape are stable enough to drive UI. |

## Process Guidance

Use Factory V2 for bounded planning before implementation.

Do not use Factory V2 as a reason to delay small documentation maintenance that is already clear and low-risk.

Do not move Factory V3 work into this repository. Factory V3 remains a separate mission-governance repository.

In this roadmap, Factory V2 means the starter-kit process. Factory V3 means the separate newer repository and is not scaffolded here.

The next Factory V2 planning run should consume `docs/PROJECT_MEMORY_ARCHITECTURE.md` and produce the first implementation plan for a local Project Memory object-model prototype.

Do not start the product shell before Project Memory has at least a local object-model prototype. The Workspace experience should be built around memory and thinking primitives, not around a generic app shell.
