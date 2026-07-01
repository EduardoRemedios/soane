# Premortem: Coding Proof Harness v0

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage E premortem.

## Failure Scenarios

1. The harness duplicates Intake, Discovery, Context, Adapter, or Review logic instead of composing existing services.
2. Proposed provider output becomes accepted truth without Candidate Review and Promotion.
3. Provider surface selection implies permission to execute.
4. Brownfield fixtures skip audit/readiness checks and behave like Greenfield fixtures.
5. A live CLI, SDK, model, database, or repository mutation enters the proof.
6. CLI/TUI wrapper work expands into Workspace Shell.
7. The harness becomes too generic and loses the first coding-proof thread.

## Mitigations

- Require service-composition tests over existing primitives.
- Require candidate-only output tests and review-promotion tests.
- Preserve capability and authority fields in Provider Invocation records.
- Keep Greenfield and Brownfield fixture expectations separate.
- Add static and unit checks for no live integration dependencies.
- Make wrapper work optional and skippable.
- Keep acceptance criteria tied to coding proof fixtures, not general workflow automation.
