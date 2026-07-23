# Premortem: CLR-V0-001 Codex CLI Read-Only Proof

## Version

v2

## Change Log

- v1 (2026-07-23): Initial Stage E premortem.
- v2 (2026-07-23): Added parent-process credential recovery and proxy isolation.

## Failure Scenarios

### FS-001: Disposable Fixture, Exposed Workstation

The runner uses a temporary fixture on the workstation and calls that isolated,
while model shell commands can still read the host home or unrelated repositories.

Mitigation: require an attested disposable execution environment with no host-home,
Soane, unrelated-repository, credential-store, agent-socket, or container-control
mounts. Stop before provider invocation when topology evidence is incomplete.

### FS-002: Credential Reaches Model Shell

The Codex process receives `CODEX_API_KEY`; child environment inheritance is
stripped, but a model-generated command recovers it from parent-process metadata,
procfs, process listings, files, sockets, or diagnostics.

Mitigation: prefer a single-run credential-isolating provider proxy outside every
Codex-visible boundary. Direct-key auth remains blocked unless the exact runner
denies and proves all parent-inspection paths. Keep shell filtering and bounded
secret scans as secondary controls.

### FS-003: Hidden State Alters The Run

Saved auth, user config, project instructions, managed policy, MCP, plugins, hooks,
skills, apps, proxy variables, or session state changes tool availability or
persistence.

Mitigation: use a fresh controlled `CODEX_HOME`, an instruction-free fixture,
explicit config overrides, ignored user config/rules, and fail closed on unknown
state or events.

### FS-004: Wrapper Manufactures A Pass

The supervisor records its own evidence writes as Codex behavior, truncates a
failure, accepts unknown JSONL, or lets a correct final answer outweigh missing
containment evidence.

Mitigation: keep evidence outside Codex-visible roots, parse incrementally, use
stable reason codes, attribute writes, and require every containment gate before
checking answer quality.

### FS-005: One Call Becomes Several

Auth refresh, fallback, resume, retry, timeout recovery, or operator rerun produces
more provider requests than authorized.

Mitigation: implement a terminal one-shot state machine. Any ambiguous or failed
attempt consumes the allowance and produces a failed receipt; a new attempt needs a
new explicit authority decision.

### FS-006: Documentation And Runtime Diverge

The installed CLI ignores, rejects, or changes a required flag or configuration
key, yet the proof is interpreted against current documentation.

Mitigation: pin an approved version range and runner identity, revalidate official
sources, test command compatibility without provider use, and stop on any drift.

### FS-007: Evidence Leaks Or Outlives Its Purpose

Raw output contains the credential, sensitive diagnostics, or unnecessary model
content and is stored in normal generated artifacts.

Mitigation: apply pre-persistence byte and secret gates, quarantine bounded raw
evidence, write only redacted deterministic receipts to normal paths, and document
retention/destruction.

### FS-008: Narrow Success Becomes Broad Authorization

A single correct read-only receipt is used to approve real repositories, write
mode, retries, other models, or automatic Project Memory promotion.

Mitigation: stamp the receipt with exact executable/model/platform/fixture/time
scope, residual risks, candidate-only status, and a requirement for a separate Go.
