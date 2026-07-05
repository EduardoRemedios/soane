# Raw Brief: Live Coding Adapter Evaluation Plan

## Request

Create a Factory V2 `PLANNING_ONLY` pack for evaluating live coding adapter surfaces before any live provider invocation is introduced into Soane.

## Background

Soane has completed mock-first adapter twins, Coding Proof Harness v0, Coding Harness Workflow v0, and deterministic Brownfield multi-repo coding proof behavior.

The next roadmap item is to evaluate live coding adapter surfaces:

- Codex CLI
- Cursor CLI
- Cursor SDK
- OpenAI SDK
- OpenAI Agents SDK

The plan should determine which surface, if any, is suitable for the first live proof and what contracts must exist before execution.

## Goal

Produce a bounded implementation plan for a future adapter evaluation harness that can compare live adapter surfaces without allowing uncontrolled repository mutation, credential exposure, authority bypass, or candidate-output promotion.

## Required Constraints

- Keep this run `PLANNING_ONLY`.
- Do not invoke live Codex, Cursor, OpenAI, SDK, CLI, API, or cloud agent surfaces during this planning run.
- Do not install dependencies.
- Do not add live adapter code in this run.
- Do not introduce product UI or Workspace Shell.
- Evaluate live surfaces as adapters behind Provider Invocation, Capability Reference, Inference Strategy, authority, evidence, and Project Memory contracts.
- Preserve mock-first ordering. Live evaluation must be gated behind explicit future human Go.
- Prefer CLI-backed proofs before SDK-backed integrations unless evidence shows otherwise.

## Required Evaluation Dimensions

- invocation mode
- auth and credential handling
- sandbox and mutation controls
- structured output or event stream availability
- traceability and observability
- cost and latency metadata
- resumability or thread/session identity
- repository scope and working-directory controls
- compatibility with Greenfield, Brownfield single-repo, and Brownfield multi-repo proofs
- support for blocked or dry-run behavior
- candidate-only output capture and review-gated promotion
- failure modes and fail-closed behavior

## Expected Output

A Factory pack for `LCAE-V0-001` that can be reviewed for Go/No-go before implementation.
