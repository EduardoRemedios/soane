# Fixtures: LCAE-V0-001

## Version

v1

## Change Log

- v1 (2026-07-05): Initial Stage F fixture notes.

## Purpose

Future implementation should add deterministic adapter-evaluation fixtures rather than live provider calls.

## Required Fixture Families

- `adapter_surface_profiles`: one source-backed profile per candidate surface.
- `adapter_precondition_checks`: auth, authority, sandbox, output, trace, cost, latency, repository scope, and review gates.
- `blocked_surfaces`: missing authority, unsafe mutation, missing structured output, missing traceability, or unclear credential handling.
- `recommendation_cases`: first live proof recommendation and rejected alternatives.

## Non-Goals

- No fixture may require a real API key, login, network call, CLI install, SDK install, external repository, or real provider invocation.
