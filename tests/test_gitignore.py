import os
import subprocess
import unittest

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GITIGNORE_PATH = os.path.join(PROJECT_ROOT, ".gitignore")


class TestGitignore(unittest.TestCase):
    def setUp(self):
        with open(GITIGNORE_PATH, encoding="utf-8") as f:
            self.content = f.read()
        self.preview_html = os.path.join(PROJECT_ROOT, "preview", "design.html")

    def test_gitignore_exists(self):
        self.assertTrue(
            os.path.exists(GITIGNORE_PATH),
            f".gitignore not found at {GITIGNORE_PATH}",
        )

    def test_preview_dir_is_ignored(self):
        self.assertIn(
            "preview/",
            self.content,
            ".gitignore must ignore preview/ (build artifacts)",
        )

    def test_preview_design_html_is_actually_ignored(self):
        if not os.path.exists(self.preview_html):
            self.skipTest(f"{self.preview_html} not present yet")
        result = subprocess.run(
            ["git", "check-ignore", "-q", "preview/design.html"],
            cwd=PROJECT_ROOT,
            capture_output=True,
        )
        self.assertEqual(
            result.returncode,
            0,
            "git check-ignore preview/design.html should exit 0 (file is ignored)",
        )

    def test_python_bytecode_is_ignored(self):
        has_explicit = "*.pyc" in self.content
        has_compound = "*.py[cod]" in self.content
        self.assertTrue(
            has_explicit or has_compound,
            ".gitignore must ignore compiled Python files (either *.pyc or *.py[cod])",
        )


if __name__ == "__main__":
    unittest.main()
