# Pre-Mortem

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage E pre-mortem.

## Failure Scenarios

### PM-001 False Certainty

Discovery hypotheses are presented as conclusions.

Mitigation: Keep hypotheses as candidates with uncertainty state and evidence-gap links.

### PM-002 Generic Questions

Question generation ignores the project category or baseline source gap.

Mitigation: Require every question to include a source reason and category-specific fixture coverage.

### PM-003 Hidden Model Dependency

Implementation calls an LLM or assumes model output is available.

Mitigation: Require deterministic local fixtures and no-model-call tests.

### PM-004 Answer Promotion Drift

User answers silently become accepted Project Memory.

Mitigation: Route answers and hypotheses through candidate review and promotion semantics.

### PM-005 Authority Drift

Answers create a readiness state that implies permission to execute.

Mitigation: Keep needs-authority separate from needs-evidence and ready-for-planning.

### PM-006 Wrapper Scope Creep

CLI or TUI work becomes product UX or duplicates service logic.

Mitigation: Keep wrappers optional, thin, and service-backed.

## Top Mitigation Summary

The future implementation should start with deterministic session, question, answer, hypothesis, and stop-condition fixtures before any wrapper.
