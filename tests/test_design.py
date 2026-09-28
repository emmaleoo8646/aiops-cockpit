import os
import unittest

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DESIGN_PATH = os.path.join(PROJECT_ROOT, "design.md")

REQUIRED_SECTIONS = [
    "# AIOps Cockpit 设计稿",
    "## 1. 概述",
    "## 2. 设计目标与边界",
    "## 3. 整体架构",
    "## 4. 三大监控域",
    "### 4.1 网络安全",
    "### 4.2 系统本身",
    "### 4.3 业务问题",
    "## 5. AI 分析引擎",
    "## 6. 驾驶舱（Cockpit）",
    "## 7. Windows",
    "## 8. 关键决策",
    "## 9. 分阶段实施计划",
    "## 10. 风险与缓解",
]

REQUIRED_DECISION_KEYWORDS = [
    "≤ 200",
    "云端",
    "只读",
    "应用错误日志",
    "Windows + Linux",
    "单租户",
    "人确认",
]

CLOUD_AI_HINTS = [
    "云端",
    "OpenAI",
    "脱敏",
]


class TestDesignDocument(unittest.TestCase):
    def setUp(self):
        with open(DESIGN_PATH, encoding="utf-8") as f:
            self.content = f.read()

    def test_design_file_exists(self):
        self.assertTrue(
            os.path.exists(DESIGN_PATH),
            f"design.md not found at {DESIGN_PATH}",
        )

    def test_design_file_is_non_trivial(self):
        self.assertGreater(
            len(self.content),
            1000,
            "design.md content too short, expected a real design document",
        )

    def test_required_sections_present(self):
        for section in REQUIRED_SECTIONS:
            with self.subTest(section=section):
                self.assertIn(section, self.content, f"missing section: {section}")

    def test_key_decisions_reflected(self):
        for kw in REQUIRED_DECISION_KEYWORDS:
            with self.subTest(keyword=kw):
                self.assertIn(kw, self.content, f"missing decision keyword: {kw}")

    def test_cloud_ai_decision_present(self):
        for hint in CLOUD_AI_HINTS:
            with self.subTest(hint=hint):
                self.assertIn(hint, self.content, f"cloud-AI hint missing: {hint}")


if __name__ == "__main__":
    unittest.main()
