#!/usr/bin/env python3
"""okf_validate.py — OKF 一致性校验。

检查 content/concepts/ 下每个概念文件：
  A. 有合法 YAML frontmatter 且含非空 `type` 字段（OKF 唯一强制字段）。
  B. 每个**内部 .md 链接**都能解析到真实文件（图完整性，防断链）。

用法：
  python3 scripts/okf_validate.py        # 校验本仓库
  python3 -m unittest test_okf_validate  # 跑单测

返回码：全部通过 0；有违例 1（供 CI fail-fast）。
"""
import glob
import os
import sys
from datetime import datetime, timezone

import okf_lib

try:
    import yaml  # PyYAML：可选，用于严格 YAML 校验（CI 装；本地无则降级跳过）
    HAVE_YAML = True
except ImportError:
    HAVE_YAML = False

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 仓库根
CONCEPTS_DIR = os.path.join(ROOT, 'content', 'concepts')
CONTENT_ROOT = os.path.join(ROOT, 'content')

# 断链工单：校验发现违例时自动写入 inbox/，供下次 agent 跑时修复
TICKET_PATH = os.path.join(CONTENT_ROOT, 'inbox', '_broken-links.md')


def validate(concepts_dir, content_root):
    """返回违例清单（list[str]，每条 '相对路径[:行]: 原因'）。空=通过。"""
    errors = []
    files = sorted(glob.glob(os.path.join(concepts_dir, '**', '*.md'), recursive=True))
    for path in files:
        name = os.path.basename(path)
        if name == 'index.md':
            continue  # 索引页不参与概念校验
        rel = os.path.relpath(path, ROOT if os.path.isdir(ROOT) else content_root)
        try:
            with open(path, encoding='utf-8') as f:
                text = f.read()
        except OSError as e:
            errors.append(f"{rel}: 读取失败 {e}")
            continue

        # A0. 严格 YAML 校验（PyYAML 可用时；坏 YAML 会让 Quartz 构建直接失败）
        if HAVE_YAML:
            m_fm = okf_lib.FM_RE.match(text)
            if m_fm:
                try:
                    yaml.safe_load(m_fm.group(1))
                except yaml.YAMLError as e:
                    first = (str(e).strip().splitlines() or [str(e)])[0]
                    errors.append(
                        f"{rel}: frontmatter 不是合法 YAML（Quartz 会构建失败）: {first}"
                    )

        # A. type 校验
        fm = okf_lib.parse_doc(text)
        if fm is None:
            errors.append(f"{rel}: 缺 frontmatter")
        elif not (fm.get('type') or '').strip():
            errors.append(f"{rel}: frontmatter 缺 type 字段")

        # B. 断链校验
        for line_no, target in okf_lib.extract_md_links(text):
            if not okf_lib.resolve_link(path, target, content_root):
                errors.append(f"{rel}:{line_no}: 断链 -> {target}")

    return errors


def write_ticket(errors):
    """把违例清单写成 inbox/_broken-links.md 工单（供下次 agent 跑时修复）。
    无违例时删除遗留工单，避免 stale 工单反复触发。"""
    if not errors:
        if os.path.exists(TICKET_PATH):
            os.remove(TICKET_PATH)
            print(f"[ticket] 校验干净，删除遗留工单 {TICKET_PATH}")
        return
    ts = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    body = [
        '---',
        'type: "Note"',
        'title: "断链工单（自动生成）"',
        'description: "OKF 校验器检测到的 concepts/ 断链清单；agent 修完后把本文件移到 _done/"',
        'tags: ["okf", "maintenance"]',
        f'timestamp: "{ts}"',
        '---',
        '',
        '# ⚠️ 断链工单（自动生成，勿当知识资料）',
        '',
        '本文件由 `scripts/okf_validate.py` 在 `concepts/` 发现断链或缺 type 时自动写入 `inbox/`。',
        '**这不是知识资料——不要把本文件本身转成概念。**',
        '',
        '逐条修复后，把本文件 `mv` 到 `inbox/_done/`。每条修法二选一：',
        '1. 目标值得收录（术语/工具）→ 在 `concepts/` 新建对应 stub 概念（带 `type` frontmatter）；',
        '2. 目标不值得单独成条 → 把那条 `[x](path.md)` 改成纯文本 `x`。',
        '',
        f'## 违例清单（{len(errors)} 条）',
        '',
    ]
    body += [f'- {e}' for e in errors]
    body.append('')
    os.makedirs(os.path.dirname(TICKET_PATH), exist_ok=True)
    with open(TICKET_PATH, 'w', encoding='utf-8') as f:
        f.write('\n'.join(body))
    print(f"[ticket] 写入 {len(errors)} 条违例工单 -> {TICKET_PATH}")


def main():
    errors = validate(CONCEPTS_DIR, CONTENT_ROOT)
    write_ticket(errors)  # 工单总是反映当前状态（有违例写、干净删）
    if errors:
        print(f"❌ OKF 校验失败：{len(errors)} 个违例\n")
        for e in errors:
            print(f"  - {e}")
        return 1
    n = len([f for f in glob.glob(os.path.join(CONCEPTS_DIR, '**', '*.md'), recursive=True)
             if os.path.basename(f) != 'index.md'])
    print(f"✅ OKF 校验通过：{n} 个概念，全部有 type，无断链。")
    return 0


if __name__ == '__main__':
    sys.exit(main())
