---
type: "Tool"
title: "sharedoc-mcp（AugustusW/sharedoc-mcp）"
description: "AI 智能体生成的 Markdown 内容（报告 / 摘要 / 笔记）不必再一段段复制进聊天窗口，直接变成一个链接发给任何人。"
resource: "https://github.com/AugustusW/sharedoc-mcp"
tags: "[markdown, sharing, mcp, ai-agent, link-publishing, agent-tools]"
timestamp: "2026-07-31T20:30:00Z"
---

# sharedoc-mcp（AugustusW/sharedoc-mcp）

[sharedoc-mcp](https://github.com/AugustusW/sharedoc-mcp) 是一个 **MCP 工具**：让 AI 智能体生成的 Markdown 内容（报告、摘要、笔记）**直接变成一个可分享的链接**，发给任何人——不用一段段复制粘贴到聊天窗口，也不用来回切换应用。

## 它是什么

- 以 **MCP 服务器**形式接入 agent
- agent 调用一个工具，即把 Markdown 文本转为 URL
- 任何人点链接就能看完整 Markdown 渲染效果

## 为什么用它 / 适合什么场景

| 痛点 | sharedoc-mcp 怎么解 |
|------|----------------------|
| 长 Markdown 在 IM 里格式崩 | 给一个链接，对方浏览器里看 |
| 多人传报告互相复制很容易丢版本 | 链接唯一，对应一份 Markdown |
| 截图分享排版抖动 | 链接渲染稳定 |
| 想给非技术同事 / 客户一份结构化内容 | Markdown 网页更易读 |

## 关键能力

| 能力 | 说明 |
|------|------|
| MCP 服务 | 与 Claude Code / Cursor 等 agent 即插即用 |
| Markdown 转 URL | 一行 agent 输出即得链接 |
| 渲染稳定 | 浏览器里看，不受 IM 限制 |
| 可分享 | 任何人都能打开 |

## 相关概念

- [article-tools](./tool-article-tools.md) — 纯前端 HTML 工具集（封面 / 二维码 / MD 转微信公众号等），与 sharedoc-mcp 同属「Markdown 处理流水线」
- [Clarify](./tool-clarify.md) — 本地优先 CLI + AI 可读 llms.txt 的发布工具，与 sharedoc-mcp 形成「自托管 vs 即时分享」
- [OpenBrowser](./tool-openbrowser.md) — 浏览器自动化，可与 sharedoc-mcp 组合自动分享
- [Agent Skills（代理技能包）](./term-agent-skills.md) — sharedoc-mcp 本身就是一个典型的 agent skill（via MCP）
