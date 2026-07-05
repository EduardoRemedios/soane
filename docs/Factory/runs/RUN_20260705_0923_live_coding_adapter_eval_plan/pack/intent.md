# Intent: LCAE-V0-001 Live Coding Adapter Evaluation Plan

## Version

v1

## Change Log

- v1 (2026-07-05): Initial Stage A intent.

## Purpose

Plan the smallest safe implementation slice for evaluating live coding adapter surfaces before Soane introduces any live provider invocation.

## Goal

Create a deterministic, source-backed adapter evaluation contract that compares Codex CLI, Cursor CLI, Cursor SDK, OpenAI SDK, and OpenAI Agents SDK against Soane's Provider Invocation, Capability, Authority, Evidence, Project Memory, and coding-proof requirements.

## Non-Goals

- Do not implement live adapters.
- Do not call live Codex, Cursor, OpenAI, SDK, CLI, API, cloud agent, or model surfaces.
- Do not install dependencies.
- Do not read, clone, or mutate external repositories.
- Do not introduce product UI, Workspace Shell, persistence, or mission execution.
- Do not decide final provider strategy for all Soane domains.

## Principles

- Capability does not imply authority.
- Provider output remains candidate-only until reviewed.
- Source-backed evaluation precedes live invocation.
- CLI-backed coding proofs remain preferred before SDK-backed integrations unless evidence changes the sequencing.
- Evaluation must fail closed when credential, sandbox, repository scope, mutation, or traceability requirements are unclear.

## Roles

- Workspace: owns adapter evaluation criteria, Project Memory semantics, and user-facing readiness.
- Adapter surfaces: provide capabilities only; they do not define Soane authority, memory, evidence, or mission governance.
- Human reviewer: grants or denies future live-evaluation Go.
- Project Memory: records Provider Invocation and evaluation evidence objects when implementation eventually runs.

## Acceptance Criteria

- Future implementation creates a source-backed adapter capability profile for all five candidate surfaces.
- Future implementation defines a deterministic suitability score or decision matrix without making live calls.
- Future implementation records required preconditions for any later live invocation: auth, sandbox, command permissions, repository scope, output capture, trace capture, cost/latency metadata, and review path.
- Future implementation selects a recommended first live proof surface, expected to be Codex CLI unless evidence contradicts that.
- Future implementation includes blocked fixtures for unsafe surfaces or missing preconditions.
- Future implementation proves no live call, install, credential read, external clone, or repository mutation occurs.

## Open Questions

- NON-BLOCKING: Should the future implementation include local `--help` or `--version` probes if a CLI is already installed?
- NON-BLOCKING: Should the adapter evaluation matrix become a Project Memory fixture, a Thinking Engine fixture, or both?
- NON-BLOCKING: Should Cursor SDK evaluation remain documentation-only until a Cursor API key and sandbox policy are available?

## Go Or No-Go Rule

Go only if the pack preserves planning-only posture, keeps live invocation out of scope, verifies all Critical and High safety requirements, and produces a bounded implementation path that can be executed without credentials or external side effects.
