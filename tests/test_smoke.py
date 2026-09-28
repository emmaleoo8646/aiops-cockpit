import io
import contextlib
import unittest

from aiops_cockpit import __version__
from aiops_cockpit.cli import build_parser, main


class TestSmoke(unittest.TestCase):
    def test_version_is_nonempty_string(self):
        self.assertIsInstance(__version__, str)
        self.assertGreater(len(__version__), 0)

    def test_version_matches_semver_shape(self):
        parts = __version__.split(".")
        self.assertGreaterEqual(len(parts), 2)
        for part in parts:
            self.assertTrue(part.isdigit(), f"version part not numeric: {part}")

    def test_cli_parser_builds(self):
        parser = build_parser()
        self.assertIsNotNone(parser)

    def test_cli_no_command_exits_zero(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            result = main([])
        self.assertEqual(result, 0)
        self.assertIn("usage", buf.getvalue().lower())

    def test_cli_serve_command(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            result = main(["serve"])
        self.assertEqual(result, 0)
        self.assertIn("serve", buf.getvalue().lower())

    def test_cli_collect_command(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            result = main(["collect"])
        self.assertEqual(result, 0)
        self.assertIn("collect", buf.getvalue().lower())

    def test_cli_version_flag_exits_zero(self):
        buf = io.StringIO()
        with self.assertRaises(SystemExit) as cm:
            with contextlib.redirect_stdout(buf):
                main(["--version"])
        self.assertEqual(cm.exception.code, 0)
        self.assertIn(__version__, buf.getvalue())


if __name__ == "__main__":
    unittest.main()
