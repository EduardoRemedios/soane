# Fixtures: LCAE-V0-001

## Version

v2

## Change Log

- v1 (2026-07-05): Initial Stage F fixture notes in the upstream planning run.
- v2 (2026-07-20): Added source contradiction, context payload, and no-safe-surface families.

## Purpose

Future implementation uses committed deterministic fixtures instead of provider discovery or invocation.

## Required Fixture Families

- `adapter_surface_profiles`: one current source-backed profile per in-scope surface.
- `invalid_profiles`: unknown, duplicate, malformed, incomplete, stale-without-review, and path-escaping data.
- `hard_blockers`: source contradiction, missing read-only guarantee, mutation-capable mode, trace privacy uncertainty, and missing authority/permission.
- `recommendation_cases`: one eligible winner, blocked high scorer, deterministic tie, reversed input, and no safe surface.
- `agent_context_payloads`: ready, degraded, blocked, budget-truncated, graph-excluded, and freshness-changed existing command output.
- `candidate_boundary`: simulated Provider Invocation/output remains proposed and non-current until existing review.

## Non-Goals

No fixture may require a real key, login, environment credential, provider config, session history, installed CLI/SDK, provider import, network, external repository, or live invocation.
