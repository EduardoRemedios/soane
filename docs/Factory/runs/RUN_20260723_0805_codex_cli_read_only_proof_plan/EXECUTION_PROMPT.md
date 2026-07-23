# Execution Prompt: CLR-V0-001 Offline Proof Runner

## Version

v1

## Change Log

- v1 (2026-07-23): Generated after Stage I2 PASS and human offline-implementation Go.

## Run Metadata

- RUN_ID: `RUN_20260723_0805_codex_cli_read_only_proof_plan`
- Sprint ID: `CLR-V0-001`
- Created: 2026-07-23 09:45 local
- Source Pack: `docs/Factory/runs/RUN_20260723_0805_codex_cli_read_only_proof_plan/pack/`

## Purpose

Implement MS-00 through MS-03 only: deterministic offline tests, proof core, one
Docker/OCI runner-attestation contract, one external credential-proxy attestation
contract, and a generated offline execution candidate. Do not invoke Docker, Codex,
a provider, credentials, or user state. MS-04 remains separately gated.

## Required Read Order

1. `docs/PROJECT_STATE.md`
2. `docs/ROADMAP.md`
3. `docs/Factory/ORCHESTRATION.md`
4. `docs/Factory/SCRATCHPAD.md` (`## Active Pitfalls (Mandatory)` only)
5. `pack/intent.md`
6. `pack/intent_lock_report.md`
7. `pack/risk_register.md`
8. `pack/verification_plan.md`
9. `pack/traceability_matrix.md`
10. `pack/verification_manifest.yaml`
11. `pack/micro_sprints.md`
12. `pack/CLR-V0-001_ENVELOPE.md`
13. `pack/PACK_AUDIT_REPORT.md`

## Skill Routing Contract

- Use the `factory-execution-closeout` skill for final execution reconciliation.
- No dedicated skill applies to implementation; execute via the locked pack.

## Hard Guardrails

- Implement only MS-00 through MS-03.
- Do not invoke or inspect Docker, Codex, provider/model endpoints, credentials,
  authentication, user config, sessions, keychains, plugins, MCP, or external repos.
- Use standard-library Python and committed fixtures only.
- The single concrete runner contract is Docker/OCI with an immutable digest,
  read-only fixture, fresh private runtime, and no host/Soane mounts or sockets.
- The single credential contract is an externally supplied, single-run,
  single-provider proxy attestation. Do not build or run a proxy.
- Direct-key auth is fail-closed unless every child and parent inspection path is
  proven denied; this implementation must emit it as blocked, not improvise.
- Produce a BLOCKED offline candidate when runner, credential, authority, model,
  spend, source, or compatibility evidence is incomplete.
- Do not add a provider framework, runner registry, generic proxy, persistence,
  Project Memory promotion, UI, mission, or neighbouring-product behavior.

## SIMPLE-CODE-GATE (v2)

- Implement the smallest clear local change.
- Prefer immutable dataclasses, enums, pure validation, stable reason codes, and
  structured JSON over clever abstractions or string heuristics.
- No dependency creep, silent failures, broad passthrough, hidden side effects,
  generic registries, strategy layers, or premature extension points.
- Fail closed for invalid configuration and preserve evidence-chain integrity.

## Micro-Sprint Execution Sequence

1. MS-00: add the committed tiny fixture and failing focused tests for VC-001
   through VC-020.
2. MS-01: implement exact command construction, manifests, event policy, bounded
   evidence checks, one-shot state, schema/fact validation, and receipts.
3. MS-02: implement Docker/OCI and external credential-proxy attestation validation
   without subprocess or network execution.
4. MS-03: emit a deterministic offline execution candidate and stop BLOCKED unless
   every live input is supplied and validated.

## Verification Contract

- Execute every check in `pack/verification_manifest.yaml` in order.
- Treat every `halt_on_failure: true` failure as a stop condition.
- Record evidence in `VALIDATION_CLOSEOUT_REPORT.md`.
- VC-021 through VC-026 remain `NOT_RUN_UNAUTHORIZED`; do not weaken or simulate
  them as live proof.

## Troubleshooting And Failure Policy

- Stop on schema or contract drift and reconcile the pack before more code.
- Never resolve missing live inputs by reading environment or local user state.
- A BLOCKED execution candidate is a valid offline result.
- Do not retry or cross MS-04 to improve the result.

## Final Exit Checklist

- [ ] MS-00 through MS-03 delivered within file budgets.
- [ ] SIMPLE-CODE-GATE v2 satisfied.
- [ ] VC-001 through VC-020 and VC-027 have offline evidence.
- [ ] VC-021 through VC-026 are explicitly unauthorized/not run.
- [ ] No Docker, Codex, provider, credential, or user-state access occurred.
- [ ] Canonical docs and validation closeout are truthful.
- [ ] MS-04 remains blocked behind a separate human Go.
