# Portfolio Context

## Status

This document explains the wider portfolio from the Workspace's perspective.

It is a Soane document. It does not define the internal architecture of neighbouring products. It records how the Workspace should understand and coordinate the portfolio without absorbing it.

Source posture: based on `docs/VISION.md`, `docs/CORE_CONCEPTS.md`, and `/Users/eduardodosremedios/Eduardo_Product_Stack/docs/portfolio/portfolio-architecture-briefing-new-ai-workspace.md`.

## Why The Workspace Exists

The Workspace exists because governed AI work needs a project-centric human environment.

Its role is to help people understand, plan, discuss, negotiate, prototype, supervise, and improve work across projects. It owns the experience of Project Memory, Thinking, discovery, synthesis, decision support, mission planning UI, mission monitoring, collaboration, voice, desktop, cloud, mobile, and cross-project knowledge.

The Workspace is separate because these responsibilities are not the same as mission governance, agent-team execution, proof, boundary discovery, regulated conversation, or the current planning methodology.

The Workspace is not "Factory V3 with a UI." Factory V3 is a mission-governance engine. The Workspace is a project-centric product experience that can use Factory V3 and other portfolio systems through clear contracts.

## Architectural Layering

The portfolio should be understood as cooperating architectural layers.

```text
Experience layer
  Workspace
  Harmony surfaces for regulated conversations

Operational product layer
  Temper agent teams and packs
  Harmony regulated workflow runtime

Mission/work execution layer
  Factory V3 supervised missions
  Factory V2 planning discipline and fallback

Authority/proof layer
  Aegis kernel
  Sentinel boundary discovery

Domain proof organisms and adapters
  Casino, payments, Temporal Fruits, operator adapters, future vertical packs
```

The Workspace belongs primarily in the experience layer. It has orchestration responsibility across operational and mission layers, but it should not sink into the authority/proof layer.

## Portfolio Responsibilities

### Factory V2

Factory V2 is the current planning-first delivery discipline.

It owns:

- planning-first software delivery process
- stage contracts from raw brief through pack audit
- Product Owner lane for phase intent and sprint brief production
- explicit execution-mode controls
- human Go/No-go checkpoints
- verification design before implementation
- stage lint, pack lint, knowledge lint, and context recall discipline
- Mission Mode as an additive multi-sprint wrapper
- reusable templates and validators

Factory V2 is the stable baseline and fallback path. The Workspace may use Factory V2 methods, templates, and verification discipline when helping humans prepare work. It should not become Factory V2.

### Factory V3

Factory V3 is the supervised mission-governance engine for AI workers.

It owns:

- executable mission-envelope schema
- mission governance rules
- AI-worker checkpointing
- human decision interrupts
- halt, recovery, fallback, and safe-hold semantics
- mission records and replay
- operational profile promotion criteria
- mission validators
- worker-runtime supervision for bounded execution

Factory V3 currently has meaningful evidence but narrow approval. Optional operational use is approved only for bounded code-change missions. Broader long-running mission governance remains research-only, advisory, non-enforcing, or explicitly gated until promoted.

The Workspace may create, inspect, monitor, pause, resume, and review missions. Factory V3 decides whether a mission is valid, executable, paused, failed, replayable, or promotable.

### Temper

Temper is the governed agent-team orchestration product.

It owns:

- governed agent teams
- Agent Pack runtime
- capability mesh
- work ledger
- governed action ingress
- pack install, activation, and composition
- operational workflow packaging
- adapter trust tiers for agent work
- agent-team evidence exports

The Workspace may help users discover, configure, launch, and monitor Temper teams. Temper remains the runtime for operational agent teams.

### Aegis

Aegis is the authority and proof substrate.

It owns:

- constitutional autonomy kernel
- authority leasing
- receipts
- high-assurance evidence packets
- offline verification
- temporal and finality semantics
- fail-closed mediation
- proof-strengthening for consequential actions
- trust, verification, simulation, and evidence primitives

The Workspace may request, display, and reason over Aegis authority and proof. It must not invent its own leases, receipts, or proof semantics.

### Sentinel

Sentinel is the boundary discovery layer within the Aegis orbit.

It owns:

- passive boundary discovery
- effect-boundary classification
- topology and consequence mapping
- bypass and orphan reports
- governance-readiness analysis
- first-boundary recommendations
- data-minimized, no-write, removable observation

Sentinel is currently best treated as research/pre-implementation design that is architecturally important for discovering where governance should attach in unfamiliar systems.

The Workspace consumes Sentinel findings. Sentinel discovers boundaries.

### Harmony

Harmony is the regulated conversational runtime.

It owns:

- conversational ingress and intent normalization
- deterministic policy-pack evaluation
- confirmation and disclosure lifecycles
- typed response blocks
- channel and surface contracts
- adapter dispatch under fail-closed rules
- runtime-authored evidence and receipts
- operator-specific integration surfaces
- regulated interaction workflows

The Workspace owns general project conversation and voice. Harmony owns regulated conversation, regulated workflow voice, policy packs, confirmations, receipts, and channel/runtime semantics.

## What The Workspace Owns

The Workspace owns the project-centric knowledge-work experience:

- multi-project workspace
- Project Memory and project graph
- canonical Markdown knowledge management
- discovery, Thinking, synthesis, negotiation, and decision support
- human/AI collaboration surfaces
- voice-first project interaction
- desktop, cloud, and mobile product experiences
- cross-project search, retrieval, and summarization
- mission planning UI
- mission monitoring dashboard
- prototype orchestration and preview surfaces
- operational improvement loops across projects
- provider-neutral AI interaction at the product UX layer
- role-aware collaboration for solo developers and enterprise teams
- display and navigation of evidence, receipts, mission records, and proof artifacts produced by other systems

What it should own exclusively:

- the user's project-centric mental model
- the canonical Workspace knowledge graph
- cross-project synthesis and negotiation
- voice UX for project work
- the product shell across desktop, cloud, and mobile
- the portfolio-level improvement view

## What The Workspace Does Not Own

The Workspace deliberately does not own:

- executable mission governance
- worker-runtime supervision
- operational agent-team runtime
- Agent Pack runtime
- authority leases
- receipts
- high-assurance proof
- passive boundary discovery
- regulated conversational runtime
- policy-pack execution for regulated workflows
- current Factory V2 process doctrine

When the Workspace needs these responsibilities, it should call the owning product through an explicit contract.

## How Humans Experience The Portfolio

Humans should experience the portfolio through the Workspace as one coherent operating environment without losing the boundaries that make it governable.

In practice:

- the Workspace helps humans clarify goals, assumptions, constraints, hypotheses, and decisions
- Project Memory preserves understanding across conversations, documents, repositories, missions, and evidence
- Factory V2 provides current process discipline and fallback planning structure
- Factory V3 validates and governs executable missions
- Temper executes governed agent-team work
- Aegis provides authority, receipts, proof, and stronger trust semantics
- Sentinel discovers boundaries and governance readiness
- Harmony handles regulated conversational workflows and channel runtime

The user should see what requires judgement, who or what owns the next action, what evidence exists, what authority is required, and which system is responsible.

## Boundary Principle

The strongest long-term architecture is not one monolithic AI operating system.

It is a portfolio of cooperating products with explicit ownership boundaries and shared governance contracts.

The Workspace coordinates the portfolio. It should never absorb the portfolio.

