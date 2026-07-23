# Micro-Sprints: CLR-V0-001

## Version

v2

## Change Log

- v1 (2026-07-23): Initial Stage G sequence.
- v2 (2026-07-23): Added credential-isolating route work and parent-process gates.

## Sprint Sequence

### MS-00 Executable Contract And Test Scaffold

- Objective: translate the locked fixture, command, reason-code, topology, and
  receipt contracts into failing focused tests before implementation.
- Inputs: `pack/intent.md`, `pack/fixtures/`, `pack/verification_plan.md`.
- Outputs: implementation-owned test fixtures and focused tests for VC-001 through
  VC-020.
- Entry Criteria: future human Go authorizes implementation but not provider use.
- Exit Criteria: tests cover every offline gate, forbidden argument/event/state,
  one-shot transition, secret sentinel, and receipt outcome.
- Stop/Go Gate: stop if a test requires a real credential, provider call, user
  config, workstation repository, or unbounded runner abstraction.

### MS-01 Pure Proof Core

- Objective: implement standard-library command construction, manifests, normalized
  event policy, bounded stream handling, one-shot state, schema/fact checks, and
  deterministic receipts with no subprocess side effects in unit tests.
- Inputs: MS-00 tests and committed fixture cases.
- Outputs: one bounded proof-core module and focused passing tests.
- Entry Criteria: MS-00 exit criteria pass.
- Exit Criteria: VC-005, VC-007, VC-009, VC-010, VC-013, VC-016 through VC-020 pass
  with injected fake process/clock/filesystem boundaries.
- Stop/Go Gate: stop if core logic reads environment credentials, invokes Codex,
  owns Project Memory promotion, or becomes a general provider framework.

### MS-02 Exact Runner And Credential Isolation

- Objective: implement the smallest adapter for one approved immutable disposable
  runner mechanism, including topology attestation, fresh controlled home,
  read-only fixture exposure, model-shell and parent-process sentinel canaries,
  one exact credential-isolation route, bounded pipes, and teardown evidence.
- Inputs: MS-01 core, approved runner mechanism/identity, topology and shell fixtures.
- Outputs: one isolation supervisor adapter plus offline integration tests.
- Entry Criteria: a human-approved exact runner mechanism is available without
  installing or provisioning a general platform.
- Exit Criteria: VC-001 through VC-004, VC-006, VC-008, VC-011, VC-012, and VC-015
  pass without a provider credential.
- Stop/Go Gate: stop if the runner can see host home/Soane/unrelated repos/sockets,
  cannot attest its identity, cannot isolate credentials from child and parent
  inspection, exposes a proxy to model commands, requires broad platform/proxy work,
  or needs provider use for testing.

### MS-03 Offline Gate And Execution Candidate

- Objective: assemble the exact fixed fixture and command, revalidate official
  sources/runtime compatibility, run all offline and regression checks, and emit a
  blocked or ready execution-candidate receipt without invoking Codex.
- Inputs: MS-01 and MS-02 outputs, authority-input schema, official source allowlist.
- Outputs: offline gate report and redacted execution-candidate manifest.
- Entry Criteria: MS-02 exit criteria pass.
- Exit Criteria: VC-001 through VC-020 and VC-027 pass; candidate records exact
  runner, CLI, model input slot, command, ceilings, fixture hash, and missing or
  satisfied authority references. Compatibility probes are limited to
  credential-free/network-denied `codex --version` and `codex exec --help` inside
  the runner.
- Stop/Go Gate: stop before process start for source/runtime drift, dirty Soane,
  missing authority/project permission/model/spend/auth/runner references, or any
  offline failure.

### MS-04 Human Live Gate And One-Shot Observation

- Objective: after a distinct explicit human Go for provider use, execute exactly
  one Codex CLI request in the approved disposable runner and produce a terminal
  receipt.
- Inputs: passing MS-03 candidate, secure dedicated auth input, explicit model and
  spend approval, authority and project-permission references, and one unique live
  authorization ID.
- Outputs: bounded quarantined evidence, redacted generated receipt, and teardown
  evidence.
- Entry Criteria: every VC-001 through VC-020 and VC-027 check passes and the human
  explicitly authorizes the exact one-call V4 transition.
- Exit Criteria: VC-021 through VC-026 are evaluated; a PASS, FAIL, or BLOCKED
  terminal receipt exists; runner teardown is recorded.
- Stop/Go Gate: no retry under any outcome. Any timeout, auth failure, ambiguous
  request count, secret match, forbidden event, mutation, malformed output, source
  drift, or teardown failure consumes the allowance and ends the sprint.

### MS-05 Review And Validation Closeout

- Objective: reconcile the receipt with the locked scope, record residual risks,
  update canonical state docs, and recommend or reject a separately planned next
  proof.
- Inputs: MS-04 receipt/evidence, verification plan, traceability matrix, diff.
- Outputs: validation closeout, canonical state updates, and Candidate Review hook
  if promotion is proposed.
- Entry Criteria: MS-04 has a terminal receipt, including BLOCKED or FAIL.
- Exit Criteria: every VC has evidence or an explicit failed outcome; no receipt is
  promoted automatically; tests, knowledge/context checks, and diff hygiene pass.
- Stop/Go Gate: stop if closeout broadens authorization, hides a failed gate,
  retries the invocation, or treats generated evidence as accepted Project Memory.

## Bounded Deferrals

- Additional runner mechanisms: owner Human Authority Owner with Factory Root
  Planner; MS-05 may recommend one separate pack after receipt evidence.
- Additional models, fixtures, platforms, providers, or repositories: separate pack
  owned by Human Authority Owner with Factory Root Planner; hook MS-05.
- Write-capable proof: owner Human Authority Owner with Verification Specialist;
  MS-05 may propose a separate authority/threat-review pack but cannot authorize it.
- Receipt promotion: owner Candidate Reviewer; existing Candidate Review path only;
  hook MS-05.

Reusable provider, proxy, or sandbox platform work is a rejected non-goal, not a
deferred deliverable.
