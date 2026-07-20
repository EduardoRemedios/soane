# External Source Review: Live Coding Adapter Surfaces

## Version

v2

## Change Log

- v1 (2026-07-05): Initial bounded official-source review in the upstream planning run.
- v2 (2026-07-20): Refreshed official sources and recorded contradictions and adjacent Codex SDK evidence.

## Review Method

- Access date: 2026-07-20
- Evidence kind: official documentation only
- No provider, CLI, SDK, API, model, cloud agent, auth, credential, config, or session was invoked or inspected.
- Documentation claims remain subject to implementation-time revalidation.

## Source Allowlist

- OpenAI Codex documentation under `https://developers.openai.com/codex/` and its official `https://learn.chatgpt.com/docs/` redirects.
- OpenAI API documentation under `https://developers.openai.com/api/`.
- OpenAI Agents SDK documentation under `https://openai.github.io/openai-agents-python/`.
- Cursor documentation under `https://cursor.com/docs/` and `https://docs.cursor.com/`.
- Cursor first-party product material under `https://cursor.com/blog/`.

## Source Notes

| Surface | Official Sources Reviewed | Current Planning Evidence | Contradiction Or Limitation |
| --- | --- | --- | --- |
| Codex CLI | `https://developers.openai.com/codex/cli/reference/`, `https://developers.openai.com/codex/security/` | `codex exec` documents working-directory control, newline-delimited JSON events, output schemas, ephemeral rollout mode, resume identity, and `read-only`, `workspace-write`, or `danger-full-access` sandbox values. | Documentation evidence does not prove local policy, network isolation, credential handling, hook behavior, or zero filesystem writes by a live run. |
| Cursor CLI | `https://docs.cursor.com/en/cli/reference/parameters`, `https://docs.cursor.com/en/cli/headless`, `https://docs.cursor.com/en/cli/using` | Official pages document non-interactive text/JSON/stream-JSON output, resume identity, command controls, and `--force`. | Official pages conflict: one says print mode has write/bash tools or full write access, while another says changes without `--force` are proposed rather than applied. Read-only containment is therefore unproven and blocked. |
| Cursor SDK | `https://cursor.com/docs/sdk/typescript`, `https://cursor.com/blog/typescript-sdk` | Public-beta TypeScript SDK supports local and cloud agents, streamed events, reconnectable runs, dedicated cloud VMs, repository cloning, branches, and pull requests. | A hard read-only mode and exact local mutation boundary were not established by reviewed sources. Cloud mode is inherently an external repository/runtime operation and is out of scope here. |
| OpenAI SDK | `https://developers.openai.com/api/docs/libraries`, `https://developers.openai.com/api/docs/guides/responses-vs-chat-completions` | Official SDKs invoke the Responses API and automatically use API-key configuration; this is a model/tool surface rather than a coding-agent harness. | It does not supply repository sandbox, coding context, approval, or patch governance by itself. |
| OpenAI Agents SDK | `https://openai.github.io/openai-agents-python/`, `https://openai.github.io/openai-agents-python/human_in_the_loop/`, `https://openai.github.io/openai-agents-python/tracing/` | SDK supports agents, tools, handoffs, sessions, guardrails, human approval, serializable run state, and traces across model/tool/guardrail/handoff events. | The application owns orchestration and tool policy. Traces may include sensitive model and tool data by default, and approval/state handling needs explicit privacy and persistence policy. |

## Adjacent Evidence: Codex SDK

`https://developers.openai.com/codex/sdk/` now documents TypeScript and Python SDKs with resumable threads; the Python SDK exposes `read_only`, `workspace_write`, and `full_access` sandbox presets. This makes Codex SDK a credible later candidate, but adding it would expand the locked five-surface evaluation and is deferred.

## Refresh Conclusions

- Codex CLI has the strongest documentation-level fit for a future read-only coding proof, but the evaluator must derive that result rather than encode it.
- Cursor CLI must be blocked on `source_contradiction` and `hard_read_only_unproven` until a separate authorized proof resolves behavior.
- Cursor SDK must be blocked for the first live read-only proof unless a hard local read-only contract becomes official and is independently verified.
- OpenAI SDK remains a model/tool invocation surface, not a coding-agent executor.
- OpenAI Agents SDK remains an orchestration surface whose trace privacy, approvals, state, and tool policies require a larger application-owned contract.
- No documentation claim authorizes live use, credential access, repository mutation, or automatic Project Memory promotion.
