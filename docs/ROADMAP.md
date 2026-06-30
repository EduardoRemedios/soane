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

## Current Candidates

| Candidate | Status | Notes |
| --- | --- | --- |
| Project Memory implementation planning | Next | Use Factory V2 to plan the first small implementation slice for object modeling, lifecycle states, provenance, and traceability. |
| Thinking Engine architecture | Candidate | Define discovery, Thinking, Socratic dialogue, hypotheses, inference strategies, and Discovery Playbooks. |
| Workspace product shell architecture | Candidate | Define desktop, web, mobile, voice, collaboration, dashboards, and mission monitoring surfaces. |
| Factory V2 first planning run | Candidate | Use the scaffold to plan the first implementation slice once the next concrete build objective is chosen. |

## Process Guidance

Use Factory V2 for bounded planning before implementation.

Do not use Factory V2 as a reason to delay small documentation maintenance that is already clear and low-risk.

Do not move Factory V3 work into this repository. Factory V3 remains a separate mission-governance repository.

In this roadmap, Factory V2 means the starter-kit process. Factory V3 means the separate newer repository and is not scaffolded here.

The next Factory V2 planning run should consume `docs/PROJECT_MEMORY_ARCHITECTURE.md` and produce the first implementation plan for a local Project Memory object-model prototype.
