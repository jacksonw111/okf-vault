#!/usr/bin/env python3
"""OKF 共享工具：frontmatter 解析 + markdown 内部链接解析。

被 okf_validate.py / flatten_concepts.py 复用，保证"解析口径一致"。
只用标准库。
"""
import os
import re

# frontmatter：文件开头的 --- ... --- 块
FM_RE = re.compile(r'^---\r?\n(.*?)\r?\n---\r?\n', re.DOTALL)

# markdown 链接 [text](target)，捕获 target
LINK_RE = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')


def parse_frontmatter(fm_text):
    """极简 YAML 解析：只取 `key: value` 标量行，值去首尾双引号。
    不处理嵌套/多行复杂结构——OKF 只关心 type/title/description 等标量。
    """
    data = {}
    for line in fm_text.split('\n'):
        m = re.match(r'^(\w+):\s*(.*)$', line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if len(val) >= 2 and val.startswith('"') and val.endswith('"'):
            val = val[1:-1]
        data[key] = val
    return data


def parse_doc(text):
    """从整篇 markdown 文本取 frontmatter dict；无则返回 None。"""
    m = FM_RE.match(text)
    if not m:
        return None
    return parse_frontmatter(m.group(1))


def read_frontmatter(path):
    """读文件并解析 frontmatter；文件不存在/无 frontmatter 返回 None。"""
    try:
        with open(path, encoding='utf-8') as f:
            text = f.read()
    except OSError:
        return None
    return parse_doc(text)


def extract_md_links(text):
    """返回 [(line_no(1-based), target_core), ...]，只含**内部 .md 链接**。
    排除 http(s)/mailto、纯锚点(#x)、非 .md 目标；剥离 #锚点 与 ?query 与 "title"。
    **跳过代码**：围栏代码块(``` / ~~~)内的行、行内代码 `` `...` `` 内的链接都不算
    （避免把示例文字 `[X](./x.md)` 误判为真链接）。
    """
    out = []
    in_fence = False
    for i, line in enumerate(text.split('\n'), start=1):
        stripped = line.lstrip()
        if stripped.startswith('```') or stripped.startswith('~~~'):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        cleaned = re.sub(r'`[^`]*`', '', line)  # 去行内代码段
        for m in LINK_RE.finditer(cleaned):
            target = m.group(2).strip().split(' ')[0]  # 去 "title"
            core = target.split('#')[0].split('?')[0]
            if not core:
                continue
            if core.startswith(('http://', 'https://', 'mailto:', 'tel:')):
                continue
            if not core.endswith('.md'):
                continue
            out.append((i, core))
    return out


def resolve_link(from_file, target, root):
    """把相对 target 解析为 root 内的绝对文件路径。
    from_file: 链接所在文件的绝对路径；target: 相对它的 core（已去锚点）。
    返回存在的文件绝对路径，否则 None（含"指向 root 之外"的情况）。
    """
    base_dir = os.path.dirname(from_file)
    cand = os.path.normpath(os.path.join(base_dir, target))
    try:
        rel = os.path.relpath(cand, root)
    except ValueError:
        return None
    if rel == '..' or rel.startswith('..' + os.sep):
        return None  # 指向 root 之外
    if os.path.isfile(cand):
        return cand
    return None
