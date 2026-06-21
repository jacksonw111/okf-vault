---
type: "Tool"
title: "Proxide（任意 Agent 接 ChatGPT Pro 网页强模型）"
description: "Proxide = 让任意 Agent（不必是 Codex / Claude Code）通过 MCP 或浏览器把本地项目上下文喂给 ChatGPT Pro 这类网页端强模型：MCP 模式用 Rust 写的服务器让 ChatGPT Pro 直接读项目；Bridge 模式把上下文审查后通过浏览器手动塞给网页模型。两路都不挑 Agent，只要它能跑命令 / 调 MCP / 会操作浏览器就行。"
resource: "https://t.co/FgFwzuonnz"
tags: "[agent, chatgpt, mcp, rust, bridge, web-model]"
timestamp: "2026-06-21T16:13:00Z"
---

# Proxide（任意 Agent 接 ChatGPT Pro 网页强模型）

## 它是什么

**Proxide**：一个让**任意 Agent 都能用 ChatGPT Pro** 这类网页强模型的桥接器。**不挑 Agent** —— 只要它能跑命令、调 MCP 或会操作浏览器就行，两条路：

1. **MCP 模式**：Rust 写的服务器，让 ChatGPT Pro（通过 MCP 客户端）直接读本地项目。
2. **Bridge 模式**：把上下文审查后通过浏览器手动塞给网页模型（适合 ChatGPT 网页版不能直接接 MCP 的场景）。

## 为什么用它 / 适合什么场景

- 你用的 Agent 不是 Codex / Claude Code，但又想把本地项目交给 ChatGPT Pro 这种网页强模型。
- 想用 ChatGPT Pro（GPT-5 / o-series）的能力，但不想订阅 + 配置一整套官方 API + 客户端。
- 在网页模型 vs 本地模型之间切换：网页模型强在推理，Proxide 让本地 Agent 能直接调它。

## 关键能力

| 模式 | 说明 |
|------|------|
| MCP 模式 | Rust 服务器，提供 MCP 接口给 ChatGPT Pro（需 ChatGPT 客户端支持 MCP） |
| Bridge 模式 | 把项目上下文打包 → 浏览器手动贴入网页版 ChatGPT；适合官方网页不能直接接 MCP 的场景 |
| 上下文审查 | Bridge 模式下可对要发出去的上下文做审查（避免敏感信息泄露） |
| Agent 无关 | 不绑定 Codex / Claude Code / Cursor；任何能跑命令 / 调 MCP / 操作浏览器的 Agent 都能用 |

## 适用边界

- Bridge 模式依赖人工介入（手动复制粘贴 / 浏览器操作），不算全自动。
- MCP 模式需要 ChatGPT 客户端支持 MCP 接入。

## 媒体

- 截图：![](https://pbs.twimg.com/media/HLTOUp5bQAApTWP.jpg)

## 相关概念

- [CodexPro](tool-codexpro.md) — 同为「Agent ↔ 网页强模型」桥接，但定位在 ChatGPT Web ↔ 本地仓库 MCP
- [Codex Control Plane MCP](tool-codex-control-plane-mcp.md) — 同为 Codex Desktop 周边工具，但定位在持久化任务队列
- [DevSpace](tool-devspace-mcp.md) — 同为「让 ChatGPT 变 Codex CLI」类的桥接器