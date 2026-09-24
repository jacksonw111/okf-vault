---
type: "Tool"
title: "PR Lens（PR 转架构 / 数据流视图）"
description: "把 GitHub PR 转成架构图、数据流与逐步变更动画，让 reviewer 先理解「系统如何变化」再下钻具体代码——尤其适合 Agent Coding 时代 Review 大量 AI 提交 PR 的场景。"
resource: "https://github.com/coldteadotai/pr-lens"
tags: "[pr, review, architecture, diagram, agent-coding, visualization, tool]"
timestamp: "2026-09-24T21:55:00Z"
---

# PR Lens（PR 转架构 / 数据流视图）

## 它是什么

[PR Lens](https://github.com/coldteadotai/pr-lens) 把一个 GitHub PR 转成可视化的架构图 + 数据流图，并生成「一步步怎么变过来」的动画。Reviewer 不必先逐行读 diff，而是先看清「系统哪些组件受影响 / 调用链怎么变 / 数据怎么流」，再决定下钻哪些代码段。

## 解决的问题

- Agent 提交的 PR 越来越多，逐行 review 既不现实也没必要
- 对「Agent 写的代码」或「外部 PR」往往没足够信心，但又必须知道到底改了啥
- Review 流程从「先理解代码 → 理解系统变化」变为「先理解系统变化 → 再决定哪些代码值得下钻」

## 关键能力

| 能力 | 说明 |
|------|------|
| 架构图 | 自动生成 PR 影响到的组件关系图 |
| 数据流 | 展示调用链变化与数据流向 |
| 变更动画 | 把 PR 的逐步变更做成动画在线查看 |
| Web 在线 | 直接在网页里看，不需要本地装环境 |
| Fork 友好 | 适合 Fork 一份到公司内部署 |

## 适用场景

- 公司 / 团队每天接收大量 agent PR，需要新的 Review 工具
- 外部贡献者提来的「裸 PR」需要快速理解影响面
- 想给团队内部搭建 Review 工作流基础设施

## 原始链接
- 项目主页：<https://github.com/coldteadotai/pr-lens>

## 相关概念
- [Code Review 工具与工作流](./tool-open-code-review.md) — 通用代码 review 工具生态