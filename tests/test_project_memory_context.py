from __future__ import annotations

import unittest
from pathlib import Path

from soane.project_memory.context import ContextRequest, build_context_package, render_markdown_view
from soane.project_memory.fixtures import load_fixtures
from soane.project_memory.semantics import PROJECT_READER, PROJECT_REVIEWER, ProjectMemory


FIXTURE_DIR = Path(__file__).parent / "fixtures" / "project_memory" / "golden"


class ProjectMemoryContextTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixtures = load_fixtures(FIXTURE_DIR)
        cls.memory = ProjectMemory.from_fixtures(cls.fixtures)
        cls.by_fixture = {fixture.fixture_id: fixture for fixture in cls.fixtures}

    def test_context_package_separates_current_from_stale_and_superseded(self) -> None:
        package = build_context_package(
            self.memory,
            ContextRequest(purpose="MS-03 current truth proof", access=PROJECT_READER),
        )
        current_ids = {item.object.id for item in package.current}
        surfaced_ids = {item.object.id for item in package.surfaced}
        stale = self.by_fixture["GF-004"].objects["evidence"]
        superseded = self.by_fixture["GF-010"].objects["old_decision"]
        self.assertNotIn(stale.id, current_ids)
        self.assertNotIn(superseded.id, current_ids)
        self.assertIn(stale.id, surfaced_ids)
        self.assertIn(superseded.id, surfaced_ids)

    def test_context_package_surfaces_contradictions(self) -> None:
        package = build_context_package(
            self.memory,
            ContextRequest(purpose="MS-03 contradiction proof", access=PROJECT_READER),
        )
        titles = {tuple(sorted((left.title, right.title))) for left, right in package.contradictions}
        self.assertIn(
            tuple(
                sorted(
                    (
                        "Source A says live adapters should be used first",
                        "Source B says mock-first adapters should be used first",
                    )
                )
            ),
            titles,
        )

    def test_context_package_records_visibility_exclusions(self) -> None:
        fixture = self.by_fixture["GF-012"]
        memory = ProjectMemory(fixture.objects.values())
        allowed_question = fixture.objects["allowed_question"]
        restricted = fixture.objects["restricted_evidence"]
        package = build_context_package(
            memory,
            ContextRequest(
                purpose="MS-03 visibility proof",
                access=PROJECT_READER,
                seed_object_ids=(allowed_question.id,),
            ),
        )
        self.assertIn(
            (restricted.id, "not_visible_to_access_context"),
            {(item.object_id, item.reason) for item in package.exclusions},
        )

    def test_context_package_records_propagation_exclusions(self) -> None:
        fixture = self.by_fixture["GF-012"]
        memory = ProjectMemory(fixture.objects.values())
        restricted = fixture.objects["restricted_evidence"]
        package = build_context_package(
            memory,
            ContextRequest(
                purpose="MS-03 propagation proof",
                access=PROJECT_REVIEWER,
                boundary="external_adapter_context",
                seed_object_ids=(restricted.id,),
            ),
        )
        self.assertFalse(package.current)
        self.assertIn(
            (restricted.id, "blocked_by_propagation_rule"),
            {(item.object_id, item.reason) for item in package.exclusions},
        )

    def test_context_package_records_seed_visibility_exclusions(self) -> None:
        restricted = self.by_fixture["GF-009"].objects["restricted_decision"]
        package = build_context_package(
            self.memory,
            ContextRequest(
                purpose="MS-03 seed visibility proof",
                access=PROJECT_READER,
                seed_object_ids=(restricted.id,),
            ),
        )
        self.assertFalse(package.current)
        self.assertIn(
            (restricted.id, "not_visible_to_access_context"),
            {(item.object_id, item.reason) for item in package.exclusions},
        )

    def test_markdown_view_maps_rendered_items_to_sources(self) -> None:
        fixture = self.by_fixture["GF-005"]
        markdown_object = fixture.objects["markdown"]
        memory = ProjectMemory(fixture.objects.values())
        package = build_context_package(
            memory,
            ContextRequest(
                purpose="MS-03 markdown source mapping proof",
                access=PROJECT_READER,
                seed_object_ids=(markdown_object.id,),
            ),
        )
        view = render_markdown_view(package)
        self.assertIn("# Context Package: MS-03 markdown source mapping proof", view.body)
        self.assertIn("current-001", view.source_map)
        self.assertEqual(markdown_object.id, view.source_map["current-001"].object_id)
        self.assertIn("docs/ROADMAP.md", view.source_map["current-001"].source_refs)
        self.assertIn(fixture.objects["decision"].id, view.source_map["current-001"].related_object_ids)


if __name__ == "__main__":
    unittest.main()
