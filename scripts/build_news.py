#!/usr/bin/env python3
"""Generate public news timeline pages grouped by date."""
import glob
import os
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import okf_lib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_ROOT = os.path.join(ROOT, "content")


def strip_quotes(value):
    return (value or "").strip().strip('"').strip("'")


def esc(text):
    return (text or "").replace("|", "\\|").replace("\n", " ")


def md_link(base_dir, target):
    rel = os.path.relpath(target, base_dir).replace(os.sep, "/")
    if not rel.startswith("."):
        rel = "./" + rel
    return rel


def frontmatter_date(fm, *keys):
    for key in keys:
        value = strip_quotes(fm.get(key))
        if re.match(r"^\d{4}-\d{2}-\d{2}", value):
            return value[:10]
    return ""


def read_body_excerpt(path):
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except OSError:
        return ""
    text = okf_lib.FM_RE.sub("", text).strip()
    text = re.sub(r"## 来源[\s\S]*$", "", text).strip()
    text = re.sub(r"\s+", " ", text)
    return text[:220] + ("…" if len(text) > 220 else "")


def author_from_path(news_dir, path):
    rel_parts = os.path.relpath(path, news_dir).split(os.sep)
    if len(rel_parts) >= 3 and rel_parts[0] == "twitter":
        return rel_parts[1]
    return rel_parts[0]


def collect_news(content_root):
    news_dir = os.path.join(content_root, "news")
    items = []
    for path in sorted(glob.glob(os.path.join(news_dir, "twitter", "*", "*.md"))):
        fm = okf_lib.read_frontmatter(path) or {}
        day = frontmatter_date(fm, "published", "published_at", "created", "timestamp")
        if not day and re.match(r"^\d{4}-\d{2}-\d{2}", os.path.basename(path)):
            day = os.path.basename(path)[:10]
        if not day:
            continue
        published_at = strip_quotes(fm.get("published_at")) or day + "T00:00:00.000Z"
        source = strip_quotes(fm.get("source"))
        items.append(
            {
                "path": path,
                "date": day,
                "published_at": published_at,
                "time": published_at[11:16] if len(published_at) >= 16 else "--:--",
                "author": author_from_path(news_dir, path),
                "title": strip_quotes(fm.get("title")) or os.path.basename(path)[:-3],
                "source": source,
                "excerpt": read_body_excerpt(path),
            }
        )
    return items


def render_date_page(content_root, day, items):
    news_dir = os.path.join(content_root, "news")
    source_counts = defaultdict(int)
    for item in items:
        source_counts[item["author"]] += 1

    out = [
        "---",
        'type: "Index"',
        f'title: "{day} 新闻"',
        f'description: "{day} 的新闻时间线，按发布时间从早到晚排列。"',
        "tags: [news, twitter]",
        f'timestamp: "{datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}"',
        "---",
        "",
        f"# {day} 新闻",
        "",
        f'<div class="news-hero"><strong>{len(items)}</strong><span>条新闻</span><em>{len(source_counts)} 个来源</em></div>',
        "",
        "<style>",
        ".news-hero{display:flex;align-items:baseline;gap:.6rem;border:1px solid var(--lightgray);border-radius:8px;padding:1rem;margin:1rem 0 1.25rem;background:rgba(132,165,157,.14)}",
        ".news-hero strong{font-size:2rem;color:var(--secondary);line-height:1}",
        ".news-hero span{font-weight:700}",
        ".news-hero em{margin-left:auto;color:var(--gray);font-style:normal}",
        ".news-timeline{display:grid;gap:.9rem;margin:1rem 0}",
        ".news-item{display:grid;grid-template-columns:4.5rem 1fr;gap:1rem;border-top:1px solid var(--lightgray);padding-top:.9rem}",
        ".news-time{font-family:var(--codeFont);color:var(--secondary);font-weight:700}",
        ".news-card h3{margin:.05rem 0 .25rem;font-size:1.05rem}",
        ".news-meta{color:var(--gray);font-size:.9rem;margin-bottom:.45rem}",
        ".news-card p{margin:.35rem 0}",
        "@media(max-width:700px){.news-item{grid-template-columns:1fr;gap:.25rem}.news-hero{display:block}.news-hero em{display:block;margin-top:.25rem}}",
        "</style>",
        "",
        "## 来源分布",
        "",
        "| 来源 | 数量 |",
        "|---|---:|",
    ]
    for author, count in sorted(source_counts.items()):
        out.append(f"| @{esc(author)} | {count} |")

    out.extend(["", "## 新闻时间线", "", '<div class="news-timeline">'])
    for item in sorted(items, key=lambda item: (item["published_at"], item["path"])):
        source_link = f'<a href="{item["source"]}">原文</a>' if item["source"] else ""
        out.extend(
            [
                '<div class="news-item">',
                f'<div class="news-time">{esc(item["time"])}</div>',
                '<div class="news-card">',
                f"<h3>{esc(item['title'])}</h3>",
                f'<div class="news-meta">@{esc(item["author"])}' + (f" · {source_link}" if source_link else "") + "</div>",
                f'<p>{esc(item["excerpt"])}</p>',
                "</div>",
                "</div>",
            ]
        )
    out.extend(["</div>", "", "---", "*本页由 `scripts/build_news.py` 自动生成。*", ""])
    return "\n".join(out)


def write_index(content_root, dates):
    news_dir = os.path.join(content_root, "news")
    out = [
        "---",
        'type: "Index"',
        'title: "新闻"',
        'description: "按日期聚合的公开新闻时间线；来自单独配置的 X/Twitter 新闻源，不进入 inbox 的 AI 整理流程。"',
        "tags: [news, twitter]",
        "---",
        "",
        "# 新闻",
        "",
        "公开新闻流按日期分页。同一天不同来源的内容会合并到同一个日期页面，并按发布时间从早到晚排列。",
        "",
        "## 日期",
        "",
    ]
    if dates:
        for day in sorted(dates, reverse=True):
            out.append(f"- [{day}](./{day}.md)")
    else:
        out.append("暂无新闻。")
    out.extend(["", "## 来源", "", "- @fxtrader", "- @livermoerR", ""])
    with open(os.path.join(news_dir, "index.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(out))


def build_news(content_root=CONTENT_ROOT):
    news_dir = os.path.join(content_root, "news")
    os.makedirs(news_dir, exist_ok=True)
    by_date = defaultdict(list)
    for item in collect_news(content_root):
        by_date[item["date"]].append(item)

    outputs = []
    for day, items in sorted(by_date.items()):
        output = os.path.join(news_dir, f"{day}.md")
        with open(output, "w", encoding="utf-8") as f:
            f.write(render_date_page(content_root, day, items))
        outputs.append(output)

    write_index(content_root, by_date.keys())
    return outputs


def main():
    outputs = build_news(CONTENT_ROOT)
    print(f"[news] 已生成 {len(outputs)} 个日期页")
    return 0


if __name__ == "__main__":
    sys.exit(main())
