# Raw Brief: Project Memory v0 Object Model Prototype

## Run Identity

- Run ID: `RUN_20260701_0848_project_memory_v0_plan`
- Date: 2026-07-01
- Repository: Soane / Workspace
- Execution Mode: `PLANNING_ONLY`

## User Intent

Create a Factory V2 planning-only implementation pack for the first local Project Memory v0 object-model prototype.

The pack should bridge the accepted Project Memory architecture into a bounded implementation plan. It must not implement code.

## Context

Soane is the working codename for the Workspace: the primary human-facing environment for governed AI work.

The Workspace is broader than coding, but coding may be used as the first proof path because it exposes concrete project memory, planning, delegation, review, evidence, and execution feedback loops.

The first implementation path should be:

1. Project Memory v0 contract
2. Project Memory v0 prototype
3. headless CLI
4. thin TUI
5. validation pass
6. later Thinking Engine and Workspace Shell work

## Required Source Documents

The planning pack must consume:

- `docs/VISION.md`
- `docs/CORE_CONCEPTS.md`
- `docs/GOVERNANCE_MODEL.md`
- `docs/PROJECT_MEMORY_ARCHITECTURE.md`
- `docs/research/PROJECT_MEMORY_RESEARCH_SYNTHESIS.md`
- `docs/INTEGRATION_ARCHITECTURE.md`
- `docs/ROADMAP.md`
- `docs/PROJECT_STATE.md`

## Required Planning Outputs

The pack must define:

- first implementation slice
- non-goals
- file/module layout
- Project Memory v0 object contract
- minimal object model
- required fields and governed memory invariants
- lifecycle states
- lifecycle transition rules
- provenance representation
- relationship representation
- evidence-level handling
- capture, review, and promotion flow
- contradiction, staleness, supersession, and redaction behavior
- validation strategy
- pre-mortem
- golden fixtures
- scope and visibility enforcement proof
- temporal supersession proof
- provenance lineage proof
- controlled propagation proof for context assembly
- context assembly v0
- canonical Markdown source-mapping proof
- commands/tests to add
- headless CLI command surface
- simple TUI navigation scope
- mock-first Cursor/Codex/OpenAI adapter contract
- persistence, deterministic ID, and migration guardrails

## Golden Fixture Requirements

The golden fixture set should include at least:

- Decision linked to Evidence
- Assumption superseded by Evidence
- Contradiction between sources
- Stale Evidence
- canonical Markdown source mapping
- Provider Invocation via mocked Cursor/Codex/OpenAI adapter
- Capability without Authority
- redaction or retrieval suppression
- unauthorized retrieval blocked by scope or visibility
- stale or superseded record excluded as current truth
- promoted claim with reconstructable provenance lineage
- context assembly respects visibility and propagation rules

## Governed Memory Invariants

The planning pack should require invariant tests for:

- Scope: retrieval and direct lookup must enforce the same visibility and policy constraints.
- Time: stale, superseded, invalidated, and revoked objects must remain inspectable without being treated as current truth.
- Provenance: promoted claims must retain source, writer, time, evidence level, and derivation lineage where applicable.
- Propagation: context assembly must control which memory crosses task, actor, project, or adapter boundaries.
- Resolution: contradictions must remain explicit until reviewed; deduplication must not suppress structural conflicts before contradiction handling.

## Adapter Posture

The adapter proof order should be:

1. mock-first adapter contract
2. CLI-backed coding harness adapter
3. SDK-backed integration only after the contract is stable

Candidate adapter surfaces:

- Codex CLI
- Cursor CLI
- Cursor SDK
- OpenAI SDK
- OpenAI Agents SDK

The adapter contract must sit behind Provider Invocation, Capability Reference, Inference Strategy, and governed work contracts. It must not define Project Memory, authority, evidence semantics, mission governance, or the Workspace product boundary.

## Non-Goals

This run must not:

- implement application code
- choose a final database
- build the CLI
- build the TUI
- build product UI
- create live Cursor, Codex, or OpenAI integrations
- create Factory V3 mission governance
- create Aegis authority or proof semantics
- duplicate Temper, Sentinel, Harmony, Factory V3, or Aegis responsibilities
- treat generated Markdown as the Project Memory substrate
- treat coding as the only Workspace use case

## Go / No-Go Rule

This planning pack is ready for review only if it:

- remains `PLANNING_ONLY`
- produces a bounded implementation plan
- includes a pre-mortem
- includes golden fixture definitions
- preserves Project Memory, Evidence, Decision, Capability, Authority, Mission, and Proof distinctions
- preserves the Factory V2 versus Factory V3 boundary
- keeps coding as the first proof path without narrowing Soane to coding
- passes Stage A through I2 lint and final pack lint

