---
type: "Tool"
title: "Codex-X（OpenAI Codex 桌面端的一站式管理器）"
description: "为 OpenAI Codex 桌面端提供提示词注入、Provider 切换和配置可视化管理的一站式桌面工具；Tauri 2 跨平台，内置 gpt5.4-unrestricted / gpt5.5-unrestricted 指令模板可一键启用。"
tags: "[codex, openai, desktop, tauri, prompt, manager]"
timestamp: "2026-07-06T13:12:00.000Z"
resource: "https://github.com/yynxxxxx/Codex-X"
---

# Codex-X（OpenAI Codex 桌面端的一站式管理器）

## 它是什么

[`Codex-X`](https://github.com/yynxxxxx/Codex-X) 是一个基于 **Tauri 2** 的跨平台桌面管理器，专为 OpenAI Codex CLI / 桌面端设计。它解决「Codex 命令行配置散落各处、切换 Provider 要手动改文件、提示词注入只能复制粘贴」这几个痛点，提供统一的 GUI 面板。

## 关键能力

| 能力 | 说明 |
|------|------|
| 提示词注入 | 内置 `gpt5.4-unrestricted` / `gpt5.5-unrestricted` 两套指令模板，一键启用/禁用 |
| Provider 切换 | 可视化切换不同 API 端点，免手动改配置 |
| 配置管理 | GUI 管理所有 Codex 相关配置（模型、API Key、行为参数） |
| 跨平台 | 基于 Tauri 2，macOS / Windows / Linux 一份代码 |

![Codex-X 配置面板](https://pbs.twimg.com/media/HMgbjiEbcAELdLU.jpg)

## 适用场景

- 用 Codex CLI 写代码但懒得手动改 yaml/toml 切 Provider
- 想尝试不同的「解限」指令模板比较效果
- 团队要给非技术成员配 Codex 环境，GUI 比命令行友好得多

## 注意事项

工具内置的 `unrestricted` 模板会让模型行为偏离默认安全策略，使用者需自行判断合规性与风险。

## 参考链接

- [项目链接](https://github.com/yynxxxxx/Codex-X)

## 相关概念

- [CodexPro](tool-codexpro.md) — ChatGPT Web ↔ 本地仓库的 MCP 桥
- [Codex Control Plane MCP](tool-codex-control-plane-mcp.md) — Codex Desktop 的持久化任务队列 MCP