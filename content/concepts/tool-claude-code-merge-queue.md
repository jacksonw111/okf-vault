---
type: Tool
title: "claude-code-merge-queue（本地零成本 Claude Code 合并队列）"
description: "在本地零成本运行的合并队列，让多个并行的 Claude Code 工作树按 FIFO 顺序串行落地、构建、测试，避免同时推送造成的 rebase 冲突、构建争抢和测试互相干扰。"
resource: "https://github.com/funador/claude-code-merge-queue"
tags: "[claude-code, merge-queue, git, fifo, ci, monorepo]"
timestamp: "2026-07-09T20:50:00Z"
---

# claude-code-merge-queue（本地零成本 Claude Code 合并队列）

## 它是什么
`funador/claude-code-merge-queue` 是一个**本地跑、零成本**的合并队列：

- 让多个**并行工作的 Claude Code 工作树**（worktree）按 FIFO 顺序**串行落地 + 构建 + 测试**
- 避免：**rebase 冲突 + 构建资源争抢 + 测试结果互相污染**
- 完全本地，不需要 GitHub Actions 等外部 CI

## 为什么用它 / 适合什么场景
- **同时跑了多个 Claude Code agent**在干同一仓库的不同 worktree，怕落地时撞车。
- 团队多人 + 多个 agent 并行提交到同一主干，怕 CI 雪崩。
- 想给 Claude Code 工作流加 **「merge 后做最后验证」** 这一步而无需付费。
- 适合：agent 编码流水线 / monorepo / CI 不充裕的小团队 / 个人疯狂并行 vibe coding。

## 关键能力
| 能力 | 说明 |
|------|------|
| FIFO 调度 | 多个 worktree 落地按入队顺序 |
| 本地零成本 | 无需云 CI |
| 构建 + 测试串行 | 防止资源争抢与互相干扰 |
| 重 base 处理 | 自动解决 rebase 冲突 |
| 与 Claude Code 协同 | 直接对接 worktree 机制 |

## 媒体参考

工具截图：
- ![](https://pbs.twimg.com/media/HMrTXTxboAAEU8v.jpg)

## 相关概念
- [Firstmate](tool-firstmate.md) — 把终端编码 AI 变「大副」，自动派多个 crewmate 并行干活（前置"派工"，本工具是"派工后的合并")
- [MCO](tool-mco.md) — 多 AI 编程代理编排层
- [Vibe-Trading](tool-vibe-trading.md) — 港大实验室的 AI 交易研究平台（同样涉及并行任务调度）
- [Mux（Claude Code tmux 插件）](tool-mux-claude-tmux.md) — 多 Claude Code 会话面板管理

## 参考链接
- 项目链接：<https://github.com/funador/claude-code-merge-queue>
