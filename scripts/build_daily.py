#!/usr/bin/env python3
"""Generate a daily public report from concepts and news."""
import glob
import os
import re
import sys
from collections import Counter
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import okf_lib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_ROOT = os.path.join(ROOT, "content")


def local_today():
    return datetime.now(timezone(timedelta(hours=8))).date().isoformat()


def strip_quotes(value):
    return (value or "").strip().strip('"').strip("'")


def esc(text):
    return (text or "").replace("|", "\\|").replace("\n", " ")


def md_link(base_dir, target):
    rel = os.path.relpath(target, base_dir).replace(os.sep, "/")
    if not rel.startswith("."):
        rel = "./" + rel
    return rel


def doc_title(path, fallback):
    fm = okf_lib.read_frontmatter(path) or {}
    return strip_quotes(fm.get("title")) or fallback


def frontmatter_date(fm, *keys):
    for key in keys:
        value = strip_quotes(fm.get(key))
        if re.match(r"^\d{4}-\d{2}-\d{2}", value):
            return value[:10]
    return ""


def collect_concepts(content_root, report_date):
    concepts_dir = os.path.join(content_root, "concepts")
    items = []
    for path in sorted(glob.glob(os.path.join(concepts_dir, "**", "*.md"), recursive=True)):
        if os.path.basename(path) == "index.md":
            continue
        fm = okf_lib.read_frontmatter(path) or {}
        if frontmatter_date(fm, "timestamp", "created", "published") != report_date:
            continue
        items.append(
            {
                "path": path,
                "title": strip_quotes(fm.get("title")) or os.path.basename(path)[:-3],
                "type": strip_quotes(fm.get("type")) or "未分类",
                "description": strip_quotes(fm.get("description")),
            }
        )
    return items


def collect_news(content_root, report_date):
    news_dir = os.path.join(content_root, "news")
    items = []
    for path in sorted(glob.glob(os.path.join(news_dir, "**", "*.md"), recursive=True)):
        if os.path.basename(path) == "index.md":
            continue
        fm = okf_lib.read_frontmatter(path) or {}
        published = frontmatter_date(fm, "published", "created", "timestamp")
        if not published and os.path.basename(path).startswith(report_date):
            published = report_date
        if published != report_date:
            continue
        rel_parts = os.path.relpath(path, news_dir).split(os.sep)
        source = rel_parts[1] if len(rel_parts) >= 3 and rel_parts[0] == "twitter" else rel_parts[0]
        items.append(
            {
                "path": path,
                "title": strip_quotes(fm.get("title")) or os.path.basename(path)[:-3],
                "source": source,
            }
        )
    return items


def bar_row(label, value, total):
    width = 0 if total == 0 else max(8, round(value / total * 100))
    return (
        '<div class="daily-bar-row">'
        f'<span>{esc(label)}</span>'
        '<div class="daily-track">'
        f'<div class="daily-fill" style="width:{width}%"></div>'
        "</div>"
        f'<strong>{value}</strong>'
        "</div>"
    )


def render_report(content_root, report_date, concepts, news):
    daily_dir = os.path.join(content_root, "daily")
    base_dir = daily_dir
    type_counts = Counter(item["type"] for item in concepts)
    source_counts = Counter(item["source"] for item in news)
    total = len(concepts) + len(news)

    out = [
        "---",
        'type: "Index"',
        f'title: "{report_date} 日报"',
        f'description: "{report_date} 的概念发现、新闻来源和当天知识库增量。"',
        "tags: [daily, okf, news]",
        f'timestamp: "{datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}"',
        "---",
        "",
        f"# {report_date} 日报",
        "",
        '<div class="daily-hero">',
        f"<p>今天发现了 {len(concepts)} 个概念，新闻 {len(news)} 条。</p>",
        '<div class="daily-score">',
        f"<span>总输入</span><strong>{total}</strong>",
        "</div>",
        "</div>",
        "",
        "<style>",
        ".daily-hero{border:1px solid var(--lightgray);border-radius:8px;padding:1rem 1.1rem;margin:1rem 0 1.25rem;background:linear-gradient(135deg,rgba(40,75,99,.10),rgba(132,165,157,.16));display:flex;justify-content:space-between;gap:1rem;align-items:center}",
        ".daily-hero p{margin:0;font-size:1.05rem}",
        ".daily-score{min-width:7rem;text-align:right}",
        ".daily-score span{display:block;color:var(--gray);font-size:.8rem}",
        ".daily-score strong{font-size:2rem;line-height:1;color:var(--secondary)}",
        ".daily-bars{display:grid;gap:.55rem;margin:1rem 0 1.25rem}",
        ".daily-bar-row{display:grid;grid-template-columns:minmax(5rem,10rem) 1fr 2.5rem;gap:.75rem;align-items:center}",
        ".daily-track{height:.65rem;border-radius:999px;background:var(--lightgray);overflow:hidden}",
        ".daily-fill{height:100%;border-radius:999px;background:linear-gradient(90deg,var(--secondary),var(--tertiary))}",
        "@media(max-width:700px){.daily-hero{display:block}.daily-score{text-align:left;margin-top:1rem}.daily-bar-row{grid-template-columns:1fr 2.5rem}.daily-track{grid-column:1 / -1;grid-row:2}}",
        "</style>",
        "",
        "## 今日概览",
        "",
        "| 指标 | 数量 |",
        "|---|---:|",
        f"| 新概念 | {len(concepts)} |",
        f"| 新闻 | {len(news)} |",
        f"| 来源账号 | {len(source_counts)} |",
        "",
    ]

    out.append("## 概念分布")
    out.append("")
    out.append('<div class="daily-bars">')
    if type_counts:
        for label, value in sorted(type_counts.items(), key=lambda item: (-item[1], item[0])):
            out.append(bar_row(label, value, len(concepts)))
    else:
        out.append(bar_row("无新增概念", 0, 0))
    out.append("</div>")
    out.append("")

    out.append("## 今天发现的概念")
    out.append("")
    if concepts:
        out.append("| 概念 | 类型 | 摘要 |")
        out.append("|---|---|---|")
        for item in concepts:
            link = md_link(base_dir, item["path"])
            out.append(f'| [{esc(item["title"])}]({link}) | {esc(item["type"])} | {esc(item["description"])} |')
    else:
        out.append("今天没有新的概念文件。")
    out.append("")

    out.append("## 新闻")
    out.append("")
    if source_counts:
        out.append('<div class="daily-bars">')
        for label, value in sorted(source_counts.items(), key=lambda item: (-item[1], item[0])):
            out.append(bar_row("@" + label, value, len(news)))
        out.append("</div>")
        out.append("")
        out.append("| 新闻 | 来源 |")
        out.append("|---|---|")
        for item in news:
            link = md_link(base_dir, item["path"])
            out.append(f'| [{esc(item["title"])}]({link}) | @{esc(item["source"])} |')
    else:
        out.append("今天没有新的新闻条目。")
    out.append("")
    out.append("---")
    out.append("*本页由 `scripts/build_daily.py` 自动生成。*")
    out.append("")
    return "\n".join(out)


def write_index(content_root):
    daily_dir = os.path.join(content_root, "daily")
    reports = sorted(
        path for path in glob.glob(os.path.join(daily_dir, "*.md")) if os.path.basename(path) != "index.md"
    )
    out = [
        "---",
        'type: "Index"',
        'title: "日报"',
        'description: "每日概念发现和新闻摘要。"',
        "tags: [daily, okf]",
        "---",
        "",
        "# 日报",
        "",
    ]
    if reports:
        for path in reversed(reports):
            name = os.path.basename(path)[:-3]
            out.append(f"- [{name}](./{name}.md)")
    else:
        out.append("暂无日报。")
    out.append("")
    with open(os.path.join(daily_dir, "index.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(out))


def build_daily(content_root=CONTENT_ROOT, report_date=None):
    report_date = report_date or local_today()
    daily_dir = os.path.join(content_root, "daily")
    os.makedirs(daily_dir, exist_ok=True)
    concepts = collect_concepts(content_root, report_date)
    news = collect_news(content_root, report_date)
    report = render_report(content_root, report_date, concepts, news)
    output = os.path.join(daily_dir, f"{report_date}.md")
    with open(output, "w", encoding="utf-8") as f:
        f.write(report)
    write_index(content_root)
    return output


def main():
    report_date = sys.argv[1] if len(sys.argv) > 1 else None
    output = build_daily(CONTENT_ROOT, report_date)
    print(f"[daily] 已生成 {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
