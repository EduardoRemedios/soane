# Project Memory Architecture

## Status

This document defines the conceptual architecture for Workspace Project Memory.

It is a canonical Soane architecture document. It is not an implementation plan, storage design, API specification, UI specification, or database selection.

It consumes:

- `docs/VISION.md`
- `docs/CORE_CONCEPTS.md`
- `docs/GOVERNANCE_MODEL.md`
- `docs/research/PROJECT_MEMORY_RESEARCH_SYNTHESIS.md`

## Purpose

Project Memory is the durable source of truth for a Project.

It exists so humans and AI systems can understand:

- what is known
- what is assumed
- what is uncertain
- what has been decided
- what evidence exists
- what work has happened
- what authority or proof references exist
- what should happen next

Project Memory is not chat history. It is not a vector database. It is not a document folder. It is not a transcript archive.

Project Memory is the structured, inspectable, amendable, model-independent substrate from which the Workspace assembles context, generates canonical Markdown, supports decisions, and supervises delegation.

## Responsibilities

Project Memory is responsible for:

- preserving durable project understanding
- distinguishing facts, assumptions, hypotheses, decisions, constraints, and evidence
- maintaining provenance for important claims
- supporting Project Graph relationships
- supporting context assembly for Thinking, research, planning, and review
- supporting canonical Markdown generation
- linking to external mission, authority, proof, evidence, and regulated-conversation records
- preserving operational learning
- surfacing unresolved uncertainty
- supporting amendment, supersession, invalidation, and retirement

## Non-Goals

Project Memory does not:

- own Factory V3 mission governance
- own Temper agent execution
- own Aegis authority or proof
- own Sentinel boundary discovery
- own Harmony regulated conversation
- replace source repositories
- mirror neighbouring product state
- treat generated Markdown as the only source of truth
- treat model output as authoritative by default
- choose a storage engine in this document
- define API endpoints in this document
- define UI flows in this document

## Architectural Principle

Project Memory should separate durable memory from transient context.

Memory is the source substrate.

Context is a selected, task-specific view over memory and external sources.

Generated Markdown is a human-readable view over memory.

Conversation is an input to memory, not memory itself.

## Memory Layers

Project Memory contains five conceptual layers.

These are architectural layers, not required services, databases, or deployment units.

### Canonical Knowledge Layer

Stores durable project understanding.

Examples:

- product vision
- core concepts
- architectural boundaries
- roadmap commitments
- stable project facts
- accepted summaries
- durable domain knowledge

This layer should answer: what does the Project currently understand as stable?

### Governance Record Layer

Stores governed project records.

Examples:

- Decisions
- Assumptions
- Constraints
- Evidence Artifacts
- Verification records
- Authority References
- Proof References
- Approval records

This layer should answer: why is the Project allowed to believe, decide, or do something?

### Inquiry Layer

Stores uncertainty and structured investigation.

Examples:

- Questions
- Hypotheses
- Research Findings
- Discovery Playbooks
- open risks
- unresolved contradictions
- candidate interpretations

This layer should answer: what is not yet known, and how is uncertainty being reduced?

### Execution State Layer

Stores references to delegated work and operational learning.

Examples:

- Mission References
- checkpoint references
- work item references
- failed branches
- safe-hold states
- stale execution states
- operational learning
- replay and evidence links

This layer should answer: what work has happened, what state did it leave behind, and what was learned?

Project Memory records execution state references and learning. It does not own Factory V3 mission governance or Temper runtime state.

### Context Assembly Layer

Builds task-specific context packages from Project Memory and external references.

Examples:

- architecture discussion context
- mission-planning context
- research context
- decision-review context
- mobile approval context
- voice conversation context

This layer should answer: what does this task need to know right now?

Context Assembly is not the source of truth. It is a retrieval, ranking, filtering, and packaging function over memory.

## First-Class Object Model

Project Memory should model the following objects first.

Each object type should have a stable identity, lifecycle status, provenance, timestamps, source references, and typed relationships.

### Project

The durable unit of human intent, organisational memory, and supervised work.

Required relationships:

- owns Project Memory
- contains Conversations
- contains Decisions
- contains Assumptions
- contains Evidence Artifacts
- contains Canonical Knowledge Artifacts
- references external repositories, systems, missions, and authority records

### Conversation

An interaction between humans, AI systems, or both.

Conversation is not automatically Project Memory.

Conversation becomes memory only when relevant claims, questions, decisions, assumptions, or evidence are extracted, reviewed, linked, and retained.

### Question

A known gap in understanding.

Questions should link to:

- affected Decisions
- affected Hypotheses
- affected Missions
- relevant Evidence
- blocking status

### Assumption

A statement treated as true for planning without enough evidence to treat it as established fact.

Assumptions should link to:

- source
- owner or introducer
- dependent Decisions or plans
- validation path
- risk level
- current status

### Hypothesis

A testable proposition used to reduce uncertainty.

Hypotheses should link to:

- Question addressed
- supporting Evidence
- conflicting Evidence
- validation method
- implications if true
- implications if false
- related Decision if accepted

### Constraint

A limitation or requirement that shapes acceptable options.

Constraints should link to:

- source
- scope
- strength
- duration
- affected Decisions
- supporting Evidence or Authority Reference

### Decision

An explicit commitment to a course of action, interpretation, boundary, priority, design, policy, or plan.

Decisions should link to:

- context
- options considered
- rationale
- evidence used
- assumptions accepted
- constraints applied
- owner or authority
- reversal conditions
- affected objects

### Evidence Artifact

Information used to support or challenge a claim, assumption, hypothesis, decision, verification, or governance action.

Evidence Artifacts should record:

- type
- source
- provenance
- freshness
- reliability
- related claims
- producing system
- integrity metadata when available

Evidence is not Proof. Proof references belong to Aegis or another authorized proof system.

### Verification

A check that evaluates whether a claim, output, implementation, decision condition, or mission result satisfies criteria.

Verification should link to:

- checked object
- method
- result
- evidence produced
- criteria
- residual uncertainty

### Mission Reference

A reference to a Factory V3-governed Mission or other mission-governed external record.

Mission References should record:

- external mission identifier
- owning system
- status
- mission envelope reference
- checkpoint references
- evidence references
- replay or record reference

Project Memory does not own mission governance.

### Authority Reference

A reference to external authority, lease, permission, approval, or governance right.

Authority References should record:

- issuing system
- scope
- permitted action
- subject
- conditions
- expiry or revocation state
- related receipt or proof reference

Project Memory does not create authority.

### Capability Reference

A declared or observed ability of a human, agent, system, tool, model, product, or integration.

Capability References should distinguish:

- declared capability
- verified competence
- allowed use
- authority to act
- evidence of past successful use

Capability is not Authority.

### Research Finding

A structured output of Research.

Research Findings should record:

- question being answered
- sources consulted
- conclusion
- confidence
- assumptions introduced
- uncertainty remaining
- affected Hypotheses, Decisions, or architecture documents

### Operational Learning

Durable knowledge gained from executing, monitoring, verifying, or recovering work.

Operational Learning should link to:

- Mission Reference or work item
- outcome
- failure mode
- recovery action
- affected readiness criteria
- future planning implication

### Canonical Knowledge Artifact

A human-readable generated or curated view over Project Memory.

Canonical Knowledge Artifacts should record:

- source memory objects
- generation or curation method
- version
- review status
- related Decisions, Assumptions, Evidence, and Questions

Canonical Markdown documents are examples of Canonical Knowledge Artifacts.

## Common Object Fields

Every Project Memory object should support:

- `id`
- `type`
- `title`
- `status`
- `created_at`
- `updated_at`
- `created_by`
- `source_refs`
- `provenance`
- `relationships`
- `evidence_level`
- `visibility`
- `supersedes`
- `superseded_by`

Some objects also require:

- `owner`
- `authority_ref`
- `confidence`
- `risk_level`
- `expiry`
- `revoked_at`
- `decision_date`
- `verification_result`

This document does not define final field names or schemas. It defines the conceptual requirements that future schemas must satisfy.

## Lifecycle States

Project Memory objects should have explicit lifecycle states.

Common states:

- `proposed`
- `active`
- `accepted`
- `rejected`
- `superseded`
- `invalidated`
- `retired`
- `archived`

Inquiry-specific states:

- `open`
- `under_investigation`
- `answered`
- `deferred`
- `blocked`

Evidence-specific states:

- `submitted`
- `reviewed`
- `accepted`
- `challenged`
- `stale`
- `revoked`

Decision-specific states:

- `proposed`
- `accepted`
- `amended`
- `superseded`
- `retired`

Lifecycle transitions should preserve history. Project Memory should not silently overwrite meaning.

## Memory Creation And Promotion

Project Memory should support a staged path from raw input to durable knowledge.

### 1. Capture

Raw input is captured.

Examples:

- conversation
- document
- research note
- mission record
- evidence artifact
- external system reference

Capture does not make the input authoritative.

### 2. Extraction

Candidate memory objects are extracted from captured input.

Examples:

- candidate Assumption
- candidate Question
- candidate Decision
- candidate Evidence Artifact
- candidate Research Finding

Extracted objects begin as proposed unless the source has explicit authority.

### 3. Review

Humans or governed processes review extracted objects.

Review should check:

- correctness
- source grounding
- object type
- relationships
- evidence level
- authority implications
- duplicate or contradiction status

### 4. Promotion

Reviewed objects may be promoted into active Project Memory.

Promotion should record:

- reviewer
- reason
- evidence
- date
- affected objects

### 5. Amendment

Objects may be amended when understanding changes.

Amendment should preserve prior state.

### 6. Supersession Or Invalidation

Objects may be superseded or invalidated when they are outdated, wrong, or replaced.

Superseded or invalidated objects remain inspectable and should not be silently retrieved as current truth.

## Provenance Rules

Important Project Memory claims must be traceable.

Provenance should answer:

- where did this come from?
- who or what introduced it?
- when was it introduced?
- what evidence supported it?
- what assumptions were accepted?
- what changed since then?
- what is its current status?

Claims without provenance may be useful as notes, but they should not become canonical knowledge.

## Evidence Rules

Project Memory uses the evidence levels defined in `docs/GOVERNANCE_MODEL.md`.

At minimum, Project Memory should preserve:

- stated intent
- source references
- reviewed synthesis
- mechanical verification
- runtime or mission evidence
- authority or proof references

Evidence should be attached to claims and decisions, not merely stored nearby.

Evidence should have freshness and relevance. Stale evidence should not silently support current claims.

## Contradiction Handling

Project Memory should represent contradictions explicitly.

Contradictions may occur between:

- two source references
- a human claim and repository evidence
- a prior decision and new evidence
- a stale assumption and current state
- a generated summary and source material
- a mission result and expected outcome

When contradiction is detected, Project Memory should create or update a Question, Assumption, Hypothesis, or Decision need.

Contradictory records should not be flattened into false synthesis.

## Staleness Handling

Project Memory should track whether objects may be stale.

Potential staleness triggers:

- source file changed
- repository state changed
- portfolio source changed
- mission completed or failed
- assumption expired
- authority reference expired or was revoked
- evidence age exceeds its usefulness
- canonical document was amended

Staleness should affect context assembly and readiness assessment.

## Forgetting, Redaction, And Revocation

Project Memory must support removal or restriction of memory where required.

Reasons include:

- privacy
- legal or contractual requirement
- user request
- source revocation
- incorrect extraction
- sensitive information
- expired authority

Forgetting should distinguish:

- deletion
- redaction
- archival
- access restriction
- retrieval suppression
- supersession

The architecture should preserve auditability where appropriate without retaining content that must be removed.

## Context Assembly

Context Assembly selects relevant information for a specific task.

It should consider:

- task intent
- Project
- current user
- policy context
- privacy constraints
- source freshness
- evidence level
- authority requirements
- unresolved Questions
- active Assumptions
- relevant Decisions
- current lifecycle state

Context Assembly should surface uncertainty. It should include blocking Questions or weak Assumptions when they materially affect the task.

Context Assembly should not treat retrieval rank as truth.

## Canonical Markdown Generation

Canonical Markdown files are generated or curated views over Project Memory.

Generation should record:

- source memory objects
- generation time
- generation method
- reviewer or approval state
- unresolved assumptions
- evidence gaps
- superseded source objects

Generated Markdown should be:

- readable
- diffable
- portable
- reviewable
- traceable

Markdown should not be the only source of truth once Project Memory exists.

## Integration Boundaries

### Factory V2

Factory V2 provides planning discipline and evidence-backed process artifacts.

Project Memory may ingest Factory V2 run outputs as working documents, Evidence Artifacts, Decisions, Questions, or Research Findings.

Factory V2 does not create authority or proof.

### Factory V3

Factory V3 owns mission governance.

Project Memory stores Mission References, checkpoint references, mission evidence links, replay references, closeout summaries, and operational learning.

Project Memory does not own mission lifecycle, mission admission, checkpoint semantics, or mission replay.

### Temper

Temper owns governed agent teams and operational execution.

Project Memory stores Capability References, work references, evidence exports, approvals, denials, and operational learning from Temper where relevant.

Project Memory does not own Temper work ledger state.

### Aegis

Aegis owns authority, receipts, proof, evidence packets, and high-assurance trust semantics.

Project Memory stores Authority References, Receipt References, Proof References, and Evidence Packet References.

Project Memory does not create Aegis-grade proof.

### Sentinel

Sentinel owns boundary discovery and governance-readiness findings.

Project Memory stores Sentinel topology references, boundary reports, readiness blockers, Questions, Constraints, and Evidence Artifacts derived from Sentinel outputs.

Project Memory does not perform Sentinel observation.

### Harmony

Harmony owns regulated conversational runtime.

Project Memory stores regulated conversation references, policy decision references, conversation evidence references, and operational learning where appropriate.

Project Memory does not own regulated conversation policy execution.

## Model Independence

Project Memory must not depend on any specific AI model.

Models may:

- extract candidate memory
- summarize source material
- suggest relationships
- identify contradictions
- propose context packages
- draft canonical Markdown

Models must not silently create authoritative memory.

The memory substrate must remain inspectable and usable across model providers, local models, cloud models, specialist models, and future inference strategies.

## V1 Architecture Boundary

The initial Project Memory implementation remains intentionally small.

Implemented v0 foundations now define:

- object type registry
- lifecycle states
- provenance model
- relationship model
- evidence-level attachment
- canonical Markdown source mapping
- context assembly rules

The import path from existing Markdown documents remains pending. It must create reviewable candidates rather than silently promote extracted claims.

V1 should not define:

- final database technology
- distributed synchronization
- full search ranking
- enterprise permissions
- UI flows
- public API endpoints
- full integration clients for portfolio products
- automated memory extraction without review

## Implementation Reconciliation

The original readiness criteria have been satisfied for the v0 prototype:

- this conceptual architecture is accepted
- v1 object types are selected
- object lifecycle states are sufficient for Decisions, Assumptions, Evidence, and Questions
- provenance and source-reference requirements are clear
- canonical Markdown generation rules are bounded
- non-goals remain explicit

The v0 implementation proved memory object modeling, traceability, candidate review, context assembly, and agent-facing commands before durable persistence.

## Remaining Questions

- How should canonical documents be regenerated without losing human edits?
- Which Factory V2 run artifacts should be imported into Project Memory first?
- How should Markdown source changes mark linked memory objects stale or affected?
- What bounded typed-relationship traversal is useful for agent context without causing graph explosion?
- Which context access patterns must be proven before persistence architecture begins?

## Architecture Decision

Project Memory architecture begins with object semantics, lifecycle, provenance, and relationships.

Storage, APIs, UI, and advanced retrieval are deferred.

This decision is intentional. The Workspace needs a trustworthy memory model before it needs a memory database.
