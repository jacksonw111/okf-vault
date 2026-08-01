---
type: Tool
title: "claude-code-router"
description: "02Fabs/claude-code-router，把 Claude Code / Codex / Grok 这些 AI 编程工具接到一个本地网关，统一管模型、凭据、路由和故障切换。"
resource: "https://github.com/02Fabs/claude-code-router"
tags: "[ai-coding, router, failover, local-gateway, claude-code, codex, grok]"
timestamp: "2026-08-01T20:30:00Z"
---

# claude-code-router

## 它是什么

[`02Fabs/claude-code-router`](https://github.com/02Fabs/claude-code-router) 是一个**本地 AI 网关**：把 Claude Code / Codex / Grok 这些 AI 编程工具统一接到同一个本地路由层，统一管理**模型选择、凭据、路由策略、故障切换**。

## 解决什么痛点

- Claude Code 配 OpenAI key、Codex 配 Anthropic key、Grok 又要另一套凭据——凭据散乱
- 想给不同任务配不同模型（debug 用 Sonnet、生成文档用本地 Ollama）
- Claude Code 官方 API 挂了想自动切到 Anthropic 备用 key 或别家模型

## 关键能力

| 能力 | 说明 |
|------|------|
| 多 AI 编程工具兼容 | Claude Code / Codex / Grok 等 |
| 统一凭据 | 一处配置 OpenAI / Anthropic / Gemini / Groq 等 key |
| 路由策略 | 按任务类型 / 关键词 / 模型质量分配请求 |
| 故障切换 | 主模型挂了自动切到备选 |
| 本地网关 | 跑在本地机器上，延迟低、隐私有保障 |

## 适合什么场景

- 同时用多个 AI 编程工具，想统一管理凭据和模型选择
- 想做「任务分级」——简单任务用便宜模型、复杂任务用强模型
- 想给 AI 编程工具做「自动备份」——主 API 挂了切备用

## 与同类工具的差异

| 工具 | 形态 | 差异 |
|------|------|------|
| [grafana-ai-sdk](./tool-grafana-ai-sdk.md) | Go SDK | 后端 SDK 层多 provider 抽象，不做网关路由 |
| [bbarit-agent-oss](./tool-bbarit-agent-oss.md) | CLI | 单二进制 CLI，替代 Claude Code 本身 |
| [openclaude-improved](./tool-openclaude-improved.md) | TypeScript CLI | 通用 CLI + 多 provider |
| claude-code-router | 本地网关 | 适配 Claude Code 协议，做路由 + 故障切换 |

## 媒体

![claude-code-router 截图](https://pbs.twimg.com/media/HOhX6IuaMAAtYJp.jpg)

## 原始链接

- [项目仓库](https://github.com/02Fabs/claude-code-router)
- [原始推文](https://x.com/QingQ77/status/2083407624750477594)

## 相关概念

- [grafana-ai-sdk](./tool-grafana-ai-sdk.md) — 后端 SDK 层多 provider，claude-code-router 是网关层多 provider
- [bbarit-agent-oss](./tool-bbarit-agent-oss.md) — 直接替代 Claude Code，claude-code-router 是 Claude Code 的「外挂路由」