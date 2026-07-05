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
| Brownfield multi-repo coding proof planning | Done | `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/` |
| Brownfield multi-repo coding proof implementation | Done | `soane/thinking_engine/coding_harness.py`, `soane/thinking_engine/coding_workflow.py`, `tests/fixtures/coding_proof_harness/`, `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/VALIDATION_CLOSEOUT_REPORT.md` |
| Live coding adapter evaluation planning | Done | `docs/Factory/runs/RUN_20260705_0923_live_coding_adapter_eval_plan/` |

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
| 23 | Brownfield multi-repo coding proof planning | Done | Factory V2 `PLANNING_ONLY` pack completed at `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/`; pack-lint passed. |
| 24 | Brownfield multi-repo coding proof implementation | Done | Implemented deterministic multi-repo Brownfield fixtures, system-boundary context, blocked readiness behavior, workflow summaries, candidate-only provider output, and validation closeout. |
| 25 | Live coding adapter evaluation planning | Done | Factory V2 `PLANNING_ONLY` pack completed at `docs/Factory/runs/RUN_20260705_0923_live_coding_adapter_eval_plan/`; pack-lint passed. |
| 26 | Live coding adapter evaluation implementation | Next | Build deterministic, source-backed adapter profiles, scoring, and CLI evaluation output for Codex CLI, Cursor CLI, Cursor SDK, OpenAI SDK, and OpenAI Agents SDK. No live provider calls, credential reads, dependency installs, or repository mutation. |
| 27 | First live read-only coding proof | Pending | Run only after `LCAE-V0-001` selects a first surface and a separate human-approved live-proof pack defines auth, sandbox, read-only scope, output capture, evidence capture, and rollback/stop rules. |
| 28 | Second domain proof selection | Pending | Select a non-coding proof domain so Workspace primitives are not overfit to software repositories. Candidate domains include research, digital marketing, operations, consulting, or product strategy. |
| 29 | Memory provider evaluation | Pending | Evaluate Supermemory-style providers as external retrieval/context adapters, not canonical Project Memory. |
| 30 | Project Memory persistence architecture | Pending | Define persistence after workflow, provider, and live-proof evidence clarifies which objects and transitions must be durable. |
| 31 | Workspace Shell architecture | Pending | Define desktop, web, mobile, voice, collaboration, dashboards, notifications, mission monitoring, and portfolio views after workflow, integration, memory, and second-domain boundaries are clearer. |
| 32 | First product surface prototype | Pending | Build only after Project Memory, CLI/TUI navigation, Thinking Engine primitives, coding workflow, adapter evaluation, and shell architecture are coherent enough to support a real workflow. |

## Decision Gates

| Gate | Unlocks | Required Evidence |
| --- | --- | --- |
| Deterministic adapter evaluation gate | First live read-only coding proof | `LCAE-V0-001` implementation passes tests, recommends a first live surface, records blocked alternatives, and proves no live calls, credential reads, dependency installs, or repository mutation. |
| Live coding proof gate | Broader coding adapter work | Separate Factory pack authorizes live use, repository scope is read-only unless explicitly approved otherwise, sandbox and approval policy are recorded, output and trace capture are deterministic enough for review, and Provider Invocation records remain candidate-only until reviewed. |
| Second domain gate | Workspace generalization beyond coding | A non-coding proof domain is selected with concrete context sources, authority rules, evidence types, and expected outputs. The proof must show that Project Memory and Thinking Engine primitives are domain-general. |
| Persistence gate | Project Memory persistence architecture | Local memory semantics, context assembly, candidate review, adapter invocation records, provider evaluation, and at least one live-proof path reveal which objects and transitions need durable storage. |
| Shell gate | Workspace Shell architecture | CLI/TUI workflow, memory boundaries, thinking workflow, adapter strategy, live-proof evidence, and second-domain requirements are stable enough to design a human-facing shell around real workflows. |

## Immediate Next Move

Proceed only after human Go/No-go with:

`LCAE-V0-001` Live Coding Adapter Evaluation implementation

Recent implementation evidence:

- `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/VALIDATION_CLOSEOUT_REPORT.md`
- `docs/Factory/runs/RUN_20260705_0923_live_coding_adapter_eval_plan/`

Current state:

- Brownfield multi-repo coding proof: implemented and passed validation closeout.
- Live coding adapter evaluation planning: complete and pack-lint passed.
- Next work: implement deterministic evaluation profiles, scoring, recommendation output, blocked cases, and a thin CLI wrapper for the five candidate surfaces before any live provider invocation.

The completed Brownfield multi-repo coding proof implementation proves deterministic multi-repository Brownfield fixtures, repository maps, in-scope and out-of-scope repositories, service boundaries, integration contracts, ownership, build/test responsibility, authority path, blocked readiness, workflow summaries, and candidate review behavior without live providers or real repository access.

The completed live coding adapter evaluation plan keeps the next implementation bounded to evidence-backed profile generation. It must not call live Codex, Cursor, OpenAI, SDK, CLI, cloud-agent, credential, or dependency-install surfaces.

## Backlog Notes

These notes are not the immediate next move. They are retained because they remain useful constraints for future Project Memory, persistence, and non-coding proof work.

The governed memory invariants should include:

- Scope: retrieval and direct lookup must enforce the same visibility and policy constraints.
- Time: stale, superseded, invalidated, and revoked objects must remain inspectable without being treated as current truth.
- Provenance: promoted claims must retain source, writer, time, evidence level, and derivation lineage where applicable.
- Propagation: context assembly must control which memory crosses task, actor, project, or adapter boundaries.
- Resolution: contradictions must remain explicit until reviewed; deduplication must not suppress structural conflicts before contradiction handling.

Future fixture expansion should continue to cover Decision linked to Evidence, Assumption superseded by Evidence, contradiction between sources, stale Evidence, canonical Markdown source mapping, Provider Invocation through adapter twins, Capability without Authority, retrieval suppression, unauthorized retrieval blocked by scope or visibility, stale records excluded as current truth, promoted claims with reconstructable provenance lineage, and context assembly respecting visibility and propagation rules.

## Current Candidates

| Candidate | Status | Notes |
| --- | --- | --- |
| Project Memory v0 contract | Done | Object contracts, lifecycle transitions, relationship types, evidence levels, governed memory invariants, deterministic fixture IDs, and validation tests exist. |
| Decision Record format | Pending | Should become durable when persistence architecture clarifies storage, migration, and source-of-truth rules. |
| Evidence Artifact format | Pending | Should become durable when persistence architecture clarifies storage, traceability, and retrieval rules. |
| Golden fixture suite | Done | Current fixture corpus covers core v0 memory, context, review, adapter twin, intake, discovery, and coding workflow behavior; future expansion remains expected. |
| Canonical Markdown generation rules | Partial | Source mapping exists in Project Memory v0; durable canonical generation rules should wait for persistence architecture. |
| Mock Cursor/Codex/OpenAI adapter contract | Done | Implemented as deterministic adapter twins for Cursor CLI, Codex CLI, Cursor SDK, OpenAI SDK, and OpenAI Agents SDK. |
| Context assembly v0 | Done | Implemented task-specific context packaging with source maps and lifecycle-aware memory selection. |
| Capture/review/promotion flow | Done | Candidate Review and Promotion v0 prevents raw conversation, notes, and model output from silently becoming accepted Project Memory truth. |
| Persistence guardrails | Pending | Should keep storage portable, IDs deterministic, fixtures stable, and migration/rewrite behavior explicit before database selection. |
| Governed memory invariant tests | Done | Current tests cover scope, temporal supersession, provenance preservation, controlled propagation, contradiction representation, and retrieval/current-truth behavior at v0 scale. |
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
| Brownfield multi-repo coding proof planning | Done | `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/` defines `BMR-CPH-V0-001`. |
| Brownfield multi-repo coding proof implementation | Done | Implemented deterministic multi-repo Brownfield fixtures, local system-boundary context, workflow summaries, blocked readiness behavior, and validation closeout. |
| Live coding adapter evaluation planning | Done | `docs/Factory/runs/RUN_20260705_0923_live_coding_adapter_eval_plan/` defines `LCAE-V0-001`. |
| Live coding adapter evaluation implementation | Next | Implement deterministic adapter profiles, scoring, recommendation output, blocked cases, and CLI evaluation output without live provider calls. |
| First live read-only coding proof | Pending | Requires a separate human-approved live-proof pack after deterministic adapter evaluation selects a first surface. |
| Second domain proof | Pending | Should prevent Soane from becoming coding-only by proving the same primitives on a non-coding workflow. |
| Memory provider evaluation | Candidate | Evaluate Supermemory-style providers as external retrieval/context adapters before persistence choices. |
| Project Memory persistence architecture | Candidate | Defer until workflow and provider evidence clarifies durable storage requirements. |
| Workspace Shell architecture | Candidate | Defer until workflow and integration boundaries are clearer. |

## Process Guidance

Use Factory V2 for bounded planning before implementation.

Do not use Factory V2 as a reason to delay small documentation maintenance that is already clear and low-risk.

Do not move Factory V3 work into this repository. Factory V3 remains a separate mission-governance repository.

In this roadmap, Factory V2 means the starter-kit process. Factory V3 means the separate newer repository and is not scaffolded here.

The next implementation run should consume `docs/Factory/runs/RUN_20260705_0923_live_coding_adapter_eval_plan/` after explicit human Go. It should evaluate live coding adapter surfaces through deterministic local profiles before any live provider invocation is introduced.

Define the Project Memory v0 contract before implementation. The CLI should wrap the contract; it should not become the accidental architecture.

Treat recent governed shared memory research as supporting evidence, not product direction. Soane should adopt the relevant invariants: scoped retrieval, temporal supersession, provenance lineage, controlled propagation, and live-measurable failure modes.

Use mock-first adapter proofs for Cursor CLI, Codex CLI, Cursor SDK, OpenAI SDK, and OpenAI Agents SDK as relevant. Prefer CLI-backed coding harness adapters before SDK-backed integrations because CLIs are observable, scriptable, and fit the headless CLI/TUI proof path. Live CLI or SDK integration should wait until Provider Invocation, Capability Reference, evidence, and trace semantics are stable enough to test deterministically.

Use a headless CLI before a TUI, and use the TUI before a web or product shell. The CLI should prove the command model. The TUI should improve navigation without creating a separate product surface.

Do not start the product shell before Project Memory has at least a local object-model prototype and CLI/TUI proof path. The Workspace experience should be built around memory and thinking primitives, not around a generic app shell.
