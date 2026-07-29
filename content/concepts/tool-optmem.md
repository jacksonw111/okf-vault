---
type: Tool
title: "OptMem（426 token 极简 AI Agent 跨会话记忆）"
description: "AI Agent 跨会话持久化记忆问题，OptMem 用一个 426 token 的 prompt 加一个脚本解决——极小、极简、立刻可用。"
resource: "https://github.com/VictorTaelin/OptMem"
tags: [agent, memory, minimal, persistence, token-efficient]
timestamp: "2026-07-28T10:22:00.000Z"
---

# OptMem

## 它是什么

针对一个常见痛点：**AI Agent 每次对话都从空白开始**。

OptMem 的解法：**426 token 的 prompt + 一个脚本**，把跨会话持久化记忆塞进现有 Agent 工作流。

视频示例：
- <https://video.twimg.com/tweet_video/HOSMh4wbwAAnoCv.mp4>

## 为什么它值得收藏

- **极小**：426 token 几乎不增加成本
- **极简**：单脚本 + 单 prompt
- **立刻可用**：任何 OpenAI 兼容 Agent 都能套

## 与「复杂记忆框架」的差异

| 维度 | 复杂框架 | OptMem |
|------|----------|--------|
| Token 成本 | 数 K token | 426 token |
| 依赖 | 数据库 / 向量库 | 单脚本 |
| 学习曲线 | 高 | 低 |
| 适用 | 大团队 / 复杂场景 | 个人 / 轻量项目 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 426 token prompt | 几乎无开销 |
| 单脚本 | 复制就能跑 |
| 跨会话持久 | 解决"每次都从空白开始" |
| 通用 | 任意 Agent 框架 |

## 原始链接

- [项目仓库](https://github.com/VictorTaelin/OptMem)
- [推文剪藏](https://x.com/QingQ77/status/2082048921694810455)

## 相关概念

- [Zestmem](./tool-zestmem.md) — 多智能体协作的分布式持久化记忆服务（更重量级）
- [EverOS](./tool-everos.md) — 统一本地长期记忆层，让不同 agent 共享并进化记忆
- [EchoesVault（OpenCode 持久记忆）](./tool-echoes-vault-opencode.md) — OpenCode 插件，会话结束自动记决策
- [Token Diet](./tool-token-diet.md) — Shell 编码代理令牌减肥技能