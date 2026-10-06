---
type: "Tool"
title: "Gitframe（终端 Git + 源码浏览 TUI）"
description: "hiroaqii 开源——在终端里把 Git 改动、源码浏览、提交历史和分支对比放进同一个 TUI，省去在 diff 工具和 git 命令之间来回切换；适合编码 Agent / 命令行重度用户的日常 git 界面。"
resource: "https://github.com/hiroaqii/gitframe"
tags: "[git, tui, terminal, code-review, cli]"
timestamp: "2026-10-06T22:51:00Z"
---

# Gitframe（终端 Git + 源码浏览 TUI）

## 它是什么

**Gitframe** 是 hiroaqii 开源的 TUI（Terminal User Interface）——在终端里把 **Git 改动 / 源码浏览 / 提交历史 / 分支对比**放进同一个界面，省去在 `git diff` / VS Code / GitHub 之间来回切换。

## 为什么用它 / 适合什么场景

- **终端党友好**：不用退出终端就能看 diff / 文件 / 历史
- **编码 Agent 协作**：TUI 界面可被脚本 / Agent 调用
- **极简高效**：键盘驱动，比打开 GUI 快得多
- **统一视图**：改动、文件树、历史、分支对比在一屏内

## 关键能力

| 能力 | 说明 |
|------|------|
| Git 改动视图 | staged / unstaged / untracked 分类 |
| 源码浏览 | 文件树 + 高亮 |
| 提交历史 | 图形化 log |
| 分支对比 | 任意两分支对比 |
| 终端原生 | 键盘驱动，TUI 界面 |

## 参考链接

- 项目链接：<https://github.com/hiroaqii/gitframe>

## 相关概念

- [Codex](./term-codex.md) / [Claude Code](./term-claude-code.md) — 也常用 git 操作
