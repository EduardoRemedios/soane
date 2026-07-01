from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

from soane.project_memory.fixtures import load_fixtures
from soane.project_memory.semantics import PROJECT_READER
from soane.project_memory.tui import TuiScreen, build_tui_model, render_tui_model


FIXTURE_DIR = Path(__file__).parent / "fixtures" / "project_memory" / "golden"


class ProjectMemoryTuiTests(unittest.TestCase):
    def test_overview_model_uses_shared_memory_and_context_counts(self) -> None:
        fixtures = load_fixtures(FIXTURE_DIR)
        model = build_tui_model(fixtures, TuiScreen.OVERVIEW, PROJECT_READER)
        rendered = render_tui_model(model, width=100)

        self.assertEqual(TuiScreen.OVERVIEW, model.screen)
        self.assertIn("Screen: Project Navigation", rendered)
        self.assertIn("Validation", rendered)
        self.assertIn("Current Memory", rendered)
        self.assertIn("Contradictions", rendered)
        self.assertIn("Actions: q quit", rendered)

    def test_memory_screen_lists_current_visible_records(self) -> None:
        rendered = self._run_tui("--screen", "memory").stdout

        self.assertIn("Screen: Memory Browser", rendered)
        self.assertIn("decision/accepted", rendered)
        self.assertIn("Use CLI before TUI", rendered)
        self.assertNotIn("Suppressed implementation note", rendered)

    def test_adapter_screen_lists_provider_invocations_and_capabilities(self) -> None:
        rendered = self._run_tui("--screen", "adapters", "--width", "140").stdout

        self.assertIn("Screen: Adapter Invocations And Capabilities", rendered)
        self.assertIn("provider_invocation/accepted", rendered)
        self.assertIn("Mock Codex CLI fixture test invocation", rendered)
        self.assertIn("capability_reference/accepted", rendered)

    def test_questions_screen_lists_unresolved_questions(self) -> None:
        rendered = self._run_tui("--screen", "questions").stdout

        self.assertIn("Screen: Unresolved Questions", rendered)
        self.assertIn("question/open", rendered)
        self.assertIn("What does MS-02 need to know?", rendered)

    def test_list_screens_exposes_navigation_surface(self) -> None:
        result = self._run_tui("--list-screens")
        screens = set(result.stdout.splitlines())

        self.assertEqual({screen.value for screen in TuiScreen}, screens)

    def test_unknown_fixture_dir_fails_cleanly(self) -> None:
        result = self._run_tui("--fixture-dir", "missing-fixtures", expect_success=False)

        self.assertNotEqual(0, result.returncode)
        self.assertIn("error:", result.stderr)

    def _run_tui(self, *args: str, expect_success: bool = True) -> subprocess.CompletedProcess[str]:
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "soane.project_memory.tui",
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
            self.fail(f"TUI failed with {result.returncode}\nstdout={result.stdout}\nstderr={result.stderr}")
        return result


if __name__ == "__main__":
    unittest.main()
