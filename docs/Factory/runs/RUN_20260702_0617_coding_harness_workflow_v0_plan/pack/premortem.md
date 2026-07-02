# Premortem: Coding Harness Workflow v0

## Version

v1

## Change Log

- v1 (2026-07-02): Initial Stage E premortem.

## Failure Scenarios

1. CLI wrapper duplicates coding harness service behavior.
2. CLI output makes mocked provider invocation look like live execution.
3. Proposed provider output appears accepted rather than candidate-only.
4. JSON output omits provenance, provider, or review status fields needed for inspection.
5. Optional TUI work becomes Workspace Shell or product UX.
6. Tests accidentally depend on live providers or repository state.

## Mitigations

- Require service delegation tests.
- Include mock/live status in summaries.
- Include candidate/review status in summaries.
- Require text and JSON verification.
- Keep TUI optional and skippable.
- Keep fixture-backed tests local and deterministic.
