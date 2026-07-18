"""Bounded typed traversal over local Project Memory relationships."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import Callable, Iterable

from soane.project_memory.contract import MemoryObject, RelationshipType
from soane.project_memory.semantics import (
    NON_CURRENT_STATUSES,
    AccessContext,
    ProjectMemory,
    is_visible,
)


MAX_DEPTH = 2
MAX_OBJECTS = 64
MAX_PATHS_PER_OBJECT = 4
MAX_EXAMINED_EDGES = 512
MAX_EXCLUSIONS = 64
MAX_TRUNCATIONS = 32


class GraphTraversalError(ValueError):
    """Raised when a graph traversal request violates a hard ceiling."""


class TraversalDirection(StrEnum):
    OUTBOUND = "outbound"
    INBOUND = "inbound"


@dataclass(frozen=True)
class GraphStep:
    source_id: str
    relationship_type: RelationshipType
    direction: TraversalDirection
    target_id: str


@dataclass(frozen=True)
class GraphPath:
    seed_id: str
    steps: tuple[GraphStep, ...]


@dataclass(frozen=True)
class GraphSelection:
    object: MemoryObject
    depth: int
    paths: tuple[GraphPath, ...]


@dataclass(frozen=True)
class GraphExclusion:
    reason: str
    source_id: str | None
    direction: TraversalDirection | None
    relationship_type: RelationshipType | None
    target_id: str


@dataclass(frozen=True)
class GraphTruncation:
    reason: str
    omitted_count: int


@dataclass(frozen=True)
class GraphTraversalRequest:
    seed_object_ids: tuple[str, ...]
    access: AccessContext
    directions: frozenset[TraversalDirection]
    relationship_types: frozenset[RelationshipType]
    max_depth: int = 1
    object_limit: int = 32
    path_limit_per_object: int = 2
    examined_edge_limit: int = 256
    include_non_current: bool = False


@dataclass(frozen=True)
class GraphTraversalResult:
    admitted_seed_ids: tuple[str, ...]
    selections: tuple[GraphSelection, ...]
    exclusions: tuple[GraphExclusion, ...]
    truncations: tuple[GraphTruncation, ...]
    examined_edge_count: int


def graph_result_payload(result: GraphTraversalResult) -> dict[str, object]:
    """Return a stable JSON-compatible traversal summary."""

    return {
        "admitted_seed_ids": list(result.admitted_seed_ids),
        "examined_edge_count": result.examined_edge_count,
        "selections": [
            {
                "object": {
                    "id": selection.object.id,
                    "type": selection.object.type.value,
                    "title": selection.object.title,
                    "status": selection.object.status.value,
                },
                "depth": selection.depth,
                "paths": [
                    {
                        "seed_id": path.seed_id,
                        "steps": [
                            {
                                "source_id": step.source_id,
                                "relationship_type": step.relationship_type.value,
                                "direction": step.direction.value,
                                "target_id": step.target_id,
                            }
                            for step in path.steps
                        ],
                    }
                    for path in selection.paths
                ],
            }
            for selection in result.selections
        ],
        "exclusions": [
            {
                "reason": exclusion.reason,
                "source_id": exclusion.source_id,
                "direction": exclusion.direction.value if exclusion.direction else None,
                "relationship_type": (
                    exclusion.relationship_type.value if exclusion.relationship_type else None
                ),
                "target_id": exclusion.target_id,
            }
            for exclusion in result.exclusions
        ],
        "truncations": [
            {"reason": truncation.reason, "omitted_count": truncation.omitted_count}
            for truncation in result.truncations
        ],
    }


@dataclass
class _MutableSelection:
    object: MemoryObject
    depth: int
    paths: list[GraphPath]


@dataclass(frozen=True)
class _Neighbor:
    source_id: str
    direction: TraversalDirection
    relationship_type: RelationshipType
    target_id: str


def traverse_memory(memory: ProjectMemory, request: GraphTraversalRequest) -> GraphTraversalResult:
    """Traverse authored relationships with deterministic policy and work bounds."""

    _validate_request(request)
    truncation_counts: dict[str, int] = {}
    exclusions: list[GraphExclusion] = []
    omitted_exclusions = 0

    def truncate(reason: str, count: int = 1) -> None:
        truncation_counts[reason] = truncation_counts.get(reason, 0) + count

    def exclude(exclusion: GraphExclusion) -> None:
        nonlocal omitted_exclusions
        if exclusion in exclusions:
            return
        if len(exclusions) >= MAX_EXCLUSIONS:
            omitted_exclusions += 1
            return
        exclusions.append(exclusion)

    if not request.seed_object_ids:
        truncate("no_seeds")
        return _result((), {}, exclusions, truncation_counts, 0, omitted_exclusions)

    selections: dict[str, _MutableSelection] = {}
    admitted_seeds: list[str] = []
    seed_candidates = _seed_candidates(memory, request, exclude)
    for memory_object in seed_candidates:
        if len(selections) >= request.object_limit:
            truncate("object_limit")
            continue
        path = GraphPath(seed_id=memory_object.id, steps=())
        selections[memory_object.id] = _MutableSelection(memory_object, 0, [path])
        admitted_seeds.append(memory_object.id)

    if not selections:
        return _result((), selections, exclusions, truncation_counts, 0, omitted_exclusions)
    if not request.directions:
        truncate("empty_direction_allowlist")
        return _result(admitted_seeds, selections, exclusions, truncation_counts, 0, omitted_exclusions)
    if not request.relationship_types:
        truncate("empty_relationship_allowlist")
        return _result(admitted_seeds, selections, exclusions, truncation_counts, 0, omitted_exclusions)
    inbound: dict[str, tuple[tuple[str, RelationshipType], ...]] = {}
    examined_edges = 0
    if TraversalDirection.INBOUND in request.directions:
        inbound, examined_edges, index_complete = _build_inbound_index(
            memory,
            edge_limit=request.examined_edge_limit,
        )
        if not index_complete:
            truncate("examined_edge_limit")
            return _result(
                admitted_seeds,
                selections,
                exclusions,
                truncation_counts,
                examined_edges,
                omitted_exclusions,
            )
    frontier = tuple(admitted_seeds)
    edge_limit_reached = False

    for depth in range(request.max_depth + 1):
        next_frontier: set[str] = set()
        for current_id in sorted(frontier, key=lambda item: _selection_sort_key(selections[item])):
            current = selections[current_id]
            base_path = min(current.paths, key=_path_sort_key)
            for neighbor in _neighbors(memory, inbound, current.object, request.directions):
                if examined_edges >= request.examined_edge_limit:
                    truncate("examined_edge_limit")
                    edge_limit_reached = True
                    break
                examined_edges += 1
                if neighbor.relationship_type not in request.relationship_types:
                    exclude(_edge_exclusion("disallowed_relationship", neighbor))
                    continue
                if depth >= request.max_depth:
                    truncate("depth_limit_reached")
                    continue

                target = memory.inspect(neighbor.target_id)
                if target is None:
                    reason = "missing_local_target" if neighbor.target_id.startswith("pmem_") else "external_target"
                    exclude(_edge_exclusion(reason, neighbor))
                    continue
                if not is_visible(target, request.access):
                    exclude(_edge_exclusion("inaccessible_target", neighbor))
                    continue
                if not request.include_non_current and target.status in NON_CURRENT_STATUSES:
                    exclude(_edge_exclusion("non_current_excluded", neighbor))
                    continue

                step = GraphStep(
                    source_id=current_id,
                    relationship_type=neighbor.relationship_type,
                    direction=neighbor.direction,
                    target_id=target.id,
                )
                path = GraphPath(seed_id=base_path.seed_id, steps=(*base_path.steps, step))
                if target.id in _path_object_ids(base_path):
                    exclude(_edge_exclusion("cycle", neighbor))
                    continue

                existing = selections.get(target.id)
                target_depth = depth + 1
                if existing is not None:
                    if existing.depth == target_depth and path not in existing.paths:
                        if len(existing.paths) < request.path_limit_per_object:
                            existing.paths.append(path)
                            existing.paths.sort(key=_path_sort_key)
                        else:
                            truncate("path_limit")
                    continue
                if len(selections) >= request.object_limit:
                    truncate("object_limit")
                    continue

                selections[target.id] = _MutableSelection(target, target_depth, [path])
                next_frontier.add(target.id)
            if edge_limit_reached:
                break
        frontier = tuple(next_frontier)
        if edge_limit_reached or not frontier:
            break

    return _result(
        admitted_seeds,
        selections,
        exclusions,
        truncation_counts,
        examined_edges,
        omitted_exclusions,
    )


def _validate_request(request: GraphTraversalRequest) -> None:
    _bounded_int("max_depth", request.max_depth, minimum=0, maximum=MAX_DEPTH)
    _bounded_int("object_limit", request.object_limit, minimum=1, maximum=MAX_OBJECTS)
    _bounded_int(
        "path_limit_per_object",
        request.path_limit_per_object,
        minimum=1,
        maximum=MAX_PATHS_PER_OBJECT,
    )
    _bounded_int(
        "examined_edge_limit",
        request.examined_edge_limit,
        minimum=1,
        maximum=MAX_EXAMINED_EDGES,
    )
    if not all(isinstance(item, TraversalDirection) for item in request.directions):
        raise GraphTraversalError("directions contain an invalid value")
    if not all(isinstance(item, RelationshipType) for item in request.relationship_types):
        raise GraphTraversalError("relationship_types contain an invalid value")


def _bounded_int(name: str, value: int, *, minimum: int, maximum: int) -> None:
    if type(value) is not int or not minimum <= value <= maximum:
        raise GraphTraversalError(f"{name} must be between {minimum} and {maximum}")


def _seed_candidates(
    memory: ProjectMemory,
    request: GraphTraversalRequest,
    exclude: Callable[[GraphExclusion], None],
) -> tuple[MemoryObject, ...]:
    candidates: list[MemoryObject] = []
    for object_id in dict.fromkeys(request.seed_object_ids):
        memory_object = memory.inspect(object_id)
        if memory_object is None:
            exclude(GraphExclusion("missing_seed", None, None, None, object_id))
            continue
        if not is_visible(memory_object, request.access):
            exclude(GraphExclusion("inaccessible_seed", None, None, None, object_id))
            continue
        if not request.include_non_current and memory_object.status in NON_CURRENT_STATUSES:
            exclude(GraphExclusion("non_current_seed_excluded", None, None, None, object_id))
            continue
        candidates.append(memory_object)
    return tuple(sorted(candidates, key=_object_sort_key))


def _build_inbound_index(
    memory: ProjectMemory,
    *,
    edge_limit: int,
) -> tuple[dict[str, tuple[tuple[str, RelationshipType], ...]], int, bool]:
    index: dict[str, set[tuple[str, RelationshipType]]] = {}
    examined = 0
    for source in sorted(memory.objects(), key=_object_sort_key):
        for relationship in sorted(
            source.relationships,
            key=lambda item: (item.type.value, item.target_id, item.evidence_ids),
        ):
            if examined >= edge_limit:
                return _frozen_inbound_index(index), examined, False
            examined += 1
            index.setdefault(relationship.target_id, set()).add((source.id, relationship.type))
    return _frozen_inbound_index(index), examined, True


def _frozen_inbound_index(
    index: dict[str, set[tuple[str, RelationshipType]]],
) -> dict[str, tuple[tuple[str, RelationshipType], ...]]:
    return {
        target_id: tuple(sorted(edges, key=lambda item: (item[1].value, item[0])))
        for target_id, edges in index.items()
    }


def _neighbors(
    memory: ProjectMemory,
    inbound: dict[str, tuple[tuple[str, RelationshipType], ...]],
    memory_object: MemoryObject,
    directions: frozenset[TraversalDirection],
) -> tuple[_Neighbor, ...]:
    items: set[_Neighbor] = set()
    if TraversalDirection.OUTBOUND in directions:
        for relationship in memory_object.relationships:
            items.add(
                _Neighbor(
                    source_id=memory_object.id,
                    direction=TraversalDirection.OUTBOUND,
                    relationship_type=relationship.type,
                    target_id=relationship.target_id,
                )
            )
    if TraversalDirection.INBOUND in directions:
        for source_id, relationship_type in inbound.get(memory_object.id, ()):
            items.add(
                _Neighbor(
                    source_id=memory_object.id,
                    direction=TraversalDirection.INBOUND,
                    relationship_type=relationship_type,
                    target_id=source_id,
                )
            )
    return tuple(sorted(items, key=lambda item: _neighbor_sort_key(memory, item)))


def _neighbor_sort_key(memory: ProjectMemory, neighbor: _Neighbor) -> tuple[object, ...]:
    target = memory.inspect(neighbor.target_id)
    target_key = _object_sort_key(target) if target is not None else (2, "", "", neighbor.target_id)
    return (
        target_key[0],
        neighbor.relationship_type.value,
        neighbor.direction.value,
        *target_key[1:],
    )


def _object_sort_key(memory_object: MemoryObject) -> tuple[object, ...]:
    return (
        int(memory_object.status in NON_CURRENT_STATUSES),
        memory_object.type.value,
        memory_object.title,
        memory_object.id,
    )


def _selection_sort_key(selection: _MutableSelection) -> tuple[object, ...]:
    return (selection.depth, *_object_sort_key(selection.object))


def _path_sort_key(path: GraphPath) -> tuple[object, ...]:
    return (
        path.seed_id,
        tuple(
            (
                step.relationship_type.value,
                step.direction.value,
                step.source_id,
                step.target_id,
            )
            for step in path.steps
        ),
    )


def _path_object_ids(path: GraphPath) -> frozenset[str]:
    return frozenset((path.seed_id, *(step.target_id for step in path.steps)))


def _edge_exclusion(reason: str, neighbor: _Neighbor) -> GraphExclusion:
    return GraphExclusion(
        reason=reason,
        source_id=neighbor.source_id,
        direction=neighbor.direction,
        relationship_type=neighbor.relationship_type,
        target_id=neighbor.target_id,
    )


def _result(
    admitted_seeds: Iterable[str],
    selections: dict[str, _MutableSelection],
    exclusions: list[GraphExclusion],
    truncation_counts: dict[str, int],
    examined_edges: int,
    omitted_exclusions: int,
) -> GraphTraversalResult:
    if omitted_exclusions:
        truncation_counts["exclusion_limit"] = omitted_exclusions
    selection_items = tuple(
        GraphSelection(
            object=item.object,
            depth=item.depth,
            paths=tuple(sorted(item.paths, key=_path_sort_key)),
        )
        for item in sorted(selections.values(), key=_selection_sort_key)
    )
    exclusion_items = tuple(
        sorted(
            exclusions,
            key=lambda item: (
                item.reason,
                item.source_id or "",
                item.relationship_type.value if item.relationship_type else "",
                item.direction.value if item.direction else "",
                item.target_id,
            ),
        )
    )
    sorted_truncations = sorted(truncation_counts.items())
    if len(sorted_truncations) > MAX_TRUNCATIONS:
        retained = sorted_truncations[: MAX_TRUNCATIONS - 1]
        omitted_count = sum(count for _, count in sorted_truncations[MAX_TRUNCATIONS - 1 :])
        sorted_truncations = [*retained, ("truncation_limit", omitted_count)]
    truncation_items = tuple(GraphTruncation(reason, count) for reason, count in sorted_truncations)
    return GraphTraversalResult(
        admitted_seed_ids=tuple(admitted_seeds),
        selections=selection_items,
        exclusions=exclusion_items,
        truncations=truncation_items,
        examined_edge_count=examined_edges,
    )
