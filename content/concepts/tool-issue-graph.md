---
type: Tool
title: "issue-graph（Vercel Labs 出品的 GitHub issue / PR 关联图工具）"
description: "Vercel Labs 实验品：在动手改代码前，先把 GitHub issue 和 PR 之间的引用关系、重复修复和未跟进的后续项理清楚。npm 装的命令行工具，Node.js 20+，复用本机 gh 的 GitHub 登录态。"
resource: "https://github.com/vercel-labs/issue-graph"
tags: [github, issue-tracker, cli, vercel, dev-workflow, npm]
timestamp: 2026-09-30T04:46:00Z
---

# issue-graph

## 它是什么

**issue-graph** 是 [Vercel Labs](https://github.com/vercel-labs) 的实验项目：一个 npm 命令行工具，用来**把 GitHub issue 和 PR 之间的引用关系画出来**。

典型用法场景是"动手改代码之前"——先看清：

- 哪些 issue 引用了哪些 PR。
- 同一问题是否被多个 PR「重复修复」。
- 哪些后续项开着但没人跟进。

依赖与运行要求：

- Node.js 20+
- 复用本机 `gh` CLI 的 GitHub 登录态（无需额外 token）。

## 为什么用它 / 适合什么场景

- 接手一个维护期项目，想了解 issue / PR 之间**真正的引用图**而不是靠人脑记。
- 在扫 GitHub issue 列表时想知道「这个 PR 是不是重复修复」「是否已经合并的 PR 解决了但 issue 没关」。
- 想找一个**零配置**（沿用 `gh` 登录态）的 GitHub 关联可视化工具。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | npm CLI 工具 |
| Node 要求 | 20+ |
| 认证 | 复用本机 `gh` 登录态 |
| 输出 | issue ↔ PR 引用关系图 |
| 适合场景 | 动手改代码前的项目状态梳理 |

## 参考链接

- 仓库：<https://github.com/vercel-labs/issue-graph>

## 媒体

- ![](https://pbs.twimg.com/media/HTXXJTHaQAAZMbr.png)

## 相关概念

- [GitHub Workflow](./playbook-codex-standard-devflow.md) — 同为 Vercel Labs 等团队维护的"标准开发流程"工具组合