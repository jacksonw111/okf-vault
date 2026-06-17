#!/usr/bin/env python3
"""
format_clippings.py — 把剪藏的 markdown 文件规范成标准格式。

设计原则：
  - 只做安全的、幂等的规范化；绝不破坏「代码块 / 行内代码 / frontmatter」内容。
  - best-effort：任何文件出错都跳过，不阻断 commit。

会做的规范化：
  1. 统一 UTF-8、LF 行尾，去 BOM
  2. 去掉每行行尾多余空白
  3. <br> / <br/> → 换行（代码块内不动）
  4. 标题井号后多余空白归一：`##    标题` → `## 标题`
  5. 子节错级修正：`# 1.1 ...` → `### 1.1 ...`（单井号 + 带点编号几乎都是剪藏错误）
  6. 标题前后确保一个空行；代码块前后确保一个空行
  7. 连续 3+ 空行压缩为 1 个空行
  8. 文件末尾确保恰好一个换行
  9. 若没有 frontmatter，补一个最小 frontmatter（type: Note，标题取首个 # 或文件名）

用法：format_clippings.py <file1> [file2 ...]
"""
import sys
import os
import re
import time

FENCE_RE = re.compile(r'^\s{0,3}(```|~~~)')
HEADING_LINE_RE = re.compile(r'^#{1,6}\s')
H1_TITLE_RE = re.compile(r'^#\s+(.+?)\s*$')


def split_segments(text):
    """把文本切成 [('verbatim'|'code'|'prose', text), ...]。
    verbatim = 开头的 frontmatter；code = 围栏代码块；prose = 其余。
    verbatim / code 原样保留，只有 prose 会被规范化。
    """
    segs = []

    # 1) 开头的 frontmatter（整体原样保留，绝不规范化 YAML）
    if text.startswith('---\n') or text.startswith('---\r\n'):
        lines = text.split('\n')
        end = None
        for i in range(1, len(lines)):
            if lines[i].strip() in ('---', '...'):
                end = i
                break
        if end is not None:
            segs.append(('verbatim', '\n'.join(lines[:end + 1])))
            text = '\n'.join(lines[end + 1:])

    # 2) 围栏代码块逐段切出（原样保留）
    lines = text.split('\n')
    cur = []
    cur_prose = False
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        if FENCE_RE.match(line):
            if cur_prose and cur:
                segs.append(('prose', '\n'.join(cur)))
                cur = []
                cur_prose = False
            block = [line]
            i += 1
            while i < n:
                block.append(lines[i])
                if FENCE_RE.match(lines[i]) and len(block) >= 2:
                    i += 1
                    break
                i += 1
            segs.append(('code', '\n'.join(block)))
        else:
            cur_prose = True
            cur.append(line)
            i += 1
    if cur:
        segs.append(('prose', '\n'.join(cur)))
    return segs


def norm_prose(text):
    # <br> / <br/> → 换行
    text = re.sub(r'(?i)<br\s*/?>', '\n', text)

    processed = []
    for l in text.split('\n'):
        l = l.rstrip()  # 去行尾空白
        # 子节错级修正：# 1.1 ... → ### 1.1 ...
        dm = re.match(r'^#\s+(\d+\.\d+.*)$', l)
        if dm:
            l = '### ' + dm.group(1)
        else:
            # 标题井号后多余空白归一：##    标题 → ## 标题
            hm = re.match(r'^(#{1,6})\s+(.*)$', l)
            if hm:
                l = hm.group(1) + ' ' + hm.group(2)
        processed.append(l)

    # 标题前后补空行
    out = []
    m = len(processed)
    for idx, l in enumerate(processed):
        is_h = HEADING_LINE_RE.match(l) is not None
        if is_h:
            if out and out[-1].strip() != '':
                out.append('')
            out.append(l)
            nxt = processed[idx + 1] if idx + 1 < m else ''
            if nxt.strip() != '' and not HEADING_LINE_RE.match(nxt):
                out.append('')
        else:
            out.append(l)

    text = '\n'.join(out)
    text = re.sub(r'\n{3,}', '\n\n', text)  # 压缩 3+ 空行
    return text


def join_segments(segs):
    """各段之间确保恰好一个空行分隔；整体首尾去多余空行，末尾留一个换行。"""
    chunks = []
    for kind, body in segs:
        body = body.strip('\n')
        if not body:
            continue
        if kind == 'prose':
            body = norm_prose(body).strip('\n')
            if not body:
                continue
        if chunks:
            chunks.append('')  # 段间空行
        chunks.append(body)
    text = '\n'.join(chunks)
    return (text.strip('\n') + '\n') if text else ''


def first_h1_title(segs):
    """在剥离了 frontmatter/code 后的 prose 段里找首个 H1，避免误取代码块注释。"""
    for kind, body in segs:
        if kind != 'prose':
            continue
        for l in body.split('\n'):
            m = H1_TITLE_RE.match(l)
            if m:
                return m.group(1).strip()
    return None


def derive_title(segs, filepath):
    title = first_h1_title(segs)
    if title:
        return title
    stem = os.path.splitext(os.path.basename(filepath))[0]
    pretty = stem.replace('-', ' ').replace('_', ' ').strip()
    return pretty or stem


def has_frontmatter(text):
    return text.startswith('---\n') or text.startswith('---\r\n')


def ensure_frontmatter(text, segs, filepath):
    if has_frontmatter(text):
        return text
    title = derive_title(segs, filepath).replace('"', '\\"')
    ts = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(os.path.getmtime(filepath)))
    fm = (
        "---\n"
        'type: "Note"\n'
        f'title: "{title}"\n'
        'description: ""\n'
        'tags: [clipping]\n'
        f"timestamp: {ts}\n"
        "---\n\n"
    )
    return fm + text.lstrip('\n')


def format_text(raw_bytes, filepath):
    text = raw_bytes.decode('utf-8', errors='replace')
    if text.startswith('\ufeff'):  # 去 BOM
        text = text[1:]
    text = text.replace('\r\n', '\n').replace('\r', '\n')  # 统一 LF
    segs = split_segments(text)
    normed = join_segments(segs)
    return ensure_frontmatter(normed, segs, filepath)


def main():
    changed = []
    for fp in sys.argv[1:]:
        try:
            if not fp.endswith('.md') or not os.path.isfile(fp):
                continue
            with open(fp, 'rb') as fh:
                before = fh.read().decode('utf-8', errors='replace')
            after = format_text(before.encode('utf-8'), fp)
            if after != before:
                with open(fp, 'w', encoding='utf-8') as fh:
                    fh.write(after)
                changed.append(fp)
        except Exception as e:  # best-effort：出错跳过，不阻断
            print(f"[skip] {fp}: {e}", file=sys.stderr)
    if changed:
        print(f"[format] 规范化了 {len(changed)} 个文件：")
        for c in changed:
            print(f"  - {c}")
    else:
        print("[format] 无需改动")
    return 0


if __name__ == '__main__':
    sys.exit(main())
