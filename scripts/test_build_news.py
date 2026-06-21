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
        self.assertNotIn("@fxtrader", text)
        self.assertNotIn("@livermoerR", text)
        self.assertLess(text.index("12:30"), text.index("08:10"))
        self.assertIn('href="https://x.com/fxtrader/status/2"', text)
        self.assertNotIn("Yesterday", text)

        with open(os.path.join(self.content, "news", "index.md"), encoding="utf-8") as f:
            index = f.read()
        self.assertIn("[2026-06-20](./2026-06-20.md)", index)

    def test_renders_full_body_and_clickable_media(self):
        long_body = "这是完整正文。" + "继续显示。" * 80
        image = "https://pbs.twimg.com/media/example.jpg"
        video = "https://video.twimg.com/ext_tw_video/example.mp4"
        write(
            os.path.join(self.content, "news", "twitter", "fxtrader", "2026-06-20-3.md"),
            f"""---
title: "Full media note"
source: "https://x.com/fxtrader/status/3"
published: 2026-06-20
published_at: "2026-06-20T09:00:00.000Z"
---
{long_body}

![]({image})

视频：
- <{video}>
""",
        )

        build_news.build_news(self.content)

        with open(os.path.join(self.content, "news", "2026-06-20.md"), encoding="utf-8") as f:
            text = f.read()

        self.assertIn(long_body, text)
        self.assertNotIn(long_body[:220] + "…", text)
        self.assertIn(f'<a class="news-media news-image" href="{image}"', text)
        self.assertIn(f'<img src="{image}"', text)
        self.assertIn(f'<a href="{video}" target="_blank" rel="noopener">查看视频</a>', text)
        self.assertIn('href="https://x.com/fxtrader/status/3"', text)

    def test_quote_source_link_does_not_include_closing_marker(self):
        source = "https://x.com/fxtrader/status/12345"
        write(
            os.path.join(self.content, "news", "twitter", "fxtrader", "2026-06-20-4.md"),
            f"""---
title: "Quote note"
published: 2026-06-20
published_at: "2026-06-20T10:00:00.000Z"
---
> 原帖：<{source}>
>
> quoted body
""",
        )

        build_news.build_news(self.content)

        with open(os.path.join(self.content, "news", "2026-06-20.md"), encoding="utf-8") as f:
            text = f.read()

        self.assertNotIn("原帖：", text)
        self.assertIn(f'<blockquote>引用原文：<a href="{source}" target="_blank" rel="noopener">打开链接</a></blockquote>', text)
        self.assertNotIn("<p>&gt;</p>", text)


if __name__ == "__main__":
    unittest.main()
