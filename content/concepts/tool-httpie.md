---
type: "Tool"
title: "HTTPie"
description: "命令行 HTTP 客户端：比 curl 人类友好的替代品，语法直观、支持彩色输出、JSON 高亮、会话保持、文件上传。"
resource: "https://httpie.org/"
tags: [http-client, cli, developer-tools, json]
timestamp: "2026-08-08T20:00:00Z"
---

# HTTPie

## 它是什么

HTTPie 是一款命令行 HTTP 客户端，被誉为「curl 的现代友好替代品」。它的设计目标是「让 API 在终端里像对话一样自然」，提供彩色输出、JSON 高亮、会话保持、文件上传、表单提交等开箱即用能力。

## 为什么用它 / 适合什么场景

- 平时用 curl 调试 API 觉得语法难记。
- 喜欢结构化、彩色化的终端输出。
- 需要保存常用请求为命名端点（类似 Postman）。
- 在本地 / 远程 / CI 各种环境都用同一套命令。

## 关键能力

| 能力 | 说明 |
|------|------|
| 友好语法 | `http GET example.com` 直观可读 |
| 彩色输出 | 终端彩色 JSON / 表头 / 响应体 |
| JSON 高亮 | 自动识别 JSON 并按 key 上色 |
| 会话保持 | `--session` 保存登录态、cookie |
| 文件上传 | 一行命令上传文件、表单 |
| Web / 桌面 UI | httpie.io 提供 GUI 版 |

## 相关概念

- [Postcat](./tool-postcat.md) — 终端 HTTP 调试 TUI（Rust + ratatui），键盘驱动
- [Bruno](./tool-bruno.md) — 同为本地优先 HTTP 客户端，但走桌面 / 文件存储