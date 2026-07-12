# Core Concepts

## Status

Version: 1.1.

This document defines the core vocabulary of the Workspace.

It exists to reduce ambiguity across product, architecture, engineering, governance, and future AI-agent work. Terms in this document should be used consistently in code, documentation, user interfaces, planning artifacts, and integration contracts.

When a term in this document conflicts with later usage, one of two things should happen:

- the later usage should be corrected
- this document should be intentionally amended through governance

This document builds on `docs/VISION.md`. It does not replace it.

## Vocabulary Principles

The Workspace is software for thinking, governed collaboration, and supervised delegation. Its vocabulary should preserve that purpose.

Core terms should be:

- precise enough to support architecture
- stable enough to support long-term memory
- understandable to humans
- inspectable by AI agents
- compatible with portfolio boundaries

Terms should not be overloaded for convenience. A conversation is not a decision. A decision is not proof. Evidence is not authority. A mission is not a project. A capability is not permission to act.

## Concept Map

At the highest level:

- a `Project` is the durable unit of work and memory
- `Project Memory` is the governed system of record for the Workspace's current understanding of that project
- `Conversations`, `Discoveries`, `Claims`, `Hypotheses`, `Decisions`, `Decision Reviews`, `Evidence`, and `Missions` are recorded in Project Memory
- a `Mission` is delegated work performed through governed execution systems
- `Authority` determines whether an action may proceed
- `Evidence` supports understanding, decisions, verification, and trust
- `Capabilities` describe what systems or agents can do

The Workspace coordinates these concepts. It does not own every system that implements them.

## Workspace

The Workspace is the primary human-facing environment through which people perform governed AI work.

It helps humans think, understand, decide, collaborate, govern, and supervise autonomous execution. It coordinates other portfolio systems through APIs and integration contracts.

The Workspace owns the experience of project understanding and supervised delegation. It does not own mission governance, agent runtime, authority, proof, or regulated conversational runtime.

## Thinking

Thinking is the deliberate process of reducing uncertainty through exploration, questioning, comparison, reasoning, synthesis, and judgement.

Thinking precedes planning.

Planning precedes delegation.

The Workspace treats Thinking as a first-class engineering activity rather than an informal precursor to implementation.

The purpose of the Thinking Engine is not to replace human thinking, but to augment it by making uncertainty visible, challenging assumptions, surfacing trade-offs, and improving decision quality.

## Project

A Project is a durable unit of human intent, organisational memory, and supervised work.

A Project may represent a software product, repository, system, initiative, customer implementation, internal programme, research effort, operational domain, or other bounded area of responsibility.

A Project contains:

- goals
- context
- conversations
- discoveries
- assumptions
- hypotheses
- constraints
- decisions
- evidence
- architecture
- plans
- missions
- outcomes
- operational learning

A Project is not merely a repository, chat thread, folder, task list, or execution plan. Those may be attached to a Project, but they do not define it.

Projects should be stable enough to preserve memory over time. If a unit of work is too small to require durable context, it may be a task or mission rather than a Project.

## Project Memory

Project Memory is the governed system of record for the Workspace's current understanding of a Project.

It stores the structured and retrievable record of what is asserted, observed, supported, accepted, assumed, uncertain, decided, reviewed, and performed.

Project Memory does not supersede the authority of external source systems. It records their references and the Workspace's governed interpretation while preserving provenance, source authority, epistemic status, and contradiction.

Project Memory includes:

- conversations
- discoveries
- claims
- hypotheses
- assumptions
- constraints
- decisions
- Decision Reviews
- architecture
- roadmap
- evidence
- verification
- mission history
- operational learning

Project Memory is more fundamental than generated documents. Canonical Markdown files are generated views over Project Memory.

Project Memory must be:

- durable
- inspectable
- queryable
- traceable
- amendable
- portable
- model independent

Project Memory should preserve both conclusions and the reasoning that produced them. It should allow a future human or AI agent to understand why the current state of the Project exists.

## Project Graph

The Project Graph is the structured representation of relationships inside Project Memory.

It connects entities such as goals, systems, people, teams, repositories, documents, claims, decisions, Decision Reviews, assumptions, evidence, missions, capabilities, authorities, and knowledge scopes.

The Project Graph should support:

- context assembly
- dependency analysis
- impact analysis
- cross-project retrieval
- evidence tracing
- ownership understanding
- mission readiness assessment

The Project Graph is not a visualisation. Visual graphs may be generated from it, but the graph itself is an underlying knowledge structure.

## Canonical Document

A Canonical Document is a human-readable authored, generated, or curated representation of an authoritative understanding of part of a Project.

Examples include:

- vision documents
- core concept documents
- architecture records
- governance documents
- project plans
- readiness reports
- mission briefs

Canonical Documents are important because they are readable, reviewable, diffable, and portable. They should be treated as stable interfaces between humans, AI agents, and governance processes.

Canonical Documents should remain traceable to Project Memory. If a Canonical Document becomes the only place a decision or fact exists, Project Memory has failed to capture the underlying knowledge.

Canonical Documents have three modes:

- **Authored authority** is maintained directly by accountable humans or governance processes and must not be overwritten by generation.
- **Generated projection** is rendered from Project Memory and may be regenerated from its recorded source objects.
- **Curated round trip** begins from structured memory but accepts reviewed human amendment; changes must be reconciled back into candidate memory before regeneration treats them as authoritative.

The mode, write authority, source mapping, and review state should be explicit.

## Conversation

A Conversation is an interaction between humans, AI systems, or both.

Conversations may contain questions, answers, proposals, disagreements, decisions, assumptions, evidence references, and action requests.

A Conversation is not automatically Project Memory. It becomes Project Memory when relevant content is extracted, structured, linked, and retained.

The Workspace should not force humans or agents to reconstruct project truth from raw conversation history. Conversation is an input to memory, not a substitute for memory.

## Claim

A Claim is a proposition asserted about a Project, its environment, or its work.

A Claim is not automatically a fact. It should record:

- the proposition
- claimant or producing system
- source and source authority
- provenance and derivation
- scope and applicable context
- supporting and challenging Evidence
- Verification state
- confidence where relevant
- freshness and review state
- current epistemic status

Useful epistemic states include `asserted`, `observed`, `supported`, `contested`, `accepted`, `verified`, `superseded`, and `invalidated`. These states are not interchangeable, and no retrieval score or model confidence may promote a Claim by itself.

An accepted fact is a Claim whose provenance, evidence, verification, source authority, scope, and review status satisfy the applicable governance standard. Fact is therefore a revisable epistemic status, not an unqualified object label.

## Discovery

Discovery is the process of identifying relevant context, constraints, unknowns, systems, stakeholders, risks, opportunities, and existing knowledge.

Discovery may involve:

- repository analysis
- documentation ingestion
- stakeholder dialogue
- system mapping
- policy review
- operational history review
- external research

Discovery produces candidate knowledge. It does not automatically produce settled truth.

## Discovery Playbook

A Discovery Playbook defines a structured approach for reducing uncertainty within a particular domain.

Different domains require different discovery approaches.

Examples include:

- software engineering
- research
- digital marketing
- operations
- consulting
- product strategy

The Thinking Engine should select, adapt, or compose Discovery Playbooks according to the nature of the Project rather than applying a single generic process.

The output of a Discovery Playbook contributes to Project Memory and Readiness.

## Research

Research is directed investigation intended to answer a question or reduce uncertainty.

Research may use internal sources, external sources, code analysis, documents, interviews, experiments, or model-assisted synthesis.

Research outputs should identify:

- the question being answered
- the sources consulted
- the confidence level
- the remaining uncertainty
- any assumptions introduced
- any evidence generated or referenced

Research is not a decision. It informs decisions.

## Question

A Question is a known gap in understanding.

Questions may be asked by humans, AI agents, systems, policies, or governance processes. Questions should be recorded when they affect readiness, risk, architecture, priority, authority, or execution.

Questions may be:

- open
- answered
- deferred
- superseded
- invalidated

Important Questions should be linked to the hypotheses, decisions, evidence, or missions they affect.

## Assumption

An Assumption is a statement treated as true for the purpose of reasoning or planning without sufficient evidence to treat it as established fact.

Assumptions are necessary, but they must be visible.

An Assumption should record:

- the statement being assumed
- why it is being assumed
- who or what introduced it
- what depends on it
- how it could be validated or invalidated
- its current risk

Assumptions should not silently become facts. They should be promoted, revised, or removed as evidence changes.

## Hypothesis

A Hypothesis is a testable proposition used to reduce uncertainty.

Hypotheses are stronger than questions and weaker than decisions. They propose a possible explanation, direction, design, risk, opportunity, or outcome that can be investigated.

A Hypothesis should record:

- the proposition
- the uncertainty it addresses
- supporting evidence
- conflicting evidence
- validation method
- expected implications if true
- expected implications if false
- current status

Hypothesis status should be explicit. Common statuses include:

- proposed
- under investigation
- supported
- weakened
- rejected
- converted to decision

A Hypothesis should not be treated as a Decision until the relevant human or governance authority has accepted it.

## Constraint

A Constraint is a limitation or requirement that shapes the set of acceptable options.

Constraints may be technical, organisational, legal, financial, operational, regulatory, temporal, architectural, contractual, or strategic.

Constraints should be recorded because they explain why some reasonable alternatives are not acceptable.

A Constraint should identify:

- source
- scope
- strength
- duration
- affected decisions
- evidence or authority supporting it

Constraints may change. When they do, affected decisions and plans should be revisited.

## Decision

A Decision is an explicit commitment to a course of action, interpretation, boundary, priority, design, policy, or plan.

Decisions reduce uncertainty by selecting among alternatives.

A Decision should record:

- the decision statement
- decision owner or responsible authority
- date
- context
- options considered
- rationale
- evidence used
- assumptions accepted
- constraints applied
- expected consequences
- reversal conditions
- affected systems or projects

A Decision is not proof. It is a governed commitment made under known conditions.

Decisions may be:

- proposed
- accepted
- rejected
- superseded
- amended
- retired

Important Decisions should be traceable to the conversations, research, evidence, assumptions, and authorities that shaped them.

## Decision Review

A Decision Review compares what a Decision expected with what was later observed.

A Decision Review should record:

- the Decision reviewed
- expected outcomes and indicators
- original confidence and causal assumptions
- review date or trigger
- observed outcomes and Evidence
- whether relevant Assumptions and Constraints held
- causal uncertainty and confounding factors
- resulting Operational Learning
- amendment, reversal, continuation, or further-review action

Decision Review exists to improve future judgement, not merely to score past decision makers.

## Evidence

Evidence is information used to support or challenge a claim, assumption, hypothesis, decision, verification, or governance action.

Evidence may include:

- source code
- tests
- logs
- documents
- architectural records
- user research
- metrics
- external references
- screenshots
- transcripts
- execution traces
- mission outputs
- receipts

Evidence should be evaluated for relevance, reliability, freshness, provenance, and completeness.

Evidence is not the same as proof. Evidence supports reasoning. Proof is a stronger governance or trust construct owned by Aegis.

The Workspace may store, index, present, and reason over Evidence. It should not claim to be the ultimate authority for proof when that responsibility belongs to Aegis.

## Verification

Verification is the process of checking whether a claim, output, implementation, decision condition, or mission result satisfies defined criteria.

Verification should identify:

- what was checked
- how it was checked
- who or what performed the check
- when it was checked
- what evidence was produced
- what criteria were used
- what uncertainty remains

Verification may support readiness, approval, mission completion, or operational trust.

Verification is not the same as authority. A result can be verified but still require approval before action proceeds.

## Mission

A Mission is a bounded unit of delegated work performed by AI systems, agents, or execution platforms under governance.

Missions exist to carry out work after sufficient understanding, authority, constraints, and success criteria have been established.

A Mission should have:

- objective
- scope
- context
- constraints
- responsible authority
- required capabilities
- execution system
- checkpoints
- evidence requirements
- completion criteria
- rollback or recovery expectations

A Mission is not a Project. A Project may contain many Missions. Missions should write outcomes, evidence, and operational learning back into Project Memory.

Mission governance, mission lifecycle, checkpointing, evidence, and replay belong to Factory V3. The Workspace may plan, launch, monitor, and review missions through Factory V3.

## Mission Plan

A Mission Plan is the structured intent for a Mission before execution.

It should define what is to be done, why it is safe or appropriate to proceed, what systems or agents will be involved, what authority is required, and what evidence must be produced.

Mission Plans should be generated from Project Memory rather than from isolated chat context.

A Mission Plan is not execution. It is the bridge between human judgement and governed delegation.

## Readiness

Readiness is the assessed state of whether a Project, Decision, or Mission has enough understanding, evidence, authority, and constraint clarity to proceed.

Readiness is not a feeling of confidence. It should be supported by explicit criteria.

Readiness may consider:

- known goals
- unresolved questions
- active assumptions
- validated constraints
- evidence quality
- decision status
- authority status
- risk level
- rollback options
- operational dependencies

The Workspace should make readiness visible before delegating work.

## Inference Strategy

An Inference Strategy defines how one or more reasoning systems are selected and combined to perform a specific task.

An Inference Strategy may use:

- a single model
- multiple models
- local models
- cloud models
- specialist models
- verifier models
- Mixture of Agents
- sequential reasoning pipelines

Inference Strategies should be selected according to task requirements, policy, privacy, confidence, cost, latency, and available capabilities.

The Workspace owns Inference Strategies.

It does not own the models themselves.

## Capability

A Capability is a declared ability of a human, agent, system, tool, model, product, or integration to perform a type of work.

Capabilities describe what can be done. They do not, by themselves, grant permission to do it.

Examples of Capabilities include:

- repository analysis
- code modification
- test execution
- document synthesis
- architecture critique
- data analysis
- mission execution
- evidence verification
- policy evaluation

Capability management for governed agent teams and capability mesh responsibilities belongs to Temper. The Workspace may discover, display, select, and request Capabilities through Temper or other systems.

## Agent

An Agent is an AI-driven worker that can perform tasks using models, tools, memory, capabilities, and instructions.

Agents may research, analyse, implement, simulate, operate, or verify. Agents may act alone or as part of governed teams.

The Workspace may coordinate with Agents, but it should not treat Agent output as authoritative by default. Agent work should be linked to evidence, verification, and authority where required.

Operational execution and governed agent teams belong to Temper. The Workspace supervises and coordinates from the human-facing side.

## Authority

Authority is the governed right to make a decision, approve an action, delegate work, access a resource, or accept risk.

Authority may belong to a person, role, responsibility, policy, governance process, organisation, or external system.

Authority should answer:

- who or what may act
- what action is permitted
- under what conditions
- within what scope
- with what evidence
- with what accountability
- for what duration

The Workspace does not own Authority. Authority, proof, receipts, evidence, trust, and constitutional governance belong to Aegis.

The Workspace should keep Authority explicit. It should not confuse recommendation, capability, approval, execution, verification, or proof with Authority.

## Delegation

Delegation is the governed assignment of bounded discretion or work from an Authority-bearing person, responsibility, policy, or external system to another subject.

Delegation should identify:

- issuing Authority Reference
- subject receiving the delegation
- permitted decisions or actions
- scope, conditions, and duration
- evidence and policy requirements
- budget or resource limits
- accountability and monitoring responsibility
- escalation, interruption, expiry, and revocation conditions

Delegation does not transfer ultimate accountability unless the governing Authority explicitly says so. Capability does not create Delegation, and the Workspace does not create Authority by recording one.

## Responsibility

Responsibility is an assigned obligation to decide, review, approve, execute, monitor, or maintain something.

The Workspace should model governance as responsibility-based rather than role-based. Roles may be used by organisations, but Responsibilities are the more precise primitive.

Responsibilities may include:

- decision owner
- reviewer
- approver
- mission supervisor
- evidence reviewer
- system owner
- policy owner
- operational responder

Responsibilities should be assignable through policy and visible in Project Memory.

## Policy

Policy is a rule or rule set that constrains, permits, requires, or routes action.

Policies may affect:

- model routing
- privacy
- authority
- approval
- evidence requirements
- capability usage
- mission execution
- data retention
- regulated conversation

The Workspace may apply, surface, or request policy decisions. It should not silently bypass policy to improve convenience.

Policy packs and regulated conversational policy responsibilities belong to Harmony where customer interaction and regulated conversational runtime are involved.

## Approval

Approval is an explicit acceptance that a proposed decision, action, mission, or risk may proceed.

Approval requires Authority. Approval should identify what was approved, by whom or what, under what conditions, and based on what evidence.

Approval is not the same as agreement. Agreement may indicate preference or alignment. Approval carries governed permission.

## Proof

Proof is a governance-grade demonstration that a claim, action, authority, or result satisfies required trust conditions.

Proof is stronger than Evidence and more formal than Verification.

Proof belongs to Aegis. The Workspace may present or request Proof, but it should not redefine the proof model.

## Receipt

A Receipt is a durable record that an action, approval, proof, delegation, execution step, or governance event occurred.

Receipts support accountability, replay, trust, and auditability.

Receipts belong to the trust and evidence responsibilities of Aegis and related governance systems. The Workspace may display and link Receipts in Project Memory.

## Checkpoint

A Checkpoint is a governed review point within a Mission or process.

Checkpoints allow humans, policies, or governance systems to inspect state, evaluate evidence, approve continuation, redirect work, or stop execution.

Checkpointing and mission replay belong to Factory V3. The Workspace should make checkpoints understandable and actionable to humans.

## Context

Context is the relevant subset of Project Memory and external information assembled for a specific reasoning, planning, decision, or execution task.

Context should be purposeful. More context is not always better. The Workspace should assemble context based on relevance, freshness, provenance, policy, privacy, and task intent.

Context is not memory. Context is a selected view used for a specific activity. Project Memory is the durable substrate.

## Knowledge Scope

Knowledge Scope defines where a Project Memory object may be retained, retrieved, used, or promoted.

Initial scopes may include private working context, Project, organisation, portfolio, and external or public. Wider scope must not be inferred from relevance, repetition, or technical accessibility.

Cross-project promotion should be explicit and governed. It should preserve provenance, source authority, privacy, contractual restrictions, consent requirements, and unresolved contradictions. If promotion authority or propagation rules are unclear, retrieval should fail closed.

## Memory Rights

Memory Rights govern capture, access, amendment, correction, export, retention, deletion, redaction, restriction, and revocation.

They should identify the subject or owner, accountable controller, purpose, applicable policy, retention basis, and any legal or contractual hold. Derived knowledge should retain applicable restrictions from its sources. Auditability should not be used as a reason to preserve content that must lawfully or validly be removed.

## Synthesis

Synthesis is the process of combining information from multiple sources into a coherent understanding.

Synthesis should preserve uncertainty. It should not flatten disagreement, conflict, or weak evidence into false confidence.

Good synthesis identifies:

- what is known
- what is uncertain
- what conflicts
- what matters
- what should happen next

## Negotiation

Negotiation is structured resolution of competing goals, constraints, preferences, responsibilities, or risks.

Negotiation may occur between humans, teams, policies, AI agents, or portfolio systems. The Workspace should support negotiation by making trade-offs visible and preserving the reasoning behind outcomes.

Negotiation may produce Decisions, Constraints, revised Hypotheses, or Mission Plans.

## Knowledge Consolidation

Knowledge Consolidation is the process of turning scattered project information into durable Project Memory.

It may transform conversations, research outputs, code analysis, documents, mission results, and human feedback into structured memory and Canonical Documents.

Knowledge Consolidation should preserve provenance. It should not erase the difference between observed facts, inferred claims, assumptions, hypotheses, and decisions.

## Mission History

Mission History is the record of delegated work performed for a Project.

It should include:

- mission plans
- execution summaries
- checkpoints
- evidence
- approvals
- outcomes
- failures
- recovery actions
- operational learning

Mission History should feed back into Project Memory so future planning and delegation improve over time.

## Operational Learning

Operational Learning is durable knowledge gained from executing, monitoring, verifying, or recovering work.

It includes lessons about systems, people, processes, risks, capabilities, tools, policies, and failure modes.

Operational Learning should affect future readiness assessments, mission planning, architecture decisions, and governance expectations.

## Boundary Terms

Some terms are deliberately adjacent but distinct.

### Project and Mission

A Project is durable memory and intent. A Mission is bounded delegated execution.

A Project may contain many Missions. A Mission should update Project Memory, but it should not define the whole Project.

### Evidence and Proof

Evidence supports reasoning. Proof satisfies stronger trust or governance requirements.

The Workspace may manage Evidence. Aegis owns Proof.

### Capability and Authority

Capability means an actor can do something. Authority means the actor is permitted to do it.

The Workspace must keep this distinction explicit.

### Hypothesis and Decision

A Hypothesis is a testable proposition. A Decision is a governed commitment.

Supported hypotheses may inform decisions, but they are not decisions until accepted by the relevant authority.

### Conversation and Memory

A Conversation is interaction history. Project Memory is structured, durable understanding.

The Workspace should extract reviewed memory candidates from conversations rather than treating conversation history as governed project understanding.

### Verification and Approval

Verification checks whether criteria are satisfied. Approval grants permission to proceed.

A verified result may still require approval. An approval may require verification evidence.

## Required Discipline

Future work in this repository should use these terms deliberately.

When adding features, APIs, schemas, prompts, agents, documents, or user interfaces, contributors should ask:

- which core concept is being represented
- whether the term is being used consistently
- whether the concept belongs to the Workspace or another portfolio product
- whether the authoritative record is an external source, authored authority, Project Memory object, or generated view
- whether evidence, authority, and decisions are being kept distinct
- whether the design reduces uncertainty before execution

Terminology is part of the architecture. Ambiguous vocabulary creates ambiguous systems.
