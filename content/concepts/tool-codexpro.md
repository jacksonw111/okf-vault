---
type: "Tool"
title: "CodexPro（ChatGPT Web ↔ 本地仓库 MCP 桥）"
description: "通过 MCP 协议在 ChatGPT Developer Mode 与本地仓库之间搭桥：全局安装后 codexpro setup 自动配 MCP Server 与隧道（Cloudflare / ngrok），把生成的地址贴到 ChatGPT Create App，ChatGPT 即可直接读写本地文件、搜代码、跑安全命令。"
resource: "https://github.com/qingq77/codexpro"
tags: "[mcp, chatgpt, dev-mode, tunnel, bridge]"
timestamp: "2026-06-21T00:00:00Z"
---

# CodexPro（ChatGPT Web ↔ 本地仓库 MCP 桥）

## 它是什么

由 `@QingQ77` 在 2026-06 推荐的 MCP 桥接工具：在 **ChatGPT Developer Mode**（网页版）和 **本地代码仓库** 之间搭一座桥。安装后 `codexpro setup` 自动配好 MCP Server 和公网隧道，ChatGPT 就能像 Codex CLI 一样直接动你的本地文件。

## 工作流

1. 全局安装：`npm i -g codexpro`
2. 运行 `codexpro setup`：自动配 MCP Server + 隧道（Cloudflare 或 ngrok 二选一）。
3. 把生成的公网地址贴到 ChatGPT 的「Create App」里。
4. ChatGPT 即可：读 / 写本地文件、搜代码、跑安全命令。

## 与 DevSpace 的差异

| 维度 | CodexPro | DevSpace |
|------|----------|----------|
| 接入方式 | ChatGPT Developer Mode | ChatGPT MCP 客户端（更通用） |
| 隧道 | 内置 Cloudflare / ngrok | 自托管 |
| 命令 | `codexpro setup` 全自动 | 手工配 MCP |

## 适用场景

- 不想装 Codex CLI，但想让网页版 ChatGPT 帮我改本地仓库。
- 在远程机器上写代码，想把隧道配自动化。
- 已经在用 ChatGPT Developer Mode 加自定义 App 的开发者。

## 相关概念

- [DevSpace](tool-devspace-mcp.md) — 同样做 ChatGPT ↔ 本地仓库 MCP 桥，自托管路线
- [ngrok / webernetes](tool-ngrok-webernetes.md) — CodexPro 内置的隧道选项之一
- [Codex Control Plane MCP](tool-codex-control-plane-mcp.md) — Codex Desktop 端的队列 MCP