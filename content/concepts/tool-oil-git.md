---
type: "Tool"
title: "oil-git（只读 Git 桌面查看器）"
description: "oil-oil 开源：把本地 Git 仓库的分支、提交图、暂存与工作区变更、文件 diff 做成只读桌面界面，查看时不会碰仓库一下。"
resource: "https://github.com/oil-oil/oil-git"
tags: "[git, desktop-app, read-only, code-review, branch-visualization]"
timestamp: "2026-10-08T23:50:00Z"
---

# oil-git

## 它是什么

[oil-git](https://github.com/oil-oil/oil-git) 是 oil-oil 开源的「**只读 Git 桌面查看器**」：

- 把本地 Git 仓库的**分支、提交图、暂存与工作区变更、文件 diff** 做成桌面 GUI
- **只读**——查看时**不会碰仓库一下**（不写 reflog、不改状态、不影响 commit）
- 适合想「看清 Git 历史」又怕 GUI 工具乱动仓库的人

## 为什么用它 / 适合什么场景

- **怕 GUI 工具乱动仓库**：某些 Git GUI 会触发 stash / reflog 写入，干扰你
- **想看清提交图**：CLI 看不到清晰的 branch 图
- **日常 code review**：只看 diff / blame 不动手
- **教学**：把 Git 历史「画」出来给新人看

## 关键能力

| 能力 | 说明 |
| ------ | ------ |
| 形态 | 桌面 GUI（只读） |
| 分支图 | 直观看到分支 / merge |
| 提交图 | DAG 视图 |
| 暂存 / 工作区变更 | 文件级状态 |
| 文件 diff | 行级比较 |
| 零副作用 | 不会写 reflog / 不会 stash |

## 参考链接

- 项目链接：<https://github.com/oil-oil/oil-git>

## 媒体

![](https://pbs.twimg.com/media/HUE_7YIbkAAkYb1.jpg)

## 相关概念

- [gitframe](./tool-gitframe.md) — 同为 Git 工具，但 gitframe 是 TUI、oil-git 是 GUI 且只读