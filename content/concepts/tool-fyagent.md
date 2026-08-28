---
type: Tool
title: "FyAgent（多 AI 编码代理统一配置管理器）"
description: "本地桌面应用，把 Claude Code / Codex / Gemini CLI 等多个 AI 编码代理的模型 Key / MCP / 提示词等配置收进一处，改一处同步到所有支持的 AI 工具。"
resource: "https://github.com/fy-agent/fyagent"
tags: [agent-config, claude-code, codex, gemini-cli, mcp, desktop]
timestamp: "2026-08-27T00:35:00Z"
---

# FyAgent

## 它是什么
[fy-agent/fyagent](https://github.com/fy-agent/fyagent) 是一个**本地桌面应用**，用来统一管理 Claude Code、Codex、Gemini CLI 等多个 AI 编码代理的：

- **模型 API Key**（不同 provider 各一套）；
- **MCP 服务器配置**；
- **提示词 / 系统指令**。

平时这些配置散落在各家代理自己的配置目录里，改一处需要去 N 个地方同步。FyAgent 把它们收进**一个本地桌面应用**，**改一处即可同步到所有支持的 AI 工具**。

## 为什么用它 / 适合什么场景
- 同时使用 Claude Code + Codex + Gemini CLI，每次换 Key / 加 MCP / 改 system prompt 都要去 N 个配置文件改；
- 团队内 Key 轮换 / MCP 升级频繁，需要统一管理；
- 想给个人 / 小团队一个"AI 编码代理控制台"，避免每个代理各自一套心智模型。

## 关键能力
| 能力 | 说明 |
|------|------|
| 统一 Key 管理 | 多 provider Key 集中存放 |
| 统一 MCP | 一处配置，同步到各代理 |
| 统一提示词 | system prompt / 项目级 prompt 集中编辑 |
| 自动同步 | 改一处 → 推到所有支持的代理 |
| 本地优先 | 配置存本地，不上云 |
| 桌面 GUI | 不必手改 JSON / TOML |

## 相关概念
- [Multi-AI-Coding-Config-Panel](tool-multi-ai-coding-config-panel.md) — 3641397194-wq 的同类工具：把 Codex / Claude Code / Grok / DeepSeek 等本地 AI 编码代理的部署 / 校验 / 快照 / 恢复收进一个面板
- [api-balance-checker-extension](tool-api-balance-checker-extension.md) — 给 Chrome/Edge 写的多 AI 中转站余额聚合，与 FyAgent 同属「多 AI 工具栈统一管理」思路

## 参考链接
- 项目链接：<https://github.com/fy-agent/fyagent>
