from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from soane.project_memory.agent_context import (
    MarkdownRole,
    build_agent_context_bundle,
    markdown_role_for_source,
)
from soane.project_memory.fixtures import load_fixtures
from soane.project_memory.semantics import PROJECT_READER, ProjectMemory


FIXTURE_DIR = Path(__file__).parent / "fixtures" / "project_memory" / "golden"
REPO_ROOT = Path(__file__).parents[1]
MEMORY_DIR = REPO_ROOT / "docs" / "project_memory" / "objects"


class ProjectMemoryAgentContextTests(unittest.TestCase):
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
