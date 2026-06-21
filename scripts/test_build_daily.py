#!/usr/bin/env python3
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_daily  # noqa: E402


def write(path, body):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(body)


class BuildDailyTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.content = os.path.join(self.tmp, "content")

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def test_daily_report_summarizes_today_concepts_and_news(self):
        write(
            os.path.join(self.content, "concepts", "tool-alpha.md"),
            """---
type: "Tool"
title: "Alpha"
description: "A useful tool"
timestamp: "2026-06-21T08:00:00Z"
tags: [ai, tool]
---
正文
""",
        )
        write(
            os.path.join(self.content, "concepts", "term-old.md"),
            """---
type: "Term"
title: "Old"
timestamp: "2026-06-20T08:00:00Z"
---
正文
""",
        )
        write(
            os.path.join(self.content, "news", "twitter", "fxtrader", "2026-06-21-1.md"),
            """---
title: "Market note"
author:
  - "[[@fxtrader]]"
tweet_id: "1"
published: 2026-06-21
tags:
  - "news"
  - "twitter"
---
news body
""",
        )

        report_path = build_daily.build_daily(self.content, "2026-06-21")
        with open(report_path, encoding="utf-8") as f:
            text = f.read()

        self.assertIn("今天发现了 1 个概念", text)
        self.assertIn("[Alpha](../concepts/tool-alpha.md)", text)
        self.assertNotIn("Old", text)
        self.assertIn("新闻 1 条", text)
        self.assertIn("[Market note](../news/twitter/fxtrader/2026-06-21-1.md)", text)
        self.assertIn('<div class="daily-bars"', text)

        with open(os.path.join(self.content, "daily", "index.md"), encoding="utf-8") as f:
            index = f.read()
        self.assertIn("[2026-06-21](./2026-06-21.md)", index)


if __name__ == "__main__":
    unittest.main()
