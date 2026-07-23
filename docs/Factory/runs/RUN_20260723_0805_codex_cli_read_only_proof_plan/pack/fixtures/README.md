# CLR-V0-001 Verification Fixtures

## Version

v2

## Change Log

- v1 (2026-07-23): Defined the verification fixture set.
- v2 (2026-07-23): Added Factory fixture metadata and fixture directory.

## Purpose

These committed planning fixtures define deterministic cases for the future
implementation. They contain no credentials and authorize no live execution.

## Files

- `proof_fixture_spec.json`: tiny repository content, fixed question, expected facts,
  and final-response schema contract.
- `runner_topology_cases.json`: allowed and forbidden isolation topologies.
- `shell_environment_cases.json`: model-subprocess allowlist and sentinel cases.
- `credential_route_cases.json`: approved proxy and blocked direct-key routes.
- `event_policy_cases.json`: normalized allowed and forbidden stream events.
- `receipt_cases.json`: terminal outcomes and stable reason codes.

## Rules

- Future tests may copy these cases into implementation-owned test fixtures without
  changing their semantics.
- Raw Codex JSONL must be normalized by one narrow parser before comparison with
  `event_policy_cases.json`.
- Unknown fields may be retained as evidence, but unknown event classes fail.
- `SENTINEL_SECRET_VALUE` is deliberately non-secret test data.
- No fixture may contain a real provider key, auth token, host path, or user state.
