# Verification Plan

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage F verification plan.

## Strategy

Verify Socratic Discovery v0 with deterministic local fixtures and unit tests before any wrapper, persistence, live integration, product shell, or live model work.

## Verification Tiers

- V0 artifact proof
- V1 static or mechanical check
- V2 focused fixture or unit test
- V3 regression suite
- V4 live or external proof

## Required Checks

| Check ID | Tier | Required Proof |
| --- | --- | --- |
| VC-001 | V2 | Discovery Session v0 handles greenfield, brownfield single-repo, brownfield multi-repo, non-repository, and blocked contexts. |
| VC-002 | V2 | Every generated question includes a source reason from baseline gaps, assumptions, constraints, open questions, missing context, or playbook prompt. |
| VC-003 | V2 | Captured answers produce Project Memory candidates with provenance and do not become accepted truth. |
| VC-004 | V2 | Generated hypotheses remain candidates with uncertainty state. |
| VC-005 | V2 | Hypotheses retain evidence-gap links. |
| VC-006 | V2 | Stop conditions distinguish blocked, needs evidence, needs authority, and ready for planning. |
| VC-007 | V2 | Discovery Playbook references influence question selection without creating a generic process engine. |
| VC-008 | V2 | Candidate Review and Promotion is the only promotion path for answers and hypotheses. |
| VC-009 | V1 | No live model, live adapter, database, or external connector is required or invoked. |
| VC-010 | V1 | CLI/TUI wrappers call shared service functions if implemented. |
| VC-011 | V1 | No product shell or Workspace Shell implementation is introduced. |

## Deferred Verification

- Product UI verification is deferred.
- Persistence and migration verification are deferred.
- Live Cursor, Codex, OpenAI, analytics, CRM, ads, design, and repository connector verification is deferred.
- Live LLM behavior verification is deferred.
- Workspace Shell verification is deferred.

## Acceptance Standard

Future implementation is ready for review when all V1 and V2 checks pass locally and discovery outputs are traceable, candidate-only, uncertainty-preserving, and promotion-gated.
