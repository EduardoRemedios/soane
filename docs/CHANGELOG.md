# Changelog

## 2026-07-01

- Added governed memory invariants to the Project Memory v0 roadmap, informed by the MemClaw governed shared memory paper: scope and visibility, temporal supersession, provenance lineage, controlled propagation, contradiction handling, and equivalent enforcement across retrieval paths.
- Clarified that Cursor CLI and Codex CLI are candidate coding harness adapter surfaces alongside Cursor SDK, OpenAI SDK, and OpenAI Agents SDK, with a preferred mock-first, CLI-backed, then SDK-backed proof order.
- Added Factory V2 planning-only pack `RUN_20260701_0848_project_memory_v0_plan` for the Project Memory v0 object-model prototype, including v0 contract gates, golden fixtures, governed memory invariants, mock adapter proof, CLI/TUI sequencing, and final pack audit.
- Implemented MS-00 Project Memory v0 contract scaffold with object types, lifecycle transitions, relationship types, evidence levels, governed memory invariants, deterministic fixture IDs, and static unit tests.
- Implemented MS-01 Project Memory golden fixture corpus with twelve fixture files, a fixture loader, deterministic ID validation, and fixture conformance tests.
- Implemented MS-02 Project Memory local semantics with lifecycle transitions, provenance preservation, relationship/evidence queries, visibility enforcement, current-truth filtering, suppression handling, and contradiction representation tests.
- Implemented MS-03 Project Memory context assembly and Markdown source mapping with lifecycle-aware context packages, visibility and propagation exclusions, contradiction and stale-record surfacing, and explicit Markdown source maps.

## 2026-06-30

- Added the founding Workspace vision document.
- Added `CORE_CONCEPTS.md` and updated it to Version 1.1 with `Thinking`, `Discovery Playbook`, and `Inference Strategy`.
- Added `docs/GOVERNANCE_MODEL.md` to define document status, amendment rules, decisions, assumptions, evidence levels, authority boundaries, and implementation blockers.
- Added portfolio context documents for Workspace-facing portfolio boundaries, assumptions, and conceptual integration architecture.
- Added a local Factory V2 process scaffold from `/Users/eduardodosremedios/factory-starter-kit`.
- Added `docs/Factory/README.md` and `docs/Factory/SOANE_FACTORY_V2_ADAPTER.md` to make the Factory V2 versus Factory V3 boundary explicit.
- Added Soane-specific repository adapter docs: `AGENTS.md`, `docs/PROJECT_STATE.md`, `docs/ROADMAP.md`, and this changelog.
- Added a Factory V2 planning-only research spike for Project Memory architecture at `docs/Factory/runs/RUN_20260630_1129_project_memory_research/`.
- Added `docs/research/PROJECT_MEMORY_RESEARCH_SYNTHESIS.md` as the research input for the future Project Memory architecture.
- Added `docs/PROJECT_MEMORY_ARCHITECTURE.md` as the conceptual architecture for Project Memory, including layers, first-class objects, lifecycle, provenance, context assembly, Markdown generation, and portfolio boundaries.
- Clarified `docs/ROADMAP.md` into an explicit sequence from foundation documents through Project Memory prototype, Thinking Engine architecture, Workspace Shell architecture, and first product surface.
- Clarified that Cursor SDK and OpenAI SDK may be used as early adapter-backed proof paths for coding workflows without narrowing the Workspace to coding-only use cases.
- Updated the roadmap to make the implementation path explicit: Project Memory v0, then headless CLI, then simple TUI, before any broader Workspace product shell.
- Tightened the roadmap with Project Memory v0 contract gates, golden fixtures, mock-first adapter proof, context assembly v0, capture/review/promotion flow, and persistence guardrails before implementation.
