# Intent Synthesis: CLR-V0-001

## Version

v2

## Change Log

- v1 (2026-07-23): Synthesized Stage B findings into intent v2.
- v2 (2026-07-23): Synthesized second-cycle parent-process credential findings into
  intent v3.

## Iteration: 2 of max 2

## Resolution Summary

| Stage B Finding | Resolution In Intent v2 | Status |
| --- | --- | --- |
| Host read scope is broader than the disposable fixture. | Made an attested disposable isolated runner with no host or unrelated project mounts the primary boundary. | RESOLVED |
| API credential can enter model shell subprocesses. | Locked the shell environment policy, required a non-secret offline canary, and blocked versions that cannot honor the policy. | RESOLVED |
| A stripped child can still inspect its parent Codex process for a direct key. | Preferred an external single-run credential-isolating proxy; direct-key auth now requires mechanical denial and sentinel proof for parent-process paths. | RESOLVED |
| Ignored user config does not prove empty state. | Required a fresh controlled `CODEX_HOME`, no saved auth/config, explicit overrides, and fail-closed compatibility checks. | RESOLVED |
| Raw evidence can leak data or blur write attribution. | Moved evidence behind supervisor-owned bounded pipes, added pre-persistence exact-secret rejection, quarantine, and write attribution. | RESOLVED |
| Installed CLI may drift from documented flags. | Added source and version compatibility gates before provider invocation. | RESOLVED |
| One process can still hide retries or fallback. | Required a one-shot state machine with no retry, resume, login, refresh, or model fallback; ambiguity fails. | RESOLVED |
| Unknown events or network semantics may be accepted. | Required explicit event allowlists and separate treatment of provider transport versus model-accessible tools. | RESOLVED |
| Correct task output can mask containment failure. | Kept containment and evidence gates mandatory before answer correctness. | RESOLVED |
| Receipt may be mistaken for authority. | Kept the output generated and candidate-only with separate review and Go requirements. | RESOLVED |

## Scope Assessment

- No `[SCOPE EXPANSION]` was introduced.
- Isolation supervision is a necessary containment correction to the already scoped
  live proof, not a general execution-platform feature.
- The implementation remains one provider, one fixture, one command, one model
  invocation, one receipt, and no automatic promotion.

## Locked Planning Position

The future proof is allowed to proceed to implementation planning only if it can
make both mutation and confidentiality claims narrowly. A disposable fixture alone
is insufficient, and child environment filtering alone is insufficient. The bounded
product is therefore a one-shot proof runner plus the smallest exact runner and
credential-isolation adapters needed for the approved mechanism, not a reusable
provider, proxy, or sandbox platform.

## Residual Questions For Purple

- Confirm that making the isolated runner a hard execution precondition is a
  containment correction rather than unapproved platform scope.
- Confirm that inability to attest runner topology or shell-environment isolation
  is a hard no-go, even when Codex would otherwise run read-only.
