---
type: "Tool"
title: "Aura-IDE（Planner/Worker 双智能体本地编码工作台）"
description: "本地优先的 AI 编码工作台，Planner 读代码库结构写技术规范，Worker 按规范执行文件编辑；写文件前先显示 diff 让用户逐条审批，落盘后自动跑验证，验证失败 Worker 自动试恢复。"
resource: "https://github.com/CarpseDeam/Aura-IDE"
tags: [ai-coding, agent, ide, local-first, multi-agent, diff-approval]
timestamp: "2026-06-24T15:30:00Z"
---

# Aura-IDE（Planner/Worker 双智能体本地编码工作台）

## 它是什么

[`CarpseDeam/Aura-IDE`](https://github.com/CarpseDeam/Aura-IDE) 是一个**本地优先的 AI 编码工作台**，采用 **Planner / Worker 双智能体协作**模式：

- **Planner** — 读代码库结构、写技术规范（spec），定义要改什么 / 怎么改；
- **Worker** — 按规范执行文件编辑（edit）。

中间关键设计是 **diff 审批门**：

> 每次要写文件前先显示 diff，你逐条审批才落盘；落盘后自动跑验证，验证失败 Worker 自动试恢复，不会留下烂摊子。

## 为什么用它 / 适合什么场景

- **可审查** — 不像一些 agent 黑盒改文件，每次改动都先看 diff，信任感高；
- **可恢复** — 验证失败自动试恢复，不会把项目改坏；
- **多模型可换** — 支持 DeepSeek / OpenAI / Anthropic / Gemini，随任务 / 成本切换；
- **不想管 API Key** — 有 Aura Credits 免管理密钥方案。

## 关键能力

| 能力 | 说明 |
|---|---|
| 双智能体 | Planner（写 spec） + Worker（执行 edit） |
| diff 审批 | 每次落盘前用户逐条审 |
| 自动验证 | 落盘后跑测试 / lint / type-check |
| 失败恢复 | 验证失败 Worker 自动试修复 |
| 多模型 | DeepSeek / OpenAI / Anthropic / Gemini |
| API Key 免管 | 内置 Aura Credits 方案 |

## 媒体 / 参考链接

![截图](https://pbs.twimg.com/media/HLex-4qagAAbHgq.jpg)

- [项目链接](https://github.com/CarpseDeam/Aura-IDE)

## 相关概念

- [Claude Code](tool-claude-code.md) — 终端 AI 编码 agent，Aura-IDE 是其 GUI 化、加 diff 审批门的版本
- [PeakCode](tool-peakcode.md) — 多 AI 编码代理统一 GUI
- [Vercel Eve 框架](tool-vercel-eve-framework.md) — filesystem convention 的 Agent 框架
