---
type: "Tool"
title: "second-brain-cloudflare（Cloudflare 上的开源共享记忆层）"
description: "部署在 Cloudflare Workers 上的开源记忆层，让 Claude、ChatGPT、Cursor、Codex 等多个 AI 客户端通过 MCP 协议共享同一个长期记忆；记忆数据存在用户自己的 Cloudflare 账户（D1 / Vectorize / KV / Workers AI），强调语义检索。"
tags: "[mcp, memory, cloudflare, ai-agent, vectorize, shared-brain]"
timestamp: "2026-06-28T14:12:00Z"
resource: "https://github.com/rahilp/second-brain-cloudflare"
---

# second-brain-cloudflare（Cloudflare 上的开源共享记忆层）

## 它是什么

second-brain-cloudflare 是一个**部署在 Cloudflare Workers 上的开源「共享大脑」**，让多个 AI 客户端（Claude、ChatGPT、Cursor、Codex 等）通过 **MCP 协议**共享同一份长期记忆。记忆数据存在**用户自己的 Cloudflare 账户**（D1 / Vectorize / KV / Workers AI），不在第三方服务器上。

定位类似 [EverOS](tool-everos.md) 与 [Brigade](tool-brigade.md) 的 Tideline，但走**云端 + 单一权威源**路线。

## 关键能力

| 能力 | 说明 |
|------|------|
| Cloudflare Workers 部署 | 部署成本极低，个人规模可在免费额度内 |
| MCP 协议对外 | Claude / Cursor / Codex 等 MCP 客户端均可直连 |
| 数据归用户 | 记忆存用户自己的 D1 / Vectorize / KV / Workers AI |
| 语义检索 | 走 Workers AI 做向量检索，非字面匹配 |
| 多客户端共享 | 一次记忆，跨 Claude / ChatGPT / Cursor / Codex 通用 |
| 开源 | 完整代码可自部署可改 |

## 架构

```
AI Client (Claude / Codex / Cursor)
    │
    └─ MCP protocol
         │
         └─ Cloudflare Worker
              ├── D1 (结构化事实)
              ├── KV (键值缓存)
              ├── Vectorize (语义检索索引)
              └── Workers AI (嵌入模型推理)
```

## 与同类对比

- vs [EverOS](tool-everos.md) — EverOS 偏本地长期记忆层，second-brain-cloudflare 偏云端 + 用户自有账户
- vs [Brigade](tool-brigade.md) — Brigade 自研 Tideline 协议，second-brain-cloudflare 用 MCP 标准协议
- vs [Recall](tool-recall-claude-code.md) — Recall 是 Claude Code 离线本地记忆插件；second-brain-cloudflare 是云端跨客户端共享

## 部署

```bash
git clone https://github.com/rahilp/second-brain-cloudflare
wrangler deploy
# 把生成的 Worker URL 配到各 AI 客户端的 MCP 设置
```

## 参考链接

- [项目仓库](https://github.com/rahilp/second-brain-cloudflare)
- [原始链接](https://x.com/Wen_Zw/status/2071235175350964439)

## 相关概念

- [EverOS](tool-everos.md) — 本地长期记忆层，让不同 agent 共享并进化记忆
- [Brigade](tool-brigade.md) — 本地多 AI 代理协作框架 + Tideline 共享长期记忆
- [Recall](tool-recall-claude-code.md) — Claude Code 离线持久化项目记忆插件
- [EchoesVault（OpenCode 持久记忆）](tool-echoes-vault-opencode.md) — OpenCode 插件，会话结束自动记决策
- [Codex Control Plane MCP](tool-codex-control-plane-mcp.md) — 同样基于 MCP 的 Codex 持久化任务队列