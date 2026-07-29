---
type: Tool
title: "Factory（编码 Agent 自动持续工作 runtime）"
description: "让编码 Agent 在仓库上自动持续工作，替代人工在每个步骤的终端编排。"
resource: "https://github.com/owainlewis/factory"
tags: [agent, runtime, automation, coding-agent, continuous-work]
timestamp: "2026-07-29T10:47:00.000Z"
---

# Factory

## 它是什么

一个让**编码 Agent 持续自动工作**的 runtime——人工不必在每个步骤手动编排终端命令，Agent 自己驱动、自己验证、循环跑。

![示意图](https://pbs.twimg.com/media/HOSSMpRaIAAH7fi.jpg)

## 它取代了什么

传统编码 Agent 工作流里：

1. 用户开终端
2. 写一句 prompt
3. Agent 跑一步
4. 用户看输出
5. 用户写下一句 prompt
6. …

Factory 取代了步骤 1 / 3 / 4 / 5 的"人工中介"——Agent 自己循环驱动整个仓库。

## 关键能力

| 能力 | 说明 |
|------|------|
| 自动持续工作 | 不需人手逐句 prompt |
| 仓库级 runtime | 跨文件 / 跨命令 |
| 替代终端编排 | 减少人工介入 |
| 编码 Agent 框架 | 与 Claude Code / Codex 等契合 |

## 适用场景

- 大型 PR 自动化
- 重复性重构（批量改接口）
- CI / CD 之外的"开发循环自动化"
- 让 Agent "自己干一晚上"

## 原始链接

- [项目仓库](https://github.com/owainlewis/factory)
- [推文剪藏](https://x.com/QingQ77/status/2082417601054179430)

## 相关概念

- [Optim Agent](./tool-optim-agent.md) — 让 Claude Code / Codex 替你跑超参寻优
- [Metis（编程模型外层包装）](./tool-metis.md) — 类似思路：包一层让编码更稳
- [Loop Engineering](./tool-loop-engineering.md) — "把 AI agent 编成自动循环"的方法论 + CLI 工具
- [MCO（多 AI 编程代理编排层）](./tool-mco.md) — 同时调度多种 CLI 代理的中立编排层