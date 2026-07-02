---
type: Tool
title: "animarouter"
description: "TypeScript 全栈项目，把 16+ 个 LLM 提供商的免费额度聚合成单一 OpenAI 兼容接口，9 种路由策略含 Auto 元老虎机、动态降级、统一基准评分、推理 Token 公平计速、端到端思考链透传。"
resource: "https://github.com/animaios/animarouter"
tags: "[llm, router, openai-compatible, api-gateway, typescript, free-tier]"
timestamp: "2026-07-02T13:30:00Z"
---

# animarouter

## 它是什么
TypeScript 全栈项目，在 freellmapi 与 api-gateway 的基础上，把 16+ 个 LLM 提供商的**免费额度**聚合到单一 OpenAI 兼容接口。带智能路由策略与学习能力。

## 为什么用它 / 适合什么场景
- 想要一份 `OPENAI_BASE_URL` 就同时调用 16+ 家免费模型服务。
- 想用同一套客户端代码（OpenAI SDK / Cursor / Claude Code 等）透明路由到多家提供商。
- 想让路由器根据过去表现自动选最划算的提供商（Auto 元老虎机策略）。
- 想做大规模 benchmark / 自动化作业，不想被单一提供商的速率限制或额度卡死。

## 关键能力
| 能力 | 说明 |
|------|------|
| 提供商聚合 | 16+ LLM 提供商免费额度统一接入 |
| 接口兼容 | OpenAI 兼容 API（替换 base_url 即用） |
| 路由策略 | 9 种策略，含 Auto 元老虎机（按历史表现自动选） |
| 动态降级 | 主提供商故障时自动切备用 |
| 基准测试 | 统一评分，便于对比各提供商 |
| Token 计速 | 推理 Token 公平计速，避免某些提供商因推理 token 偷算费率 |
| 思考链透传 | 端到端思考链（reasoning chain）透传 |

## 相关概念
- [Proxide](tool-proxide.md) — 类似思路（让任意 Agent 透明接多源模型）；animarouter 专注免费额度聚合 + 路由
- [MCO](tool-mco.md) — 多 AI 编程代理编排层；animarouter 是 LLM API 层，MCO 是 CLI Agent 层
- [second-brain-cloudflare](tool-second-brain-cloudflare.md) — 同作者 / 同思路：把多源能力聚合到统一接口（这里是记忆而非 LLM）

## 项目链接
- 项目主页：<https://github.com/animaios/animarouter>

## 媒体
![](https://pbs.twimg.com/media/HML1RTuboAAOXAw.jpg)