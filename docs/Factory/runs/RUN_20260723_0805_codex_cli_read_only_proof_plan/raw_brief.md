# Raw Brief: First Codex CLI Read-Only Proof

## Request

Create a separate Factory planning session for the first bounded live read-only
coding proof after `LCAE-V0-001` recommended Codex CLI at documentation level.

## Authorization Posture

- Execution Mode: PLANNING_ONLY
- Planning Authorization: User agreement in the current Codex task on 2026-07-23
- Live Provider Invocation: NOT_APPROVED
- Credential, Auth, Config, Version, Or Session Inspection: NOT_APPROVED
- Downstream Fan-Out: NOT_APPROVED

This run may create planning artifacts and reconcile canonical planning state. It
must not invoke Codex CLI, inspect local Codex state, install or update Codex, make
a model request, expose credentials, or execute the future proof.

## Upstream Evidence

- `RUN_20260720_0708_live_coding_adapter_eval_refresh`
- `LCAE-V0-001`
- `docs/Factory/runs/RUN_20260720_0708_live_coding_adapter_eval_refresh/VALIDATION_CLOSEOUT_REPORT.md`
- `soane/thinking_engine/adapter_evaluation.py`
- `tests/fixtures/live_adapter_evaluation/profiles/codex_cli.json`

The upstream evaluator recommends Codex CLI only at documentation level. It does
not prove installed behavior, authentication, network containment, hook behavior,
filesystem containment, cost, latency, trace capture, or live safety.

## Planning Goal

Produce a review-ready implementation-and-proof pack for one future Codex CLI
invocation that:

1. runs against a disposable copy of a tiny committed fixture repository, never
   against the Soane working tree or another product repository;
2. asks a bounded read-only repository-understanding question with a fixed JSON
   response schema and deterministic expected facts;
3. uses explicit read-only sandboxing, ephemeral session mode, ignored user config
   and execpolicy rules, no web search, no MCP, no resume, no output file written by
   Codex, one attempt, and no retry;
4. captures JSONL events, stderr, timing, usage, exact command shape with secrets
   redacted, and before/after filesystem hashes as local evidence;
5. fails closed on any file-change event, repository hash change, unexpected tool
   class, missing structured output, source drift, version incompatibility,
   unapproved auth route, missing spend approval, or ambiguous receipt;
6. keeps the receipt and provider output candidate-only and performs no automatic
   Project Memory promotion.

## Required Distinctions

- Documentation claim versus locally measured behavior.
- Codex capability versus authentication, authority, project permission, sandbox
  policy, network policy, and Candidate Review state.
- Repository immutability versus permitted wrapper-owned evidence writes outside
  the disposable repository.
- Model-generated command containment versus Codex host-process metadata behavior.
- Planning approval versus later implementation/live-execution authorization.

## Proposed Future Proof Boundary

- Standard-library-only proof runner under `scripts/`.
- Fixed fixture repository, response schema, and expected result under `tests/fixtures/`.
- Mocked/offline runner tests before any live call.
- A preflight that records executable version compatibility, explicit auth route,
  human authority reference, project permission, and spend ceiling without
  printing secret values.
- A single live call only after all offline gates pass and a later explicit human Go
  enables execution.
- Evidence written only to the authorized Factory run evidence directory.

## Non-Goals

- No Soane code modification by Codex.
- No workspace-write or danger-full-access mode.
- No arbitrary repository, prompt, model, or command execution.
- No Cursor, SDK, Agents SDK, Codex SDK, cloud agent, multi-agent, MCP, plugin,
  browser, web-search, or external-repository proof.
- No credential provisioning, login flow, package installation, CLI update, or
  account/config/session migration.
- No automatic Project Memory write, persistence, UI, Workspace Shell, mission
  execution, or second-domain work.
- No claim that one successful proof establishes production safety.

## Go Or No-Go Rule

The pack may pass only if it defines a single inspectable command contract,
disposable-repository containment, explicit authentication and spend gates,
non-secret evidence capture, hash and event-based mutation detection, stop
conditions, candidate-only output handling, and a separate later human Go before
implementation or live invocation.
