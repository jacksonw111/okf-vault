#!/usr/bin/env python3
"""一次性迁移：把 concepts/{type}/*.md 扁平化为 concepts/*.md，
并重写所有指向概念的内部链接到新的扁平位置。

策略（解析后重新相对化，对 3 种旧链接风格都鲁棒）：
  1. 收集所有概念 basename（去重校验，防扁平后冲突）。
  2. git mv 每个子目录文件上移到 concepts/，删空子目录（保留 git rename 历史）。
  3. 遍历 content/ 下 .md（跳过 private/、inbox/_done/、.obsidian/、templates/、
     log.md、overview.md），对每个 markdown 链接：取 basename，若是概念，
     重写为"从当前文件到 concepts/<basename>.md"的正确相对路径（自动得
     同目录概念→<basename>.md，content/ 根文件→concepts/<basename>.md）。

用法：python3 scripts/flatten_concepts.py
"""
import glob
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import okf_lib  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, 'content')
CONCEPTS = os.path.join(CONTENT, 'concepts')
TYPE_DIRS = ['term', 'tool', 'playbook', 'note']
LINK_RE = okf_lib.LINK_RE

SKIP_DIRS = {'private', os.path.join('inbox', '_done'), '.obsidian', 'templates'}
SKIP_FILES = {'log.md', 'overview.md'}


def git(args):
    return subprocess.run(['git', '-C', ROOT] + args, check=True,
                          capture_output=True, text=True)


def should_skip(rel_to_content):
    """rel_to_content: 相对 content/ 的路径。"""
    norm = rel_to_content.replace('\\', '/')
    if norm in SKIP_FILES:
        return True
    for d in SKIP_DIRS:
        if norm == d or norm.startswith(d + '/'):
            return True
    return False


def rewrite_links(text, old_dir, new_dir, concept_basenames):
    """重写指向概念/内容的相对链接。
    - 概念链接（basename ∈ concepts）：重写到 concepts/<base> 相对 new_dir。
    - 非概念相对链接：仅当文件移动过（old_dir != new_dir），按旧位置解析目标，
      再重新相对化到 new_dir（修 overview.md/index.md 这类因上移而错位的链接）。
    """
    lines = text.split('\n')
    in_fence = False
    changed = 0

    def repl(m):
        nonlocal changed
        label = m.group(1)
        target = m.group(2)
        core = target.split(' ')[0]          # 去 "title"
        anchor = ''
        if '#' in core:                       # 保留 #锚点
            core, a = core.split('#', 1)
            anchor = '#' + a
        base = os.path.basename(core)
        if base in concept_basenames:
            new_core = os.path.relpath(os.path.join(CONCEPTS, base), new_dir)
            changed += 1
            return f'[{label}]({new_core}{anchor})'
        if old_dir != new_dir and not os.path.isabs(core):
            old_target = os.path.normpath(os.path.join(old_dir, core))
            if os.path.isfile(old_target):
                new_core = os.path.relpath(old_target, new_dir)
                changed += 1
                return f'[{label}]({new_core}{anchor})'
        return m.group(0)

    out = []
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith('```') or stripped.startswith('~~~'):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        out.append(LINK_RE.sub(repl, line))
    return '\n'.join(out), changed


def main():
    # 1. 收集概念文件
    moved = []
    for td in TYPE_DIRS:
        src_dir = os.path.join(CONCEPTS, td)
        if not os.path.isdir(src_dir):
            continue
        moved += sorted(glob.glob(os.path.join(src_dir, '*.md')))
    basenames = [os.path.basename(f) for f in moved]
    dupes = {b for b in basenames if basenames.count(b) > 1}
    assert not dupes, f"扁平化后有重名冲突: {dupes}"
    concept_basenames = set(basenames)
    print(f"[flatten] 待移动 {len(moved)} 个概念文件")

    # 2. git mv 上移；记录 old_dir 供链接重写用
    moves = {}  # new_path -> old_dir
    for f in moved:
        dst = os.path.join(CONCEPTS, os.path.basename(f))
        moves[dst] = os.path.dirname(f)
        git(['mv', os.path.relpath(f, ROOT), os.path.relpath(dst, ROOT)])
    for td in TYPE_DIRS:
        d = os.path.join(CONCEPTS, td)
        if os.path.isdir(d) and not os.listdir(d):
            os.rmdir(d)
    print(f"[flatten] 已上移到 concepts/，子目录已清")

    # 3. 重写链接
    targets = glob.glob(os.path.join(CONTENT, '**', '*.md'), recursive=True)
    rewrite_count = 0
    files_changed = 0
    for path in sorted(set(targets)):
        rel = os.path.relpath(path, CONTENT)
        if should_skip(rel):
            continue
        new_dir = os.path.dirname(path)
        old_dir = moves.get(path, new_dir)  # 移动过的文件用旧目录；其余用自身目录
        text = open(path, encoding='utf-8').read()
        new_text, n = rewrite_links(text, old_dir, new_dir, concept_basenames)
        if n > 0:
            open(path, 'w', encoding='utf-8').write(new_text)
            files_changed += 1
            rewrite_count += n
    print(f"[flatten] 重写 {rewrite_count} 条链接，涉及 {files_changed} 个文件")
    print("[flatten] 完成。请运行: python3 scripts/okf_validate.py  确认 0 断链")


if __name__ == '__main__':
    main()
