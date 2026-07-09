"""Agent-facing context bundles over Project Memory and Factory recall."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from scripts.factory_context_index import build_context_index, recall_context
from soane.project_memory.context import ContextPackage, ContextRequest, build_context_package
from soane.project_memory.contract import MemoryObject
from soane.project_memory.semantics import AccessContext, ProjectMemory


class MarkdownRole(StrEnum):
    CONSTITUTIONAL = "constitutional"
    CANONICAL = "canonical"
    WORKING = "working"
    GENERATED = "generated"
    EVIDENCE = "evidence"
    DEPRECATED = "deprecated"


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


@dataclass(frozen=True)
class AgentContextBundle:
    task: str
    scope: str | None
    index_refreshed: bool
    memory: ContextPackage
    documents: tuple[DocumentSlice, ...]
    explanation: tuple[str, ...]


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
    db_path: Path | None = None,
    refresh_index: bool = True,
) -> AgentContextBundle:
    """Build a small, explained context bundle for an agent task."""

    if not task.strip():
        raise ValueError("task is required")
    if limit <= 0:
        raise ValueError("limit must be positive")

    repo_root = root.resolve()
    if refresh_index:
        build_context_index(repo_root, db_path=db_path)

    documents = _select_document_slices(
        root=repo_root,
        task=task,
        queries=_dedupe_preserve_order((task, *queries)),
        scope=scope,
        limit=limit,
        db_path=db_path,
        memory=memory,
        access=access,
    )
    related_object_ids = _related_memory_object_ids(memory.visible_objects(access), documents)
    context_seed_ids = tuple(_dedupe_preserve_order((*seed_object_ids, *related_object_ids)))
    context_package = build_context_package(
        memory,
        ContextRequest(
            purpose=f"Agent context: {task}",
            access=access,
            boundary="agent_context",
            seed_object_ids=context_seed_ids,
        ),
    )
    return AgentContextBundle(
        task=task,
        scope=scope,
        index_refreshed=refresh_index,
        memory=context_package,
        documents=documents,
        explanation=_explanation(documents, context_package, context_seed_ids),
    )


def format_agent_context_markdown(bundle: AgentContextBundle) -> str:
    """Render an agent context bundle as compact Markdown."""

    lines = [
        f"# Agent Context: {bundle.task}",
        "",
        f"- Scope: `{bundle.scope or 'ALL'}`",
        f"- Index refreshed: `{str(bundle.index_refreshed).lower()}`",
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
                    f"  - Excerpt: {document.excerpt.replace(chr(10), ' ')}",
                ]
            )
    else:
        lines.append("- None")
    if bundle.memory.exclusions:
        lines.extend(["", "## Exclusions"])
        for exclusion in bundle.memory.exclusions:
            lines.append(f"- `{exclusion.object_id}` {exclusion.title}: {exclusion.reason}")
    return "\n".join(lines) + "\n"


def agent_context_summary(bundle: AgentContextBundle) -> dict[str, Any]:
    return {
        "ok": True,
        "command": "agent-context",
        "task": bundle.task,
        "scope": bundle.scope,
        "index_refreshed": bundle.index_refreshed,
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
    slices: list[DocumentSlice] = []
    seen_chunks: set[int] = set()
    visible_objects = memory.visible_objects(access)
    for query in queries:
        payload = recall_context(root=root, query=query, db_path=db_path, scope=scope, limit=limit)
        for match in payload["matches"]:
            chunk_id = int(match["chunk_id"])
            if chunk_id in seen_chunks:
                continue
            seen_chunks.add(chunk_id)
            source_path = match["source_path"]
            slices.append(
                DocumentSlice(
                    source_path=source_path,
                    start_line=int(match["start_line"]),
                    end_line=int(match["end_line"]),
                    heading=match["heading"],
                    excerpt=match["excerpt"],
                    artifact_type=match["artifact_type"],
                    markdown_role=markdown_role_for_source(source_path, match["artifact_type"]),
                    selected_by=query if query != task else "task",
                    score=int(match["score"]),
                    related_memory_object_ids=_memory_refs_for_source(visible_objects, source_path),
                )
            )
            if len(slices) >= limit:
                return tuple(slices)
    return tuple(slices)


def _related_memory_object_ids(
    memory_objects: Iterable[MemoryObject],
    documents: Sequence[DocumentSlice],
) -> tuple[str, ...]:
    selected = set()
    for document in documents:
        selected.update(document.related_memory_object_ids)
    return tuple(object_id for object_id in (obj.id for obj in memory_objects) if object_id in selected)


def _memory_refs_for_source(memory_objects: Iterable[MemoryObject], source_path: str) -> tuple[str, ...]:
    normalized_source = _normalize_source_ref(source_path)
    refs: list[str] = []
    for memory_object in memory_objects:
        source_refs = tuple(_normalize_source_ref(ref) for ref in memory_object.provenance.source_refs)
        derivation_refs = tuple(_normalize_source_ref(ref) for ref in memory_object.provenance.derivation_refs)
        if normalized_source in source_refs or normalized_source in derivation_refs:
            refs.append(memory_object.id)
    return tuple(refs)


def _normalize_source_ref(ref: str) -> str:
    return ref.strip().lstrip("./").split("#", 1)[0]


def _explanation(
    documents: Sequence[DocumentSlice],
    context_package: ContextPackage,
    seed_object_ids: Sequence[str],
) -> tuple[str, ...]:
    lines = [
        "Document slices were selected through the Factory context index, so doc recall and memory context share one retrieval entry point.",
        "Project Memory objects were selected by matching recalled document paths against object provenance and derivation references.",
    ]
    if seed_object_ids:
        lines.append(f"{len(seed_object_ids)} Project Memory object(s) seeded context assembly.")
    else:
        lines.append("No Project Memory objects matched recalled document sources.")
    if context_package.exclusions:
        lines.append(f"{len(context_package.exclusions)} memory object(s) were excluded by visibility or propagation rules.")
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
