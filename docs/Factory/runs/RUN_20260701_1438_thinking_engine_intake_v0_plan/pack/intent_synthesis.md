# Intent Synthesis

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage C synthesis.

## Iteration

Iteration: 1 of max 2.

## Synthesis

The red-team findings are valid and have been absorbed into `intent.md` v2.

The hardened intent now:

- keeps the future implementation local and deterministic
- requires Greenfield, Brownfield single-repo, Brownfield multi-repo, and non-repository fixtures
- forbids live integrations in the first slice
- forbids premature readiness scoring
- treats Thinking Engine outputs as Project Memory candidates until reviewed
- keeps CLI/TUI as wrappers over service functions

## Scope Expansion Review

No scope expansion remains.

The non-repository context requirement is not an expansion. It was already present in the canonical Thinking Engine architecture and the latest roadmap.

## Remaining Issues

### BLOCKING

- None.

### NON-BLOCKING

- The future implementation may choose whether marketing fixtures are behavior-driving or fixture-only in the first micro-sprint.

## Exit Position

Intent is ready for Purple lock.
