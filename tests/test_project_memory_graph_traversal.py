from __future__ import annotations

import unittest
from dataclasses import asdict
from datetime import datetime, timezone
from hashlib import sha256

import soane.project_memory as project_memory
from soane.project_memory.contract import (
    EvidenceLevel,
    LifecycleStatus,
    MemoryObject,
    MemoryObjectType,
    Provenance,
    Relationship,
    RelationshipType,
    Visibility,
)
from soane.project_memory.graph import (
    MAX_EXAMINED_EDGES,
    MAX_EXCLUSIONS,
    MAX_OBJECTS,
    MAX_PATHS_PER_OBJECT,
    GraphTraversalError,
    GraphTraversalRequest,
    TraversalDirection,
    traverse_memory,
)
from soane.project_memory.semantics import PROJECT_READER, ProjectMemory


SOURCE_PATH = "docs/PROJECT_MEMORY_ARCHITECTURE.md"
CREATED_AT = datetime(2026, 7, 18, tzinfo=timezone.utc)


class ProjectMemoryGraphTraversalTests(unittest.TestCase):
    def test_request_validation_and_fail_closed_empty_inputs(self) -> None:
        memory, objects = _realistic_graph()

        empty_seeds = traverse_memory(
            memory,
            GraphTraversalRequest(
                seed_object_ids=(),
                access=PROJECT_READER,
                directions=frozenset({TraversalDirection.OUTBOUND}),
                relationship_types=frozenset({RelationshipType.DEPENDS_ON}),
            ),
        )
        empty_relationships = traverse_memory(
            memory,
            GraphTraversalRequest(
                seed_object_ids=(objects["claim"].id,),
                access=PROJECT_READER,
                directions=frozenset({TraversalDirection.OUTBOUND}),
                relationship_types=frozenset(),
                include_non_current=True,
            ),
        )

        self.assertFalse(empty_seeds.selections)
        self.assertEqual("no_seeds", empty_seeds.truncations[0].reason)
        self.assertEqual([objects["claim"].id], [item.object.id for item in empty_relationships.selections])
        self.assertEqual("empty_relationship_allowlist", empty_relationships.truncations[0].reason)

        invalid_requests = (
            {"max_depth": 3},
            {"object_limit": MAX_OBJECTS + 1},
            {"path_limit_per_object": MAX_PATHS_PER_OBJECT + 1},
            {"examined_edge_limit": MAX_EXAMINED_EDGES + 1},
            {"object_limit": 0},
        )
        for overrides in invalid_requests:
            with self.subTest(overrides=overrides), self.assertRaises(GraphTraversalError):
                traverse_memory(
                    memory,
                    GraphTraversalRequest(
                        seed_object_ids=(objects["claim"].id,),
                        access=PROJECT_READER,
                        directions=frozenset({TraversalDirection.OUTBOUND}),
                        relationship_types=frozenset({RelationshipType.DEPENDS_ON}),
                        **overrides,
                    ),
                )
        self.assertIs(project_memory.traverse_memory, traverse_memory)
        self.assertIs(project_memory.TraversalDirection, TraversalDirection)

    def test_inbound_and_outbound_paths_are_distinct(self) -> None:
        memory, objects = _realistic_graph()
        outbound = _traverse(
            memory,
            objects["decision"].id,
            directions={TraversalDirection.OUTBOUND},
            relationships={RelationshipType.DEPENDS_ON},
            include_non_current=True,
        )
        inbound = _traverse(
            memory,
            objects["claim"].id,
            directions={TraversalDirection.INBOUND},
            relationships={RelationshipType.DEPENDS_ON},
            include_non_current=True,
        )

        self.assertIn(objects["claim"].id, _selected_ids(outbound))
        self.assertIn(objects["constraint"].id, _selected_ids(outbound))
        self.assertIn(objects["decision"].id, _selected_ids(inbound))
        self.assertNotIn(objects["constraint"].id, _selected_ids(inbound))
        decision_path = next(item.paths[0] for item in inbound.selections if item.object.id == objects["decision"].id)
        self.assertEqual(TraversalDirection.INBOUND, decision_path.steps[0].direction)
        self.assertEqual(RelationshipType.DEPENDS_ON, decision_path.steps[0].relationship_type)

    def test_visibility_is_enforced_at_every_hop_without_hidden_bridge(self) -> None:
        memory, objects = _realistic_graph()
        result = _traverse(
            memory,
            objects["claim"].id,
            directions={TraversalDirection.INBOUND},
            relationships={RelationshipType.DEPENDS_ON},
            max_depth=2,
            include_non_current=True,
        )

        self.assertNotIn(objects["hidden"].id, _selected_ids(result))
        self.assertNotIn(objects["hidden_downstream"].id, _selected_ids(result))
        hidden_exclusion = next(item for item in result.exclusions if item.target_id == objects["hidden"].id)
        self.assertEqual("inaccessible_target", hidden_exclusion.reason)
        self.assertFalse(hasattr(hidden_exclusion, "title"))
        self.assertFalse(hasattr(hidden_exclusion, "object_type"))

    def test_cycles_terminate_and_results_ignore_insertion_order(self) -> None:
        first_memory, objects = _realistic_graph(reverse=False)
        second_memory, _ = _realistic_graph(reverse=True)
        first = _traverse(
            first_memory,
            objects["decision"].id,
            directions={TraversalDirection.OUTBOUND, TraversalDirection.INBOUND},
            relationships={RelationshipType.DEPENDS_ON, RelationshipType.SUPPORTS},
            max_depth=2,
        )
        second = _traverse(
            second_memory,
            objects["decision"].id,
            directions={TraversalDirection.OUTBOUND, TraversalDirection.INBOUND},
            relationships={RelationshipType.DEPENDS_ON, RelationshipType.SUPPORTS},
            max_depth=2,
        )

        self.assertEqual(len(_selected_ids(first)), len(set(_selected_ids(first))))
        self.assertTrue(any(item.reason == "cycle" for item in first.exclusions))
        self.assertEqual(asdict(first), asdict(second))

    def test_non_current_inclusion_is_explicit_and_current_objects_rank_first(self) -> None:
        memory, objects = _realistic_graph()
        current_only = _traverse(
            memory,
            objects["evidence"].id,
            directions={TraversalDirection.INBOUND},
            relationships={RelationshipType.DERIVED_FROM},
        )
        with_history = _traverse(
            memory,
            objects["claim"].id,
            directions={TraversalDirection.INBOUND},
            relationships={RelationshipType.DEPENDS_ON, RelationshipType.SUPERSEDES},
            include_non_current=True,
        )

        self.assertNotIn(objects["claim"].id, _selected_ids(current_only))
        selected = _selected_ids(with_history)
        self.assertLess(selected.index(objects["decision"].id), selected.index(objects["old_decision"].id))
        self.assertEqual(LifecycleStatus.PROPOSED, objects["claim"].status)
        self.assertEqual("asserted", objects["claim"].metadata["epistemic_status"])

    def test_object_path_and_edge_budgets_are_explicit(self) -> None:
        memory, objects = _realistic_graph()
        object_limited = _traverse(
            memory,
            objects["decision"].id,
            directions={TraversalDirection.OUTBOUND},
            relationships={RelationshipType.DEPENDS_ON},
            object_limit=2,
            include_non_current=True,
        )
        edge_limited = _traverse(
            memory,
            objects["decision"].id,
            directions={TraversalDirection.OUTBOUND, TraversalDirection.INBOUND},
            relationships={
                RelationshipType.DEPENDS_ON,
                RelationshipType.SUPPORTS,
                RelationshipType.SUPERSEDES,
            },
            examined_edge_limit=1,
        )

        self.assertEqual(2, len(object_limited.selections))
        self.assertTrue(any(item.reason == "object_limit" for item in object_limited.truncations))
        self.assertEqual(1, edge_limited.examined_edge_count)
        self.assertEqual([objects["decision"].id], _selected_ids(edge_limited))
        self.assertTrue(any(item.reason == "examined_edge_limit" for item in edge_limited.truncations))

    def test_equal_shortest_paths_are_canonical_and_path_limited(self) -> None:
        root = _object(
            "path_root",
            MemoryObjectType.DECISION,
            "Path root",
            relationships=(
                Relationship(RelationshipType.DEPENDS_ON, "pmem_constraint_graph_path_left"),
                Relationship(RelationshipType.DEPENDS_ON, "pmem_constraint_graph_path_right"),
            ),
        )
        left = _object(
            "path_left",
            MemoryObjectType.CONSTRAINT,
            "Left path",
            relationships=(Relationship(RelationshipType.SUPPORTS, "pmem_evidence_artifact_graph_path_target"),),
        )
        right = _object(
            "path_right",
            MemoryObjectType.CONSTRAINT,
            "Right path",
            relationships=(Relationship(RelationshipType.SUPPORTS, "pmem_evidence_artifact_graph_path_target"),),
        )
        target = _object("path_target", MemoryObjectType.EVIDENCE_ARTIFACT, "Shared target")
        memory = ProjectMemory((root, left, right, target))

        one_path = _traverse(
            memory,
            root.id,
            directions={TraversalDirection.OUTBOUND},
            relationships={RelationshipType.DEPENDS_ON, RelationshipType.SUPPORTS},
            max_depth=2,
            path_limit_per_object=1,
        )
        two_paths = _traverse(
            memory,
            root.id,
            directions={TraversalDirection.OUTBOUND},
            relationships={RelationshipType.DEPENDS_ON, RelationshipType.SUPPORTS},
            max_depth=2,
            path_limit_per_object=2,
        )

        one_target = next(item for item in one_path.selections if item.object.id == target.id)
        two_target = next(item for item in two_paths.selections if item.object.id == target.id)
        self.assertEqual(1, len(one_target.paths))
        self.assertEqual(2, len(two_target.paths))
        self.assertTrue(any(item.reason == "path_limit" for item in one_path.truncations))
        self.assertEqual(left.id, one_target.paths[0].steps[0].target_id)

    def test_external_missing_and_disallowed_edges_have_distinct_reasons(self) -> None:
        memory, objects = _realistic_graph()
        allowed = _traverse(
            memory,
            objects["unrelated"].id,
            directions={TraversalDirection.OUTBOUND},
            relationships={RelationshipType.REFERENCES},
        )
        disallowed = _traverse(
            memory,
            objects["unrelated"].id,
            directions={TraversalDirection.OUTBOUND},
            relationships={RelationshipType.DEPENDS_ON},
        )

        allowed_reasons = {item.reason for item in allowed.exclusions}
        self.assertIn("external_target", allowed_reasons)
        self.assertIn("missing_local_target", allowed_reasons)
        self.assertEqual({"disallowed_relationship"}, {item.reason for item in disallowed.exclusions})

    def test_exclusion_output_is_capped_with_aggregate_omitted_count(self) -> None:
        root = _object(
            "exclusion_root",
            MemoryObjectType.DECISION,
            "Exclusion root",
            relationships=tuple(
                Relationship(RelationshipType.REFERENCES, f"external_ref_{index:03d}")
                for index in range(MAX_EXCLUSIONS + 6)
            ),
        )
        result = _traverse(
            ProjectMemory((root,)),
            root.id,
            directions={TraversalDirection.OUTBOUND},
            relationships={RelationshipType.DEPENDS_ON},
            examined_edge_limit=MAX_EXCLUSIONS + 6,
        )

        self.assertEqual(MAX_EXCLUSIONS, len(result.exclusions))
        omitted = next(item for item in result.truncations if item.reason == "exclusion_limit")
        self.assertEqual(6, omitted.omitted_count)

    def test_every_non_seed_selection_has_a_bounded_typed_path(self) -> None:
        memory, objects = _realistic_graph()
        result = _traverse(
            memory,
            objects["claim"].id,
            directions={TraversalDirection.INBOUND, TraversalDirection.OUTBOUND},
            relationships={
                RelationshipType.DEPENDS_ON,
                RelationshipType.DERIVED_FROM,
                RelationshipType.SUPPORTS,
            },
            max_depth=2,
            path_limit_per_object=2,
            include_non_current=True,
        )

        for selection in result.selections:
            if selection.depth == 0:
                continue
            self.assertGreaterEqual(len(selection.paths), 1)
            self.assertLessEqual(len(selection.paths), 2)
            self.assertEqual(selection.object.id, selection.paths[0].steps[-1].target_id)
            self.assertTrue(all(step.relationship_type in {
                RelationshipType.DEPENDS_ON,
                RelationshipType.DERIVED_FROM,
                RelationshipType.SUPPORTS,
            } for path in selection.paths for step in path.steps))


def _traverse(
    memory: ProjectMemory,
    seed_id: str,
    *,
    directions: set[TraversalDirection],
    relationships: set[RelationshipType],
    max_depth: int = 1,
    object_limit: int = 32,
    path_limit_per_object: int = 2,
    examined_edge_limit: int = 256,
    include_non_current: bool = False,
):
    return traverse_memory(
        memory,
        GraphTraversalRequest(
            seed_object_ids=(seed_id,),
            access=PROJECT_READER,
            directions=frozenset(directions),
            relationship_types=frozenset(relationships),
            max_depth=max_depth,
            object_limit=object_limit,
            path_limit_per_object=path_limit_per_object,
            examined_edge_limit=examined_edge_limit,
            include_non_current=include_non_current,
        ),
    )


def _selected_ids(result) -> list[str]:
    return [item.object.id for item in result.selections]


def _realistic_graph(*, reverse: bool = False) -> tuple[ProjectMemory, dict[str, MemoryObject]]:
    objects: dict[str, MemoryObject] = {}
    objects["claim"] = _claim()
    objects["evidence"] = _object("evidence", MemoryObjectType.EVIDENCE_ARTIFACT, "Canonical source evidence")
    objects["constraint"] = _object(
        "constraint",
        MemoryObjectType.CONSTRAINT,
        "Context must remain bounded",
        relationships=(Relationship(RelationshipType.SUPPORTS, "pmem_decision_graph_decision"),),
    )
    objects["decision"] = _object(
        "decision",
        MemoryObjectType.DECISION,
        "Use graph-aware agent context",
        relationships=(
            Relationship(RelationshipType.DEPENDS_ON, objects["claim"].id),
            Relationship(RelationshipType.DEPENDS_ON, objects["constraint"].id),
            Relationship(RelationshipType.DEPENDS_ON, objects["claim"].id),
        ),
    )
    objects["claim"] = _claim(
        relationships=(Relationship(RelationshipType.DERIVED_FROM, objects["evidence"].id),),
    )
    objects["old_decision"] = _object(
        "old_decision",
        MemoryObjectType.DECISION,
        "Use broad repository context",
        status=LifecycleStatus.SUPERSEDED,
        relationships=(Relationship(RelationshipType.SUPERSEDES, objects["claim"].id),),
    )
    objects["hidden"] = _object(
        "hidden",
        MemoryObjectType.ASSUMPTION,
        "Secret bridge assumption",
        visibility=Visibility.RESTRICTED,
        relationships=(Relationship(RelationshipType.DEPENDS_ON, objects["claim"].id),),
    )
    objects["hidden_downstream"] = _object(
        "hidden_downstream",
        MemoryObjectType.DECISION,
        "Visible object behind hidden bridge",
        relationships=(Relationship(RelationshipType.DEPENDS_ON, objects["hidden"].id),),
    )
    objects["unrelated"] = _object(
        "unrelated",
        MemoryObjectType.MISSION_REFERENCE,
        "Unrelated mission",
        relationships=(
            Relationship(RelationshipType.REFERENCES, "external_portfolio_record"),
            Relationship(RelationshipType.REFERENCES, "pmem_decision_graph_missing"),
        ),
    )

    ordered = list(objects.values())
    if reverse:
        ordered.reverse()
    memory = ProjectMemory()
    for item in ordered:
        memory.add(item)
    return memory, objects


def _claim(*, relationships: tuple[Relationship, ...] = ()) -> MemoryObject:
    proposition = "Project Memory context should use typed graph paths"
    fingerprint = sha256(proposition.encode("utf-8")).hexdigest()
    return MemoryObject(
        id="pmem_claim_graph_claim",
        type=MemoryObjectType.CLAIM,
        title=proposition,
        status=LifecycleStatus.PROPOSED,
        visibility=Visibility.PROJECT,
        provenance=Provenance(
            source_refs=(SOURCE_PATH,),
            created_by="markdown-ingestion-v0",
            created_at=CREATED_AT,
            evidence_level=EvidenceLevel.E1_SOURCE_REFERENCE,
        ),
        relationships=relationships,
        metadata={
            "proposition": proposition,
            "source_path": SOURCE_PATH,
            "heading_path": "Project Memory Architecture > Context Assembly",
            "anchor_key": "context-assembly",
            "occurrence_id": "001",
            "block_fingerprint": fingerprint,
            "document_fingerprint": fingerprint,
            "markdown_role": "canonical",
            "authority_mode": "authored_authority",
            "source_authority": "repo-canonical-docs",
            "knowledge_scope": "project",
            "epistemic_status": "asserted",
            "extraction_method": "canonical_prose_v0",
            "source_snapshot_version": "markdown-source-v0",
            "start_line": 100,
            "end_line": 100,
            "candidate": True,
            "promotion_required": True,
        },
    )


def _object(
    key: str,
    object_type: MemoryObjectType,
    title: str,
    *,
    status: LifecycleStatus = LifecycleStatus.ACTIVE,
    visibility: Visibility = Visibility.PROJECT,
    relationships: tuple[Relationship, ...] = (),
) -> MemoryObject:
    return MemoryObject(
        id=f"pmem_{object_type.value}_graph_{key}",
        type=object_type,
        title=title,
        status=status,
        visibility=visibility,
        provenance=Provenance(
            source_refs=(f"fixture://graph/{key}",),
            created_by="graph-fixture",
            created_at=CREATED_AT,
            evidence_level=EvidenceLevel.E2_REVIEWED_SYNTHESIS,
        ),
        relationships=relationships,
    )


if __name__ == "__main__":
    unittest.main()
