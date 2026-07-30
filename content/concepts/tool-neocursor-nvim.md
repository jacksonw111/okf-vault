---
type: Tool
title: "neocursor.nvim（Neovim 插件读 Cursor 私有 API 拿补全）"
description: "Neovim 插件，读本地 Cursor 的登录信息，直接连 Cursor 的私有 API 拿补全结果。支持多行 ghost text、差异改写、Tab 跳转。不需要 API Key 或额外注册，前提是装了 Cursor Desktop 并登录过。"
resource: "https://github.com/teocns/neocursor.nvim"
tags: [neovim, cursor, ai-coding, completion, plugin, ghost-text]
timestamp: "2026-07-30T06:41:00.000Z"
---

# neocursor.nvim

## 它是什么

**Neovim 插件，借 Cursor 的私有 API 实现 AI 补全**—— Cursor 的 AI Tab 体验被很多 Neovim 重度用户羡慕，但又不舍得放弃 Neovim。

neocursor.nvim 解决方案：

- 读你本机 Cursor 的登录凭据（无需新注册）
- 直接连 Cursor 的私有 API
- 在 Neovim 里实现 ghost text、差异改写、Tab 跳转
- 通过 Python sidecar + uv 管理依赖，不污染系统 Python

![效果截图](https://pbs.twimg.com/media/HOXZZAAbIAAlZWR.jpg)

## 关键能力

| 能力 | 说明 |
|------|------|
| 多行 ghost text | 跟在 Cursor Tab 后面 |
| 差异改写 | diff 风格替换 |
| Tab 跳转 | 连续 Tab 跳到下一处 |
| 免 API Key | 复用 Cursor 登录态 |
| 跨平台 | macOS / Linux / Windows |
| 依赖隔离 | uv 管理 Python sidecar |

## 前提与风险

- ⚠️ 必须装 Cursor Desktop 并登录过
- ⚠️ 走私有 API，Cursor 改协议可能挂掉
- ✅ 不上传代码（本地代理）

## 适合谁

- Neovim 重度用户想体验 Cursor Tab 的流畅
- 同时装两个编辑器的人
- 想节省 Cursor 单独订阅费（只装 Desktop，不买 Code 编辑器订阅）

## 原始链接

- [项目仓库](https://github.com/teocns/neocursor.nvim)
- [推文剪藏](https://x.com/QingQ77/status/2082718081420329334)

## 相关概念

- [openclaude-improved](./tool-openclaude-improved.md) — 多 AI 后端 CLI 编程代理
- [Nyx Local AI](./tool-nyx-local-ai.md) — VS Code / Cursor 本地 AI 编码插件