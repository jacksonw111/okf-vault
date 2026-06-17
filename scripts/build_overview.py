#!/usr/bin/env python3
"""
build_overview.py — 构建前生成 overview.md 仪表盘。

扫描 content/concepts/ 下所有 .md 的 frontmatter（type / tags / title / timestamp），
生成一个带真实统计的仪表盘页面（统计卡片 + 按类型分组表 + 最近更新表），
交给 Quartz 当普通 markdown 渲染。

设计：
  - 只用标准库；best-effort（解析失败的概念跳过）。
  - tags 兼容两种写法：数组 [a,b] 或字符串 "[a,b]"（历史加引号导致）。
  - 输出固定写到 content/overview.md。
"""
import os
import re
import sys
import glob
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONCEPTS_DIR = os.path.join(ROOT, "content", "concepts")
OUTPUT = os.path.join(ROOT, "content", "overview.md")

FM_RE = re.compile(r'^---\n(.*?)\n---\n', re.DOTALL)


def parse_frontmatter(fm_text):
    """极简 YAML 解析，只取我们关心的标量/列表字段。"""
    data = {}
    for line in fm_text.split('\n'):
        m = re.match(r'^(\w+):\s*(.*)$', line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val.startswith('"') and val.endswith('"'):
            val = val[1:-1]
        data[key] = val
    return data


def parse_tags(val):
    """兼容 [a, b] 数组 与 "[a, b]" 字符串 两种写法。"""
    if not val:
        return []
    val = val.strip()
    if val.startswith('[') and val.endswith(']'):
        val = val[1:-1]
    val = val.strip('"').strip("'")
    if not val:
        return []
    return [t.strip().strip('"').strip("'").lower() for t in val.split(',') if t.strip()]


def collect():
    concepts = []
    for path in sorted(glob.glob(os.path.join(CONCEPTS_DIR, '*.md'))):
        name = os.path.basename(path)
        if name == 'index.md':
            continue
        try:
            text = open(path, encoding='utf-8').read()
            m = FM_RE.match(text)
            if not m:
                continue
            fm = parse_frontmatter(m.group(1))
            tags = parse_tags(fm.get('tags', ''))
            concepts.append({
                'slug': name[:-3],  # 去 .md
                'filename': name,
                'type': fm.get('type', '未分类').strip('"'),
                'title': fm.get('title', name[:-3]).strip('"'),
                'description': fm.get('description', '').strip('"'),
                'tags': tags,
                'timestamp': fm.get('timestamp', '').strip('"'),
            })
        except Exception as e:
            print(f"[skip] {name}: {e}", file=sys.stderr)
    return concepts


def esc(s):
    return (s or '').replace('|', '\\|').replace('\n', ' ')


def render(concepts):
    total = len(concepts)
    type_counter = Counter(c['type'] for c in concepts)
    tag_counter = Counter(t for c in concepts for t in c['tags'])

    # 最近更新：按 timestamp 倒序取前 10
    def ts_key(c):
        return c.get('timestamp') or ''
    recent = sorted(concepts, key=ts_key, reverse=True)[:10]

    out = []
    out.append('---')
    out.append('type: "Index"')
    out.append('title: "知识库仪表盘"')
    out.append('description: "知识库总览：实时统计概念数、类型分布、标签云、最近更新。构建前自动生成。"')
    out.append('tags: [okf, dashboard]')
    out.append(f'timestamp: "{__import__("time").strftime("%Y-%m-%dT%H:%M:%SZ", __import__("time").gmtime())}"')
    out.append('---')
    out.append('')
    out.append('# 📊 知识库仪表盘')
    out.append('')
    out.append('> 本页由 `scripts/build_overview.py` 在每次 Quartz 构建前**自动生成**，数据来自 `concepts/` 下所有概念文件的 frontmatter，永远最新。')
    out.append('')

    # 统计卡片（用表格模拟卡片布局）
    out.append('## 📈 概览')
    out.append('')
    out.append(f'| 概念总数 | 类型数 | 标签数 |')
    out.append(f'|:---:|:---:|:---:|')
    out.append(f'| **{total}** | **{len(type_counter)}** | **{len(tag_counter)}** |')
    out.append('')

    # 类型分布表
    out.append('## 🗂 按类型分布')
    out.append('')
    out.append('| 类型 | 数量 |')
    out.append('|---|:---:|')
    for t, n in sorted(type_counter.items(), key=lambda x: -x[1]):
        out.append(f'| {esc(t)} | {n} |')
    out.append('')

    # 标签云（按热度：≥2 的显示，长尾收起）
    out.append('## 🏷️ 标签（按热度，点击进标签聚合页）')
    out.append('')
    top_tags = [(t, n) for t, n in sorted(tag_counter.items(), key=lambda x: (-x[1], x[0])) if n >= 2]
    if top_tags:
        tags_line = ' · '.join(
            f'**[{t}](./tags/{t})** ({n})'
            for t, n in top_tags
        )
        out.append(tags_line)
        out.append('')
    out.append(f'<details><summary>查看全部 {len(tag_counter)} 个标签（含长尾）</summary>')
    out.append('')
    out.append(' '.join(f'[{t}](./tags/{t})' for t, _ in sorted(tag_counter.items())))
    out.append('')
    out.append('</details>')
    out.append('')

    # 最近更新
    out.append('## 🕒 最近更新')
    out.append('')
    out.append('| 概念 | 类型 | 更新时间 |')
    out.append('|---|---|---|')
    for c in recent:
        date = (c['timestamp'] or '—')[:10]
        out.append(f'| [{esc(c["title"])}](./concepts/{c["slug"]}) | {esc(c["type"])} | {date} |')
    out.append('')

    # 全部概念（分类型）
    out.append('## 📚 全部概念（按类型）')
    out.append('')
    for t in sorted(type_counter.keys()):
        items = [c for c in concepts if c['type'] == t]
        out.append(f'### {t}（{len(items)}）')
        out.append('')
        for c in sorted(items, key=lambda x: x['title']):
            desc = c['description'][:60] + ('…' if len(c['description']) > 60 else '')
            out.append(f'- [{esc(c["title"])}](./concepts/{c["slug"]}) — {esc(desc)}')
        out.append('')

    out.append('---')
    out.append('*本页由脚本自动生成，请勿手动编辑。要改仪表盘请改 `scripts/build_overview.py`。*')
    out.append('')
    return '\n'.join(out)


def main():
    concepts = collect()
    if not concepts:
        print('[overview] 未找到概念，跳过生成')
        return 0
    md = render(concepts)
    # 注意：overview.md 也被 .gitignore 了吗？检查（应不被忽略）
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        f.write(md)
    print(f'[overview] 已生成 {OUTPUT}（{len(concepts)} 个概念，{len(set(c["type"] for c in concepts))} 种类型）')
    return 0


if __name__ == '__main__':
    sys.exit(main())
