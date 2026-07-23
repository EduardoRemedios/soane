# Intent Red Team: CLR-V0-001

## Version

v2

## Change Log

- v1 (2026-07-23): Initial Stage B adversarial review.
- v2 (2026-07-23): Second-cycle review added parent-process credential recovery.

## Iteration: 2 of max 2

## Findings

| Severity | Finding | Why It Matters | Fix Recommendation |
| --- | --- | --- | --- |
| Critical | `--sandbox read-only` prevents model-generated writes but does not prove that model-generated commands can read only the fixture. | A disposable fixture protects repository integrity but still leaves unrelated host files, credentials, sockets, and user state potentially readable. | Require an attested disposable execution environment with no host home, Soane tree, credential store, Docker socket, or unrelated project mounts. Expose only the fixture read-only plus a wrapper-owned evidence destination that is not visible to Codex. |
| Critical | Passing `CODEX_API_KEY` to the Codex process can expose it to model-generated shell subprocesses unless shell inheritance is explicitly constrained. | The model could accidentally or maliciously print the credential into JSONL, stderr, or provider-visible context. | Lock `shell_environment_policy.inherit="none"`, an exact `include_only` allowlist, `experimental_use_profile=false`, and default secret exclusions. Prove the policy offline with a non-secret canary before any credentialed invocation; stop if the installed CLI cannot honor it. |
| Critical | Even with child environment filtering, a model shell command may recover a direct API key from its parent Codex process through `/proc`, `ps`, process APIs, files, sockets, or crash diagnostics. | Stage B v1 treated environment stripping as complete credential isolation, but it only controls inheritance and does not constrain every parent-inspection path. | Prefer a single-run credential-isolating provider proxy outside every Codex-visible boundary. Prohibit direct-key auth unless the exact runner/version mechanically denies and proves all parent-inspection routes with a sentinel. Treat stream scanning as detection, not prevention. |
| High | `--ignore-user-config` and `--ignore-rules` do not alone establish an empty configuration, state, MCP, plugin, hook, skill, or managed-policy surface. | Hidden configuration can add tools, instructions, persistence, or behavior that invalidates the proof. | Use a newly created controlled `CODEX_HOME`, reject pre-existing contents, forbid mounted auth/config state, pass explicit disabling overrides, and record the exact controlled config. Treat any unknown or managed configuration influence as a blocker. |
| High | Wrapper evidence writes and raw stream capture can become a side channel or be mistaken for Codex writes. | A proof could leak sensitive output or report its own artifacts as provider mutation. | Keep evidence outside Codex-visible roots, stream through byte/event ceilings and exact-secret detection before persistence, separate raw/quarantined evidence from the redacted receipt, and attribute every write to the wrapper. |
| High | A locally documented command may not match the installed CLI version. | Unsupported, renamed, ignored, or differently scoped flags can create false assurance. | Add a no-provider compatibility preflight against an approved version range and committed capability fixture; do not discover auth or user state. Revalidate official sources immediately before execution and fail on drift. |
| High | An invocation may fail before a model request, while retry logic or auth recovery silently creates a second attempt. | "One process" and "one billed/provider request" are not equivalent, and automatic recovery can breach spend or authority. | Implement a one-shot state machine with no retry, resume, login, refresh, or fallback; record process-start and observed request/usage evidence, and classify ambiguity as failure rather than retrying. |
| High | Unknown JSONL events, provider-network semantics, or approval behavior could be interpreted permissively. | A new event class or tool path could bypass the intended no-web/no-external-tool boundary. | Maintain an explicit event allowlist, require `--ask-for-approval never`, fail on approval requests and unknown events, and distinguish the required Codex provider request from model-accessible network tools. |
| Medium | Correct fixture facts could dominate the result even when containment evidence is incomplete. | Task quality is not proof of read-only containment. | Make containment, credential, configuration, invocation-count, and evidence-integrity gates independently mandatory; score answer correctness only after they pass. |
| Medium | A successful receipt could be treated as operational authorization or accepted Project Memory. | One bounded observation does not grant broader authority or establish a durable truth. | Emit a generated candidate receipt with exact scope and residual risks; require existing Candidate Review for promotion and a new Go for any broader use. |

## Agent Failure Modes

- Runs Codex on the workstation because the fixture itself is disposable.
- Assumes `read-only` means "fixture-only reads."
- Inherits `CODEX_API_KEY`, proxy variables, `HOME`, or `CODEX_HOME` into model shell commands.
- Reads the Codex parent process environment after child inheritance was stripped.
- Uses existing CLI login state because it avoids an environment variable.
- Creates a controlled config under the user's real `CODEX_HOME`.
- Lets Codex see the evidence directory or output schema through a writable mount.
- Persists raw output before applying size and secret-leak gates.
- Treats an unfamiliar JSONL event as harmless progress.
- Retries after an auth, schema, timeout, or transient provider failure.
- Interprets a correct answer as a passing proof despite missing containment evidence.
- Promotes the receipt or broadens adapter use without a separate authority decision.

## Verification Holes Closed By Synthesis

- Add an isolated-runner topology fixture and mount allowlist/denylist tests.
- Add shell-environment policy construction tests plus a non-secret subprocess canary.
- Add parent-process, procfs, process-list, file/socket, and crash-path sentinel
  tests; add proxy-route isolation and single-destination/single-attempt fixtures.
- Add controlled-`CODEX_HOME`, forbidden-state, and unknown-config fixtures.
- Add exact-secret streaming rejection tests without persisting the secret.
- Add one-shot state-machine tests covering auth failure, timeout, malformed output,
  unknown events, and apparent transient errors.
- Add pre/post fixture manifests and wrapper-write attribution tests.
- Add version/source compatibility, provider-network distinction, and no-promotion
  receipt checks.
