# Risk Register: Project Memory v0 Plan

## Version

v1

## Change Log

- v1 (2026-07-01): Initial Stage E risk register.

| ID | Severity | Risk | Mitigation | Verification Hook |
| --- | --- | --- | --- | --- |
| R-001 | High | Prototype proves persistence but not memory semantics. | Require governed memory invariants and object lifecycle rules. | Golden fixture suite and invariant tests. |
| R-002 | High | Context assembly becomes hidden RAG. | Define rule-driven context assembly v0. | Context assembly fixture with stale, contradictory, and restricted records. |
| R-003 | High | Adapter proof couples to live Cursor, Codex, or OpenAI behavior. | Use mock-first adapter contract. | Provider Invocation fixture with mocked adapter event. |
| R-004 | High | Capability is confused with authority. | Model Capability Reference and Authority Reference separately. | Capability without Authority fixture. |
| R-005 | High | Scope or visibility bypass leaks memory. | Enforce same policy on direct lookup, retrieval, and context assembly. | Unauthorized retrieval blocked fixture. |
| R-006 | High | Superseded or stale records appear as current truth. | Lifecycle and temporal rules must affect context assembly. | Stale/superseded exclusion fixture. |
| R-007 | Medium | Coding proof narrows domain model. | Keep object types domain-general. | Fixture review includes non-coding object semantics. |
| R-008 | Medium | Provenance lineage is incomplete. | Require source, writer, time, evidence level, and derivation metadata. | Promoted claim provenance fixture. |
| R-009 | Medium | Storage format becomes hard to migrate. | Use portable local storage and deterministic fixture IDs. | Persistence guardrail review. |
| R-010 | Medium | Markdown becomes source of truth. | Treat Markdown as generated or curated view over objects. | Markdown source-mapping fixture. |
| R-011 | Medium | Prototype scope is too broad. | Sequence contract, prototype, CLI, TUI, validation. | Micro-sprint gates. |
| R-012 | Medium | Redaction is implemented as deletion only. | Distinguish deletion, redaction, access restriction, and retrieval suppression. | Redaction/retrieval suppression fixture. |

