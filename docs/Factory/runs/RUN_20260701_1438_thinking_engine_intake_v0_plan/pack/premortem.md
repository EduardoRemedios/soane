# Premortem

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage E premortem.

## Failure Scenarios

### F1: Intake becomes a generic product shell

The future slice tries to build full UI workflows, connectors, and project management behavior.

Mitigation: keep implementation to local services, fixtures, and CLI/TUI wrappers.

### F2: Brownfield means only one repo

The model works for simple repositories but fails for real systems spanning multiple repositories and external artifacts.

Mitigation: require multi-repo and non-repository fixtures.

### F3: Readiness becomes a fake score

A numeric readiness score hides missing evidence and context.

Mitigation: use explainable states and dimensions only.

### F4: Thinking output becomes truth too early

Model synthesis or intake summaries are written directly as accepted memory.

Mitigation: write candidate Project Memory objects and require review/promotion boundaries.

### F5: Live integrations dominate the design

Connector behavior drives the schema before semantics are stable.

Mitigation: defer live repo, analytics, CRM, ads, design, Cursor, Codex, and OpenAI calls.

## Overall Mitigation

Use fixtures and deterministic tests as the first proof, with Project Memory as the substrate and no product shell work.
