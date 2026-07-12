from __future__ import annotations

import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from threading import Event
from unittest.mock import patch

from scripts.factory_context_index import (
    FactoryContextIndexError,
    build_context_index,
    describe_context,
    recall_context,
)


class FactoryContextIndexAtomicTests(unittest.TestCase):
    def test_failed_rebuild_preserves_previous_valid_index(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = self._repo(Path(tmp)).resolve()
            db_path = root / "context.sqlite3"
            build_context_index(root, db_path=db_path)

            def broken_discovery(*_args: object, **_kwargs: object):
                yield root / "docs" / "ROADMAP.md"
                raise OSError("forced source discovery failure")

            with patch("scripts.factory_context_index._discover_source_paths", broken_discovery):
                with self.assertRaises(FactoryContextIndexError):
                    build_context_index(root, db_path=db_path)

            payload = recall_context(root=root, query="agent context", db_path=db_path)
            self.assertGreater(payload["match_count"], 0)

    def test_concurrent_rebuilds_publish_complete_index(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = self._repo(Path(tmp)).resolve()
            db_path = root / "context.sqlite3"

            with ThreadPoolExecutor(max_workers=4) as executor:
                results = list(executor.map(lambda _: build_context_index(root, db_path=db_path), range(4)))

            self.assertTrue(all(result["refresh_state"] == "refreshed" for result in results))
            described = describe_context(root=root, db_path=db_path)
            self.assertEqual(3, described["source_count"])
            self.assertGreater(recall_context(root=root, query="agent context", db_path=db_path)["match_count"], 0)

    def test_reader_sees_previous_snapshot_during_rebuild(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = self._repo(Path(tmp)).resolve()
            db_path = root / "context.sqlite3"
            build_context_index(root, db_path=db_path)
            (root / "docs" / "ROADMAP.md").write_text(
                "# Roadmap\n\nReplacement context wording.\n",
                encoding="utf-8",
            )
            discovery_started = Event()
            allow_rebuild = Event()

            from scripts import factory_context_index as context_index

            original_discovery = context_index._discover_source_paths

            def paused_discovery(*args: object, **kwargs: object):
                discovery_started.set()
                self.assertTrue(allow_rebuild.wait(timeout=5))
                yield from original_discovery(*args, **kwargs)

            with patch("scripts.factory_context_index._discover_source_paths", paused_discovery):
                with ThreadPoolExecutor(max_workers=1) as executor:
                    future = executor.submit(build_context_index, root, db_path)
                    self.assertTrue(discovery_started.wait(timeout=5))
                    previous = recall_context(root=root, query="agent context relevance", db_path=db_path)
                    allow_rebuild.set()
                    future.result(timeout=5)

            self.assertGreater(previous["match_count"], 0)
            self.assertGreater(recall_context(root=root, query="replacement context", db_path=db_path)["match_count"], 0)

    def _repo(self, root: Path) -> Path:
        docs = root / "docs"
        docs.mkdir(parents=True)
        (root / "AGENTS.md").write_text("# Agents\n\nAgent context commands.\n", encoding="utf-8")
        (docs / "PROJECT_STATE.md").write_text("# Project State\n\nAgent context exists.\n", encoding="utf-8")
        (docs / "ROADMAP.md").write_text("# Roadmap\n\nAgent context relevance next.\n", encoding="utf-8")
        return root


if __name__ == "__main__":
    unittest.main()
