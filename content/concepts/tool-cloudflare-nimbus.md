---
type: "Tool"
title: "Cloudflare Nimbus（Cloudflare 出品：双读者文档站框架）"
description: "Cloudflare 官方开源的文档站生成框架：处于 0.x 阶段，明确信号是「文档站以后要写给两种读者——人和 Agent」。"
resource: "https://github.com/cloudflare/nimbus"
tags: "[cloudflare, documentation, agent, llm-readable, doc-site, framework]"
timestamp: "2026-09-28T23:45:00Z"
---

# Cloudflare Nimbus（Cloudflare 出品：双读者文档站框架）

## 它是什么

[Nimbus](https://github.com/cloudflare/nimbus) 是 **Cloudflare** 官方开源的**文档站生成框架**。目前仍处于 **0.x** 版本，官方自己说小版本之间接口都可能变，建议**锁版本**。

最值得关注的产品定位是：「**文档站以后要写给两种读者——人和 Agent**」。文档同时为人类阅读与 LLM Agent 消费而设计。

## 为什么用它 / 适合什么场景

- 想建一个**对 LLM Agent 友好的文档站**（比如 MCP `llms.txt`、机器可读元数据、结构化内容块）。
- 偏好 Cloudflare 官方维护、长期会持续迭代的方案。
- 项目对**接口稳定性**要求高——能接受锁版本与早期 API 变更。
- 想为开源项目做「**面向 Agent 的文档**」基础设施。

## 关键能力

| 能力 | 说明 |
|------|------|
| 出品 | Cloudflare |
| 形态 | 文档站生成框架 |
| 版本 | 0.x（接口可能变化，建议锁版本） |
| 核心定位 | 同时服务人类读者 + LLM Agent |
| 与 Agent 友好 | 输出结构化内容，方便 Agent 消费 |

## 相关概念

- [Cloudflare Kumo](./tool-kumo.md) — Cloudflare 官方开源的 UI 组件库与文档框架（同源生态）