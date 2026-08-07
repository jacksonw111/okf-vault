---
type: Tool
title: "Pi Bifrost"
description: "Pi 终端 AI 助手的模型自动切换层：每次生成前把 Pi 实际激活的模型自动切到配置中对应的档位，按任务复杂度 / 价格 / 速度 / 上下文长度路由。"
resource: "https://github.com/iamaamir/pi-bifrost"
tags: [pi, model-routing, llm-cost, llm-gateway, ai-agent]
timestamp: 2026-08-06T14:00:00Z
---

# Pi Bifrost

## 它是什么

iamaamir 开源的 Pi 扩展：在 Pi 调用模型前根据任务维度自动选择配置好的模型档位，让 Pi 不再「每个对话都固定用同一个模型」。

## 为什么用它 / 适合什么场景

- 你日常用 Pi，但每次都要手动切换模型档位（Haiku / Sonnet / Opus），嫌烦。
- 想让「简单改一行」跑便宜小模型、「复杂重构」跑贵但强的大模型，按任务自动路由。
- 想以「价格 / 速度 / 上下文长度」中的一项为优先做硬路由，而不是让 Pi 内部瞎猜。

## 关键能力

| 能力 | 说明 |
|------|------|
| 自动档位切换 | 生成前拦截 Pi 的模型调用，按任务映射到配置档位 |
| 多维路由 | 任务复杂度、价格、速度、上下文长度任选一项作为判据 |
| 配置驱动 | 不同档位对应不同模型在配置里声明，无需改 Pi 自身 |

## 相关概念
- [Claude Code Router](./tool-claude-code-router.md) — 本地网关统一管 Claude Code / Codex / Grok 凭据 / 路由 / 故障切换
- [Aimux](./tool-aimux.md) — Rust crate 收敛上百家 AI 服务商 HTTP 接口为统一 API
- [Pi-tbox](./tool-pi-tbox.md) — Pi 扩展工具开关面板