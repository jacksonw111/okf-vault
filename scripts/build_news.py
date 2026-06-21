#!/usr/bin/env python3
"""Generate public news timeline pages grouped by date."""
import glob
import html
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


def html_text(text):
    return html.escape(text or "", quote=False)


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


def read_body(path):
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except OSError:
        return ""
    text = okf_lib.FM_RE.sub("", text).strip()
    text = re.sub(r"## 来源[\s\S]*$", "", text).strip()
    text = re.sub(r"(?m)^>\s*原帖：<https://x\.com/[^/]+/status/\d+>\s*$", "", text)
    return text


def public_status_url(tweet_id, fallback):
    if tweet_id:
        return f"https://x.com/i/web/status/{tweet_id}"
    match = re.search(r"/status/(\d+)", fallback or "")
    if match:
        return f"https://x.com/i/web/status/{match.group(1)}"
    return fallback


def render_inline_links(text):
    escaped = html_text(text)
    return re.sub(
        r"https?://[^\s<>()]+?(?=&gt;|\s|$)",
        lambda m: f'<a href="{public_status_url("", m.group(0))}" target="_blank" rel="noopener">{public_status_url("", m.group(0))}</a>',
        escaped,
    )


def render_body_html(body):
    out = ['<div class="news-body">']
    in_list = False
    for raw_line in body.splitlines():
        line = raw_line.strip()
        if not line:
            if in_list:
                out.append("</ul>")
                in_list = False
            continue
        if line == ">":
            continue

        image = re.match(r"^!\[[^\]]*\]\((https?://[^)]+)\)$", line)
        if image:
            if in_list:
                out.append("</ul>")
                in_list = False
            url = html.escape(image.group(1), quote=True)
            out.append(
                f'<a class="news-media news-image" href="{url}" target="_blank" rel="noopener"><img src="{url}" alt="新闻图片" loading="lazy"></a>'
            )
            continue

        video = re.match(r"^-?\s*<((?:https?://)[^>]+)>$", line)
        if video:
            if not in_list:
                out.append('<ul class="news-media-list">')
                in_list = True
            url = html.escape(video.group(1), quote=True)
            out.append(f'<li><a href="{url}" target="_blank" rel="noopener">查看视频</a></li>')
            continue

        if line.startswith("> "):
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append(f"<blockquote>{render_inline_links(line[2:])}</blockquote>")
            continue

        if in_list:
            out.append("</ul>")
            in_list = False
        out.append(f"<p>{render_inline_links(line)}</p>")

    if in_list:
        out.append("</ul>")
    out.append("</div>")
    return "\n".join(out)


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
        source = public_status_url(strip_quotes(fm.get("tweet_id")), strip_quotes(fm.get("source")))
        items.append(
            {
                "path": path,
                "date": day,
                "published_at": published_at,
                "time": published_at[11:16] if len(published_at) >= 16 else "--:--",
                "title": strip_quotes(fm.get("title")) or os.path.basename(path)[:-3],
                "source": source,
                "body_html": render_body_html(read_body(path)),
            }
        )
    return items


def render_date_page(content_root, day, items):
    out = [
        "---",
        'type: "Index"',
        f'title: "{day} 新闻"',
        f'description: "{day} 的新闻时间线，按发布时间从新到旧排列。"',
        "tags: [news, twitter]",
        f'timestamp: "{datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}"',
        "---",
        "",
        f"# {day} 新闻",
        "",
        f'<div class="news-hero"><strong>{len(items)}</strong><span>条新闻</span><em>最新在前</em></div>',
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
        ".news-body{display:grid;gap:.55rem}",
        ".news-body p{margin:0;line-height:1.65}",
        ".news-body blockquote{margin:.15rem 0;padding:.1rem 0 .1rem .8rem;border-left:3px solid var(--lightgray);color:var(--darkgray)}",
        ".news-media{display:block;margin:.35rem 0}",
        ".news-image img{max-width:min(100%,42rem);border:1px solid var(--lightgray);border-radius:8px}",
        ".news-media-list{margin:.25rem 0 .1rem;padding-left:1.2rem}",
        "@media(max-width:700px){.news-item{grid-template-columns:1fr;gap:.25rem}.news-hero{display:block}.news-hero em{display:block;margin-top:.25rem}}",
        "</style>",
        "",
        "## 新闻时间线",
        "",
        '<div class="news-timeline">',
    ]
    for item in sorted(items, key=lambda item: (item["published_at"], item["path"]), reverse=True):
        source_link = f'<a href="{item["source"]}" target="_blank" rel="noopener">原文</a>' if item["source"] else ""
        out.extend(
            [
                '<div class="news-item">',
                f'<div class="news-time">{esc(item["time"])}</div>',
                '<div class="news-card">',
                f"<h3>{esc(item['title'])}</h3>",
                f'<div class="news-meta">{source_link}</div>' if source_link else '<div class="news-meta"></div>',
                item["body_html"],
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
        'description: "按日期聚合的公开新闻时间线；不进入 inbox 的 AI 整理流程。"',
        "tags: [news, twitter]",
        "---",
        "",
        "# 新闻",
        "",
        "公开新闻流按日期分页。同一天的内容会合并到同一个日期页面，并按发布时间从新到旧排列。",
        "",
        "## 日期",
        "",
    ]
    if dates:
        for day in sorted(dates, reverse=True):
            out.append(f"- [{day}](./{day}.md)")
    else:
        out.append("暂无新闻。")
    out.append("")
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
