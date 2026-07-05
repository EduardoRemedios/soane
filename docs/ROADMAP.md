# Roadmap

> Purpose: Track near-term Soane repository work.
>
> Last updated: 2026-07-05

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
| Thinking Engine architecture | Done | `docs/THINKING_ENGINE_ARCHITECTURE.md` |
| Thinking Engine Intake v0 | Done | `soane/thinking_engine/intake.py`, `tests/test_thinking_engine_intake.py`, `docs/Factory/runs/RUN_20260701_1438_thinking_engine_intake_v0_plan/VALIDATION_CLOSEOUT_REPORT.md` |
| Candidate Review and Promotion planning | Done | `docs/Factory/runs/RUN_20260701_1455_candidate_review_promotion_v0_plan/` |
| Candidate Review and Promotion v0 | Done | `soane/project_memory/review.py`, `tests/test_project_memory_review.py`, `docs/Factory/runs/RUN_20260701_1455_candidate_review_promotion_v0_plan/VALIDATION_CLOSEOUT_REPORT.md` |
| Socratic Discovery planning | Done | `docs/Factory/runs/RUN_20260701_1529_socratic_discovery_v0_plan/` |
| Socratic Discovery v0 | Done | `soane/thinking_engine/discovery.py`, `tests/test_thinking_engine_discovery.py`, `docs/Factory/runs/RUN_20260701_1529_socratic_discovery_v0_plan/VALIDATION_CLOSEOUT_REPORT.md` |
| Coding Proof Harness planning | Done | `docs/Factory/runs/RUN_20260701_1548_coding_proof_harness_v0_plan/` |
| Coding Proof Harness v0 | Done | `soane/thinking_engine/coding_harness.py`, `tests/test_thinking_engine_coding_harness.py`, `docs/Factory/runs/RUN_20260701_1548_coding_proof_harness_v0_plan/VALIDATION_CLOSEOUT_REPORT.md` |
| Roadmap sequencing review | Done | `docs/Factory/runs/RUN_20260701_1604_roadmap_sequence_review/pack/ROADMAP_SEQUENCE_REVIEW.md` |
| Coding Harness Workflow planning | Done | `docs/Factory/runs/RUN_20260702_0617_coding_harness_workflow_v0_plan/` |
| Coding Harness Workflow v0 | Done | `soane/thinking_engine/coding_workflow.py`, `tests/test_thinking_engine_coding_workflow.py`, `docs/Factory/runs/RUN_20260702_0617_coding_harness_workflow_v0_plan/VALIDATION_CLOSEOUT_REPORT.md` |
| Factory V2 direct-source recall repair refresh | Done | `docs/Factory/ORCHESTRATION.md`, `docs/Factory/Spec/STAGE_CONTRACTS.md`, `docs/Factory/templates/CONTEXT_RECALL_REPORT_TEMPLATE.md`, `scripts/factory_pack_lint.py`, `scripts/factory_stage_lint.py`, `tests/test_context_recall_repair.py` |

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
| 8 | Thinking Engine architecture | Done | Defined discovery, Thinking, Socratic dialogue, hypotheses, inference strategies, Discovery Playbooks, Greenfield/Brownfield project intake, non-repository context sources, and readiness assessment. |
| 9 | Thinking Engine planning run | Done | Factory V2 `PLANNING_ONLY` pack completed at `docs/Factory/runs/RUN_20260701_1438_thinking_engine_intake_v0_plan/`; pack-lint passed. |
| 10 | Thinking Engine Intake v0 implementation | Done | Implemented local deterministic intake classification, Context Baseline, Discovery Playbook selection, Readiness Assessment, and Project Memory write-back candidates. No live integrations, database, or product shell were introduced. |
| 11 | Thinking Engine Intake v0 review | Done | Review selected Candidate Review and Promotion as the next bounded slice because Intake v0 emits candidates that must not silently become accepted Project Memory truth. |
| 12 | Candidate Review and Promotion planning run | Done | Factory V2 `PLANNING_ONLY` pack completed at `docs/Factory/runs/RUN_20260701_1455_candidate_review_promotion_v0_plan/`; pack-lint passed. |
| 13 | Candidate Review and Promotion v0 implementation | Done | Implemented local deterministic review decisions, provenance retention, promotion semantics, current-truth separation, negative fixtures, thin CLI wrapper, and validation closeout. |
| 14 | Socratic Discovery planning run | Done | Factory V2 `PLANNING_ONLY` pack completed at `docs/Factory/runs/RUN_20260701_1529_socratic_discovery_v0_plan/`; pack-lint passed. |
| 15 | Socratic Discovery v0 implementation | Done | Implemented deterministic discovery sessions, traceable question generation, candidate answer capture, uncertainty-preserving candidate hypotheses, stop conditions, and validation closeout. Optional wrapper was skipped. |
| 16 | Next bounded slice selection | Done | Selected Coding Proof Harness v0 before Workspace Shell architecture, so Soane has one end-to-end workflow to design around. |
| 17 | Coding Proof Harness planning run | Done | Factory V2 `PLANNING_ONLY` pack completed at `docs/Factory/runs/RUN_20260701_1548_coding_proof_harness_v0_plan/`; pack-lint passed. |
| 18 | Coding Proof Harness v0 implementation | Done | Implemented Greenfield/Brownfield coding fixtures, service composition, mocked provider invocation, candidate output capture, review-gated promotion, and validation closeout. Optional wrapper was skipped. |
| 19 | Roadmap sequencing review | Done | `ROADMAP-SEQ-001` selected a CLI-first workflow wrapper before Workspace Shell architecture. |
| 20 | Coding Harness Workflow v0 planning | Done | Factory V2 `PLANNING_ONLY` pack completed at `docs/Factory/runs/RUN_20260702_0617_coding_harness_workflow_v0_plan/`; pack-lint passed. |
| 21 | Coding Harness Workflow v0 implementation | Done | Implemented CLI-first fixture listing and execution, text and JSON summaries, candidate/review status, blocked Brownfield summary, and validation closeout. Optional TUI was skipped. |
| 22 | Factory V2 direct-source recall repair refresh | Done | Refreshed embedded Factory V2 scaffold from the starter kit so upcoming context-heavy runs can repair generated `WEAK` recall only through direct local source evidence. |
| 23 | Brownfield multi-repo coding proof | Next | Extend the coding proof to multi-repository system boundaries before product shell design hides Brownfield complexity. |
| 24 | Live coding adapter evaluation plan | Pending | Evaluate Codex CLI, Cursor CLI, Cursor SDK, OpenAI SDK, and OpenAI Agents SDK against invocation, authority, evidence, and no-mutation requirements before live use. |
| 25 | Memory provider evaluation | Pending | Evaluate Supermemory-style providers as external retrieval/context adapters, not canonical Project Memory. |
| 26 | Project Memory persistence architecture | Pending | Define persistence after workflow and provider evidence clarifies which objects and transitions must be durable. |
| 27 | Workspace Shell architecture | Pending | Define desktop, web, mobile, voice, collaboration, dashboards, notifications, mission monitoring, and portfolio views after the workflow and integration boundaries are clearer. |
| 28 | First product surface prototype | Pending | Build only after Project Memory, CLI/TUI navigation, Thinking Engine primitives, coding workflow, and shell architecture are coherent enough to support a real workflow. |

## Immediate Next Move

Continue with Factory planning for:

Brownfield multi-repo coding proof

Recent implementation pack path:

- `docs/Factory/runs/RUN_20260702_0617_coding_harness_workflow_v0_plan/`

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
- Thinking Engine architecture: complete.
- Thinking Engine planning run: complete.
- Thinking Engine Intake v0 implementation: complete.
- Thinking Engine Intake v0 proof review: complete.
- Candidate Review and Promotion planning run: complete and passed.
- Candidate Review and Promotion v0 implementation: complete.
- Socratic Discovery planning run: complete and passed.
- Socratic Discovery v0 implementation: complete and passed validation closeout.
- Coding Proof Harness planning run: complete and passed.
- Coding Proof Harness v0 implementation: complete and passed validation closeout.
- Roadmap sequencing review: complete and passed.
- Coding Harness Workflow v0 planning run: complete and passed.
- Coding Harness Workflow v0 implementation: complete and passed validation closeout.
- Factory V2 direct-source recall repair refresh: complete.
- Next work: create a Factory planning pack for the Brownfield multi-repo coding proof.

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

The completed Thinking Engine architecture builds on the validated Project Memory v0 proof and clarifies discovery, Thinking, Socratic dialogue, hypotheses, inference strategies, Discovery Playbooks, readiness assessment, and the boundary between thinking support and mission execution.

The Thinking Engine architecture must treat Greenfield and Brownfield project intake as different starting conditions:

- Greenfield projects start by creating the initial project context, canonical docs, assumptions, constraints, and working agreements before feature work begins.
- Brownfield coding projects start with a repo/workspace audit before feature work begins, including existing application structure, build/test commands, architecture documentation, dependency and integration context, known risks, missing docs, and current decision/evidence gaps.
- Brownfield systems may span multiple repositories rather than one monorepo. Intake must identify the system boundary, repository map, ownership, integration points, deployment surfaces, shared documentation, and where decisions/evidence currently live.
- Non-coding projects may have critical context outside repositories entirely. Intake must support external context sources such as analytics dashboards, campaign assets, research notes, briefs, spreadsheets, design files, CRM records, ad accounts, and other operational artifacts.
- Both paths must verify that the minimum context files, Markdown documents, or equivalent source artifacts exist before Soane agrees a starting point or delegates work.

The completed Thinking Engine planning run produced `TEI-V0-001`, a bounded implementation plan for Thinking Engine Intake v0.

The completed Thinking Engine Intake v0 implementation proves the local service layer for intake category classification, Context Baseline construction, Discovery Playbook selection, Readiness Assessment, and Project Memory candidate output. Do not extend this proof into live adapters, database selection, or a broader Workspace product shell without a new bounded plan.

The completed Candidate Review and Promotion planning run defines `CRP-V0-001`, the next bounded slice. It should close the gap between candidate output and accepted Project Memory truth before Socratic discovery or Workspace Shell work proceeds.

The completed Candidate Review and Promotion v0 implementation closes that gap locally by requiring explicit review decisions, preserving provenance and lineage, keeping candidate and non-current records out of current truth, preserving the authority boundary, and exposing a thin CLI wrapper over the shared service.

The completed Socratic Discovery planning run defines `SD-V0-001`, the next bounded Thinking Engine slice. It should prove the local guided discovery loop before Workspace Shell architecture or live model integrations proceed.

The completed Socratic Discovery v0 implementation proves the local guided discovery loop with deterministic sessions, traceable questions, Project Memory candidate answers, uncertainty-preserving candidate hypotheses, and stop conditions. It does not introduce live models, live adapters, persistence, product UI, Workspace Shell, or mission execution.

The completed Coding Proof Harness planning run defines `CPH-V0-001`, the next bounded proof slice. It should prove a coding workflow by composing existing Intake, Socratic Discovery, Project Memory context assembly, adapter-twin Provider Invocation records, candidate output capture, and Candidate Review and Promotion. It remains mock-first and does not introduce live providers, repository mutation, persistence, product UI, Workspace Shell, or mission execution.

The completed Coding Proof Harness v0 implementation proves that end-to-end path locally with Greenfield and Brownfield coding fixtures, task-specific context assembly, mocked provider selection, Provider Invocation records, candidate output capture, and review-gated promotion. It does not introduce live providers, repository mutation, persistence, product UI, Workspace Shell, or mission execution.

The completed roadmap sequencing review records that the next immediate slice should be a CLI-first workflow wrapper over the coding harness before Workspace Shell architecture. The recommended sequence after that is Brownfield multi-repo proof, live coding adapter evaluation planning, memory-provider evaluation, Project Memory persistence architecture, Workspace Shell architecture, and then first product surface prototype.

The completed Coding Harness Workflow v0 planning run defines `CHW-V0-001`, a bounded implementation slice for a thin CLI-first workflow wrapper over `soane.thinking_engine.coding_harness`. It should make the coding proof easier to navigate by listing fixtures, running selected scenarios, summarizing intake, discovery, context package, mocked provider invocation, candidate output, and review status, and optionally emitting JSON. It must not introduce live providers, repository mutation, persistence, product UI, Workspace Shell, or mission execution.

The completed Coding Harness Workflow v0 implementation provides `python3 -m soane.thinking_engine.coding_workflow` with fixture listing, fixture execution, readable text summaries, JSON summaries, explicit optional candidate review, blocked Brownfield summaries, and no live provider or repository side effects. It is the operator surface for inspecting the coding proof before multi-repo Brownfield expansion.

The completed Factory V2 direct-source recall repair refresh imports the starter-kit repair path into Soane's embedded scaffold. Generated `WEAK` Stage A recall remains blocking unless a direct-source repair addendum records concrete local files read, source summaries, remaining unresolved refs, materiality check, and `Final Repaired Verdict: REPAIRED_DIRECT_SOURCE_CHECK`.

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
| Thinking Engine architecture | Done | `docs/THINKING_ENGINE_ARCHITECTURE.md` defines intake, discovery, Socratic dialogue, hypotheses, evidence review, synthesis, inference strategy, readiness states, and boundaries. |
| Thinking Engine planning run | Done | `docs/Factory/runs/RUN_20260701_1438_thinking_engine_intake_v0_plan/` defines `TEI-V0-001`. |
| Thinking Engine Intake v0 implementation | Done | Implemented local deterministic intake classification, Context Baseline, Discovery Playbook selection, Readiness Assessment, and Project Memory write-back candidates. |
| Candidate Review and Promotion planning run | Done | `docs/Factory/runs/RUN_20260701_1455_candidate_review_promotion_v0_plan/` defines `CRP-V0-001`. |
| Candidate Review and Promotion v0 implementation | Done | Implemented local deterministic review decisions, promotion semantics, provenance retention, current-truth separation, negative fixtures, thin CLI wrapper, and validation closeout. |
| Socratic Discovery planning run | Done | `docs/Factory/runs/RUN_20260701_1529_socratic_discovery_v0_plan/` defines `SD-V0-001`. |
| Socratic Discovery v0 implementation | Done | Implemented local deterministic discovery sessions, traceable question generation, candidate answer capture, candidate hypotheses with uncertainty state and evidence-gap links, stop conditions, tests, and validation closeout. |
| Coding Proof Harness planning run | Done | `docs/Factory/runs/RUN_20260701_1548_coding_proof_harness_v0_plan/` defines `CPH-V0-001`. |
| Coding Proof Harness v0 implementation | Done | Implemented local deterministic Greenfield/Brownfield coding proof, service composition, mocked provider invocation, candidate output capture, review-gated promotion, tests, and validation closeout. |
| Roadmap sequencing review | Done | `docs/Factory/runs/RUN_20260701_1604_roadmap_sequence_review/` selects a CLI-first workflow wrapper before Workspace Shell architecture. |
| Coding Harness Workflow v0 planning | Done | `docs/Factory/runs/RUN_20260702_0617_coding_harness_workflow_v0_plan/` defines `CHW-V0-001`. |
| Coding Harness Workflow v0 implementation | Done | Implemented `python3 -m soane.thinking_engine.coding_workflow` with service-delegating fixture list/run commands and validation closeout. |
| Factory V2 direct-source recall repair refresh | Done | Embedded Factory V2 scaffold now supports validated direct-source repair for generated `WEAK` Stage A context recall reports. |
| Brownfield multi-repo coding proof | Next | Add before product shell design so system-boundary complexity is explicit. |
| Live coding adapter evaluation plan | Candidate | Evaluate live Codex/Cursor/OpenAI surfaces before any live provider invocation is introduced. |
| Memory provider evaluation | Candidate | Evaluate Supermemory-style providers as external retrieval/context adapters before persistence choices. |
| Project Memory persistence architecture | Candidate | Defer until workflow and provider evidence clarifies durable storage requirements. |
| Workspace Shell architecture | Candidate | Defer until workflow and integration boundaries are clearer. |

## Process Guidance

Use Factory V2 for bounded planning before implementation.

Do not use Factory V2 as a reason to delay small documentation maintenance that is already clear and low-risk.

Do not move Factory V3 work into this repository. Factory V3 remains a separate mission-governance repository.

In this roadmap, Factory V2 means the starter-kit process. Factory V3 means the separate newer repository and is not scaffolded here.

The next Factory V2 planning run should produce the Brownfield multi-repo coding proof plan and consume `docs/PROJECT_MEMORY_ARCHITECTURE.md`, `docs/THINKING_ENGINE_ARCHITECTURE.md`, the Coding Proof Harness v0 evidence, the Coding Harness Workflow v0 evidence, and the refreshed direct-source recall repair rules.

Define the Project Memory v0 contract before implementation. The CLI should wrap the contract; it should not become the accidental architecture.

Treat recent governed shared memory research as supporting evidence, not product direction. Soane should adopt the relevant invariants: scoped retrieval, temporal supersession, provenance lineage, controlled propagation, and live-measurable failure modes.

Use mock-first adapter proofs for Cursor CLI, Codex CLI, Cursor SDK, OpenAI SDK, and OpenAI Agents SDK as relevant. Prefer CLI-backed coding harness adapters before SDK-backed integrations because CLIs are observable, scriptable, and fit the headless CLI/TUI proof path. Live CLI or SDK integration should wait until Provider Invocation, Capability Reference, evidence, and trace semantics are stable enough to test deterministically.

Use a headless CLI before a TUI, and use the TUI before a web or product shell. The CLI should prove the command model. The TUI should improve navigation without creating a separate product surface.

Do not start the product shell before Project Memory has at least a local object-model prototype and CLI/TUI proof path. The Workspace experience should be built around memory and thinking primitives, not around a generic app shell.
