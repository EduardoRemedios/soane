# Intent: CLR-V0-001 First Codex CLI Read-Only Proof

## Version

v4

## Change Log

- v1 (2026-07-23): Initial Stage A intent contract.
- v2 (2026-07-23): Resolved first-cycle containment and evidence findings.
- v3 (2026-07-23): Closed parent-process credential exposure.
- v4 (2026-07-23): Compressed the locked contract to the Factory size cap.

## Purpose

Define one bounded future implementation and live proof that measures whether one
current Codex CLI invocation can answer a fixed repository question without
mutating a controlled fixture, exposing unrelated host state, or giving model
commands access to the real provider credential. `[SOURCE:RAW]`

## Goal

After explicit human authorization, implement a standard-library proof runner and
execute at most one `codex exec` model request in an attested disposable runner.
Produce a deterministic receipt separating documented controls, observed behavior,
wrapper writes, authority, project permission, authentication, cost, and review
state. `[SOURCE:RAW]`

## Source Requirements

- Revalidate only official Codex documentation listed in
  `pack/external_source_review.md` before implementation and immediately before the
  live transition. `[SOURCE:RAW]`
- External documentation is evidence, not authority. Record URLs/access dates and
  stop on semantic or installed-version drift. `[SOURCE:RAW]`

## Proof Contract

- Target: Codex CLI `codex exec`, one explicit model, one committed tiny fixture,
  one fixed prompt/schema, one invocation, zero retries, no resume or fallback.
  `[SOURCE:RAW]`
- The Soane tree is never visible to Codex. The future runner exposes only a
  non-writable, no-remote fixture inside one immutable disposable container, VM, or
  equivalent runner. Host home, unrelated repos, credential stores, agent/control
  sockets, ambient secrets, and cloud metadata are absent. `[INFERRED]`
- The exact secret-redacted command is:

```text
codex exec
  --cd <DISPOSABLE_FIXTURE>
  --sandbox read-only
  --ask-for-approval never
  --ephemeral
  --ignore-user-config
  --ignore-rules
  --json
  --output-schema <READ_ONLY_SCHEMA_PATH>
  --model <APPROVED_MODEL>
  -c web_search="disabled"
  -c shell_environment_policy.inherit="none"
  -c shell_environment_policy.experimental_use_profile=false
  -c shell_environment_policy.ignore_default_excludes=false
  -c shell_environment_policy.include_only=<APPROVED_NON_SECRET_ENV_ALLOWLIST>
  <FIXED_PROMPT>
```

- Reject arbitrary arguments and `workspace-write`, `danger-full-access`, `--yolo`,
  `--full-auto`, `--add-dir`, search, remote, resume, output-file, image, plugin,
  MCP, app, computer-use, or multi-agent paths. `[SOURCE:RAW]`
- Use a fresh runner-private `CODEX_HOME`; saved auth, login/status commands, user
  config/rules, sessions, hooks, skills, apps, MCP, and managed-policy influence are
  forbidden. Unknown state blocks. `[INFERRED]`

## Credential And Network Contract

- Authentication never implies authority or project permission. Human Go must name
  authority, project permission, model, spend ceiling, runner identity, credential
  route, and a unique one-use authorization ID. `[SOURCE:RAW]`
- Preferred route: a single-run, single-provider, destination-allowlisted credential
  proxy outside all Codex/model-visible process, filesystem, and network boundaries.
  Codex receives no real credential; model commands cannot reach the proxy.
  `[INFERRED]`
- Direct `CODEX_API_KEY` is prohibited unless the exact runner/version mechanically
  proves model commands cannot recover it through child environment, parent process,
  procfs, process listings, files, sockets, or diagnostics. Shell filtering alone
  is insufficient. `[INFERRED]`
- Provider host transport is necessary and separately authorized. Model-command
  network, web search, MCP, apps, remote tools, and other egress are forbidden.
  `[INFERRED]`

## Containment And Evidence

- The fixture has no executable hooks/dependencies, symlinks, submodules, nested
  repos, devices, secrets, provider config, instructions, or external references.
  Record canonical pre/post content/path/mode/symlink/Git manifests; any delta fails.
  `[SOURCE:RAW]`
- Parse JSONL incrementally under fixed byte/line/event/time limits. Unknown,
  approval, file-change, web, MCP, app, image, computer-use, multi-agent, or remote
  events fail. `[SOURCE:RAW]`
- Evidence crosses bounded supervisor pipes to quarantine outside Codex-visible
  roots. Detect protected credential forms before persistence; store no matched
  bytes. Record redacted command, CLI/model/platform/runner/source scope, exit,
  timing, usage, events, manifests, teardown, reason codes, and residual risks.
  `[INFERRED]`
- Correct facts cannot compensate for mutation, secret exposure, forbidden events,
  timeout, overflow, malformed output, non-zero exit, ambiguous request count, or
  incomplete teardown. `[SOURCE:RAW]`
- Receipt is generated and candidate-only. Project Memory promotion requires the
  existing Candidate Review path. `[SOURCE:REF:docs/CORE_CONCEPTS.md]`

## Principles

- Fail closed before provider use and at every later gate.
- Treat wrapper behavior, Codex behavior, and provider transport separately.
- Consume the unique authorization ID before process start; ambiguity is terminal.
- One observation applies only to its exact version/model/platform/fixture/time.
- Build one inspectable proof, not a provider, proxy, or sandbox platform.

## Roles

- Human Authority Owner: approves provider use and all live inputs.
- Proof Runner: enforces state, parses evidence, and emits the receipt.
- Isolation/Credential Supervisor: attests boundaries, controls pipes/routes, and
  tears down.
- Verification Specialist: maps VC-001 through VC-027 to evidence.
- Candidate Reviewer/Purple Gate: govern promotion and scope.

## Non-Goals

- Provider use during this planning run.
- Real repositories, writes, retries, interactive approval, arbitrary inputs, or
  additional models/providers/platforms.
- Codex install/update/login/logout or user-state inspection.
- General runner/proxy frameworks, persistence, UI, Workspace Shell, missions, or
  neighbouring-product responsibilities.
- Automatic Project Memory write or broader operational authorization.

## Acceptance Criteria

- AC-001: Planning remains `PLANNING_ONLY`; no Codex/provider/user state is invoked.
- AC-002: Exact command and prohibited-input rejection are deterministic.
- AC-003: Offline tests cover topology, credential isolation, command, manifests,
  events, one-shot state, schema/facts, ceilings, receipts, and teardown.
- AC-004: Soane/host state is invisible; fixture is isolated and non-writable.
- AC-005: Every authority/source/runtime/model/spend/auth input gates process start.
- AC-006: One authorization ID permits at most one attempt with no retry/resume.
- AC-007: Required CLI/config/tool/network controls are mechanically verified.
- AC-008: Every forbidden/unknown/ambiguous outcome yields stable non-PASS evidence.
- AC-009: Evidence is bounded, redacted, attributable, and invisible to Codex.
- AC-010: No automatic promotion or broader authorization occurs.
- AC-011: Focused/regression/knowledge/context/pack/diff checks pass.
- AC-012: Closeout states exact scope, residual risks, and at most one next proof.

## Open Questions

### BLOCKING

- None for planning. Live execution remains blocked until one exact runner and
  credential-isolation route plus every authority input passes MS-03.

### NON-BLOCKING

- A second model/platform/fixture proof is decided only from MS-05 evidence.

## Go Or No-Go Rule

Request implementation Go only after A through I2 and pack lint pass. MS-04 still
requires a distinct exact human Go. No-go on source/runtime drift, incomplete
offline coverage, unproven runner or credential isolation, missing authority,
reusable authorization, or inability to emit a terminal receipt without retry.

