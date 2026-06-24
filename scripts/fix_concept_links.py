#!/usr/bin/env python3
"""一次性修复：去掉 concepts/ 内文件里多余的 `concepts/` 链接前缀。

agent 在 concepts/ 里建概念时，相互链接误写成 `concepts/<name>.md`（从 content/
根算的路径），但链接文件自己就在 concepts/ 里，于是解析成 concepts/concepts/<name>.md
→ 断链。本脚本把这类链接改回同级 `<name>.md`（仅当目标 basename 确实是概念时）。

用法：python3 scripts/fix_concept_links.py
"""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import okf_lib  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONCEPTS = os.path.join(ROOT, "content", "concepts")
LINK_RE = okf_lib.LINK_RE

# 多余前缀：concepts/ 或 ./concepts/（不含 ../concepts/——那个从 concepts/ 出发反而是对的）
BAD_PREFIX = re.compile(r"^(\./)?concepts/(.+\.md)$")


def main():
    concept_basenames = {
        os.path.basename(p)
        for p in glob.glob(os.path.join(CONCEPTS, "**", "*.md"), recursive=True)
        if os.path.basename(p) != "index.md"
    }

    files = sorted(
        glob.glob(os.path.join(CONCEPTS, "**", "*.md"), recursive=True)
    )
    total_rewrites = 0
    files_changed = 0

    for path in files:
        text = open(path, encoding="utf-8").read()

        def repl(m):
            nonlocal n
            label = m.group(1)
            target = m.group(2)
            core = target.split(" ")[0]
            anchor = ""
            if "#" in core:
                core, a = core.split("#", 1)
                anchor = "#" + a
            bmatch = BAD_PREFIX.match(core)
            if bmatch and bmatch.group(2) in concept_basenames:
                n += 1
                return f"[{label}]({bmatch.group(2)}{anchor})"
            return m.group(0)

        n = 0
        new_text = LINK_RE.sub(repl, text)
        if n > 0:
            open(path, "w", encoding="utf-8").write(new_text)
            files_changed += 1
            total_rewrites += n

    print(f"[fix] 重写 {total_rewrites} 条 concepts/ 前缀链接，涉及 {files_changed} 个文件")
    print("[fix] 完成。请运行: python3 scripts/okf_validate.py  确认 0 断链")


if __name__ == "__main__":
    main()
