"""Agent-facing context bundles over Project Memory and Factory recall."""

from __future__ import annotations

import hashlib
import re
import sqlite3
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from scripts.factory_context_index import (
    FactoryContextIndexError,
    build_context_index,
    describe_context,
    recall_context,
)
from soane.project_memory.context import (
    ContextItem,
    ContextPackage,
    ContextRequest,
    ContextSelectionMode,
    build_context_package,
)
from soane.project_memory.contract import MemoryObject, RelationshipType
from soane.project_memory.semantics import NON_CURRENT_STATUSES, AccessContext, ProjectMemory


class MarkdownRole(StrEnum):
    CONSTITUTIONAL = "constitutional"
    CANONICAL = "canonical"
    WORKING = "working"
    GENERATED = "generated"
    EVIDENCE = "evidence"
    DEPRECATED = "deprecated"


class AgentSelectionMode(StrEnum):
    RELEVANCE = "relevance"
    EXPLICIT_SEED = "explicit_seed"
    EXPLICIT_BROAD = "explicit_broad"


class AgentSelectionState(StrEnum):
    READY = "ready"
    DEGRADED = "degraded"
    BLOCKED = "blocked"


class IndexRefreshState(StrEnum):
    REFRESHED = "refreshed"
    REUSED = "reused"
    FAILED = "failed"


@dataclass(frozen=True)
class DocumentSlice:
    source_path: str
    start_line: int
    end_line: int
    heading: str
    excerpt: str
    artifact_type: str
    markdown_role: MarkdownRole
    selected_by: str
    score: int
    related_memory_object_ids: tuple[str, ...]
    source_freshness: str


@dataclass(frozen=True)
class AgentContextBundle:
    task: str
    scope: str | None
    index_refresh_state: IndexRefreshState
    index_refresh_error: str | None
    selection_mode: AgentSelectionMode
    selection_state: AgentSelectionState
    selection_reason: str
    document_budget: int
    memory_budget: int
    query_plan: tuple[str, ...]
    memory_truncations: tuple[str, ...]
    memory: ContextPackage
    documents: tuple[DocumentSlice, ...]
    explanation: tuple[str, ...]

    @property
    def index_refreshed(self) -> bool:
        return self.index_refresh_state == IndexRefreshState.REFRESHED


CONSTITUTIONAL_DOCS = frozenset(
    {
        "docs/VISION.md",
        "docs/CORE_CONCEPTS.md",
        "docs/GOVERNANCE_MODEL.md",
    }
)

CANONICAL_DOCS = frozenset(
    {
        "AGENTS.md",
        "docs/PORTFOLIO_CONTEXT.md",
        "docs/PORTFOLIO_ASSUMPTIONS.md",
        "docs/INTEGRATION_ARCHITECTURE.md",
        "docs/PROJECT_MEMORY_ARCHITECTURE.md",
        "docs/THINKING_ENGINE_ARCHITECTURE.md",
        "docs/PROJECT_STATE.md",
        "docs/ROADMAP.md",
        "docs/CHANGELOG.md",
    }
)

GENERATED_NAME_MARKERS = frozenset(
    {
        "CONTEXT_RECALL_REPORT.md",
        "VALIDATION_CLOSEOUT_REPORT.md",
        "PACK_AUDIT_REPORT.md",
        "PACK_CHECKLIST.md",
        "INTENT_LOCK_REPORT.md",
        "EXECUTION_PROMPT.md",
        "MISSION_CHECKPOINT.md",
        "MISSION_COMPLETION_REPORT.md",
    }
)

EVIDENCE_NAME_MARKERS = frozenset(
    {
        "verification_plan.md",
        "traceability_matrix.md",
        "risk_register.md",
        "premortem.md",
        "external_source_review.md",
    }
)

MAX_QUERY_ATTEMPTS = 6
QUERY_STOP_WORDS = frozenset(
    {
        "a",
        "an",
        "and",
        "after",
        "before",
        "for",
        "from",
        "in",
        "of",
        "on",
        "or",
        "the",
        "to",
        "with",
    }
)
QUERY_DOMAIN_TERMS = frozenset(
    {
        "agent",
        "architecture",
        "constraint",
        "context",
        "decision",
        "evidence",
        "implementation",
        "memory",
        "project",
        "roadmap",
    }
)
ROLE_PRIORITY = {
    MarkdownRole.CONSTITUTIONAL: 50,
    MarkdownRole.CANONICAL: 40,
    MarkdownRole.EVIDENCE: 30,
    MarkdownRole.GENERATED: 20,
    MarkdownRole.WORKING: 10,
    MarkdownRole.DEPRECATED: 0,
}
AGENT_EXPANSION_RELATIONSHIPS = frozenset(
    {
        RelationshipType.SUPPORTS,
        RelationshipType.CHALLENGES,
        RelationshipType.DEPENDS_ON,
        RelationshipType.SUPERSEDES,
        RelationshipType.INVALIDATES,
        RelationshipType.DERIVED_FROM,
        RelationshipType.EVIDENCES,
        RelationshipType.HAS_CAPABILITY,
        RelationshipType.HAS_AUTHORITY,
        RelationshipType.BLOCKS,
        RelationshipType.ANSWERS,
        RelationshipType.CONTRADICTS,
        RelationshipType.MAPS_TO,
    }
)


def build_agent_context_bundle(
    *,
    root: Path,
    task: str,
    memory: ProjectMemory,
    access: AccessContext,
    scope: str | None = None,
    queries: Sequence[str] = (),
    seed_object_ids: Sequence[str] = (),
    limit: int = 5,
    memory_limit: int = 8,
    db_path: Path | None = None,
    refresh_index: bool = True,
) -> AgentContextBundle:
    """Build a small, explained context bundle for an agent task."""

    if not task.strip():
        raise ValueError("task is required")
    if limit <= 0:
        raise ValueError("limit must be positive")
    if memory_limit <= 0:
        raise ValueError("memory_limit must be positive")

    repo_root = root.resolve()
    refresh_state, refresh_error, index_available = _prepare_context_index(
        root=repo_root,
        db_path=db_path,
        refresh=refresh_index,
    )
    query_plan = plan_context_queries(task, queries)
    documents = (
        _select_document_slices(
            root=repo_root,
            task=task,
            queries=query_plan,
            scope=scope,
            limit=limit,
            db_path=db_path,
            memory=memory,
            access=access,
        )
        if index_available
        else ()
    )
    context_seed_ids, seed_reasons, memory_truncations = _select_memory_ids(
        memory=memory,
        explicit_seed_ids=seed_object_ids,
        documents=documents,
        memory_limit=memory_limit,
    )
    context_package = build_context_package(
        memory,
        ContextRequest(
            purpose=f"Agent context: {task}",
            access=access,
            boundary="agent_context",
            seed_object_ids=context_seed_ids,
            selection_mode=ContextSelectionMode.EXPLICIT_SEED,
        ),
    )
    context_package = _with_selection_reasons(context_package, seed_reasons)
    selection_mode = AgentSelectionMode.EXPLICIT_SEED if seed_object_ids else AgentSelectionMode.RELEVANCE
    selection_state, selection_reason = _selection_outcome(
        index_available=index_available,
        refresh_state=refresh_state,
        documents=documents,
        context_package=context_package,
    )
    return AgentContextBundle(
        task=task,
        scope=scope,
        index_refresh_state=refresh_state,
        index_refresh_error=refresh_error,
        selection_mode=selection_mode,
        selection_state=selection_state,
        selection_reason=selection_reason,
        document_budget=limit,
        memory_budget=memory_limit,
        query_plan=query_plan,
        memory_truncations=memory_truncations,
        memory=context_package,
        documents=documents,
        explanation=_explanation(
            documents,
            context_package,
            context_seed_ids,
            refresh_state,
            selection_state,
            selection_reason,
            query_plan,
            limit,
            memory_limit,
            memory_truncations,
        ),
    )


def format_agent_context_markdown(bundle: AgentContextBundle) -> str:
    """Render an agent context bundle as compact Markdown."""

    lines = [
        f"# Agent Context: {bundle.task}",
        "",
        f"- Scope: `{bundle.scope or 'ALL'}`",
        f"- Selection mode: `{bundle.selection_mode.value}`",
        f"- Selection state: `{bundle.selection_state.value}` ({bundle.selection_reason})",
        f"- Refresh state: `{bundle.index_refresh_state.value}`",
        f"- Budgets: documents={bundle.document_budget}, memory={bundle.memory_budget}",
        "",
        "## Why This Context",
    ]
    lines.extend(f"- {item}" for item in bundle.explanation)
    lines.extend(["", "## Project Memory"])
    if bundle.memory.current:
        for item in bundle.memory.current:
            obj = item.object
            lines.append(f"- `{obj.id}` {obj.title} ({obj.type.value}, {obj.status.value}): {item.reason}")
    else:
        lines.append("- None")
    if bundle.memory.surfaced:
        lines.extend(["", "## Surfaced Non-Current Memory"])
        for item in bundle.memory.surfaced:
            obj = item.object
            lines.append(f"- `{obj.id}` {obj.title} ({obj.type.value}, {obj.status.value}): {item.reason}")
    if bundle.memory.contradictions:
        lines.extend(["", "## Contradictions"])
        for left, right in bundle.memory.contradictions:
            lines.append(f"- `{left.id}` {left.title} <> `{right.id}` {right.title}")
    lines.extend(["", "## Document Slices"])
    if bundle.documents:
        for document in bundle.documents:
            related = ", ".join(document.related_memory_object_ids) or "none"
            lines.extend(
                [
                    f"- `{document.source_path}:{document.start_line}` ({document.markdown_role.value}, {document.artifact_type})",
                    f"  - Heading: {document.heading}",
                    f"  - Selected by: {document.selected_by}",
                    f"  - Related memory: {related}",
                    f"  - Source freshness: {document.source_freshness}",
                    f"  - Excerpt: {document.excerpt.replace(chr(10), ' ')}",
                ]
            )
    else:
        lines.append("- None")
    if bundle.memory.exclusions:
        lines.extend(["", "## Exclusions"])
        for exclusion in bundle.memory.exclusions:
            lines.append(f"- `{exclusion.object_id}` {exclusion.title}: {exclusion.reason}")
    if bundle.memory_truncations:
        lines.extend(["", "## Budget Truncations"])
        lines.extend(f"- {item}" for item in bundle.memory_truncations)
    return "\n".join(lines) + "\n"


def agent_context_summary(bundle: AgentContextBundle) -> dict[str, Any]:
    return {
        "ok": True,
        "command": "agent-context",
        "task": bundle.task,
        "scope": bundle.scope,
        "index_refreshed": bundle.index_refreshed,
        "refresh_state": bundle.index_refresh_state.value,
        "refresh_error": bundle.index_refresh_error,
        "selection_mode": bundle.selection_mode.value,
        "selection_state": bundle.selection_state.value,
        "selection_reason": bundle.selection_reason,
        "query_plan": list(bundle.query_plan),
        "budgets": {"documents": bundle.document_budget, "memory": bundle.memory_budget},
        "memory_truncations": list(bundle.memory_truncations),
        "explanation": list(bundle.explanation),
        "memory": {
            "purpose": bundle.memory.purpose,
            "boundary": bundle.memory.boundary,
            "current": [_memory_item_summary(item.object, item.reason) for item in bundle.memory.current],
            "surfaced": [_memory_item_summary(item.object, item.reason) for item in bundle.memory.surfaced],
            "contradictions": [
                {"left": _memory_object_ref(left), "right": _memory_object_ref(right)}
                for left, right in bundle.memory.contradictions
            ],
            "exclusions": [
                {"object_id": exclusion.object_id, "title": exclusion.title, "reason": exclusion.reason}
                for exclusion in bundle.memory.exclusions
            ],
        },
        "documents": [
            {
                "source_path": document.source_path,
                "start_line": document.start_line,
                "end_line": document.end_line,
                "heading": document.heading,
                "excerpt": document.excerpt,
                "artifact_type": document.artifact_type,
                "markdown_role": document.markdown_role.value,
                "selected_by": document.selected_by,
                "score": document.score,
                "related_memory_object_ids": list(document.related_memory_object_ids),
                "source_freshness": document.source_freshness,
            }
            for document in bundle.documents
        ],
    }


def markdown_role_for_source(source_path: str, artifact_type: str = "") -> MarkdownRole:
    normalized = source_path.strip().lstrip("./")
    name = Path(normalized).name
    parts = Path(normalized).parts
    lowered_parts = tuple(part.lower() for part in parts)
    if "deprecated" in lowered_parts or "archive" in lowered_parts or "archives" in lowered_parts:
        return MarkdownRole.DEPRECATED
    if normalized in CONSTITUTIONAL_DOCS:
        return MarkdownRole.CONSTITUTIONAL
    if normalized in CANONICAL_DOCS:
        return MarkdownRole.CANONICAL
    if name in GENERATED_NAME_MARKERS or artifact_type in {
        "factory_run_root_artifact",
        "mission_artifact",
        "po_phase_artifact",
    }:
        return MarkdownRole.GENERATED
    if name in EVIDENCE_NAME_MARKERS:
        return MarkdownRole.EVIDENCE
    if normalized.startswith("docs/Factory/runs/") or normalized.startswith("docs/Factory/templates/"):
        return MarkdownRole.WORKING
    if normalized.startswith("docs/research/"):
        return MarkdownRole.EVIDENCE
    return MarkdownRole.WORKING


def plan_context_queries(task: str, queries: Sequence[str]) -> tuple[str, ...]:
    """Return a small deterministic recall plan for natural task text."""

    candidates = list(queries) + [task]
    tokens = re.findall(r"[A-Za-z0-9_/-]+", task)
    pairs: list[tuple[int, int, int, str]] = []
    for index, (left, right) in enumerate(zip(tokens, tokens[1:])):
        if left.lower() in QUERY_STOP_WORDS or right.lower() in QUERY_STOP_WORDS:
            continue
        domain_score = int(left.lower() in QUERY_DOMAIN_TERMS) + int(right.lower() in QUERY_DOMAIN_TERMS)
        title_score = int(left[:1].isupper()) + int(right[:1].isupper())
        pairs.append((domain_score, title_score, index, f"{left} {right}"))
    pairs.sort(key=lambda item: (-item[0], -item[1], item[2]))
    candidates.extend(pair for _, _, _, pair in pairs)

    significant = [
        token
        for token in tokens
        if len(token) >= 4 and token.lower() not in QUERY_STOP_WORDS
    ]
    candidates.extend(sorted(significant, key=lambda token: (-len(token), token.lower())))
    return _dedupe_case_insensitive(candidates)[:MAX_QUERY_ATTEMPTS]


def _select_document_slices(
    *,
    root: Path,
    task: str,
    queries: Sequence[str],
    scope: str | None,
    limit: int,
    db_path: Path | None,
    memory: ProjectMemory,
    access: AccessContext,
) -> tuple[DocumentSlice, ...]:
    slices_by_chunk: dict[int, DocumentSlice] = {}
    visible_objects = memory.visible_objects(access)
    for query in queries:
        payload = recall_context(root=root, query=query, db_path=db_path, scope=scope, limit=limit)
        for match in payload["matches"]:
            chunk_id = int(match["chunk_id"])
            source_path = match["source_path"]
            specificity = max(0, 100 - min(int(payload["match_count"]), 100))
            candidate = DocumentSlice(
                source_path=source_path,
                start_line=int(match["start_line"]),
                end_line=int(match["end_line"]),
                heading=match["heading"],
                excerpt=match["excerpt"],
                artifact_type=match["artifact_type"],
                markdown_role=markdown_role_for_source(source_path, match["artifact_type"]),
                selected_by=query if query != task else "task",
                score=min(int(match["score"]), 20) + specificity,
                related_memory_object_ids=_memory_refs_for_source(visible_objects, source_path),
                source_freshness=_source_freshness(root, source_path, match.get("content_sha", "")),
            )
            existing = slices_by_chunk.get(chunk_id)
            if existing is None or _document_rank(candidate) < _document_rank(existing):
                slices_by_chunk[chunk_id] = candidate
    ranked = sorted(slices_by_chunk.values(), key=_document_rank)
    return tuple(ranked[:limit])


def _document_rank(document: DocumentSlice) -> tuple[int, int, str, int]:
    role_priority = ROLE_PRIORITY[document.markdown_role]
    return (
        -(document.score + role_priority),
        -role_priority,
        document.source_path,
        document.start_line,
    )


def _source_freshness(root: Path, source_path: str, indexed_sha: str) -> str:
    path = root / source_path
    if not path.is_file():
        return "missing"
    try:
        current_sha = hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return "missing"
    return "current" if current_sha == indexed_sha else "changed"


def _prepare_context_index(
    *,
    root: Path,
    db_path: Path | None,
    refresh: bool,
) -> tuple[IndexRefreshState, str | None, bool]:
    if refresh:
        try:
            build_context_index(root, db_path=db_path)
            return IndexRefreshState.REFRESHED, None, True
        except FactoryContextIndexError as exc:
            available = _has_context_index(root, db_path)
            return IndexRefreshState.FAILED, str(exc), available
    return IndexRefreshState.REUSED, None, _has_context_index(root, db_path)


def _has_context_index(root: Path, db_path: Path | None) -> bool:
    try:
        return int(describe_context(root=root, db_path=db_path)["source_count"]) > 0
    except (FactoryContextIndexError, OSError, sqlite3.Error):
        return False


def _select_memory_ids(
    *,
    memory: ProjectMemory,
    explicit_seed_ids: Sequence[str],
    documents: Sequence[DocumentSlice],
    memory_limit: int,
) -> tuple[tuple[str, ...], dict[str, str], tuple[str, ...]]:
    selected: list[str] = []
    reasons: dict[str, str] = {}
    truncations: list[str] = []
    truncated_ids: set[str] = set()

    def add(object_id: str, reason: str) -> bool:
        if object_id in reasons:
            return True
        if len(selected) >= memory_limit:
            if object_id not in truncated_ids:
                truncated_ids.add(object_id)
                truncations.append(f"memory_budget_reached:{object_id}:{reason}")
            return False
        selected.append(object_id)
        reasons[object_id] = reason
        return True

    for object_id in explicit_seed_ids:
        add(object_id, "explicit_seed")
    for document in documents:
        for object_id in document.related_memory_object_ids:
            add(object_id, f"source_ref:{document.source_path}")

    base_ids = tuple(selected)
    for source_id in base_ids:
        source = memory.inspect(source_id)
        if source is None:
            continue
        relationships = sorted(source.relationships, key=lambda item: (item.type.value, item.target_id))
        for relationship in relationships:
            if relationship.type not in AGENT_EXPANSION_RELATIONSHIPS:
                continue
            target = memory.inspect(relationship.target_id)
            if target is None:
                continue
            add(target.id, f"relationship:{relationship.type.value}:{source.id}")
    return tuple(selected), reasons, tuple(truncations)


def _with_selection_reasons(package: ContextPackage, reasons: Mapping[str, str]) -> ContextPackage:
    return ContextPackage(
        purpose=package.purpose,
        boundary=package.boundary,
        selection_mode=package.selection_mode,
        current=tuple(ContextItem(item.object, reasons.get(item.object.id, item.reason)) for item in package.current),
        surfaced=tuple(ContextItem(item.object, reasons.get(item.object.id, item.reason)) for item in package.surfaced),
        contradictions=package.contradictions,
        exclusions=package.exclusions,
    )


def _selection_outcome(
    *,
    index_available: bool,
    refresh_state: IndexRefreshState,
    documents: Sequence[DocumentSlice],
    context_package: ContextPackage,
) -> tuple[AgentSelectionState, str]:
    has_memory = bool(context_package.current or context_package.surfaced)
    if not index_available:
        if has_memory:
            return AgentSelectionState.DEGRADED, "context_index_unavailable_using_explicit_memory"
        return AgentSelectionState.BLOCKED, "context_index_unavailable"
    if not documents and not has_memory:
        return AgentSelectionState.DEGRADED, "no_relevant_context"
    if refresh_state == IndexRefreshState.FAILED:
        return AgentSelectionState.DEGRADED, "refresh_failed_using_previous_index"
    return AgentSelectionState.READY, "bounded_context_selected"


def _memory_refs_for_source(memory_objects: Iterable[MemoryObject], source_path: str) -> tuple[str, ...]:
    normalized_source = _normalize_source_ref(source_path)
    refs: list[MemoryObject] = []
    for memory_object in memory_objects:
        source_refs = tuple(_normalize_source_ref(ref) for ref in memory_object.provenance.source_refs)
        derivation_refs = tuple(_normalize_source_ref(ref) for ref in memory_object.provenance.derivation_refs)
        if normalized_source in source_refs or normalized_source in derivation_refs:
            refs.append(memory_object)
    refs.sort(key=lambda item: (item.status in NON_CURRENT_STATUSES, item.id))
    return tuple(item.id for item in refs)


def _normalize_source_ref(ref: str) -> str:
    return ref.strip().lstrip("./").split("#", 1)[0]


def _explanation(
    documents: Sequence[DocumentSlice],
    context_package: ContextPackage,
    seed_object_ids: Sequence[str],
    refresh_state: IndexRefreshState,
    selection_state: AgentSelectionState,
    selection_reason: str,
    query_plan: Sequence[str],
    document_budget: int,
    memory_budget: int,
    memory_truncations: Sequence[str],
) -> tuple[str, ...]:
    lines = [
        "Document slices were selected through the Factory context index, so doc recall and memory context share one retrieval entry point.",
        "Project Memory objects were selected by matching recalled document paths against object provenance and derivation references.",
        f"Selection state is {selection_state.value}: {selection_reason}.",
        f"Context index refresh state is {refresh_state.value}.",
        f"Query plan used {len(query_plan)} of {MAX_QUERY_ATTEMPTS} allowed attempts; budgets are documents={document_budget}, memory={memory_budget}.",
    ]
    if seed_object_ids:
        lines.append(f"{len(seed_object_ids)} Project Memory object(s) seeded context assembly.")
    else:
        lines.append("No Project Memory objects matched recalled document sources.")
    if context_package.exclusions:
        lines.append(f"{len(context_package.exclusions)} memory object(s) were excluded by visibility or propagation rules.")
    if memory_truncations:
        lines.append(f"{len(memory_truncations)} memory candidate(s) were excluded by the memory budget.")
    role_counts = _role_counts(documents)
    if role_counts:
        lines.append(
            "Markdown roles in this bundle: "
            + ", ".join(f"{role}={count}" for role, count in sorted(role_counts.items()))
            + "."
        )
    return tuple(lines)


def _role_counts(documents: Sequence[DocumentSlice]) -> Mapping[str, int]:
    counts: dict[str, int] = {}
    for document in documents:
        counts[document.markdown_role.value] = counts.get(document.markdown_role.value, 0) + 1
    return counts


def _memory_item_summary(memory_object: MemoryObject, reason: str) -> dict[str, Any]:
    summary = _memory_object_ref(memory_object)
    summary.update(
        {
            "reason": reason,
            "visibility": memory_object.visibility.value,
            "evidence_level": memory_object.provenance.evidence_level.value,
            "source_refs": list(memory_object.provenance.source_refs),
            "relationship_count": len(memory_object.relationships),
        }
    )
    return summary


def _memory_object_ref(memory_object: MemoryObject) -> dict[str, str]:
    return {
        "id": memory_object.id,
        "type": memory_object.type.value,
        "title": memory_object.title,
        "status": memory_object.status.value,
    }


def _dedupe_preserve_order(values: Sequence[str]) -> tuple[str, ...]:
    seen: set[str] = set()
    output: list[str] = []
    for value in values:
        cleaned = value.strip()
        if not cleaned or cleaned in seen:
            continue
        seen.add(cleaned)
        output.append(cleaned)
    return tuple(output)


def _dedupe_case_insensitive(values: Sequence[str]) -> tuple[str, ...]:
    seen: set[str] = set()
    output: list[str] = []
    for value in values:
        cleaned = value.strip()
        key = cleaned.lower()
        if not cleaned or key in seen:
            continue
        seen.add(key)
        output.append(cleaned)
    return tuple(output)
