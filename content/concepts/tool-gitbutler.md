---
type: "Tool"
title: "GitButler"
description: "Git 版本控制桌面客户端：以「虚拟分支」管理多任务并行，允许同时存在多个未提交改动叠加在同一工作区。"
resource: "https://gitbutler.com/"
tags: [git, version-control, desktop, developer-tools]
timestamp: "2026-08-08T20:00:00Z"
---

# GitButler

## 它是什么

GitButler 是一款 Git 版本控制桌面客户端，主打「虚拟分支（virtual branches）」：让你在同一工作区里同时维护多个未提交改动、各自走独立分支，最终按需 commit / push。比 Git Worktree 更轻、对日常工作流更友好。

## 为什么用它 / 适合什么场景

- 经常需要「切上下文」但又不想真切的分支间反复 stash / checkout。
- 想在一次 session 里同时改多个不相关的事情（修 bug + 写 feature + 改 docs）。
- 想要 Git 操作的 GUI 化，且仍能深入到命令行级 git 命令。

## 关键能力

| 能力 | 说明 |
|------|------|
| 虚拟分支 | 多个未提交改动叠加在同一工作区 |
| 拖拽分配 | UI 里把文件片段拖到不同分支 |
| 自动识别 | 自动识别改动归属的虚拟分支 |
| GitHub 集成 | 一键创建 PR |
| 桌面 GUI | macOS / Linux / Windows 桌面客户端 |

## 相关概念

- [Salience (macOS)](./tool-salience-macos.md) — 同样以 git 为中心的桌面工作流工具