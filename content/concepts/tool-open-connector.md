---
type: Tool
title: "Open Connector（开源 AI Agent 连接器网关）"
description: "开源的 AI agent 连接器网关（Composio 替代品），一次连接 1000+ SaaS provider、9400+ 预构建 Action，凭证留在运行时边界内，通过 SDK/CLI/MCP/HTTP/OpenAPI 暴露给 agent，可本地 / Cloudflare Workers / 托管部署。"
resource: "https://github.com/oomol-lab/open-connector"
tags: "[agent, integration, mcp, saas, composio-alternative, openapi, sdk]"
timestamp: "2026-07-09T20:50:00Z"
---

# Open Connector（开源 AI Agent 连接器网关）

## 它是什么
`oomol-lab/open-connector` 是 **Composio 的开源替代品**——一个 AI agent 连接器网关：

- **规模**：一次接入 1 000+ SaaS provider，9 400+ 预构建 Action
- **凭证安全**：凭证留在**运行时边界内**，不外泄到各家 SaaS 后端
- **暴露面**：通过 SDK / CLI / MCP / HTTP / OpenAPI 同一份数据
- **部署**：本地 / Cloudflare Workers / 托管三种模式

## 为什么用它 / 适合什么场景
- 想给 agent 一次接入大量 SaaS 操作（Slack / GitHub / Notion / Gmail / Sheets …）但**不想被 Composio 锁定价**或卡审计。
- 想让 SaaS 凭证**只留在自己机器**里。
- 想用 **MCP 协议**对接主流 agent 框架（Claude Code / Codex / Cursor）。
- 适合：希望 SaaS 接入"可观测 + 可控 + 可自托管"的团队 / 个人。

## 关键能力
| 能力 | 说明 |
|------|------|
| 1 000+ SaaS provider | 覆盖主流 / 长尾 SaaS |
| 9 400+ Action | 预构建的操作 |
| 凭证自管 | 留在运行时边界 |
| 多协议暴露 | SDK / CLI / MCP / HTTP / OpenAPI |
| 多部署形态 | 本地 / Cloudflare Workers / 托管 |
| 开源 | 社区维护 |

## 媒体参考

产品截图：
- ![](https://pbs.twimg.com/media/HMrKDBFboAAmPuk.jpg)

## 相关概念
- [integrations.sh](tool-integrations-sh.md) — 开源第三方集成目录
- [Open Knowledge（Inkeep）](tool-open-knowledge.md) — WYSIWYG Markdown 编辑器 + LLM 知识库，AI 可直接读写文档
- [OpenWiki](tool-openwiki.md) — LangChain 团队的 CLI，自动写入 AGENTS.md / CLAUDE.md 提示词

## 参考链接
- 项目链接：<https://github.com/oomol-lab/open-connector>
