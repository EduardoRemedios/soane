from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from soane.project_memory.agent_context import (
    AgentSelectionState,
    IndexRefreshState,
    MarkdownRole,
    build_agent_context_bundle,
    markdown_role_for_source,
    plan_context_queries,
)
from scripts.factory_context_index import FactoryContextIndexError, build_context_index
from soane.project_memory.fixtures import load_fixtures
from soane.project_memory.semantics import PROJECT_READER, ProjectMemory


FIXTURE_DIR = Path(__file__).parent / "fixtures" / "project_memory" / "golden"
REPO_ROOT = Path(__file__).parents[1]
MEMORY_DIR = REPO_ROOT / "docs" / "project_memory" / "objects"


class ProjectMemoryAgentContextTests(unittest.TestCase):
    def test_natural_task_query_uses_bounded_fallback(self) -> None:
        plan = plan_context_queries(
            "decide the next Project Memory implementation slice after agent context v0",
            (),
        )
        self.assertLessEqual(len(plan), 6)
        self.assertIn("Project Memory", plan)
        self.assertIn("agent context", plan)

        with tempfile.TemporaryDirectory() as tmp:
            bundle = build_agent_context_bundle(
                root=REPO_ROOT,
                task="decide the next Project Memory implementation slice after agent context v0",
                memory=ProjectMemory(),
                access=PROJECT_READER,
                limit=3,
                db_path=Path(tmp) / "context.sqlite3",
            )

        self.assertTrue(bundle.documents)
        self.assertLessEqual(len(bundle.documents), 3)
        self.assertTrue(any(document.source_path == "docs/ROADMAP.md" for document in bundle.documents))
        self.assertEqual(AgentSelectionState.READY, bundle.selection_state)
        self.assertEqual(IndexRefreshState.REFRESHED, bundle.index_refresh_state)

    def test_zero_match_fails_closed_without_all_memory(self) -> None:
        memory = ProjectMemory.from_fixtures(load_fixtures(FIXTURE_DIR))
        with tempfile.TemporaryDirectory() as tmp:
            bundle = build_agent_context_bundle(
                root=REPO_ROOT,
                task="xyzzynotfoundtoken",
                memory=memory,
                access=PROJECT_READER,
                scope="docs/ROADMAP.md",
                limit=2,
                memory_limit=3,
                db_path=Path(tmp) / "context.sqlite3",
            )

        self.assertFalse(bundle.documents)
        self.assertFalse(bundle.memory.current)
        self.assertFalse(bundle.memory.surfaced)
        self.assertEqual(AgentSelectionState.DEGRADED, bundle.selection_state)
        self.assertEqual("no_relevant_context", bundle.selection_reason)

    def test_explicit_seed_expands_one_hop_with_reason_and_budget(self) -> None:
        fixture = next(item for item in load_fixtures(FIXTURE_DIR) if item.fixture_id == "GF-001")
        memory = ProjectMemory(fixture.objects.values())
        decision = fixture.objects["decision"]
        evidence = fixture.objects["evidence"]
        with tempfile.TemporaryDirectory() as tmp:
            bundle = build_agent_context_bundle(
                root=REPO_ROOT,
                task="xyzzynotfoundtoken",
                memory=memory,
                access=PROJECT_READER,
                seed_object_ids=(decision.id,),
                limit=1,
                memory_limit=2,
                db_path=Path(tmp) / "context.sqlite3",
            )

        reasons = {item.object.id: item.reason for item in bundle.memory.current}
        self.assertEqual("explicit_seed", reasons[decision.id])
        self.assertEqual(f"relationship:evidences:{decision.id}", reasons[evidence.id])
        self.assertLessEqual(len(bundle.memory.current) + len(bundle.memory.surfaced), 2)
        self.assertEqual(2, bundle.memory_budget)

    def test_memory_budget_records_relationship_truncation(self) -> None:
        fixture = next(item for item in load_fixtures(FIXTURE_DIR) if item.fixture_id == "GF-001")
        decision = fixture.objects["decision"]
        with tempfile.TemporaryDirectory() as tmp:
            bundle = build_agent_context_bundle(
                root=REPO_ROOT,
                task="xyzzynotfoundtoken",
                memory=ProjectMemory(fixture.objects.values()),
                access=PROJECT_READER,
                seed_object_ids=(decision.id,),
                memory_limit=1,
                db_path=Path(tmp) / "context.sqlite3",
            )

        self.assertEqual(1, len(bundle.memory.current))
        self.assertTrue(any(item.startswith("memory_budget_reached:") for item in bundle.memory_truncations))

    def test_relationship_visibility_exclusion_remains_explained(self) -> None:
        fixture = next(item for item in load_fixtures(FIXTURE_DIR) if item.fixture_id == "GF-012")
        question = fixture.objects["allowed_question"]
        restricted = fixture.objects["restricted_evidence"]
        with tempfile.TemporaryDirectory() as tmp:
            bundle = build_agent_context_bundle(
                root=REPO_ROOT,
                task="xyzzynotfoundtoken",
                memory=ProjectMemory(fixture.objects.values()),
                access=PROJECT_READER,
                seed_object_ids=(question.id,),
                db_path=Path(tmp) / "context.sqlite3",
            )

        self.assertNotIn(restricted.id, {item.object.id for item in bundle.memory.current})
        self.assertIn(
            (restricted.id, "not_visible_to_access_context"),
            {(item.object_id, item.reason) for item in bundle.memory.exclusions},
        )

    def test_failed_refresh_reuses_previous_valid_index_truthfully(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            db_path = Path(tmp) / "context.sqlite3"
            build_context_index(REPO_ROOT, db_path=db_path)
            with patch(
                "soane.project_memory.agent_context.build_context_index",
                side_effect=FactoryContextIndexError("forced refresh failure"),
            ):
                bundle = build_agent_context_bundle(
                    root=REPO_ROOT,
                    task="agent context",
                    memory=ProjectMemory(),
                    access=PROJECT_READER,
                    limit=1,
                    db_path=db_path,
                )

        self.assertEqual(IndexRefreshState.FAILED, bundle.index_refresh_state)
        self.assertIn("forced refresh failure", bundle.index_refresh_error or "")
        self.assertTrue(bundle.documents)
        self.assertFalse(bundle.index_refreshed)

    def test_failed_refresh_without_valid_index_blocks_context(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            db_path = Path(tmp) / "context.sqlite3"
            with patch(
                "soane.project_memory.agent_context.build_context_index",
                side_effect=FactoryContextIndexError("forced initial failure"),
            ):
                bundle = build_agent_context_bundle(
                    root=REPO_ROOT,
                    task="agent context",
                    memory=ProjectMemory(),
                    access=PROJECT_READER,
                    db_path=db_path,
                )

        self.assertEqual(AgentSelectionState.BLOCKED, bundle.selection_state)
        self.assertEqual("context_index_unavailable", bundle.selection_reason)
        self.assertFalse(bundle.documents)
        self.assertFalse(bundle.memory.current)

    def test_no_refresh_reports_reused_and_observes_changed_source(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            docs = root / "docs"
            docs.mkdir()
            roadmap = docs / "ROADMAP.md"
            roadmap.write_text("# Roadmap\n\nAgent context relevance.\n", encoding="utf-8")
            db_path = root / "context.sqlite3"
            build_context_index(root, db_path=db_path)
            roadmap.write_text("# Roadmap\n\nAgent context relevance changed.\n", encoding="utf-8")
            bundle = build_agent_context_bundle(
                root=root,
                task="agent context",
                memory=ProjectMemory(),
                access=PROJECT_READER,
                limit=1,
                db_path=db_path,
                refresh_index=False,
            )

        self.assertEqual(IndexRefreshState.REUSED, bundle.index_refresh_state)
        self.assertEqual("changed", bundle.documents[0].source_freshness)

    def test_markdown_role_mapping_formalizes_repo_document_roles(self) -> None:
        self.assertEqual(MarkdownRole.CONSTITUTIONAL, markdown_role_for_source("docs/VISION.md", "canonical_doc"))
        self.assertEqual(MarkdownRole.CANONICAL, markdown_role_for_source("docs/ROADMAP.md", "canonical_doc"))
        self.assertEqual(
            MarkdownRole.GENERATED,
            markdown_role_for_source(
                "docs/Factory/runs/RUN_20260701_0848_project_memory_v0_plan/VALIDATION_CLOSEOUT_REPORT.md",
                "factory_run_root_artifact",
            ),
        )
        self.assertEqual(
            MarkdownRole.EVIDENCE,
            markdown_role_for_source(
                "docs/Factory/runs/RUN_20260701_0848_project_memory_v0_plan/pack/verification_plan.md",
                "factory_run_pack_artifact",
            ),
        )
        self.assertEqual(MarkdownRole.DEPRECATED, markdown_role_for_source("docs/archive/old.md", "canonical_doc"))

    def test_agent_context_bridges_recalled_docs_to_project_memory_refs(self) -> None:
        fixtures = load_fixtures(FIXTURE_DIR)
        memory = ProjectMemory.from_fixtures(fixtures)
        with tempfile.TemporaryDirectory() as tmp:
            bundle = build_agent_context_bundle(
                root=REPO_ROOT,
                task="Project Memory v0 context assembly",
                memory=memory,
                access=PROJECT_READER,
                scope="docs/ROADMAP.md",
                queries=("Project Memory v0",),
                limit=2,
                db_path=Path(tmp) / "context.sqlite3",
            )

        self.assertTrue(bundle.documents)
        self.assertTrue(any(document.source_path == "docs/ROADMAP.md" for document in bundle.documents))
        self.assertTrue(any(document.related_memory_object_ids for document in bundle.documents))
        self.assertTrue(bundle.memory.current or bundle.memory.surfaced)
        self.assertTrue(any("Factory context index" in line for line in bundle.explanation))

    def test_agent_context_cli_outputs_bundle_json(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "soane.project_memory.cli",
                    "agent-context",
                    "--fixture-dir",
                    str(FIXTURE_DIR),
                    "--task",
                    "Project Memory v0 context assembly",
                    "--query",
                    "Project Memory v0",
                    "--context-scope",
                    "docs/ROADMAP.md",
                    "--limit",
                    "2",
                    "--db-path",
                    str(Path(tmp) / "context.sqlite3"),
                ],
                check=False,
                cwd=REPO_ROOT,
                text=True,
                capture_output=True,
            )

        if result.returncode != 0:
            self.fail(f"CLI failed with {result.returncode}\nstdout={result.stdout}\nstderr={result.stderr}")
        payload = json.loads(result.stdout)
        self.assertTrue(payload["ok"])
        self.assertEqual("agent-context", payload["command"])
        self.assertTrue(payload["documents"])
        self.assertTrue(payload["memory"]["current"] or payload["memory"]["surfaced"])
        self.assertEqual("canonical", payload["documents"][0]["markdown_role"])
        self.assertEqual("ready", payload["selection_state"])
        self.assertEqual("refreshed", payload["refresh_state"])
        self.assertEqual(2, payload["budgets"]["documents"])
        self.assertIn("memory", payload["budgets"])

    def test_agent_context_cli_uses_repo_memory_by_default(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "soane.project_memory.cli",
                    "agent-context",
                    "--task",
                    "Markdown role vocabulary for agent context",
                    "--query",
                    "Markdown Role Vocabulary",
                    "--context-scope",
                    "docs/GOVERNANCE_MODEL.md",
                    "--limit",
                    "2",
                    "--db-path",
                    str(Path(tmp) / "context.sqlite3"),
                ],
                check=False,
                cwd=REPO_ROOT,
                text=True,
                capture_output=True,
            )

        if result.returncode != 0:
            self.fail(f"CLI failed with {result.returncode}\nstdout={result.stdout}\nstderr={result.stderr}")
        payload = json.loads(result.stdout)
        titles = {item["title"] for item in payload["memory"]["current"]}
        self.assertIn("Classify Markdown by role before agent context use", titles)
        self.assertTrue(any(document["source_path"] == "docs/GOVERNANCE_MODEL.md" for document in payload["documents"]))

    def test_repo_context_prioritizes_current_memory_before_superseded_history(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "soane.project_memory.cli",
                    "agent-context",
                    "--task",
                    "next Project Memory implementation",
                    "--query",
                    "Immediate Next Move",
                    "--context-scope",
                    "docs/ROADMAP.md",
                    "--limit",
                    "1",
                    "--memory-limit",
                    "4",
                    "--db-path",
                    str(Path(tmp) / "context.sqlite3"),
                ],
                check=False,
                cwd=REPO_ROOT,
                text=True,
                capture_output=True,
            )

        if result.returncode != 0:
            self.fail(f"CLI failed with {result.returncode}\nstdout={result.stdout}\nstderr={result.stderr}")
        payload = json.loads(result.stdout)
        current_ids = {item["id"] for item in payload["memory"]["current"]}
        surfaced_ids = {item["id"] for item in payload["memory"]["surfaced"]}
        self.assertIn("pmem_decision_soane_agent_context_correctness_gate", current_ids)
        self.assertNotIn("pmem_decision_soane_lcae_next_gate", surfaced_ids)

    def test_agent_trace_cli_shows_relationships(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "soane.project_memory.cli",
                "agent-trace",
                "--fixture-dir",
                str(FIXTURE_DIR),
                "--fixture-key",
                "GF-001",
                "decision",
            ],
            check=False,
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
        )

        if result.returncode != 0:
            self.fail(f"CLI failed with {result.returncode}\nstdout={result.stdout}\nstderr={result.stderr}")
        payload = json.loads(result.stdout)
        self.assertEqual("agent-trace", payload["command"])
        self.assertEqual("decision", payload["object"]["type"])
        self.assertTrue(any(item["type"] == "evidences" for item in payload["outgoing"]))

    def test_agent_trace_cli_reads_repo_memory_by_default(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "soane.project_memory.cli",
                "agent-trace",
                "--id",
                "pmem_decision_soane_agent_context_before_persistence",
            ],
            check=False,
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
        )

        if result.returncode != 0:
            self.fail(f"CLI failed with {result.returncode}\nstdout={result.stdout}\nstderr={result.stderr}")
        payload = json.loads(result.stdout)
        self.assertEqual("agent-trace", payload["command"])
        self.assertEqual("Build agent-facing context slices before persistence hardening", payload["object"]["title"])
        self.assertTrue(any(item["type"] == "depends_on" for item in payload["outgoing"]))

    def test_agent_affected_cli_lists_memory_refs_for_path(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "soane.project_memory.cli",
                "agent-affected",
                "--fixture-dir",
                str(FIXTURE_DIR),
                "--path",
                "docs/ROADMAP.md",
            ],
            check=False,
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
        )

        if result.returncode != 0:
            self.fail(f"CLI failed with {result.returncode}\nstdout={result.stdout}\nstderr={result.stderr}")
        payload = json.loads(result.stdout)
        self.assertEqual("agent-affected", payload["command"])
        self.assertEqual("canonical", payload["markdown_role"])
        self.assertGreater(payload["affected_count"], 0)
        self.assertTrue(any(item["type"] == "decision" for item in payload["objects"]))

    def test_agent_affected_cli_reads_repo_memory_by_default(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "soane.project_memory.cli",
                "agent-affected",
                "--path",
                "docs/GOVERNANCE_MODEL.md",
            ],
            check=False,
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
        )

        if result.returncode != 0:
            self.fail(f"CLI failed with {result.returncode}\nstdout={result.stdout}\nstderr={result.stderr}")
        payload = json.loads(result.stdout)
        titles = {item["title"] for item in payload["objects"]}
        self.assertEqual("constitutional", payload["markdown_role"])
        self.assertIn("Classify Markdown by role before agent context use", titles)

    def test_cli_validate_accepts_real_memory_dir_without_fixtures(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "soane.project_memory.cli",
                "validate",
                "--no-fixtures",
                "--memory-dir",
                str(MEMORY_DIR),
            ],
            check=False,
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
        )

        if result.returncode != 0:
            self.fail(f"CLI failed with {result.returncode}\nstdout={result.stdout}\nstderr={result.stderr}")
        payload = json.loads(result.stdout)
        self.assertEqual(0, payload["fixture_count"])
        self.assertGreaterEqual(payload["object_count"], 8)


if __name__ == "__main__":
    unittest.main()
