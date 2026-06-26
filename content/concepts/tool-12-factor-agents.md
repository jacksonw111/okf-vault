---
type: Tool
title: "12-Factor Agents（AI Agent 12 条工程原则）"
description: "HumanLayer 创始人 Dex Horthy 提炼的 12 条 AI Agent 工程原则（23.5k+ Stars），覆盖上下文管理、工具调用、状态建模、错误处理、控制流等核心环节，让 Agent 从 demo 走向实盘。"
resource: "https://github.com/humanlayer/12-factor-agents"
tags: [agent, engineering, principles, best-practice, humanlayer, prompt-engineering]
timestamp: 2026-06-26T16:50:00Z
---

# 12-Factor Agents

## 它是什么

12-Factor Agents 是 **HumanLayer 创始人 Dex Horthy** 与至少 100 位技术创始人深聊 + 实战挖掘几百个 Agent 框架后，提炼的**12 条让 AI Agent 从 demo 走向实盘的工程原则**。GitHub 23.5k+ stars。

12 条原则覆盖 Agent 工程核心环节：

- 上下文管理
- 工具调用
- 状态建模
- 错误处理
- 控制流
- 等等

## 为什么它重要

> "你的 Agent 为什么只能跑 demo，上不了实盘？"

大多数 Agent 在 demo 阶段表现良好（任务清晰、上下文短、用户宽容），但一旦进入真实业务流就会暴露出各种问题。12-Factor Agents 直面这些真实工程问题：

- 上下文溢出怎么办
- 工具调用失败怎么恢复
- 长任务状态怎么维护
- 错误如何优雅降级
- 控制流怎么避免循环

## 12 条原则速览

| 原则 | 关键词 |
|------|--------|
| 1 | 自然语言 → 结构化步骤 |
| 2 | 拥有自己的 prompts 文件 |
| 3 | 拥有自己的 context window |
| 4 | 工具就是结构化输出 |
| 5 | 状态由调用方管理，不在 prompt 里 |
| 6 | 启动 / 暂停 / 恢复 由 API 触发 |
| 7 | 通过工具调用与人交互 |
| 8 | 拥有自己的控制流 |
| 9 | 错误压缩进 context |
| 10 | 小而专注的 Agent |
| 11 | 触发器可来自多端（Slack / Email / Webhook） |
| 12 | 不做无状态 reducer |

> 完整 12 条以仓库为准——上面是简化版，仅作概要。

## 关键能力

| 能力 | 说明 |
|------|------|
| 12 条工程原则 | 经过百位创始人 + 数百框架实战验证 |
| demo → 实盘 | 直击"为什么上不了生产"痛点 |
| 跨框架适用 | 不绑定具体 Agent 框架 |
| 配套资源 | 仓库内含详细解释与代码示例 |
| 23.5k stars | 社区广泛认可 |

## 原始链接

- [项目仓库](https://github.com/humanlayer/12-factor-agents)
- [原始推文剪藏](https://x.com/Wen_Zw/status/2070549077289566223)

## 相关概念

- [claude-code-best-practice](./tool-claude-code-best-practice.md) — 同样是"Agent 最佳实践合集"，但更宽泛（工具 + 技巧）
- [mattpocock/skills](./tool-mattpocock-skills.md) — 偏 Real Engineers 风格的 Skills 合集
- [AgentStalker](./tool-agent-stalker.md) — 从"安全审计"视角审视 Agent 12 原则落地后的实际表现
- [MemGUI-Agent](./tool-memgui-agent.md) — 12 原则在"移动端长任务上下文管理"场景的具体实现
