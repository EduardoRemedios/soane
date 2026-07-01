# Pre-mortem: Project Memory v0 Plan

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage E pre-mortem.

## Failure Scenario 1: v0 becomes CRUD over JSON

The prototype stores objects but does not prove lifecycle, provenance, evidence, visibility, supersession, contradiction, or context assembly semantics.

Mitigation: require contract invariants and golden fixtures before implementation.

## Failure Scenario 2: v0 becomes hidden RAG

Context assembly silently behaves like retrieval ranking instead of governed memory selection.

Mitigation: define deterministic context assembly v0 rules and fixtures for stale, contradictory, low-evidence, and hidden records.

## Failure Scenario 3: live adapter coupling dominates the architecture

Cursor, Codex, or OpenAI behavior becomes the source of truth for the object model.

Mitigation: define mock-first adapter contracts and defer live CLI or SDK integrations.

## Failure Scenario 4: coding proof narrows the Workspace

The first proof path makes Project Memory look like a coding-only tool.

Mitigation: keep object types domain-general and isolate coding-specific behavior to provider invocation fixtures.

## Failure Scenario 5: authority is implied by capability

Available tools or agents are treated as permitted actors.

Mitigation: include Capability without Authority and unauthorized retrieval fixtures.

## Failure Scenario 6: provenance is too weak to support trust

Claims cannot be traced back to source, writer, time, evidence level, or derivation path.

Mitigation: require reconstructable provenance lineage for promoted claims.

## Failure Scenario 7: early storage choices become permanent accidentally

A quick local format becomes hard to migrate or inspect.

Mitigation: require portable storage, deterministic IDs for fixtures, and migration/rewrite guardrails.

## Failure Scenario 8: generated Markdown becomes the substrate

Markdown output becomes the only place decisions and evidence exist.

Mitigation: define Markdown source mapping as a view over object references.

## Failure Scenario 9: redaction or scope enforcement is incomplete

Direct lookup bypasses retrieval filters or context assembly leaks restricted memory.

Mitigation: require equivalent enforcement across direct lookup, retrieval, and context assembly paths.

## Failure Scenario 10: the planning pack is too broad to implement

The first implementation slice attempts object model, CLI, TUI, adapters, and Markdown generation at once.

Mitigation: sequence contract first, prototype second, CLI third, TUI fourth, validation fifth.

