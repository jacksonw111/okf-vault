---
type: Tool
title: "Braxis Blueprint"
description: "在 Oracle ARM 免费 VM 上跑起一套零 API 费用的 AI 业务系统：140+ 自主代理 + 20+ 免费 LLM 通道 + 内容生产 / 销售自动化。"
resource: "https://github.com/BraxisAI/braxis-blueprint"
tags: [ai-agents, automation, free-tier, llm-router, oracle-arm, business]
timestamp: "2026-08-25T19:30:00Z"
---

# Braxis Blueprint

## 它是什么

[BraxisAI/braxis-blueprint](https://github.com/BraxisAI/braxis-blueprint) 是「**不花一分钱 API 费**」跑 AI 业务系统的整套真实生产脚本（不是教程）。作者花一年时间在 Oracle ARM 免费 VM 上搭出来的：

- **140+ 自主代理**负责业务各环节（内容、邮件、销售、客服等）。
- **`llm_router.py`** 把 Groq / NVIDIA NIM / Gemini / Mistral / OpenRouter 免费档 + 本地 Ollama 共 **20+ 通道**串成带回退、自调优的路由链。
- 约 **107 个 cron 任务**，靠 `cronwrap` 的 `flock` 锁防重复进程。
- 业务侧跑着：每日 5 平台自动发内容、每周约 1000 封带 SPF / DKIM 的冷邮件、14 个 Stripe 商品自动发货，还有一座**市长是 LLM 代理的 3D 城市**作为彩蛋式 demo。

## 为什么用它 / 适合什么场景

- **想白嫖 LLM 跑 AI 业务**：免费档额度够用 + 路由做回退 = 不花钱。
- **小团队 / 个人副业**：不烧融资，先验证业务模式。
- **想学「生产级 LLM 路由」**：现成的多通道带回退 router，不是 demo。
- **Oracle ARM 免费层用户**：脚本针对该环境做了一系列优化（资源占用、cron 锁等）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多通道 LLM 路由 | `llm_router.py` 串 20+ 免费档通道，自带回退与自调优 |
| cron 编排 | `cronwrap` + `flock` 防重复进程 |
| 内容生产自动化 | 每日多平台自动发内容 |
| 邮件外联自动化 | 每周约 1000 封带 SPF / DKIM 的冷邮件 |
| 商品 / 支付自动化 | Stripe 商品自动发货（14 个商品） |
| AI 代理城市 | 一座 3D 城市，市长由 LLM 代理担任 |
| 免费基础设施 | 基于 Oracle ARM 免费 VM |

## 相关概念

- [OpenCodeGo_Pool](./tool-opencodego-pool.md) — 同样围绕「免费档 / 多账号」思路做的 AI 工具管理
- [Hunter Community](./tool-hunter-community.md) — 个人投资者用 AI Agent 跑量化 / 投资流程

## 参考链接

- 项目链接: <https://github.com/BraxisAI/braxis-blueprint>
- 原始链接: <https://x.com/QingQ77/status/2092179172882022597>