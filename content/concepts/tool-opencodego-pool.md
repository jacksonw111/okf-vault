---
type: Tool
title: "OpenCodeGo_Pool"
description: "管理多个 opencode 账号的配额与用量，把有效账号的 API Key 自动同步到 CLIProxyAPI，实现多账号负载均衡。"
resource: "https://github.com/xnqycs/OpenCodeGo_Pool"
tags: [opencode, quota, load-balancing, cli-proxy-api, ai-coding]
timestamp: "2026-08-25T19:30:00Z"
---

# OpenCodeGo_Pool

## 它是什么

[xnqycs/OpenCodeGo_Pool](https://github.com/xnqycs/OpenCodeGo_Pool) 是给 [opencode](https://github.com/opencode-ai/opencode) 多账号场景做配额管理与负载均衡的小工具。它做两件事：

1. **配额 / 用量监控**：跟踪每个 opencode 账号的剩余额度和当日用量。
2. **API Key 同步**：把仍然有效的账号 Key 自动同步到 CLIProxyAPI，CLIProxyAPI 据此在多账号之间做请求分发 / 负载均衡。

## 为什么用它 / 适合什么场景

- **多账号轮询防单号限流**：opencode 通常对单账号有日 / 周配额，账号多了手动切换 Key 既繁琐又容易踩坑。
- **失效 Key 自动剔除**：账号到期或被风控后，由池子主动剔除，不再被路由。
- **CLIProxyAPI 协作**：与 CLIProxyAPI 配套使用，CLIProxyAPI 负责「发请求」，本工具负责「喂 Key」，各管一段。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多账号注册 / 入池 | 把一批 opencode 账号统一加入池子 |
| 配额采集 | 周期性拉取每个账号的剩余额度与当日用量 |
| 失效检测 | 对过期 / 风控 / 无额度账号自动剔除 |
| Key 同步 | 把健康账号的 API Key 写入 CLIProxyAPI 配置 |
| 负载分发 | 由 CLIProxyAPI 在多 Key 间做加权分发 |

## 相关概念

- [Claude Code](./tool-claude-code.md) — 同样依赖多账号 / 多 Key 平衡的 AI 编码代理，本工具生态以 opencode 为中心

## 参考链接

- 项目链接: <https://github.com/xnqycs/OpenCodeGo_Pool>