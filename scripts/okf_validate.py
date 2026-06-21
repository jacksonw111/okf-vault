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

import okf_lib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 仓库根
CONCEPTS_DIR = os.path.join(ROOT, 'content', 'concepts')
CONTENT_ROOT = os.path.join(ROOT, 'content')


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


def main():
    errors = validate(CONCEPTS_DIR, CONTENT_ROOT)
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
