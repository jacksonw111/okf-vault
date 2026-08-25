---
type: Tool
title: "XingCare · 小星健康管家"
description: "克隆即跑的「结构化症状采集 + AI 问答」前后端模板：Vue 3 采集界面 + FastAPI 编排问答，默认不联网、不用密钥。"
resource: "https://github.com/k4ubx7/XingCare"
tags: [healthcare, symptom-triage, vue, fastapi, demo, open-source]
timestamp: "2026-08-25T19:30:00Z"
---

# XingCare · 小星健康管家

## 它是什么

[k4ubx7/XingCare](https://github.com/k4ubx7/XingCare) 是一个**克隆下来就能跑**的「结构化症状采集 + AI 问答」演示项目，前后端分工清晰：

- **Vue 3** 负责结构化症状采集前端界面（按分支问题一步步问下来）。
- **FastAPI** 负责编排问答与症状→建议逻辑。
- **默认不联网、不用 API Key**：开箱即可在本地跑起来，适合教学 / 演示 / 原型。

![](https://pbs.twimg.com/media/HQeBHPIacAAfLOs.png)

## 为什么用它 / 适合什么场景

- **想学或演示「医疗类 AI 前后端怎么搭」**：从结构化问诊 → AI 回答，端到端完整参考。
- **没有 GPU / 没有 API 配额**：默认无外部依赖，本地模型即可跑。
- **作为 demo 项目模板**：Vue 3 + FastAPI 组合的最小可用参考实现。
- **教学场景**：把症状采集的「分叉对话树」思路直接学走。

## 关键能力

| 能力 | 说明 |
|------|------|
| 结构化症状采集 | 树状 / 分支式问诊 UI |
| AI 问答 | FastAPI 编排症状 → 回答 |
| 零配置启动 | 默认不联网、不用 API Key |
| 前后端分离 | Vue 3 前端 + FastAPI 后端，可独立替换 |
| 演示 / 教学模板 | 适合做 demo / 教学 / 原型 |

## 相关概念

- [FDE Guidance Book](./note-fde-guidance-book.md) — 同样面向「端到端参考实现 / 演示模板」的工程实践
- [DeepSeek Harness Desktop](./tool-deepseek-harness-desktop.md) — 另一种「开箱即用桌面壳」形态

## 参考链接

- 项目链接: <https://github.com/k4ubx7/XingCare>
- 原始链接: <https://x.com/QingQ77/status/2092245107139629360>