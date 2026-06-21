#!/usr/bin/env python3
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_news  # noqa: E402


def write(path, body):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(body)


class BuildNewsTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.content = os.path.join(self.tmp, "content")

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def test_groups_multiple_authors_by_date_and_orders_timeline(self):
        write(
            os.path.join(self.content, "news", "twitter", "fxtrader", "2026-06-20-2.md"),
            """---
title: "Late market note"
author:
  - "[[@fxtrader]]"
source: "https://x.com/fxtrader/status/2"
tweet_id: "2"
published: 2026-06-20
published_at: "2026-06-20T12:30:00.000Z"
tags:
  - "news"
  - "twitter"
---
late body
""",
        )
        write(
            os.path.join(self.content, "news", "twitter", "livermoerR", "2026-06-20-1.md"),
            """---
title: "Early macro note"
author:
  - "[[@livermoerR]]"
source: "https://x.com/livermoerR/status/1"
tweet_id: "1"
published: 2026-06-20
published_at: "2026-06-20T08:10:00.000Z"
tags:
  - "news"
  - "twitter"
---
early body
""",
        )
        write(
            os.path.join(self.content, "news", "twitter", "fxtrader", "2026-06-19-0.md"),
            """---
title: "Yesterday"
published: 2026-06-19
published_at: "2026-06-19T08:10:00.000Z"
---
yesterday
""",
        )

        pages = build_news.build_news(self.content)
        self.assertIn(os.path.join(self.content, "news", "2026-06-20.md"), pages)

        with open(os.path.join(self.content, "news", "2026-06-20.md"), encoding="utf-8") as f:
            text = f.read()

        self.assertIn("新闻时间线", text)
        self.assertIn("@fxtrader", text)
        self.assertIn("@livermoerR", text)
        self.assertLess(text.index("08:10"), text.index("12:30"))
        self.assertNotIn("Yesterday", text)

        with open(os.path.join(self.content, "news", "index.md"), encoding="utf-8") as f:
            index = f.read()
        self.assertIn("[2026-06-20](./2026-06-20.md)", index)


if __name__ == "__main__":
    unittest.main()
