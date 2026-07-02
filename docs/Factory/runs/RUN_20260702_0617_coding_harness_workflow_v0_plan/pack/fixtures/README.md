# Fixtures: Coding Harness Workflow v0

## Version

v1

## Change Log

- v1 (2026-07-02): Initial fixture plan.

## Required Fixture Coverage

Future implementation should reuse the existing deterministic coding harness fixtures in `tests/fixtures/coding_proof_harness/`.

Additional fixtures should be added only if CLI behavior cannot be tested through the existing corpus.

## Required Workflow Cases

- fixture list shows available fixture IDs and titles
- run summary for Greenfield ready fixture
- run summary for Brownfield ready fixture
- run summary for Brownfield blocked fixture
- JSON summary includes readiness, provider, candidate, review, live-call, and repository-mutation fields

## Fixture Rules

- No live providers.
- No repository mutation.
- No database or persistence.
- Proposed output remains candidate-only unless reviewed through Candidate Review and Promotion.
