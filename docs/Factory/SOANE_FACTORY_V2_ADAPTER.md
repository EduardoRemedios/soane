# Soane Factory V2 Adapter

## Purpose

This document defines how Soane uses the Factory V2 starter-kit scaffold.

It exists to prevent confusion between:

- Factory V2: the current planning-first starter-kit process used in this repository
- Factory V3: the newer, separate mission-governance system under development in `/Users/eduardodosremedios/Factory_V3`

## Scope

Soane uses Factory V2 for:

- planning discipline
- raw brief hardening
- bounded execution contracts
- verification planning
- evidence-backed handoffs
- review readiness
- continuity across planning runs

Soane does not use this scaffold for:

- Factory V3 mission governance
- autonomous mission lifecycle management
- operational-profile promotion
- mission telemetry or replay
- worker-runtime supervision
- authority or proof

Those responsibilities remain outside Soane.

## How To Read Imported Factory Docs

The imported docs under `docs/Factory/` come from the Factory V2 starter kit.

When those documents say "Factory," read that as "Factory V2 starter-kit process" unless the document explicitly says otherwise.

The verification tier label `V3` in `docs/Factory/` means "regression or conformance verification tier." It is not a reference to Factory V3.

## Soane-Specific Inputs

Factory V2 runs in this repository should treat these as canonical Soane context:

- `docs/VISION.md`
- `docs/CORE_CONCEPTS.md`
- `docs/PORTFOLIO_CONTEXT.md`
- `docs/PORTFOLIO_ASSUMPTIONS.md`
- `docs/INTEGRATION_ARCHITECTURE.md`
- `docs/PROJECT_STATE.md`
- `docs/ROADMAP.md`

Factory V2 runs should preserve the Workspace boundary defined by those documents.

## Default Run Posture

Factory V2 runs in Soane default to `PLANNING_ONLY`.

Execution requires explicit human authorization in the run artifacts.

Until application code exists, most Factory runs should produce planning packs, architecture decisions, or implementation briefs rather than code changes.

## Promotion Rule

If a reusable Factory V2 process improvement is discovered while working in Soane, it should be promoted back to `/Users/eduardodosremedios/factory-starter-kit`.

Do not silently fork Factory V2 process doctrine inside Soane.

