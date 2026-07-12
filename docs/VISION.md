# The Workspace Vision

## Constitutional Status

This document defines the founding vision for the Workspace.

It is not a marketing document. It is the primary architectural and product constitution for this repository. Future architectural decisions, product boundaries, and implementation plans should remain consistent with this document unless it is intentionally amended through an explicit governance process.

The audience for this document is senior software engineers, architects, product leaders, and future AI agents working on this repository.

## Portfolio Context

The Workspace is part of a wider product portfolio that includes Factory V2, Factory V3, Temper, Aegis, Sentinel, and Harmony.

The Workspace is not a replacement for any of these products. It is the primary human-facing environment through which people perform governed AI work. It coordinates the portfolio through APIs and integration contracts. It must not absorb responsibilities that belong to other portfolio products.

The Workspace should make the wider portfolio understandable and operable to humans without weakening the boundaries that make the portfolio governable.

## Purpose

Autonomous AI makes implementation increasingly inexpensive. The scarce resource becomes human judgement.

The Workspace exists to improve:

- thinking
- understanding
- decision quality
- organisational memory
- governance
- collaboration
- supervised delegation

Implementation can be delegated. Humans retain accountability and governed authority. AI systems may exercise bounded judgement only within explicit, revocable delegations that define scope, policy, evidence, budget, escalation, and duration.

The Workspace should therefore help humans decide what should be done, why it should be done, under what constraints, with what evidence, and with what level of confidence. Execution systems may carry out work, but the Workspace exists to reduce uncertainty before that work begins and to preserve the reasoning that justified it.

## Core Philosophy

The Workspace is not primarily software for writing code.

It is software for thinking.

Its purpose is to progressively reduce uncertainty until autonomous execution can safely proceed. Every subsystem should contribute to that purpose. Features that do not improve understanding, decision quality, memory, collaboration, governance, or supervised delegation should be treated as suspect unless they directly support another constitutional responsibility.

The Workspace should make ambiguity visible. It should distinguish facts from assumptions, assumptions from hypotheses, hypotheses from decisions, and decisions from execution plans. It should help humans recognise when they know enough to proceed and when they do not.

## Human and AI Responsibilities

The Workspace assumes that humans increasingly become:

- strategists
- architects
- reviewers
- governors
- negotiators
- decision makers

It assumes that AI systems increasingly become:

- researchers
- analysts
- implementers
- simulators
- operators
- verifiers

The Workspace exists to maximise the effectiveness of both groups. Capability, recommendation, and delegated discretion do not create Authority. The Workspace should not pretend that AI owns authority, and it should not waste human attention on work that can be safely delegated once intent, constraints, evidence, accountability, and authority are clear.

## Product Scope

The Workspace owns the human-facing environment for governed AI work.

It owns:

- discovery
- research
- adaptive Socratic dialogue
- hypothesis management
- synthesis
- negotiation
- architecture discussion
- decision support
- project readiness
- project planning
- mission planning
- mission monitoring
- cross-project knowledge
- collaboration
- organisational memory
- desktop experience
- mobile experience
- cloud experience
- voice-first interaction

The Workspace does not own:

- mission governance
- agent runtime
- authority
- proof
- regulated conversational runtime

Those responsibilities remain with other portfolio products.

## Portfolio Responsibilities

### Factory V2

Factory V2 owns:

- planning discipline
- current engineering methodology
- templates
- migration path

The Workspace may surface, apply, or orchestrate Factory V2 methods, but it should not redefine them as Workspace responsibilities.

### Factory V3

Factory V3 owns:

- supervised mission governance
- mission lifecycle
- checkpointing
- mission evidence
- mission replay

The Workspace may plan, launch, monitor, and review missions through Factory V3. It should not become the mission governance system.

### Temper

Temper owns:

- governed agent teams
- capability mesh
- operational execution
- agent packs

The Workspace may delegate work to Temper and display operational state. It should not become the agent team runtime or capability mesh.

### Aegis

Aegis owns:

- authority
- proof
- receipts
- evidence
- trust
- constitutional governance

The Workspace may request, present, and reason over Aegis-backed evidence. It should not become the source of authority or proof.

### Sentinel

Sentinel owns:

- governance boundary discovery
- topology understanding
- governance readiness

The Workspace may use Sentinel to understand systems, boundaries, and readiness. It should not duplicate Sentinel's discovery or topology responsibilities.

### Harmony

Harmony owns:

- regulated conversational runtime
- policy packs
- operator workflows
- customer interaction

The Workspace may integrate with Harmony where regulated conversation or operator workflows are required. It should not become the regulated conversational runtime.

## Project Memory

Project Memory is the central architectural concept of the Workspace.

Project Memory is the governed system of record for the Workspace's current understanding of a Project. It stores the reasoning, claims, evidence, decisions, constraints, and operational history that allow humans and AI systems to understand what is asserted, supported, uncertain, decided, observed, and still open.

Project Memory does not become the ultimate authority for external reality merely by indexing or synthesising it. Source systems remain authoritative for the records they own. Project Memory should preserve source authority, provenance, epistemic status, and contradiction so accepted understanding can be revised when better evidence or governing records appear.

Project Memory stores:

- conversations
- discoveries
- claims
- hypotheses
- assumptions
- constraints
- decisions
- decision reviews
- architecture
- roadmap
- evidence
- verification
- mission history
- operational learning

Canonical Markdown files may be authored authority, generated projections, or curated round trips over Project Memory. Their mode must be explicit.

Markdown is important because it is portable, reviewable, diffable, and accessible to humans and tools. Project Memory is fundamental because it is the durable structured substrate from which generated and curated views are produced. Generated output must not overwrite authored authority, and curated changes must not silently become authoritative memory. Markdown should not be treated as the only source of project understanding when a richer Project Memory representation exists.

The Workspace should be able to regenerate canonical documents from Project Memory, explain why they say what they say, and trace important claims back to supporting evidence or decisions.

## Major Internal Subsystems

The Workspace contains three major internal subsystems:

- the Thinking Engine
- the Project Memory Engine
- the Workspace Shell

These subsystems are internal architectural responsibilities. They are not necessarily deployment units, commercial products, or organisational teams.

### Thinking Engine

The Thinking Engine is responsible for:

- discovery
- adaptive questioning
- architecture critique
- trade-off analysis
- negotiation
- research
- readiness assessment
- hypothesis management
- decision support

The Thinking Engine exists to augment human reasoning. It should help users clarify intent, surface hidden assumptions, test alternatives, identify trade-offs, and decide when a project is ready for autonomous execution.

The Thinking Engine should prefer precision over fluency. It should expose uncertainty rather than hide it. It should adapt its questioning to the current level of confidence, risk, novelty, and organisational context.

### Project Memory Engine

The Project Memory Engine is responsible for:

- project graph
- semantic knowledge graph
- claim and epistemic-status management
- context assembly
- cross-project retrieval
- decision history
- decision outcome review
- evidence indexing
- canonical Markdown generation
- search
- knowledge consolidation

The Project Memory Engine is an internal platform. It is not a separate commercial product.

It should provide the durable substrate for continuity across conversations, people, projects, agents, and execution systems. It should make project context recoverable, inspectable, and reusable without requiring humans to reconstruct history from chat logs or scattered documents.

### Workspace Shell

The Workspace Shell is responsible for:

- desktop
- web
- mobile
- voice
- collaboration
- dashboards
- notifications
- mission monitoring
- portfolio views

The Workspace Shell is the human-facing control surface. It should make thinking, review, delegation, monitoring, and governance practical across devices and working modes.

The Shell should not define the truth of the project. It should present, edit, query, and navigate Project Memory through coherent experiences.

## Model Strategy

The Workspace is model independent.

Project Memory must never depend upon a particular AI model. Models are replaceable reasoning workers. The Workspace should select inference strategies rather than treat any model as a permanent architectural dependency.

The Workspace must support:

- local models
- cloud models
- enterprise models
- specialist models
- multiple providers
- future providers
- Mixture of Agents
- policy-based routing
- privacy-aware routing
- confidence-aware routing
- cost-aware routing

Model selection should be contextual. The Workspace should consider privacy, policy, confidence, latency, cost, capability, provenance, and user intent when routing work.

No architectural decision should assume that a current model, provider, context window, tool interface, pricing model, or capability frontier will remain stable.

## Voice

Voice is a first-class interface.

Voice is not merely an accessibility feature. Users should be able to perform almost every project activity conversationally, including discovery, clarification, review, approval, monitoring, and steering. Voice must also meet accessibility, consent, authentication, privacy, and correction requirements appropriate to the interaction.

Voice should work consistently across:

- desktop
- mobile
- cloud

Voice interaction should preserve the same governance, memory, evidence, and decision boundaries as visual interaction. Spoken work is still project work. It must be captured, structured, and made available through Project Memory where appropriate.

## Mobile

Mobile is a primary control surface.

Users should be able to:

- monitor projects
- review evidence
- approve decisions
- answer clarification questions
- steer missions
- launch work
- converse with projects
- receive notifications

The mobile application is not a companion app. It is a first-class Workspace.

Mobile experiences should be designed for judgement under constraints: limited time, partial attention, smaller screens, and high-value decisions. Mobile should make it easy to understand what requires attention, why it matters, what evidence supports it, and what action is being requested.

## Team Collaboration

The Workspace must support:

- solo developers
- small teams
- large enterprises

Governance should be responsibility-based rather than role-based. Responsibilities are assigned through policy.

The same core epistemic primitives should remain useful from one person to thousands. Enterprise scale will require additional identity, tenancy, federation, administration, privacy, and compliance structures, but it should not require redefining the meaning of projects, claims, decisions, evidence, memory, or delegation.

Collaboration should preserve accountability. The Workspace should make it clear who decided, who reviewed, who approved, what evidence was available, and what assumptions were active at the time.

## Brownfield Adoption

The Workspace supports both greenfield projects and existing organisations.

For existing systems it should:

- discover repositories
- ingest documentation
- analyse source code
- consolidate knowledge
- generate canonical project memory
- validate understanding with humans

Mission execution should only begin once sufficient understanding has been established.

Brownfield adoption requires humility. Existing systems contain implicit knowledge, historical constraints, undocumented decisions, and organisational habits. The Workspace should not assume that repository analysis alone is enough. It should combine automated discovery with human validation before treating generated memory as authoritative.

## Architectural Principles

The following principles should guide future decisions.

### Preserve Boundaries

The Workspace coordinates the portfolio. It does not absorb the portfolio. When a responsibility belongs to Factory V2, Factory V3, Temper, Aegis, Sentinel, or Harmony, the Workspace should integrate with that product rather than duplicate it.

### Treat Memory as Infrastructure

Project Memory is not a feature layered on top of chat. It is the durable infrastructure of the Workspace. Interfaces, agents, documents, and execution systems should all interact with Project Memory as the source of project continuity.

### Preserve Source Authority

Project Memory records governed project understanding. It should not erase the distinction between a source-system record, an observation, an assertion, an accepted understanding, a verified finding, and a governed Decision. Retrieval rank, repetition, model confidence, and document status do not turn an assertion into fact.

### Govern Memory Rights

Memory capture and reuse should have an explicit purpose, scope, and accountable owner. The Workspace should support access restriction, correction, export, retention, deletion, redaction, revocation, and consent where required. Privacy, contractual, and source restrictions should propagate with derived knowledge.

Cross-project knowledge should fail closed. Knowledge may move from a Project to a wider organisational or portfolio scope only through an explicit, governed promotion that preserves provenance, restrictions, and unresolved conflict.

### Reduce Uncertainty

Every major subsystem should reduce uncertainty. The Workspace should identify unknowns, structure inquiry, compare alternatives, record decisions, and clarify readiness.

### Keep Authority Explicit

The Workspace may help humans reason about decisions, but authority must remain explicit and governed. It should distinguish recommendation, approval, delegation, execution, verification, and proof.

### Optimise for Human Judgement

The Workspace should protect human attention for work that requires judgement. It should avoid burying users in raw implementation detail when synthesis, evidence, and decision framing would be more useful.

### Remain Model Independent

The Workspace should not bind its architecture to any model provider or current AI capability. Models should be interchangeable workers selected by policy, task, context, confidence, privacy, and cost.

### Make Reasoning Inspectable

Important conclusions should be traceable. The Workspace should make it possible to understand why a decision was proposed, what evidence supported it, what alternatives were considered, and what uncertainty remained.

### Learn From Outcomes

Important Decisions should state expected consequences, confidence, and review conditions. The Workspace should later compare those expectations with observed outcomes, preserve causal uncertainty, and feed the resulting learning into assumptions, readiness, planning, and future Decisions.

## Measures Of Success

The Workspace should measure whether it improves project understanding and governed judgement. Useful measures include:

- time to assemble trustworthy task context
- provenance and source-authority coverage
- age of unresolved high-risk Assumptions and Questions
- time to detect stale or contradictory understanding
- Decision Review completion and prediction calibration
- escaped Constraint or Authority violations
- successful context reuse without repository-wide rereading
- human attention required per governed outcome

Artifact volume, memory-object count, conversation length, and model activity are not success measures by themselves.

## Long-Term Vision

The Workspace becomes the operating environment through which organisations think, collaborate, govern, and supervise autonomous AI work.

It remains independent of rapidly evolving AI models.

It remains independent of execution providers.

Its long-term value lies in:

- preserving organisational understanding
- improving human judgement
- coordinating autonomous work
- maintaining trusted project memory
- enabling safe delegation

The Workspace should become the place where humans and AI systems develop shared project understanding, humans retain accountability and governed authority, and agents perform reasoning and work within explicit delegations.

That allocation of understanding, accountability, authority, and delegated action should guide every future architectural decision.
