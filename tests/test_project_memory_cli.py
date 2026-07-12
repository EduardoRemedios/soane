from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from soane.project_memory.contract import MemoryObjectType, deterministic_fixture_id


FIXTURE_DIR = Path(__file__).parent / "fixtures" / "project_memory" / "golden"


class ProjectMemoryCliTests(unittest.TestCase):
    def test_validate_command_uses_fixture_contract(self) -> None:
        result = self._run_cli("validate")
        payload = json.loads(result.stdout)

        self.assertTrue(payload["ok"])
        self.assertEqual("validate", payload["command"])
        self.assertEqual(12, payload["fixture_count"])
        self.assertGreater(payload["object_count"], 12)

    def test_fixture_test_command_loads_project_memory(self) -> None:
        result = self._run_cli("fixture-test")
        payload = json.loads(result.stdout)

        self.assertTrue(payload["ok"])
        self.assertEqual("fixture-test", payload["command"])
        self.assertEqual(12, payload["fixture_count"])
        self.assertGreater(payload["visible_object_count"], 12)
        self.assertGreater(payload["expectation_count"], 0)

    def test_context_build_command_calls_context_assembly(self) -> None:
        result = self._run_cli(
            "context-build",
            "--purpose",
            "MS-05 CLI context proof",
            "--fixture-key",
            "GF-005",
            "markdown",
        )
        payload = json.loads(result.stdout)

        self.assertTrue(payload["ok"])
        self.assertEqual("context-build", payload["command"])
        self.assertEqual("MS-05 CLI context proof", payload["purpose"])
        self.assertEqual("explicit_seed", payload["selection_mode"])
        self.assertEqual("Roadmap Markdown view", payload["current"][0]["title"])

    def test_export_markdown_command_renders_markdown_and_source_map(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "context.md"
            source_map = Path(tmp) / "source-map.json"
            result = self._run_cli(
                "export-markdown",
                "--purpose",
                "MS-05 CLI markdown proof",
                "--fixture-key",
                "GF-005",
                "markdown",
                "--output",
                str(output),
                "--source-map-json",
                str(source_map),
                "--json",
            )
            payload = json.loads(result.stdout)

            self.assertTrue(payload["ok"])
            self.assertEqual("export-markdown", payload["command"])
            self.assertTrue(output.exists())
            self.assertTrue(source_map.exists())
            self.assertIn("# Context Package: MS-05 CLI markdown proof", output.read_text(encoding="utf-8"))
            self.assertIn("current-001", json.loads(source_map.read_text(encoding="utf-8")))

    def test_export_markdown_command_prints_markdown_by_default(self) -> None:
        result = self._run_cli(
            "export-markdown",
            "--purpose",
            "MS-05 CLI stdout proof",
            "--fixture-key",
            "GF-005",
            "markdown",
        )

        self.assertIn("# Context Package: MS-05 CLI stdout proof", result.stdout)
        self.assertIn("## Current Memory", result.stdout)

    def test_inspect_command_reads_by_fixture_key(self) -> None:
        result = self._run_cli("inspect", "--fixture-key", "GF-006", "invocation")
        payload = json.loads(result.stdout)

        self.assertTrue(payload["ok"])
        self.assertEqual("inspect", payload["command"])
        self.assertEqual("provider_invocation", payload["object"]["type"])
        self.assertEqual("codex_cli", payload["object"]["metadata"]["provider"])

    def test_inspect_command_respects_visibility_without_audit(self) -> None:
        denied = self._run_cli(
            "inspect",
            "--fixture-key",
            "GF-008",
            "suppressed_note",
            expect_success=False,
        )
        allowed = self._run_cli(
            "inspect",
            "--fixture-key",
            "GF-008",
            "suppressed_note",
            "--audit",
        )

        self.assertNotEqual(0, denied.returncode)
        self.assertIn("not visible", denied.stderr)
        self.assertEqual("suppressed", json.loads(allowed.stdout)["object"]["visibility"])

    def test_review_candidate_command_wraps_review_service(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            candidate_path = Path(tmp) / "candidate.json"
            candidate_path.write_text(
                json.dumps(_candidate_payload("CRP-CLI-001", "CLI accepted candidate")),
                encoding="utf-8",
            )

            result = self._run_cli(
                "review-candidate",
                "--candidate-json",
                str(candidate_path),
                "--outcome",
                "accept",
                "--reviewer",
                "cli-reviewer",
                "--rationale",
                "CLI wrapper delegates to review service.",
            )
            payload = json.loads(result.stdout)

        self.assertTrue(payload["ok"])
        self.assertEqual("review-candidate", payload["command"])
        self.assertEqual("accepted", payload["reviewed_object"]["status"])
        self.assertEqual("accept", payload["reviewed_object"]["metadata"]["review_outcome"])
        self.assertEqual("cli-reviewer", payload["reviewed_object"]["created_by"])
        self.assertIn(payload["candidate"]["id"], payload["reviewed_object"]["derivation_refs"])

    def test_review_candidate_command_surfaces_service_errors(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            candidate_path = Path(tmp) / "candidate.json"
            payload = _candidate_payload("CRP-CLI-002", "Authority-gated CLI candidate")
            payload["metadata"]["requires_authority"] = True
            candidate_path.write_text(json.dumps(payload), encoding="utf-8")

            result = self._run_cli(
                "review-candidate",
                "--candidate-json",
                str(candidate_path),
                "--outcome",
                "accept",
                "--reviewer",
                "cli-reviewer",
                "--rationale",
                "Authority is missing.",
                expect_success=False,
            )

        self.assertNotEqual(0, result.returncode)
        self.assertIn("authority_ref is required", result.stderr)

    def _run_cli(self, command: str, *args: str, expect_success: bool = True) -> subprocess.CompletedProcess[str]:
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "soane.project_memory.cli",
                command,
                "--fixture-dir",
                str(FIXTURE_DIR),
                *args,
            ],
            check=False,
            cwd=Path(__file__).parents[1],
            text=True,
            capture_output=True,
        )
        if expect_success and result.returncode != 0:
            self.fail(f"CLI failed with {result.returncode}\nstdout={result.stdout}\nstderr={result.stderr}")
        return result


def _candidate_payload(fixture_id: str, title: str) -> dict[str, object]:
    return {
        "id": deterministic_fixture_id(fixture_id, MemoryObjectType.ASSUMPTION, title),
        "type": "assumption",
        "title": title,
        "status": "proposed",
        "visibility": "project",
        "provenance": {
            "source_refs": [f"source://{fixture_id}"],
            "created_by": "thinking-engine-intake",
            "created_at": "2026-07-01T15:00:00+00:00",
            "evidence_level": "E2",
            "derivation_refs": [],
        },
        "relationships": [],
        "authority_ref": None,
        "confidence": None,
        "metadata": {"candidate": True, "promotion_required": True},
    }


if __name__ == "__main__":
    unittest.main()
