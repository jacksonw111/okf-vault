---
type: Tool
title: "gmail-mcp"
description: "把 Gmail 接到 Claude 等 MCP 客户端的 MCP Server：让 AI 助手能搜索、读取、发送和转发邮件，支持一个部署绑定多个 Google 账号，全程运行在你自己的 Cloudflare Worker 上。"
resource: "https://github.com/mkpoli/gmail-mcp"
tags: [mcp, gmail, cloudflare-workers, email, google-account, self-hosted]
timestamp: 2026-08-06T08:30:00Z
---

# gmail-mcp

## 它是什么

mkpoli 开源的 MCP（Model Context Protocol）Server，把 Gmail 邮箱能力通过标准 MCP 接口暴露给 Claude 等 MCP 客户端。

## 为什么用它 / 适合什么场景

- 想让 Claude / 其他 agent 直接读 / 发 / 转发邮件，又不想把 Gmail 凭据交给第三方中转。
- 一个人管多个 Google 账号，需要一个部署同时绑定多账号按需切换。
- 想把 MCP Server 部署到 Cloudflare Worker 上，免维护服务器、低延迟。

## 关键能力

| 能力 | 说明 |
|------|------|
| Gmail 读 / 发 / 转 | 搜索、读取、发送、转发邮件 |
| 多账号绑定 | 一个部署支持多个 Google 账号 |
| 自托管 | 部署到自己的 Cloudflare Worker 上，邮件数据完全可控 |
| MCP 协议 | 标准 Model Context Protocol，Claude Desktop / 其他 MCP 客户端开箱即用 |

## 相关概念
- [12306 MCP](./tool-12306-mcp.md) — 12306 余票 / 订单 MCP 工具集
- [Comail](./tool-comail.md) — Tauri 2 键盘流桌面邮件客户端