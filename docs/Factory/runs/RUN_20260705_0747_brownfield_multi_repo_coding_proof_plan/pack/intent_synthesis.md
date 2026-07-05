# Intent Synthesis: Brownfield Multi-Repo Coding Proof

## Version

v1

## Change Log

- v1 (2026-07-05): Initial Stage C synthesis.

## Synthesis

The red-team findings are valid and are incorporated into the locked intent.

`BMR-CPH-V0-001` should not merely add a second repository to a fixture. It should prove that Soane can reason about a Brownfield system boundary across repositories before treating a coding task as ready for mocked provider invocation.

## Intent Hardening Decisions

- Multi-repo fixture fields must include repository map, in-scope repositories, out-of-scope repositories, service boundaries, integration contracts, ownership, build/test responsibility, documentation gaps, and authority path.
- Provider invocation readiness must consider missing system-boundary or authority context, not only repository availability.
- Coding Harness Workflow should summarize multi-repo state but not own readiness logic.
- No live repository audit, cloning, command execution, or mutation is allowed.

## Scope Expansion Check

No scope expansion was introduced. The synthesis narrows the implementation to fixture-backed multi-repo semantics and summary behavior.

## Residual Non-Blocking Questions

- Fixture ID naming can be resolved during implementation without changing the architecture if deterministic tests assert the chosen IDs.
