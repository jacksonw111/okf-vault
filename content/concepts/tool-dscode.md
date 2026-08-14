---
type: "Tool"
title: "dscode"
description: "thinkany-ai 开源的多模型编码智能体运行时：默认用 DeepSeek，可按仓库任务自由切换 DeepSeek / Codex / OpenAI / Anthropic 等服务商，本地优先、不被单一厂商或云端锁定。"
resource: "https://github.com/thinkany-ai/dscode"
tags: ["coding-agent", "multi-model", "deepseek", "codex", "open-source", "local-first"]
timestamp: "2026-08-14T19:50:00Z"
---

# dscode

## 它是什么
dscode 是一个以 DeepSeek 为默认模型、本地优先的多模型编码智能体运行时。它让用户按仓库任务自由切换 DeepSeek / Codex / OpenAI / Anthropic 等服务商，避免被单一厂商或云端锁定。

## 为什么用它 / 适合什么场景
- 想用 DeepSeek 默认的性价比，但偶尔又需要 GPT-5 / Claude 处理特定任务。
- 想把多个编码模型的 API 收到一个入口下，避免来回切换不同 CLI / 工具。
- 本地优先偏好者：希望 Agent 运行时和数据都在自己机器上，不强制走云端。

## 关键能力
| 能力 | 说明 |
|------|------|
| 默认模型 | DeepSeek |
| 可选模型 | DeepSeek / Codex / OpenAI / Anthropic 等 |
| 切换维度 | 按仓库任务自由切 |
| 部署 | 本地优先 |
| 定位 | 多模型编码智能体运行时 |

## 相关概念
- [Lupin](./tool-lupin.md) — Claude Code 的本地壳代理，让本地后端跑 Claude Code 全套协议；dscode 与 Lupin 都在「多模型 Agent 运行时」赛道上
- [ModelDock](./tool-modeldock.md) — Codex CLI 的本地 Responses 桥，给 DeepSeek 补识图 / 语音 / 联网 / 跨会话记忆，与 dscode 的多模型思路相近
- [Claude Code Router](./tool-claude-code-router.md) — 本地网关统一管 Claude Code / Codex / Grok 的凭据 / 路由 / 故障切换，dscode 是更上游的多模型运行时
