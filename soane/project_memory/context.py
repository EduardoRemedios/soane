"""Context assembly and Markdown source mapping for Project Memory v0."""

from __future__ import annotations

from dataclasses import dataclass

from soane.project_memory.contract import LifecycleStatus, MemoryObject, RelationshipType
from soane.project_memory.semantics import AccessContext, NON_CURRENT_STATUSES, ProjectMemory, is_visible


class ContextAssemblyError(ValueError):
    """Raised when context assembly receives an invalid request."""


@dataclass(frozen=True)
class ContextRequest:
    purpose: str
    access: AccessContext
    boundary: str = "project_context"
    seed_object_ids: tuple[str, ...] = ()


@dataclass(frozen=True)
class ContextItem:
    object: MemoryObject
    reason: str


@dataclass(frozen=True)
class ContextExclusion:
    object_id: str
    title: str
    reason: str


@dataclass(frozen=True)
class ContextPackage:
    purpose: str
    boundary: str
    current: tuple[ContextItem, ...]
    surfaced: tuple[ContextItem, ...]
    contradictions: tuple[tuple[MemoryObject, MemoryObject], ...]
    exclusions: tuple[ContextExclusion, ...]


@dataclass(frozen=True)
class MarkdownSource:
    object_id: str
    title: str
    source_refs: tuple[str, ...]
    evidence_level: str
    related_object_ids: tuple[str, ...] = ()


@dataclass(frozen=True)
class MarkdownView:
    body: str
    source_map: dict[str, MarkdownSource]


def build_context_package(memory: ProjectMemory, request: ContextRequest) -> ContextPackage:
    """Build a deterministic v0 context package from local Project Memory."""

    if not request.purpose.strip():
        raise ContextAssemblyError("context purpose is required")

    candidates = _candidate_objects(memory, request)
    current: list[ContextItem] = []
    surfaced: list[ContextItem] = []
    exclusions = _seed_exclusions(memory, request)
    exclusions.extend(_relationship_exclusions(memory, candidates, request))

    for memory_object in candidates:
        propagation_reason = _propagation_exclusion_reason(memory_object, request.boundary)
        if propagation_reason:
            exclusions.append(ContextExclusion(memory_object.id, memory_object.title, propagation_reason))
            continue
        if memory_object.status in NON_CURRENT_STATUSES:
            surfaced.append(ContextItem(memory_object, _surface_reason(memory_object.status)))
        else:
            current.append(ContextItem(memory_object, "current_visible_memory"))

    return ContextPackage(
        purpose=request.purpose,
        boundary=request.boundary,
        current=tuple(current),
        surfaced=tuple(surfaced),
        contradictions=memory.contradictions(request.access),
        exclusions=tuple(exclusions),
    )


def render_markdown_view(package: ContextPackage) -> MarkdownView:
    """Render a human-readable Markdown view with source mappings."""

    lines = [f"# Context Package: {package.purpose}", "", f"Boundary: `{package.boundary}`", ""]
    source_map: dict[str, MarkdownSource] = {}

    lines.append("## Current Memory")
    if package.current:
        for index, item in enumerate(package.current, start=1):
            anchor = f"current-{index:03d}"
            lines.append(_render_item(anchor, item))
            source_map[anchor] = _source_for(item.object)
    else:
        lines.append("- None")

    lines.extend(["", "## Surfaced Non-Current Memory"])
    if package.surfaced:
        for index, item in enumerate(package.surfaced, start=1):
            anchor = f"surfaced-{index:03d}"
            lines.append(_render_item(anchor, item))
            source_map[anchor] = _source_for(item.object)
    else:
        lines.append("- None")

    lines.extend(["", "## Contradictions"])
    if package.contradictions:
        for index, (left, right) in enumerate(package.contradictions, start=1):
            anchor = f"contradiction-{index:03d}"
            lines.append(f"- [{anchor}] {left.title} <> {right.title}")
            source_map[f"{anchor}-left"] = _source_for(left)
            source_map[f"{anchor}-right"] = _source_for(right)
    else:
        lines.append("- None")

    lines.extend(["", "## Exclusions"])
    if package.exclusions:
        for exclusion in package.exclusions:
            lines.append(f"- {exclusion.title} ({exclusion.object_id}): {exclusion.reason}")
    else:
        lines.append("- None")

    return MarkdownView(body="\n".join(lines) + "\n", source_map=source_map)


def _candidate_objects(memory: ProjectMemory, request: ContextRequest) -> tuple[MemoryObject, ...]:
    if not request.seed_object_ids:
        return memory.visible_objects(request.access)

    candidates: list[MemoryObject] = []
    for object_id in request.seed_object_ids:
        memory_object = memory.inspect(object_id)
        if memory_object is None:
            continue
        if is_visible(memory_object, request.access):
            candidates.append(memory_object)
    return tuple(candidates)


def _seed_exclusions(memory: ProjectMemory, request: ContextRequest) -> list[ContextExclusion]:
    exclusions: list[ContextExclusion] = []
    for object_id in request.seed_object_ids:
        memory_object = memory.inspect(object_id)
        if memory_object is None:
            exclusions.append(ContextExclusion(object_id, object_id, "unknown_seed_object"))
            continue
        if not is_visible(memory_object, request.access):
            exclusions.append(ContextExclusion(memory_object.id, memory_object.title, "not_visible_to_access_context"))
            continue
        propagation_reason = _propagation_exclusion_reason(memory_object, request.boundary)
        if propagation_reason:
            exclusions.append(ContextExclusion(memory_object.id, memory_object.title, propagation_reason))
    return _dedupe_exclusions(exclusions)


def _relationship_exclusions(
    memory: ProjectMemory,
    candidates: tuple[MemoryObject, ...],
    request: ContextRequest,
) -> list[ContextExclusion]:
    exclusions: list[ContextExclusion] = []
    for memory_object in candidates:
        for relationship in memory_object.relationships:
            target = memory.inspect(relationship.target_id)
            if target is None:
                continue
            if not is_visible(target, request.access):
                exclusions.append(ContextExclusion(target.id, target.title, "not_visible_to_access_context"))
            elif _propagation_exclusion_reason(target, request.boundary):
                exclusions.append(
                    ContextExclusion(target.id, target.title, _propagation_exclusion_reason(target, request.boundary))
                )
    return _dedupe_exclusions(exclusions)


def _dedupe_exclusions(exclusions: list[ContextExclusion]) -> list[ContextExclusion]:
    seen: set[tuple[str, str]] = set()
    deduped: list[ContextExclusion] = []
    for exclusion in exclusions:
        key = (exclusion.object_id, exclusion.reason)
        if key in seen:
            continue
        seen.add(key)
        deduped.append(exclusion)
    return deduped


def _propagation_exclusion_reason(memory_object: MemoryObject, boundary: str) -> str | None:
    propagation = memory_object.metadata.get("propagation")
    if boundary == "external_adapter_context" and propagation == "exclude_from_external_adapter_context":
        return "blocked_by_propagation_rule"
    return None


def _surface_reason(status: LifecycleStatus) -> str:
    if status == LifecycleStatus.PROPOSED:
        return "candidate_record_surface_for_review"
    if status == LifecycleStatus.OPEN:
        return "open_record_surface_for_review"
    if status == LifecycleStatus.DEFERRED:
        return "deferred_record_surface_for_review"
    if status == LifecycleStatus.STALE:
        return "stale_record_surface_for_review"
    if status == LifecycleStatus.SUPERSEDED:
        return "superseded_record_surface_for_history"
    if status == LifecycleStatus.INVALIDATED:
        return "invalidated_record_surface_for_history"
    if status == LifecycleStatus.REVOKED:
        return "revoked_record_surface_for_history"
    return "non_current_record_surface_for_review"


def _render_item(anchor: str, item: ContextItem) -> str:
    obj = item.object
    return f"- [{anchor}] {obj.title} (`{obj.type.value}`, `{obj.status.value}`): {item.reason}"


def _source_for(memory_object: MemoryObject) -> MarkdownSource:
    return MarkdownSource(
        object_id=memory_object.id,
        title=memory_object.title,
        source_refs=memory_object.provenance.source_refs,
        evidence_level=memory_object.provenance.evidence_level.value,
        related_object_ids=tuple(
            relationship.target_id
            for relationship in memory_object.relationships
            if relationship.type
            in {
                RelationshipType.MAPS_TO,
                RelationshipType.DERIVED_FROM,
                RelationshipType.EVIDENCES,
            }
        ),
    )
