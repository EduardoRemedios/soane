# Project State

> Purpose: Current source of truth for the Soane repository state.
>
> Last updated: 2026-07-12

## Current Identity

Soane is the working codename for the Workspace.

The Workspace is a new product: the primary human-facing environment for governed AI work. It is project-centric. It helps humans think, preserve Project Memory, collaborate, plan, supervise missions, and coordinate neighbouring portfolio systems.

## What Exists

Implementation:

- Project Memory v0 contract scaffold at `soane/project_memory/contract.py`
- Project Memory deterministic adapter twins at `soane/project_memory/adapters.py`
- Project Memory headless CLI at `soane/project_memory/cli.py`
- Project Memory thin TUI at `soane/project_memory/tui.py`
- Project Memory context assembly and Markdown mapping at `soane/project_memory/context.py`
- Project Memory agent-facing context bundle service at `soane/project_memory/agent_context.py`
- Agent context v1 bounded query planning, fail-closed selection states, one-hop relationship expansion, source freshness reporting, and truthful refresh states
- Project Memory repo-local reviewed object seed corpus at `docs/project_memory/objects/`
- Project Memory golden fixture loader at `soane/project_memory/fixtures.py`
- Project Memory local semantics layer at `soane/project_memory/semantics.py`
- Project Memory candidate review and promotion service at `soane/project_memory/review.py`
- Thinking Engine Intake v0 local service at `soane/thinking_engine/intake.py`
- Socratic Discovery v0 local service at `soane/thinking_engine/discovery.py`
- Coding Proof Harness v0 local service at `soane/thinking_engine/coding_harness.py`
- Coding Harness Workflow v0 CLI wrapper at `soane/thinking_engine/coding_workflow.py`
- Project Memory golden fixture corpus at `tests/fixtures/project_memory/golden/`
- Project Memory review fixture corpus at `tests/fixtures/project_memory/review/`
- Thinking Engine Intake v0 fixture corpus at `tests/fixtures/thinking_engine/intake/`
- Coding Proof Harness v0 fixture corpus at `tests/fixtures/coding_proof_harness/`
- static contract tests at `tests/test_project_memory_contract.py`
- adapter twin tests at `tests/test_project_memory_adapter_twins.py`
- headless CLI tests at `tests/test_project_memory_cli.py`
- thin TUI tests at `tests/test_project_memory_tui.py`
- context assembly and Markdown mapping tests at `tests/test_project_memory_context.py`
- agent-facing context bundle tests at `tests/test_project_memory_agent_context.py`
- atomic Factory context-index rebuild tests at `tests/test_factory_context_index_atomic.py`
- golden fixture tests at `tests/test_project_memory_fixtures.py`
- memory semantics tests at `tests/test_project_memory_semantics.py`
- candidate review and promotion tests at `tests/test_project_memory_review.py`
- Thinking Engine Intake v0 tests at `tests/test_thinking_engine_intake.py`
- Socratic Discovery v0 tests at `tests/test_thinking_engine_discovery.py`
- Coding Proof Harness v0 tests at `tests/test_thinking_engine_coding_harness.py`
- Coding Harness Workflow v0 tests at `tests/test_thinking_engine_coding_workflow.py`

Constitutional documents:

- `docs/VISION.md`
- `docs/CORE_CONCEPTS.md`
- `docs/GOVERNANCE_MODEL.md`

Canonical architecture and repository records:

- `docs/PROJECT_MEMORY_ARCHITECTURE.md`
- `docs/THINKING_ENGINE_ARCHITECTURE.md`
- `docs/PORTFOLIO_CONTEXT.md`
- `docs/PORTFOLIO_ASSUMPTIONS.md`
- `docs/INTEGRATION_ARCHITECTURE.md`
- `docs/PROJECT_STATE.md`
- `docs/ROADMAP.md`
- `docs/CHANGELOG.md`
- `AGENTS.md`

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
- `tests/test_context_recall_repair.py`
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

Planning outputs:

- `docs/Factory/runs/RUN_20260701_0848_project_memory_v0_plan/`
- `docs/Factory/runs/RUN_20260701_0848_project_memory_v0_plan/VALIDATION_CLOSEOUT_REPORT.md`
- `docs/Factory/runs/RUN_20260701_1438_thinking_engine_intake_v0_plan/`
- `docs/Factory/runs/RUN_20260701_1438_thinking_engine_intake_v0_plan/VALIDATION_CLOSEOUT_REPORT.md`
- `docs/Factory/runs/RUN_20260701_1455_candidate_review_promotion_v0_plan/`
- `docs/Factory/runs/RUN_20260701_1455_candidate_review_promotion_v0_plan/VALIDATION_CLOSEOUT_REPORT.md`
- `docs/Factory/runs/RUN_20260701_1529_socratic_discovery_v0_plan/`
- `docs/Factory/runs/RUN_20260701_1529_socratic_discovery_v0_plan/VALIDATION_CLOSEOUT_REPORT.md`
- `docs/Factory/runs/RUN_20260701_1548_coding_proof_harness_v0_plan/`
- `docs/Factory/runs/RUN_20260701_1548_coding_proof_harness_v0_plan/VALIDATION_CLOSEOUT_REPORT.md`
- `docs/Factory/runs/RUN_20260701_1604_roadmap_sequence_review/`
- `docs/Factory/runs/RUN_20260702_0617_coding_harness_workflow_v0_plan/`
- `docs/Factory/runs/RUN_20260702_0617_coding_harness_workflow_v0_plan/VALIDATION_CLOSEOUT_REPORT.md`
- `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/`
- `docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/VALIDATION_CLOSEOUT_REPORT.md`
- `docs/Factory/runs/RUN_20260705_0923_live_coding_adapter_eval_plan/`
- `docs/Factory/runs/RUN_20260712_0909_agent_context_relevance_v1_plan/`
- `docs/Factory/runs/RUN_20260712_0909_agent_context_relevance_v1_plan/VALIDATION_CLOSEOUT_REPORT.md`
- `docs/Factory/runs/RUN_20260712_1011_vision_epistemic_hardening/`
- `docs/Factory/runs/RUN_20260712_1011_vision_epistemic_hardening/VALIDATION_CLOSEOUT_REPORT.md`
- `docs/Factory/runs/RUN_20260712_1030_markdown_memory_ingestion_v0_plan/`

## Current Architectural Posture

The Workspace is separate from Factory V2, Factory V3, Temper, Aegis, Sentinel, and Harmony.

Factory V2 is available locally as process discipline for planning and review. It is not a Workspace subsystem.

In this repository, `docs/Factory/` means the Factory V2 starter-kit scaffold. It does not mean Factory V3.

Factory V3 remains separate in its own repository and should continue to own mission governance.

Project Memory is constitutionally the governed system of record for the Workspace's current Project understanding, not the ultimate authority for external reality or source-system records. Claim, Decision Review, Knowledge Scope, bounded Delegation, memory rights, and explicit Markdown authority modes are accepted doctrine. Their runtime representations are deferred.

## What Does Not Exist Yet

- product UI
- full Project Memory implementation beyond v0 local contract, semantics, context, adapter twins, CLI/TUI, candidate review, agent-facing context commands, and the reviewed repo-local seed corpus
- runtime Claim epistemic states, Decision Review, Knowledge Scope promotion, bounded Delegation records, or authored/curated Markdown reconciliation
- full Thinking Engine implementation beyond Intake v0, Socratic Discovery v0, Coding Proof Harness v0, Coding Harness Workflow v0, and Brownfield multi-repo coding proof behavior
- Workspace Shell implementation
- integration clients for Factory V3, Temper, Aegis, Sentinel, or Harmony
- live Cursor CLI, Codex CLI, Cursor SDK, OpenAI SDK, or OpenAI Agents SDK adapters
- concrete API schemas
- runnable product-application tests; the repository has a runnable Python unit-test suite
- active implementation runs
- active Workspace missions

## Current Verification

Process scaffold verification:

```bash
bash scripts/knowledge_lint.sh
./scripts/factoryctl context-index
./scripts/factoryctl pack-lint --run RUN_20260701_0848_project_memory_v0_plan
python3 -m unittest tests/test_project_memory_contract.py tests/test_project_memory_fixtures.py tests/test_project_memory_semantics.py tests/test_project_memory_context.py
python3 -m unittest tests/test_project_memory_agent_context.py
python3 -m unittest tests/test_factory_context_index_atomic.py
python3 -m unittest tests/test_project_memory_adapter_twins.py
python3 -m unittest tests/test_project_memory_cli.py
python3 -m unittest tests/test_project_memory_tui.py
python3 -m unittest tests/test_project_memory_review.py
python3 -m unittest tests/test_thinking_engine_intake.py
python3 -m unittest tests/test_thinking_engine_discovery.py
python3 -m unittest tests/test_thinking_engine_coding_harness.py
python3 -m unittest tests/test_thinking_engine_coding_workflow.py
python3 -m unittest tests/test_context_recall_repair.py
./scripts/factoryctl pack-lint --run RUN_20260701_1438_thinking_engine_intake_v0_plan
./scripts/factoryctl pack-lint --run RUN_20260701_1455_candidate_review_promotion_v0_plan
./scripts/factoryctl pack-lint --run RUN_20260701_1529_socratic_discovery_v0_plan
./scripts/factoryctl pack-lint --run RUN_20260701_1548_coding_proof_harness_v0_plan
./scripts/factoryctl pack-lint --run RUN_20260701_1604_roadmap_sequence_review
./scripts/factoryctl pack-lint --run RUN_20260702_0617_coding_harness_workflow_v0_plan
./scripts/factoryctl pack-lint --run RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan
./scripts/factoryctl pack-lint --run RUN_20260705_0923_live_coding_adapter_eval_plan
./scripts/factoryctl pack-lint --run RUN_20260712_0909_agent_context_relevance_v1_plan
./scripts/factoryctl pack-lint --run RUN_20260712_1011_vision_epistemic_hardening
python3 scripts/agent_loop_bridge_validate.py tests/fixtures/agent_loop_bridge/valid_handoff.json --json
```

There is no product build yet.

Headless CLI entry point:

```bash
python3 -m soane.project_memory.cli --help
```

Thin TUI entry point:

```bash
python3 -m soane.project_memory.tui --help
```

Agent-facing context entry points:

```bash
python3 -m soane.project_memory.cli agent-context --task "<TASK>"
python3 -m soane.project_memory.cli agent-trace --id <MEMORY_OBJECT_ID>
python3 -m soane.project_memory.cli agent-affected --path <SOURCE_PATH>
python3 -m soane.project_memory.cli validate --no-fixtures --memory-dir docs/project_memory/objects
```

Coding Harness Workflow entry point:

```bash
python3 -m soane.thinking_engine.coding_workflow --help
```

Validation closeout:

```bash
cat docs/Factory/runs/RUN_20260701_0848_project_memory_v0_plan/VALIDATION_CLOSEOUT_REPORT.md
cat docs/Factory/runs/RUN_20260701_1438_thinking_engine_intake_v0_plan/VALIDATION_CLOSEOUT_REPORT.md
cat docs/Factory/runs/RUN_20260701_1455_candidate_review_promotion_v0_plan/VALIDATION_CLOSEOUT_REPORT.md
cat docs/Factory/runs/RUN_20260701_1529_socratic_discovery_v0_plan/VALIDATION_CLOSEOUT_REPORT.md
cat docs/Factory/runs/RUN_20260701_1548_coding_proof_harness_v0_plan/VALIDATION_CLOSEOUT_REPORT.md
cat docs/Factory/runs/RUN_20260702_0617_coding_harness_workflow_v0_plan/VALIDATION_CLOSEOUT_REPORT.md
cat docs/Factory/runs/RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan/VALIDATION_CLOSEOUT_REPORT.md
```

## Active Boundary Decisions

- Use Factory V2 locally for planning discipline.
- Soane's embedded Factory V2 scaffold includes the direct-source recall repair path from the Factory starter kit: generated `WEAK` Stage A context recall remains blocking unless locally verifiable direct-source repair evidence records `Final Repaired Verdict: REPAIRED_DIRECT_SOURCE_CHECK`.
- Treat `docs/Factory/` as Factory V2 starter-kit process only.
- Keep Factory V3 work in `/Users/eduardodosremedios/Factory_V3`.
- Use `/Users/eduardodosremedios/Eduardo_Product_Stack` as the portfolio context source.
- Do not duplicate neighbouring product responsibilities inside the Workspace.
- Treat `docs/GOVERNANCE_MODEL.md` as the repository-level rule for document status, amendments, decisions, evidence levels, and implementation blockers.
- Use `docs/research/PROJECT_MEMORY_RESEARCH_SYNTHESIS.md` as the research input behind the Project Memory architecture.
- Treat `docs/PROJECT_MEMORY_ARCHITECTURE.md` as the conceptual architecture for Project Memory. It intentionally defers storage, API, UI, and implementation choices.
- Treat `docs/THINKING_ENGINE_ARCHITECTURE.md` as the conceptual architecture for the Thinking Engine. It defines intake, discovery, Socratic dialogue, hypotheses, evidence review, synthesis, inference strategy, readiness states, and boundaries without defining implementation APIs or UI.
- Use coding as an acceptable first proof path for Workspace primitives, while keeping the Workspace domain-general and treating Cursor CLI, Codex CLI, Cursor SDK, and OpenAI SDK integrations as adapters.
- Use a headless CLI first, then a thin TUI, before starting the broader Workspace product shell.
- Define the Project Memory v0 contract, golden fixtures, context assembly v0, capture/review/promotion flow, and mock-first adapter contract before implementation.
- Include governed memory invariants in the Project Memory v0 contract: scope and visibility, temporal supersession, provenance lineage, controlled propagation, contradiction handling, and equivalent enforcement across retrieval paths.
- Prefer mock-first, then CLI-backed coding harness adapters, then SDK-backed integrations once the adapter contract is stable.
- Treat Greenfield and Brownfield project intake differently. Brownfield coding work may involve one repository, multiple repositories, or a wider workspace/system boundary. Intake requires repo/workspace audit, existing application context, build/test discovery, architecture/documentation gap analysis, ownership and integration mapping, and agreed starting-context files before feature planning or coding delegation.
- Do not assume all project context lives in Git. Non-coding work may depend on external artifacts such as analytics dashboards, campaign assets, research notes, briefs, spreadsheets, design files, CRM records, ad accounts, and other operational systems. Soane must be able to identify and govern those sources as context inputs.

## Current Implementation State

- `RUN_20260701_0848_project_memory_v0_plan`: Factory V2 `PLANNING_ONLY` pack for Project Memory v0 object-model prototype. Status: `PASS`; final pack lint passed.
- Human Go for `PM-V0-001` was given on 2026-07-01.
- MS-00 Contract Scaffold is implemented.
- MS-01 Golden Fixture Corpus is implemented.
- MS-02 Memory Semantics is implemented.
- MS-03 Context Assembly And Markdown Mapping is implemented.
- MS-04 Mock Coding Adapter Contract is implemented.
- MS-05 Headless CLI is implemented.
- MS-06 Thin TUI Scope is implemented.
- MS-07 Validation Closeout is complete.
- Agent-facing context slice v0 is implemented with Markdown role classification, expanded top-level doc recall, Project Memory provenance ref matching, repo-local reviewed memory-object JSON loading, compact context bundles, object tracing, source-path affected-object lookup, and focused tests.
- Thinking Engine architecture is complete.
- `RUN_20260701_1438_thinking_engine_intake_v0_plan`: Factory V2 `PLANNING_ONLY` pack for `TEI-V0-001` Thinking Engine Intake v0. Status: `PASS`; pack lint passed.
- Human Go for `TEI-V0-001` was given on 2026-07-01.
- `TEI-V0-001` Thinking Engine Intake v0 is implemented with local deterministic intake classification, Context Baseline, Discovery Playbook selection, Readiness Assessment, and Project Memory write-back candidates.
- `RUN_20260701_1455_candidate_review_promotion_v0_plan`: Factory V2 `PLANNING_ONLY` pack for `CRP-V0-001` Candidate Review and Promotion v0. Status: `PASS`; pack lint passed.
- Human Go for `CRP-V0-001` was given on 2026-07-01.
- `CRP-V0-001` Candidate Review and Promotion v0 is implemented with local deterministic review decisions, promotion semantics, provenance retention, current-truth separation, negative fixtures, a thin CLI wrapper, and validation closeout.
- `RUN_20260701_1529_socratic_discovery_v0_plan`: Factory V2 pack for `SD-V0-001` Socratic Discovery v0. Status: `PASS`; execution enabled after human Go on 2026-07-01; pack lint passed.
- `SD-V0-001` Socratic Discovery v0 is implemented with deterministic discovery sessions, traceable question generation, candidate answer capture, uncertainty-preserving candidate hypotheses, stop conditions, and validation closeout.
- `RUN_20260701_1548_coding_proof_harness_v0_plan`: Factory V2 pack for `CPH-V0-001` Coding Proof Harness v0. Status: `PASS`; execution enabled after human Go on 2026-07-01; pack lint passed.
- `CPH-V0-001` Coding Proof Harness v0 is implemented with local deterministic Greenfield/Brownfield coding fixtures, service composition, mocked provider invocation, candidate output capture, review-gated promotion, and validation closeout.
- `RUN_20260701_1604_roadmap_sequence_review`: Factory V2 `PLANNING_ONLY` pack for `ROADMAP-SEQ-001` Roadmap Sequencing Review. Status: `PASS`; pack lint passed.
- `RUN_20260702_0617_coding_harness_workflow_v0_plan`: Factory V2 pack for `CHW-V0-001` Coding Harness Workflow v0. Status: `PASS`; execution enabled after human Go on 2026-07-02; pack lint passed.
- Human Go for `CHW-V0-001` was given on 2026-07-02.
- `CHW-V0-001` Coding Harness Workflow v0 is implemented with fixture listing, selected fixture execution, text and JSON summaries, explicit optional candidate review, blocked Brownfield summaries, no live provider calls, and no repository mutation.
- Factory V2 direct-source recall repair support has been refreshed from `/Users/eduardodosremedios/factory-starter-kit` in the embedded Soane scaffold.
- `RUN_20260705_0747_brownfield_multi_repo_coding_proof_plan`: Factory V2 pack for `BMR-CPH-V0-001` Brownfield Multi-Repo Coding Proof. Status: `PASS`; execution enabled after human Go on 2026-07-05; pack lint passed.
- `BMR-CPH-V0-001` Brownfield Multi-Repo Coding Proof is implemented with deterministic ready and blocked multi-repo fixtures, local system-boundary context, task-relevant versus out-of-scope repository summaries, blocked readiness behavior, workflow JSON/text summaries, candidate-only provider output, no live provider calls, and no repository mutation.
- `RUN_20260705_0923_live_coding_adapter_eval_plan`: Factory V2 `PLANNING_ONLY` pack for `LCAE-V0-001` Live Coding Adapter Evaluation. Status: `PASS`; pack lint passed.
- Canonical-doc freshness review found that natural multi-term agent-context queries can return no document slices, while an empty memory seed set falls back to all visible memory; concurrent index refreshes also lack an explicit atomicity contract.
- `RUN_20260712_0909_agent_context_relevance_v1_plan`: Factory V2 pack for `ACR-V1-001` Agent Context Relevance and Fail-Closed Assembly. Status: `PASS`; execution enabled after human Go on 2026-07-12; Stage A through I2 and final pack lint passed.
- The prior repo-local decision that made `LCAE-V0-001` the immediate next gate is superseded by the accepted agent-context correctness gate; adapter evaluation remains queued after ACR-V1-001.
- Human Go for `ACR-V1-001` was given on 2026-07-12 and execution mode was enabled.
- `ACR-V1-001` is implemented with bounded natural-task query planning, separate document and memory budgets, fail-closed zero-match behavior, explicit broad versus seeded lower-level context, one-hop allowlisted relationship expansion, lifecycle-aware ranking, observational source freshness, SQLite-owned rebuild serialization, rollback-safe publication, explicit selection/refresh states, 14 new tests, and validation closeout.
- Next roadmap step: create a planning-only Factory pack for Markdown-to-memory candidate ingestion. `LCAE-V0-001` remains queued after ingestion and graph-aware context unless a later approved roadmap decision changes the order.
