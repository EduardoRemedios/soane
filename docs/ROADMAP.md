# Roadmap

> Purpose: Track near-term Soane repository work.
>
> Last updated: 2026-07-01

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
| 2 | Project Memory implementation planning | Done | Factory V2 `PLANNING_ONLY` pack completed at `docs/Factory/runs/RUN_20260701_0848_project_memory_v0_plan/`; human Go received on 2026-07-01. |
| 3 | Project Memory v0 contract | Done | Contract scaffold, lifecycle transitions, relationship types, evidence levels, governed memory invariants, deterministic fixture IDs, and validation tests exist in `soane/project_memory/contract.py` and `tests/test_project_memory_contract.py`. |
| 4 | Project Memory v0 prototype | Done | Contract, fixture corpus, local memory semantics, context assembly, Markdown mapping, and deterministic adapter twins are in place. No database choice unless the implementation proves it is needed. |
| 5 | Headless CLI | Done | Added `python3 -m soane.project_memory.cli` commands over Project Memory v0 primitives before building a navigable interface. |
| 6 | Simple TUI | Done | Added thin terminal navigation over the same service functions for project navigation, memory browsing, evidence, decisions, hypotheses, adapter invocations, validation state, and unresolved questions. |
| 7 | Project Memory validation pass | Done | Validation closeout passed at `docs/Factory/runs/RUN_20260701_0848_project_memory_v0_plan/VALIDATION_CLOSEOUT_REPORT.md`. |
| 8 | Thinking Engine architecture | Next | Define discovery, Thinking, Socratic dialogue, hypotheses, inference strategies, Discovery Playbooks, and readiness assessment. |
| 9 | Thinking Engine planning run | Pending | Use Factory V2 to plan the first Thinking Engine implementation slice after the architecture is accepted. |
| 10 | Workspace Shell architecture | Pending | Define desktop, web, mobile, voice, collaboration, dashboards, notifications, mission monitoring, and portfolio views after CLI/TUI proof has clarified the primitives. |
| 11 | First product surface prototype | Pending | Build only after Project Memory, CLI/TUI navigation, and Thinking Engine primitives are coherent enough to support a real workflow. |

## Immediate Next Move

Continue implementation with:

`Thinking Engine architecture`

Pack path:

- `docs/Factory/runs/RUN_20260701_0848_project_memory_v0_plan/`

Current state:

- Factory V2 planning pack: complete and passed.
- Human Go: received on 2026-07-01.
- MS-00 Contract Scaffold: complete.
- MS-01 Golden Fixture Corpus: complete.
- MS-02 Memory Semantics: complete.
- MS-03 Context Assembly And Markdown Mapping: complete.
- MS-04 Mock Coding Adapter Contract: complete.
- MS-05 Headless CLI: complete.
- MS-06 Thin TUI Scope: complete.
- MS-07 Validation Closeout: complete.
- Next work: Thinking Engine architecture.

The pack consumed:

- `docs/VISION.md`
- `docs/CORE_CONCEPTS.md`
- `docs/GOVERNANCE_MODEL.md`
- `docs/research/PROJECT_MEMORY_RESEARCH_SYNTHESIS.md`
- `docs/PROJECT_MEMORY_ARCHITECTURE.md`

The completed MS-04 micro-sprint implemented deterministic local functions and tests for:

- mocked Provider Invocation records
- Cursor/Codex/OpenAI adapter surface metadata
- input and output references
- policy context, confidence, cost, and latency fields
- capability and authority separation
- no live CLI or SDK calls

The completed MS-05 micro-sprint implemented a small headless CLI over the existing Project Memory service functions. The CLI does not duplicate contract, fixture, semantics, context assembly, or adapter-twin logic.

The completed MS-06 micro-sprint implemented the smallest thin TUI scope over the same service and CLI primitives. It improves navigation without becoming the product shell.

The completed MS-07 validation closeout validates the Project Memory v0 prototype against the canonical documents, research synthesis, Factory pack, fixtures, CLI, TUI, context assembly, Markdown mapping, and adapter-twin behavior.

The next work should define Thinking Engine architecture. It should build on the validated Project Memory v0 proof and clarify discovery, Thinking, Socratic dialogue, hypotheses, inference strategies, Discovery Playbooks, readiness assessment, and the boundary between thinking support and mission execution.

Do not implement live adapters, database selection, or a broader Workspace product shell during the Thinking Engine architecture step.

The golden fixture set should include at least:

- Decision linked to Evidence
- Assumption superseded by Evidence
- Contradiction between sources
- Stale Evidence
- canonical Markdown source mapping
- Provider Invocation via mocked Cursor/Codex or OpenAI adapter
- Capability without Authority
- redaction or retrieval suppression
- unauthorized retrieval blocked by scope or visibility
- stale or superseded record excluded as current truth
- promoted claim with reconstructable provenance lineage
- context assembly respects visibility and propagation rules

The governed memory invariants should include:

- Scope: retrieval and direct lookup must enforce the same visibility and policy constraints.
- Time: stale, superseded, invalidated, and revoked objects must remain inspectable without being treated as current truth.
- Provenance: promoted claims must retain source, writer, time, evidence level, and derivation lineage where applicable.
- Propagation: context assembly must control which memory crosses task, actor, project, or adapter boundaries.
- Resolution: contradictions must remain explicit until reviewed; deduplication must not suppress structural conflicts before contradiction handling.

## Current Candidates

| Candidate | Status | Notes |
| --- | --- | --- |
| Project Memory v0 contract | Candidate | Should define object contracts, governed memory invariants, lifecycle transitions, relationship types, and evidence-level handling before code. |
| Decision Record format | Candidate | Useful once the Project Memory prototype needs durable Decision fixtures. |
| Evidence Artifact format | Candidate | Useful once the Project Memory prototype needs traceability fixtures. |
| Golden fixture suite | Candidate | Should be the proof harness for decisions, assumptions, contradictions, staleness, source mapping, provider invocation, capability, authority, and redaction behavior. |
| Canonical Markdown generation rules | Candidate | Useful after object model and provenance are proven locally. |
| Mock Cursor/Codex/OpenAI adapter contract | Done | Implemented as deterministic adapter twins for Cursor CLI, Codex CLI, Cursor SDK, OpenAI SDK, and OpenAI Agents SDK. |
| Context assembly v0 | Candidate | Should prove task-specific context packaging from Decisions, Evidence, Assumptions, Questions, and stale or contradictory records. |
| Capture/review/promotion flow | Candidate | Needed so raw conversation, notes, and model output do not silently become durable memory. |
| Persistence guardrails | Candidate | Should keep storage portable, IDs deterministic, fixtures stable, and migration/rewrite behavior explicit before database selection. |
| Governed memory invariant tests | Candidate | Should verify scope, temporal supersession, provenance lineage, controlled propagation, contradiction resolution, and equivalent enforcement across retrieval paths. |
| CLI command model | Done | Implemented as `python3 -m soane.project_memory.cli` with validate, fixture-test, context-build, export-markdown, and inspect commands. |
| TUI navigation model | Done | Implemented as `python3 -m soane.project_memory.tui` with deterministic screens over the existing memory, context, fixture, and CLI primitives. |
| Project Memory validation closeout | Done | Validation report records VC-001 through VC-016 evidence, residual risks, budget variance, and readiness for Thinking Engine architecture. |
| Thinking Engine architecture | Next | Next major architecture document after Project Memory v0 validation. |
| Workspace Shell architecture | Candidate | Defer until Project Memory and Thinking Engine shape are stable enough to drive UI. |

## Process Guidance

Use Factory V2 for bounded planning before implementation.

Do not use Factory V2 as a reason to delay small documentation maintenance that is already clear and low-risk.

Do not move Factory V3 work into this repository. Factory V3 remains a separate mission-governance repository.

In this roadmap, Factory V2 means the starter-kit process. Factory V3 means the separate newer repository and is not scaffolded here.

The next Factory V2 planning run should consume `docs/PROJECT_MEMORY_ARCHITECTURE.md` and produce the first implementation plan for a local Project Memory object-model prototype.

Define the Project Memory v0 contract before implementation. The CLI should wrap the contract; it should not become the accidental architecture.

Treat recent governed shared memory research as supporting evidence, not product direction. Soane should adopt the relevant invariants: scoped retrieval, temporal supersession, provenance lineage, controlled propagation, and live-measurable failure modes.

Use mock-first adapter proofs for Cursor CLI, Codex CLI, Cursor SDK, OpenAI SDK, and OpenAI Agents SDK as relevant. Prefer CLI-backed coding harness adapters before SDK-backed integrations because CLIs are observable, scriptable, and fit the headless CLI/TUI proof path. Live CLI or SDK integration should wait until Provider Invocation, Capability Reference, evidence, and trace semantics are stable enough to test deterministically.

Use a headless CLI before a TUI, and use the TUI before a web or product shell. The CLI should prove the command model. The TUI should improve navigation without creating a separate product surface.

Do not start the product shell before Project Memory has at least a local object-model prototype and CLI/TUI proof path. The Workspace experience should be built around memory and thinking primitives, not around a generic app shell.
