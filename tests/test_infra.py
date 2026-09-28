import os
import unittest

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CI_PATH = os.path.join(PROJECT_ROOT, ".github", "workflows", "test.yml")
SPEC_PATH = os.path.join(PROJECT_ROOT, "packaging", "m3t.spec")


class TestCIWorkflow(unittest.TestCase):
    def setUp(self):
        with open(CI_PATH, encoding="utf-8") as f:
            self.content = f.read()

    def test_ci_file_exists(self):
        self.assertTrue(
            os.path.exists(CI_PATH),
            f"CI workflow not found at {CI_PATH}",
        )

    def test_ci_triggers_on_push_to_main(self):
        self.assertIn("push:", self.content)
        self.assertIn("main", self.content)

    def test_ci_triggers_on_pull_request(self):
        self.assertIn("pull_request:", self.content)

    def test_ci_uses_github_actions_checkout(self):
        self.assertIn("actions/checkout@v4", self.content)

    def test_ci_runs_against_multiple_python_versions(self):
        self.assertIn("3.10", self.content)
        self.assertIn("3.11", self.content)
        self.assertIn("3.12", self.content)

    def test_ci_invokes_pytest(self):
        self.assertIn("pytest", self.content)


class TestPyInstallerSpec(unittest.TestCase):
    def setUp(self):
        with open(SPEC_PATH, encoding="utf-8") as f:
            self.content = f.read()

    def test_spec_file_exists(self):
        self.assertTrue(
            os.path.exists(SPEC_PATH),
            f"PyInstaller spec not found at {SPEC_PATH}",
        )

    def test_spec_is_valid_python_module(self):
        compile(self.content, SPEC_PATH, "exec")

    def test_spec_has_analysis_block(self):
        self.assertIn("a = Analysis(", self.content)

    def test_spec_has_exe_block(self):
        self.assertIn("exe = EXE(", self.content)

    def test_spec_points_at_main_module(self):
        self.assertIn("aiops_cockpit/__main__.py", self.content)

    def test_spec_names_executable(self):
        self.assertIn("name='aiops-cockpit'", self.content)


if __name__ == "__main__":
    unittest.main()
