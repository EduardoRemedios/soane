# Fixtures: Coding Proof Harness v0

## Version

v1

## Change Log

- v1 (2026-07-01): Initial fixture plan.

## Required Fixture Coverage

Future implementation should add deterministic fixtures for:

- `CPH-GF-001`: Greenfield coding brief with missing starter context.
- `CPH-GF-002`: Brownfield single-repo coding brief with build/test/audit context.
- `CPH-GF-003`: Brownfield blocked coding brief missing authority or audit context.
- `CPH-GF-004`: Mock Codex CLI or Cursor CLI provider invocation.
- `CPH-GF-005`: Proposed provider output captured as Project Memory candidate.
- `CPH-GF-006`: Candidate output promoted only through Candidate Review and Promotion.

## Fixture Rules

- Fixtures must not require live model calls, live CLIs, live SDKs, databases, external connectors, or repository mutation.
- Fixture IDs must be deterministic and stable.
- Proposed provider output must remain candidate-only until reviewed.
