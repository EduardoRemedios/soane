# Roadmap Sequencing Review

## Version

v1

## Change Log

- v1 (2026-07-01): Initial roadmap sequencing review after Coding Proof Harness v0.

## Verdict

The roadmap was detailed enough to reach Coding Proof Harness v0, but it is no longer specific enough for the next decision point.

The immediate fork should be resolved in favor of a thin workflow wrapper before Workspace Shell architecture.

## Recommended Near-Term Sequence

1. `CHW-V0-001` Coding Harness Workflow v0: thin CLI-first workflow over the existing coding harness service, with optional TUI only if it stays service-delegating.
2. Brownfield Multi-Repo Coding Proof v0: extend the coding proof to a multi-repository system boundary.
3. Live Coding Adapter Evaluation Plan: evaluate Codex CLI, Cursor CLI, Cursor SDK, OpenAI SDK, and OpenAI Agents SDK readiness against provider invocation, authority, evidence, and no-mutation requirements.
4. Memory Provider Evaluation: evaluate Supermemory-style providers as external retrieval/context adapters, not canonical Project Memory.
5. Project Memory Persistence Architecture: choose persistence requirements after workflow and provider evidence clarifies what must be durable.
6. Workspace Shell Architecture: design the product shell around proven memory, thinking, workflow, and adapter boundaries.
7. First Product Surface Prototype: build only after the shell architecture has a stable workflow target.

## Rationale

- The coding harness service is proven but not yet navigable as a workflow.
- A CLI-first wrapper continues the established proof path: headless service, then CLI, then TUI, then product shell.
- Brownfield multi-repo should be proven before product shell because it affects system-boundary and context-source design.
- Live adapters should wait until the workflow can show exactly what context is sent, what invocation is recorded, and how output is reviewed.
- Persistence should wait until the durable object and workflow boundaries are clearer.
- Workspace Shell architecture should be informed by a real workflow, not just primitives.

## Immediate Next Slice

Recommended next pack:

`CHW-V0-001 Coding Harness Workflow v0`

Recommended starting scope:

- CLI-first wrapper over `soane.thinking_engine.coding_harness`
- fixture selection
- result summary
- context package summary
- provider invocation summary
- candidate output summary
- review/promotion status summary
- optional TUI only if thin and service-delegating

Out of scope:

- live providers
- repository mutation
- persistence
- Workspace Shell
- product web UI
