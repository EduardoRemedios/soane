# Verification Plan

## Version

v1

## Change Log

- v1 (2026-06-30): Initial planning-only verification plan.

## Verification Tiers

- V0: Artifact exists.
- V1: Static content check.
- V2: Factory V2 scaffold lint.

## Checks

| Check | Tier | Command Or Review |
| --- | --- | --- |
| Research synthesis exists | V0 | `test -s docs/research/PROJECT_MEMORY_RESEARCH_SYNTHESIS.md` |
| Factory knowledge lint passes | V2 | `bash scripts/knowledge_lint.sh` |
| Context index rebuilds | V2 | `./scripts/factoryctl context-index` |
| Markdown diff has no whitespace errors | V1 | `git diff --check` |
| Synthesis includes required distinctions | V1 | Review sections in synthesis |
