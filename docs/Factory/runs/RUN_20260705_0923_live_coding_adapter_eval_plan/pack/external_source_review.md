# External Source Review: Live Coding Adapter Surfaces

## Version

v1

## Change Log

- v1 (2026-07-05): Initial bounded source review for Stage A-F planning.

## Source Allowlist

- OpenAI official Codex manual fetched locally through the `openai-docs` skill helper.
- OpenAI official developer docs under `https://developers.openai.com/`.
- OpenAI official platform docs under `https://platform.openai.com/`.
- Cursor official docs under `https://cursor.com/docs/`.
- Cursor official cookbook repository at `https://github.com/cursor/cookbook`.

## Source Notes

| Surface | Sources Reviewed | Planning-Relevant Notes |
| --- | --- | --- |
| Codex CLI | `https://developers.openai.com/codex/cli`, local Codex manual `CLI command reference`, `Non-interactive mode`, `Agent approvals & security`, `Authentication and sessions` | Codex CLI can operate in a local repository, supports interactive TUI and non-interactive `codex exec`, exposes sandbox and approval flags, supports JSONL events and output schemas in non-interactive mode, and has explicit auth and credential-handling guidance. |
| Codex SDK | Local Codex manual `Codex SDK` | Codex SDK has TypeScript and Python library paths for controlling Codex programmatically. Python controls the local app-server and exposes sandbox presets. |
| Cursor CLI | `https://cursor.com/docs/cli/overview`, `https://cursor.com/docs/cli/using` | Cursor CLI supports terminal agent work, command approval, worktrees, history/resume, cloud handoff, and non-interactive output formats. Cursor docs state non-interactive mode has full write access, making mutation control a critical evaluation gate. |
| Cursor SDK | `https://cursor.com/docs/sdk/typescript`, `https://github.com/cursor/cookbook` | Cursor SDK is a TypeScript API for running Cursor's coding agent from apps, scripts, and workflows. Official cookbook describes local and cloud runtimes, streamed events, prompts, models, cancellation, artifacts, and conversation state. |
| OpenAI SDK | `https://developers.openai.com/api/docs/libraries`, `https://developers.openai.com/api/docs/guides/migrate-to-responses`, `https://developers.openai.com/api/reference/overview/` | Official SDKs support the Responses API, which is recommended for new model/tool integrations. This is a model/tool invocation surface, not a coding-agent harness by itself. |
| OpenAI Agents SDK | `https://developers.openai.com/api/docs/guides/agents`, `https://developers.openai.com/api/docs/guides/agents/integrations-observability` | Agents SDK is appropriate when the application owns orchestration, tool execution, approvals, and state. It includes tracing for model calls, tool calls, handoffs, guardrails, and custom spans. |

## Planning Implications

- Codex CLI is the strongest first candidate for a CLI-backed live proof because `codex exec` has documented non-interactive mode, read-only default behavior, JSONL events, output schemas, and explicit sandbox/approval controls.
- Cursor CLI remains a candidate but requires stricter guardrails because official docs state non-interactive mode has full write access.
- OpenAI SDK is best evaluated as a direct model/tool invocation adapter, not as a coding-agent executor.
- OpenAI Agents SDK is best evaluated after Soane needs application-owned orchestration, human review, and trace semantics beyond a single model/tool request.
- Cursor SDK is promising for programmatic coding-agent workflows, but its local/cloud runtime, API key, streamed events, and mutation behavior need a stricter safety review before live use.
- No live invocation should occur until Soane can record Provider Invocation, Capability Reference, authority, policy/privacy context, input/output refs, cost/latency/confidence, evidence/trace refs, and candidate-only output.
