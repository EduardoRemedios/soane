# Verification Plan: CLR-V0-001

## Version

v2

## Change Log

- v1 (2026-07-23): Initial Stage F verification plan.
- v2 (2026-07-23): Added parent-process and proxy credential-isolation proof.

## Strategy

Verification has two irreversible phases:

1. Offline V1/V2/V3 checks prove construction, isolation, parsing, one-shot state,
   and receipt semantics without a credential or provider invocation.
2. One V4 observation is permitted only after every offline and authority gate
   passes. Any attempted invocation consumes the allowance and is never retried.

## Verification Tiers

- V0: artifact assertion only
- V1: static or mechanical local check
- V2: focused fixture or unit/integration test without provider use
- V3: repository regression suite
- V4: authorized live or external observation

## Offline Required Checks

| Check ID | Tier | Required Proof |
| --- | --- | --- |
| VC-001 | V2 | Allowed topology exposes only the read-only fixture and runner-private runtime; host-home, Soane, unrelated repositories, credential stores, agent sockets, and control sockets are absent. |
| VC-002 | V1 | Runner identity is immutable and mount/environment topology is serialized before any credential is accepted. |
| VC-003 | V2 | A secret-shaped sentinel is absent from child environment and cannot be recovered through parent-process environment, procfs, process listings, credential files/sockets, or crash diagnostics. |
| VC-004 | V2 | Credential route is either a single-run/single-provider proxy outside Codex/model visibility with model-command network denied, or direct-key auth with mechanical proof for every parent-inspection path. Locked shell policy still uses `inherit="none"`, profile use false, default secret exclusions enabled, and only the committed non-secret allowlist. |
| VC-005 | V2 | Exact and committed common reversible credential forms crossing stdout/stderr are rejected before persistence; no matching bytes appear in artifacts. |
| VC-006 | V2 | Controlled `CODEX_HOME` starts empty, has no saved auth/config/session state, and is runner-private. |
| VC-007 | V2 | Command builder emits only the locked arguments and rejects arbitrary prompt, repo, schema, output, retry, resume, remote, search, write, or extra flags. |
| VC-008 | V2 | Unknown config, managed-policy influence, extra tool surfaces, and pre-existing controlled-home state block invocation. |
| VC-009 | V2 | Canonical pre/post manifests detect content, path, mode, symlink, Git status, and untracked-file deltas. |
| VC-010 | V2 | File-change events fail even when manifests and final facts otherwise look valid. |
| VC-011 | V2 | Evidence destination is outside Codex-visible roots and only the supervisor writes it through bounded pipes. |
| VC-012 | V2 | Raw-evidence quarantine, redacted receipt, retention outcome, and runner teardown are explicit and deterministic. |
| VC-013 | V2 | One-shot state machine atomically consumes a unique live-authorization ID before process start and never retries, resumes, refreshes auth, falls back models, or permits a second attempt after any terminal outcome. |
| VC-014 | V1 | Official source URLs and access date are revalidated and compared with the locked command semantics. |
| VC-015 | V2 | Approved CLI/version capability fixture supports every required flag/config key using only credential-free/network-denied `codex --version` and `codex exec --help` probes inside the isolated runner; any prompted `codex exec` or drift blocks. |
| VC-016 | V2 | Event allowlist accepts only normalized read-only lifecycle/command/message events and rejects unknown, approval, file-change, web, MCP, app, remote, image, computer-use, and multi-agent classes. |
| VC-017 | V2 | Timeout, overflow, malformed JSONL/schema, non-zero exit, wrong facts, missing usage, and ambiguous request count each produce stable non-PASS receipts. |
| VC-018 | V2 | Only after all containment gates pass does the final object validate against the schema and exact expected fixture facts. |
| VC-019 | V2 | Missing authority, project permission, auth route, model, spend ceiling, runner identity, source gate, or offline-gate evidence prevents process start. |
| VC-020 | V2 | Receipt is generated, candidate-only, narrowly scoped, and cannot invoke Project Memory promotion or authorize another run. |
| VC-027 | V3 | Focused tests, full repository tests, knowledge lint, context refresh/report, pack lint, and diff checks pass. |

## Live Required Checks

| Check ID | Tier | Required Proof |
| --- | --- | --- |
| VC-021 | V4 | The observed runner identity/topology matches the approved immutable evidence and teardown is recorded. |
| VC-022 | V4 | Codex/model-command evidence shows no real credential visibility; the proxy or mechanically proven direct route remains bounded; persisted streams/receipt contain no protected credential form. |
| VC-023 | V4 | Pre/post fixture manifests and Git status are identical and no file-change event occurred. |
| VC-024 | V4 | Exactly one Codex process/model attempt is observed; reported request/usage ambiguity fails without retry. |
| VC-025 | V4 | No forbidden or unknown event occurs; only provider transport needed by Codex is used. |
| VC-026 | V4 | Receipt records all preflight references, redacted command, executable/model/platform/source scope, bounded evidence, outcome, residual risks, and candidate-only status. |

## Live Entry Gate

The V4 transition is forbidden unless VC-001 through VC-020 and VC-027 pass, the
run is explicitly changed to execution-enabled by an approved Factory process, and
a human Go supplies all authority inputs. This planning pack itself cannot cross
the gate.

## Acceptance Standard

CLR-V0-001 succeeds only when VC-001 through VC-027 pass. Any live failure remains
useful evidence but produces a failed receipt and consumes the single invocation.
