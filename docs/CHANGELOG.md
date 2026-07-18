# Changelog

## 2026-07-18

- Recorded human Go and implemented `GCT-V0-001` with a shared storage-neutral traversal service, typed inbound/outbound shortest paths, per-hop visibility, explicit non-current inclusion, deterministic cycle and alternate-path handling, and hard depth/object/path/edge/output ceilings.
- Integrated graph traversal into `agent-context`, added bounded controls and additive graph output to `agent-trace`, and added exact-source direct/propagated explanations to `agent-affected` without persistence, inferred edges, code graphs, new relationship types, or memory mutation.
- Added realistic proposed/asserted Claim, hidden-bridge, direction, lifecycle, cycle, alternate-path, exclusion-taxonomy, budget, CLI compatibility, and unmatched-source coverage; 30 focused tests and 153 full repository tests passed before closeout.
- Added planning-only Factory run `RUN_20260718_0721_graph_aware_context_trace_plan` for `GCT-V0-001`; Stage A through I2 and final pack lint passed.
- Locked a storage-neutral two-hop traversal contract with typed inbound/outbound paths, per-hop visibility, explicit non-current inclusion, deterministic cycle and alternate-path handling, hard object/path/edge/output ceilings, and opaque exclusions.
- Planned shared integration with `agent-context`, `agent-trace`, and `agent-affected`, including a fixed MMI-style proposed Claim graph and no expansion into persistence, inferred edges, code graphs, new relationship types, external providers, UI, or automatic truth mutation.

## 2026-07-12

- Recorded human Go and implemented `MMI-V0-001` with proposed/asserted Claim validation, shared Markdown role and authority-mode vocabulary, repository-contained canonical prose ingestion, exact anchors and fingerprints, bounded candidate/snapshot/exclusion output, observational source comparison, fail-closed duplicate lineage, review-compatible JSON interchange, and `ingest-markdown`/`compare-markdown` CLI commands.
- Added fixed real-source and adversarial ingestion fixtures plus path, parser, identity, comparison, review, agent-context, and CLI coverage; 58 focused tests and 141 full repository tests passed before closeout.
- Added planning-only Factory run `RUN_20260712_1030_markdown_memory_ingestion_v0_plan` for `MMI-V0-001`; Stage A direct-source repair, Stage A through I2, and final pack lint passed with a bounded Claim contract, path-safe prose extraction, deterministic source comparison, review-only promotion, CLI, and regression envelope.
- Hardened the Workspace vision and epistemic model: Project Memory now records governed current understanding without superseding source-system authority; Claim and fact-status semantics, Decision Review, bounded Delegation, Knowledge Scope, memory rights, Markdown authority modes, decision framing, and outcome-oriented success measures are canonical doctrine.
- Added Factory run `RUN_20260712_1011_vision_epistemic_hardening` for `VEH-V1-001`; Stage A through I2, final pack lint, knowledge lint, context refresh, and all 126 repository tests passed through execution closeout.
- Kept runtime Claim, Decision Review, Knowledge Scope, Delegation, and Markdown round-trip representation explicitly deferred, and updated `MMI-V0-001` to consume the new doctrine during candidate-ingestion planning.
- Reconciled canonical document status, repository test guidance, Project Memory and Thinking Engine implementation history, and resolved architecture questions after a canonical-doc freshness review.
- Recorded the governed amendment that aligns the canonical-document registry with current architecture and repository-context records.
- Reordered the immediate roadmap around `ACR-V1-001` Agent Context Relevance and Fail-Closed Assembly after realistic task queries exposed brittle all-term recall, all-visible-memory fallback on empty seeds, and an unproven concurrent refresh contract.
- Retained the passed `LCAE-V0-001` planning pack behind the agent-context correctness gate, followed by Markdown-to-memory candidate ingestion and graph-aware context traversal before persistence architecture.
- Added `RUN_20260712_0909_agent_context_relevance_v1_plan`, a planning-only Factory pack for `ACR-V1-001`; Stage A through I2 and final pack lint passed with bounded query, zero-match, traversal, refresh, and regression verification contracts.
- Superseded the repo-local Project Memory decision that named `LCAE-V0-001` as the immediate gate and added the accepted agent-context correctness decision with Factory evidence and source derivation refs.
- Recorded human Go and implemented `ACR-V1-001` with bounded natural-task query planning, query-specificity and document-role ranking, separate document/memory budgets, fail-closed zero matches, explicit lower-level selection modes, one-hop allowlisted relationship expansion, current-before-non-current memory selection, source freshness, and explicit selection/refresh output states.
- Made Factory context-index rebuilds concurrency-safe through a SQLite-owned writer lock and one rollback-safe transaction; concurrent readers retain the previous valid snapshot until successful commit.
- Added `tests/test_factory_context_index_atomic.py` and expanded agent/context tests; 29 focused tests and 126 full repository tests passed at validation closeout.

## 2026-07-09

- Implemented an agent-facing Project Memory context slice with `soane/project_memory/agent_context.py`, bridging Factory context-index document recall with Project Memory provenance refs and Markdown role classification.
- Added `python3 -m soane.project_memory.cli agent-context`, `agent-trace`, and `agent-affected` commands so agents can request small explained bundles, trace memory object relationships, and find memory objects tied to a source path before rereading broad repo context.
- Added real Project Memory JSON input support with `--memory-file`, `--memory-dir`, and `--no-fixtures`, plus a repo-local reviewed seed corpus at `docs/project_memory/objects/` for agent-facing commands.
- Expanded the Factory context index default source patterns to include top-level `docs/*.md`, so constitutional and canonical docs can participate in agent context recall.
- Added `tests/test_project_memory_agent_context.py` covering Markdown role mapping, context-index to Project Memory ref bridging, and the new agent-facing CLI commands.
- Formalized Markdown role vocabulary in `docs/GOVERNANCE_MODEL.md` so constitutional, canonical, working, generated, evidence, and deprecated Markdown have explicit context semantics.

## 2026-07-05

- Refreshed Soane's embedded Factory V2 scaffold from `/Users/eduardodosremedios/factory-starter-kit` with the direct-source recall repair path for generated `WEAK` Stage A context recall reports, including docs, template, lint support, knowledge lint coverage, and `tests/test_context_recall_repair.py`.
- Added Factory V2 planning-only pack `RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan` for `BMR-CPH-V0-001`, the Brownfield multi-repo coding proof slice.
- Implemented `BMR-CPH-V0-001` Brownfield Multi-Repo Coding Proof with ready and blocked multi-repo fixtures, local system-boundary context, task-relevant versus out-of-scope repository summaries, blocked readiness behavior, workflow JSON/text summaries, candidate-only provider output, and validation closeout.
- Added Factory V2 planning-only pack `RUN_20260705_0923_live_coding_adapter_eval_plan` for `LCAE-V0-001`, the live coding adapter evaluation plan covering Codex CLI, Cursor CLI, Cursor SDK, OpenAI SDK, and OpenAI Agents SDK before any live provider invocation.
- Cleaned up `docs/ROADMAP.md` to separate the immediate `LCAE-V0-001` implementation step from backlog memory notes, add explicit decision gates, and add first live read-only coding proof plus second non-coding domain proof to the medium-term sequence.

## 2026-07-02

- Added Factory V2 planning-only pack `RUN_20260702_0617_coding_harness_workflow_v0_plan` for `CHW-V0-001`, a CLI-first Coding Harness Workflow v0 wrapper over the existing coding proof harness.
- Implemented `CHW-V0-001` Coding Harness Workflow v0 with service-delegating fixture list/run commands, text and JSON summaries, explicit optional candidate review, blocked Brownfield summaries, focused tests, and validation closeout.

## 2026-07-01

- Added governed memory invariants to the Project Memory v0 roadmap, informed by the MemClaw governed shared memory paper: scope and visibility, temporal supersession, provenance lineage, controlled propagation, contradiction handling, and equivalent enforcement across retrieval paths.
- Clarified that Cursor CLI and Codex CLI are candidate coding harness adapter surfaces alongside Cursor SDK, OpenAI SDK, and OpenAI Agents SDK, with a preferred mock-first, CLI-backed, then SDK-backed proof order.
- Added Factory V2 planning-only pack `RUN_20260701_0848_project_memory_v0_plan` for the Project Memory v0 object-model prototype, including v0 contract gates, golden fixtures, governed memory invariants, mock adapter proof, CLI/TUI sequencing, and final pack audit.
- Implemented MS-00 Project Memory v0 contract scaffold with object types, lifecycle transitions, relationship types, evidence levels, governed memory invariants, deterministic fixture IDs, and static unit tests.
- Implemented MS-01 Project Memory golden fixture corpus with twelve fixture files, a fixture loader, deterministic ID validation, and fixture conformance tests.
- Implemented MS-02 Project Memory local semantics with lifecycle transitions, provenance preservation, relationship/evidence queries, visibility enforcement, current-truth filtering, suppression handling, and contradiction representation tests.
- Implemented MS-03 Project Memory context assembly and Markdown source mapping with lifecycle-aware context packages, visibility and propagation exclusions, contradiction and stale-record surfacing, and explicit Markdown source maps.
- Implemented MS-04 Project Memory adapter twins for Cursor CLI, Codex CLI, Cursor SDK, OpenAI SDK, and OpenAI Agents SDK, recording deterministic Provider Invocation objects without live CLI or SDK calls.
- Implemented MS-05 Project Memory headless CLI with validate, fixture-test, context-build, export-markdown, and inspect commands over the existing service functions.
- Implemented MS-06 Project Memory thin TUI with deterministic terminal screens for project navigation, memory browsing, evidence, decisions, hypotheses, adapter invocations, validation status, and unresolved questions.
- Completed MS-07 Project Memory validation closeout with VC-001 through VC-016 evidence, residual risks, budget variance notes, and readiness for Thinking Engine architecture.
- Added Greenfield versus Brownfield project intake as a required concern for the upcoming Thinking Engine architecture, including Brownfield repo audit and starting-context readiness before feature delegation.
- Expanded upcoming Thinking Engine intake requirements to cover multi-repository Brownfield systems and non-repository context sources such as analytics dashboards, campaign assets, briefs, spreadsheets, design files, CRM records, ad accounts, and operational artifacts.
- Added `docs/THINKING_ENGINE_ARCHITECTURE.md` to define intake, discovery, Socratic dialogue, hypotheses, evidence review, synthesis, Inference Strategy, readiness assessment, Greenfield/Brownfield handling, non-repository context sources, and implementation boundaries.
- Added Factory V2 planning-only pack `RUN_20260701_1438_thinking_engine_intake_v0_plan` for `TEI-V0-001`, the first Thinking Engine Intake v0 implementation slice.
- Implemented `TEI-V0-001` Thinking Engine Intake v0 with local deterministic intake classification, Context Baseline, Discovery Playbook selection, Readiness Assessment, Project Memory write-back candidates, five intake fixtures, tests, and validation closeout.
- Added Factory V2 planning-only pack `RUN_20260701_1455_candidate_review_promotion_v0_plan` for `CRP-V0-001`, the Candidate Review and Promotion v0 slice that governs how Project Memory candidates become, or do not become, accepted truth.
- Implemented `CRP-V0-001` Candidate Review and Promotion v0 with local deterministic review decisions, provenance retention, amended lineage, authority separation, current-truth filtering for candidate and review states, six review fixtures, tests, and validation closeout.
- Added the optional thin `review-candidate` CLI wrapper over Candidate Review and Promotion v0 service semantics.
- Added Factory V2 planning-only pack `RUN_20260701_1529_socratic_discovery_v0_plan` for `SD-V0-001`, the Socratic Discovery v0 slice for deterministic guided discovery sessions, traceable questions, candidate answers, candidate hypotheses, and stop conditions.
- Implemented `SD-V0-001` Socratic Discovery v0 with local deterministic discovery sessions, traceable question generation, candidate answer capture, uncertainty-preserving candidate hypotheses, stop conditions, tests, and validation closeout.
- Added Factory V2 planning-only pack `RUN_20260701_1548_coding_proof_harness_v0_plan` for `CPH-V0-001`, the Coding Proof Harness v0 slice for a mock-first Greenfield/Brownfield coding workflow using intake, discovery, context assembly, provider invocation records, candidate output capture, and review-gated promotion.
- Implemented `CPH-V0-001` Coding Proof Harness v0 with local deterministic Greenfield/Brownfield coding fixtures, service composition, mocked provider invocation, candidate output capture, review-gated promotion, tests, and validation closeout.
- Added Factory V2 planning-only pack `RUN_20260701_1604_roadmap_sequence_review` for `ROADMAP-SEQ-001`, updating the roadmap sequence to put a CLI-first Coding Harness Workflow before Workspace Shell architecture.

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
