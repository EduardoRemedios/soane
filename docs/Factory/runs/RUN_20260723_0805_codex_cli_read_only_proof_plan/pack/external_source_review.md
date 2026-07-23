# External Source Review: Codex CLI Read-Only Proof Controls

## Version

v3

## Change Log

- v1 (2026-07-23): Initial official-source review for CLR-V0-001 planning.
- v2 (2026-07-23): Added shell-environment and narrow-permission findings from
  Stage B source revalidation.
- v3 (2026-07-23): Added official automation credential-proxy guidance and direct
  environment-key limitations.

## Review Method

- Access date: 2026-07-23
- Evidence kind: official OpenAI documentation only
- Source allowlist: `https://developers.openai.com/codex/` and official
  `https://learn.chatgpt.com/docs/` redirects
- No Codex CLI, provider, model, credential, auth state, config, installed version,
  session, network client, or external repository was invoked or inspected.

## Sources And Planning Implications

| Source | Documented Evidence | Planning Implication |
| --- | --- | --- |
| `https://developers.openai.com/codex/noninteractive/` | `codex exec` is the non-interactive surface; default sandbox is read-only; `--ephemeral` avoids rollout persistence; `--json` emits JSONL; `--output-schema` constrains the final response. Automation guidance recommends the Codex GitHub Action because it starts a Responses API proxy to reduce API-key exposure, and limits direct `CODEX_API_KEY` use to one invocation where no untrusted code shares the environment. | Require explicit read-only, ephemeral, JSONL, and schema flags rather than relying on defaults. Prefer an external credential-isolating proxy; do not infer that shell environment filtering protects a direct parent-process key. |
| `https://developers.openai.com/codex/cli/reference/` | `--cd` sets the workspace root; `--sandbox` accepts read-only/workspace-write/danger-full-access; `--ask-for-approval` accepts `never`; `--ignore-user-config` and `--ignore-rules` are available; `--output-schema` validates final shape. | Lock the exact command; reject broader modes, resume, extra dirs, output-file writes, and arbitrary flags. |
| `https://developers.openai.com/codex/config-reference/` | Top-level `web_search` supports `disabled`; config can define MCP servers and hooks; sandbox mode governs model-generated command filesystem/network access. `shell_environment_policy` supports `inherit`, `include_only`, `exclude`, profile use, and default secret filtering. Named permission profiles can express path-level read/write/deny rules. | Pass `web_search="disabled"`, ignore user config, use a fixture with no project config, fail on external tool events, and lock model subprocess inheritance to a non-secret allowlist. Do not assume named profiles constrain `codex exec` without installed-version proof. |
| `https://developers.openai.com/codex/auth/` | CLI supports ChatGPT or API-key auth; cached credentials may live under `CODEX_HOME` or a credential store. | Prefer one-process API-key auth; prohibit saved-auth inspection and secret persistence. |

## Material Limitations

- Documentation does not prove the installed executable supports the required flags.
- Read-only sandbox documentation concerns model-generated command policy; it does
  not prove a fixture-only read boundary or that the Codex host process writes
  nothing outside the repository.
- `--ephemeral` addresses rollout persistence, not every possible cache, log, token
  refresh, or host metadata write.
- `--ignore-user-config` does not remove authentication use of `CODEX_HOME`.
- The CLI reference documents named permission profiles for low-level sandbox debug
  commands, but the reviewed `codex exec` option table does not establish a
  permission-profile flag. The plan therefore cannot rely on named profiles to
  narrow host read scope.
- Documented shell-environment filters still require installed-version and
  behavior evidence before they can protect a real credential.
- Official direct-key guidance does not prove that a model-generated command cannot
  inspect the parent Codex process. This plan therefore applies a stronger
  inferred credential-isolation gate.
- Provider network traffic is necessary for a live proof and is not equivalent to
  permitting web search, MCP, or arbitrary egress.
- A fixed fixture can reduce credential-exposure risk but cannot prove all hostile
  repository scenarios.
- Official documentation can change between planning and execution.

## Source Gate

Implementation and live execution must each re-open these exact sources. If a
required flag disappears, changes meaning, or becomes incompatible with the locked
command, execution stops for pack review. Documentation evidence remains distinct
from the later measured receipt.
