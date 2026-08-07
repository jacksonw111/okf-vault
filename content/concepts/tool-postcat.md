---
type: "Tool"
title: "Postcat"
description: "终端里调试 HTTP 请求的 TUI 工具：用 Rust + ratatui 写的键盘操作界面，覆盖方法 / URL / 查询参数 / 请求头 / 三种请求体（JSON / text / form），支持 Bearer / Basic 认证，JSON 响应按原键顺序着色，SSE / 分块响应实时绘制可滚动暂停。"
resource: "https://github.com/egoist/postcat"
tags: [http-client, terminal-ui, rust, tui, ratatui, developer-tools]
timestamp: "2026-08-07T10:47:00Z"
---

# Postcat

## 它是什么

Postcat 是一个跑在终端里的 HTTP 请求调试 TUI，用 Rust + ratatui 写成，偏键盘操作。它把「编辑请求 → 发送 → 看响应」全流程塞进终端界面，一条命令就能把请求跑下来，省去切到桌面应用（Postman / Insomnia / Bruno 等）的来回切换。

## 为什么用它 / 适合什么场景

- 习惯在终端里干活，不想为单个 HTTP 请求额外启动桌面客户端。
- 在 SSH 远程机器上调试后端 API，只能用命令行。
- 想要一款轻量、键盘驱动、跨平台（macOS / Linux / Windows）的 HTTP 客户端。
- 想处理 SSE（Server-Sent Events）或分块响应，希望边发边看流式数据。

## 关键能力

| 能力 | 说明 |
|------|------|
| 方法 / URL / 查询参数 / 请求头 | 完整覆盖 HTTP 请求的常见字段 |
| 三种请求体 | JSON、text、form 一并支持 |
| Bearer / Basic 认证 | 内置常见认证方案 |
| JSON 响应着色 | 按原始键顺序上色，便于肉眼定位 |
| 状态 / 耗时 / 大小 | 响应状态码、请求耗时、响应体大小一目了然 |
| SSE / 分块响应 | 实时绘制流式数据，可滚到底部暂停、Esc 停掉 |
| 键盘优先操作 | 偏键盘流，鼠标不可用也能用 |
| 跨平台 | macOS / Linux / Windows 都可装 |
| Rust + ratatui 实现 | 体积小、启动快、占用低 |

## 媒体

- ![Postcat 终端界面截图](https://pbs.twimg.com/media/HPAcQTGacAAZ-lF.jpg)

## 相关概念

- [HTTPie](./tool-httpie.md) — 同样是终端 HTTP 调试工具，但走 CLI 而非 TUI
- [Bruno](./tool-bruno.md) — 同为本地优先 HTTP 客户端，但走桌面 / 文件存储
- [Terminal Browser](./tool-terminal-browser.md) — 把图形界面塞进终端的同类思路，可作为本工具的设计参照