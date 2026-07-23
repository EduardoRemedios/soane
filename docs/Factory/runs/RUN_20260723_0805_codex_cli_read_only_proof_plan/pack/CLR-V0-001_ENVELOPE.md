# Sprint Envelope: CLR-V0-001 First Codex CLI Read-Only Proof

## Version

v3

## Change Log

- v1 (2026-07-23): Initial Stage H sprint envelope.
- v2 (2026-07-23): Added parent-process credential isolation and bounded proxy route.
- v3 (2026-07-23): Restricted compatibility probes and made live authorization
  atomically single-use.

## Sprint ID

`CLR-V0-001`

## Execution Mode

`PLANNING_ONLY`

This pack authorizes neither implementation nor provider use. A future human Go may
authorize MS-00 through MS-03. MS-04 additionally requires a distinct explicit Go
for the exact one-call provider transition and all authority inputs in the locked
intent. That transition must have a unique authorization ID consumed atomically
before process start.

## Objective

Implement and evaluate the smallest one-shot proof that can observe whether one
approved Codex CLI version/model answers a fixed repository-understanding question
without mutating a tiny fixture or escaping a narrowly attested disposable runner.
The live transition is also required to keep the real provider credential outside
every Codex/model-command-visible boundary.

## In Scope

- One standard-library proof core for exact command construction, manifests,
  normalized event policy, bounded streams, one-shot state, schema/fact checks, and
  deterministic receipts.
- One exact isolation-supervisor adapter for a human-approved immutable disposable
  runner mechanism.
- One exact credential-isolation adapter: preferably a single-run provider proxy
  outside Codex visibility; direct-key auth is allowed only with mechanical denial
  evidence for all parent-process inspection paths.
- One fresh controlled `CODEX_HOME`, one locked model-shell environment policy, and
  one offline non-secret sentinel canary.
- One committed tiny fixture, fixed prompt, fixed output schema, and exact expected
  facts.
- Source/runtime compatibility checks that do not inspect user auth/config/session
  state.
- One execution-candidate report after all offline gates.
- At most one later human-authorized `codex exec` model invocation with no retry,
  resume, fallback, auth recovery, or automatic rerun.
- Bounded quarantined raw evidence, a redacted generated receipt, teardown evidence,
  validation closeout, and canonical state updates.

## Out Of Scope

- Running Codex against Soane, another real repository, a worktree, external repo,
  or arbitrary path.
- Supporting arbitrary prompts, fixtures, schemas, models, flags, retries, output
  paths, provider surfaces, or runner backends.
- Workspace-write, danger-full-access, interactive approval, `--yolo`, `--full-auto`,
  `--add-dir`, search, remote mode, resume, plugins, MCP, apps, images, computer use,
  or multi-agent tools.
- Installing, updating, authenticating, logging out, or configuring Codex in user
  state.
- Reading saved auth, keychains, user config, histories, sessions, profiles,
  memories, plugins, MCP servers, hooks, apps, or rules.
- Provisioning a reusable sandbox/provider platform.
- Building a reusable or multi-provider credential proxy.
- Writing to Project Memory, automatic Candidate Review, product UI, Workspace
  Shell, persistence, mission execution, or neighbouring portfolio-product work.

## File-Touch Budget

| Micro-Sprint / Area | Max Created | Max Modified | Max Deleted |
| --- | ---: | ---: | ---: |
| MS-00 fixtures and focused tests | 7 | 0 | 0 |
| MS-01 pure proof core and tests | 2 | 2 | 0 |
| MS-02 runner/credential isolation and tests | 3 | 3 | 0 |
| MS-03 offline gate/report integration | 1 | 2 | 0 |
| MS-04 generated live evidence and receipt | 4 | 0 | 0 |
| MS-05 closeout and canonical state | 1 | 3 | 0 |
| Sprint total | 18 | 10 | 0 |

- Maximum unique source/test/docs files touched or added: 22.
- Maximum generated live evidence files: 4.
- Maximum total persistent files: 26.
- Values below Factory guidance are deliberate because each micro-sprint owns one
  narrow proof boundary and reuses shared files.

Generated transient runner files and quarantined streams do not count as repository
source files but must stay within the four-file generated-evidence ceiling. Crossing
any budget requires a new planning review before edits continue.

## Required Micro-Sprints

- MS-00 Executable Contract And Test Scaffold
- MS-01 Pure Proof Core
- MS-02 Exact Runner And Credential Isolation
- MS-03 Offline Gate And Execution Candidate
- MS-04 Human Live Gate And One-Shot Observation
- MS-05 Review And Validation Closeout

## Implementation Constraints

- Apply SIMPLE-CODE-GATE v2.
- Prefer one cohesive module plus one narrow supervisor adapter over a provider
  framework.
- Keep pure policy/state/receipt functions injectable and testable without
  subprocess, environment, network, or wall-clock side effects.
- Use structured JSON parsing and canonical manifests; do not infer safety from
  command names or ad hoc string matching.
- Runtime compatibility probing is limited to credential-free, network-denied
  `codex --version` and `codex exec --help` inside the approved isolated runner. A
  prompted `codex exec`, model catalog call, doctor/status/login command, or broader
  probe is forbidden.
- Permit exactly one approved runner mechanism. Do not add a runner registry,
  plugin system, provider interface, or general command passthrough.
- Permit exactly one credential route. The real provider credential must remain
  outside Codex/model visibility unless direct-key parent isolation is mechanically
  proven. A proxy must be single-run, single-provider, destination allowlisted, and
  unreachable from model-generated commands.
- The Soane tree is fixture source only and is never visible inside the live runner.
- Model-generated subprocesses must not inherit credential, home, proxy, or user
  state.
- The evidence destination must remain outside Codex-visible roots.
- Any attempted MS-04 invocation consumes the allowance regardless of outcome.
- A unique live-authorization ID is persisted as consumed before process launch.
  Process-start ambiguity is terminal and cannot restore or reuse the ID.
- Provider output remains generated and candidate-only. Capability does not imply
  authority, and a receipt does not authorize another run.

## Required Verification

Before MS-04, run at minimum:

```bash
python3 -m unittest tests/test_thinking_engine_codex_read_only_proof.py
python3 -m unittest discover -s tests
bash scripts/knowledge_lint.sh
./scripts/factoryctl context-index
./scripts/factoryctl context-report --profile stage-a --scope RUN_20260723_0805_codex_cli_read_only_proof_plan --output docs/Factory/runs/RUN_20260723_0805_codex_cli_read_only_proof_plan/IMPLEMENTATION_CONTEXT_REPORT.md
git diff --check
```

After MS-04 or a blocked live gate, repeat focused/full tests, knowledge lint, context
refresh/report, and diff checks. Run:

```bash
./scripts/factoryctl pack-lint --run RUN_20260723_0805_codex_cli_read_only_proof_plan
```

Verification must map VC-001 through VC-027 to test, report, receipt, and live
evidence paths. `pack/verification_plan.md` and `pack/traceability_matrix.md` are
normative.

## Stop Gates

- Stop if the exact runner identity/topology is unavailable or any host home,
  Soane/unrelated repository, credential store, agent socket, or control socket is
  visible.
- Stop if the shell sentinel reaches a model-generated subprocess or the installed
  CLI cannot honor the locked environment policy.
- Stop if a direct key is recoverable through parent-process/procfs/process-list/
  file/socket/crash paths, or if a credential proxy is visible/reachable from model
  commands, has multiple destinations, or can serve more than the one attempt.
- Stop if user/managed/project state or an extra tool surface can influence the run.
- Stop if any offline VC fails, Soane is dirty at the live boundary, official source
  semantics drift, or the exact CLI capability contract is unsupported.
- Stop if authority, project permission, auth route, model, spend ceiling, runner
  identity, unique unused authorization ID, or explicit MS-04 Go is absent.
- Stop on the first provider-process attempt under every outcome. Never retry.
- Stop and fail on secret bytes, unknown/forbidden events, approval requests,
  mutation, timeout, output overflow, malformed output, non-zero exit, wrong facts,
  ambiguous request count, or incomplete teardown.
- Stop if implementation becomes a reusable platform, touches Project Memory
  promotion, or broadens repository/provider/model/fixture scope.

## Review Handoff

MS-05 must produce a validation closeout that states the exact observed executable,
model, platform, runner, fixture, command, time, usage, mutation result, event
result, teardown result, candidate status, and residual risks. It must recommend at
most one separately planned next proof and cannot execute it.
