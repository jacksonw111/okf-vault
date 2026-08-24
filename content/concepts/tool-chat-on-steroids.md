---
type: Tool
title: "chat-on-steroids"
description: "本地 MCP 服务器 + 浏览器扩展：让网页版 ChatGPT 在用户批准范围内操控 Windows 桌面的文件、命令与 GUI。"
resource: "https://github.com/totec448-spec/chat-on-steroids"
tags: [chatgpt, mcp, windows, desktop-automation, browser-extension]
timestamp: "2026-08-24T06:35:00Z"
---

# chat-on-steroids

## 它是什么

[totec448-spec/chat-on-steroids](https://github.com/totec448-spec/chat-on-steroids) 是一套把网页版 ChatGPT 接入本地电脑的桥接方案：浏览器侧扩展 + 本地 MCP（Model Context Protocol）服务器，让 ChatGPT 能在用户明确批准的范围内直接操控 Windows 桌面——读 / 写文件、执行命令、操作 GUI。

## 为什么用它 / 适合什么场景

- 想用 ChatGPT 网页端（不想买 API）作为桌面 Agent 的入口。
- 希望每次操作都经过用户显式授权（不是无脑执行所有命令）。
- 想让 ChatGPT 能干 Claude Code / Codex 类似的活：操作本地文件 + 运行命令。

## 关键能力

| 能力 | 说明 |
|------|------|
| 本地 MCP 服务器 | ChatGPT 通过 MCP 协议调用本机资源 |
| 浏览器扩展 | 在 ChatGPT 网页侧暴露「桌面工具」按钮与对话侧栏 |
| 显式授权 | 每次高风险操作（写文件 / 删文件 / 执行命令）需用户确认 |
| 文件系统操作 | 读、写、列出、搜索本地文件 |
| Shell 命令执行 | 受限 shell，命令可审计 |
| GUI 操作（可选） | 通过 Windows UI Automation 操控应用窗口 |

## 相关概念

- [Harness Router](./tool-harness-router.md) — 同类统一多 harness 入口
- [Codex Bridge](./tool-codex-bridge.md) — 类似「让 Claude 借 Codex 凭据」的桥接思路

## 参考链接

- [项目链接](https://github.com/totec448-spec/chat-on-steroids)
- ![](https://pbs.twimg.com/media/HQc25qPaYAARPwj.jpg)