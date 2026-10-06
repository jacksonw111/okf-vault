---
type: "Tool"
title: "Cloudflare OS（Cloudflare 端到端 Agent 沙箱）"
description: "Cloudflare 官方出品的端到端方案——让全公司的人都能使唤 AI agent 干活（做幻灯 / 搭小工具 / 连外部系统），同时让安全团队能睡觉：agent 与应用都关进沙箱，动外部资源要过一道带审批的关卡。"
resource: "https://github.com/cloudflare/cloudflare-os"
tags: "[cloudflare, sandbox, agent, security, governance, ai-coding-agent]"
timestamp: "2026-10-06T22:51:00Z"
---

# Cloudflare OS（Cloudflare 端到端 Agent 沙箱）

## 它是什么

**Cloudflare OS** 是 Cloudflare 官方开源的端到端方案——目标让**全公司的人**都能使唤 AI agent 干活（做幻灯片、搭小工具、连外部系统），同时让**安全团队能睡觉**：agent 与应用都关进沙箱，动外部资源要过一道**带审批**的关卡。

## 为什么用它 / 适合什么场景

- **企业级 Agent 落地**：让非工程师也能自助使唤 agent，不绕过安全
- **沙箱隔离**：agent 在 sandbox 内运行，外部资源按白名单访问
- **审批链路**：高危操作（写数据库 / 发邮件 / 改生产）需人工 review
- **可观测**：每个 agent 任务的状态、上下文、输出全程审计

## 关键能力

| 能力 | 说明 |
|------|------|
| Agent 沙箱 | agent 与应用运行在隔离沙箱 |
| 外部资源审批 | 高危操作走带审批的关卡 |
| 全员自助 | 非工程师也能使唤 agent |
| 安全合规 | 满足 SOC2 / ISO 等审计要求 |
| 边缘运行 | 跑在 Cloudflare 全球边缘 |

## 参考链接

- 项目链接：<https://github.com/cloudflare/cloudflare-os>

## 相关概念

- [Cloudflare Workers](./term-cloudflare-workers.md) — 底层运行时
- [Sandbox（沙箱）](./term-sandbox.md) — 同属沙箱形态
- [AI Coding Agent](./term-ai-coding-agent.md) — 主要消费者
