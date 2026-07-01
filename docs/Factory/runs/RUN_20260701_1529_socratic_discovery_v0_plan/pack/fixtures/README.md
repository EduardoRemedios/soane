# Fixture Plan

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage F fixture plan.

## Required Future Fixtures

The future `SD-V0-001` implementation should add deterministic fixtures for:

- `SD-GF-001`: greenfield discovery questions from missing starter context
- `SD-GF-002`: brownfield single-repo discovery from build, test, docs, and ownership gaps
- `SD-GF-003`: brownfield multi-repo discovery from system boundary and integration gaps
- `SD-GF-004`: non-repository discovery from analytics, campaign, design, or operational context sources
- `SD-GF-005`: blocked discovery where missing context prevents planning
- `SD-GF-006`: answer capture produces Project Memory candidates only
- `SD-GF-007`: hypothesis generation preserves uncertainty and evidence-gap links
- `SD-GF-008`: needs-authority stop condition remains distinct from needs-evidence

## Fixture Constraints

- Fixtures must be local JSON or Python fixture data.
- Fixtures must not call live models, adapters, external connectors, or databases.
- Every generated question must include a source reason.
- Answers and hypotheses must remain candidates until Candidate Review and Promotion acts on them.
