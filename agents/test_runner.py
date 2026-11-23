import unittest
from unittest.mock import patch
import tempfile
from pathlib import Path
import run

class RunnerTests(unittest.TestCase):
    def test_all_nine_agents(self):
        folders = [p for p in run.ROOT.iterdir() if (p / "instructions.md").is_file()]
        self.assertGreaterEqual(len(folders), 9)
        for p in folders:
            system, data = run.build_messages(p.name, run.read_text(p / "example.md"))
            self.assertIn("Never invent", system)
            self.assertTrue(data.strip())
    def test_dry_run_no_api(self):
        with patch.object(run, "generate") as generate:
            self.assertEqual(run.main(["ai-launch-reviewer", "--dry-run"]), 0)
            generate.assert_not_called()
    def test_size_limit(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "large.txt"
            p.write_text("x" * (run.LIMIT + 1))
            with self.assertRaises(ValueError):
                run.read_text(p)

if __name__ == "__main__":
    unittest.main()
