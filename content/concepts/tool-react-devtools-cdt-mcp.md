---
type: "Tool"
title: "react-devtools-cdt-mcp（React 团队实验中的 runtime Agent 工具）"
description: "React 团队实验中的工具：让 Chrome DevTools MCP 发现 / 注册 / 暴露 React 相关 devtools；并非真 MCP，让 agent 在运行时理解应用。"
resource: "https://github.com/sebastienlorber/react-devtools-cdt-mcp"
tags: "[react, devtools, mcp, ai-agent, debugging]"
timestamp: "2026-09-11T22:10:00Z"
---

# react-devtools-cdt-mcp

## 它是什么

[react-devtools-cdt-mcp](https://github.com/sebastienlorber/react-devtools-cdt-mcp) 是 **React 团队实验中的新工具**：

| 维度 | 说明 |
|------|------|
| 不是 MCP | 「This is not an MCP」——它不是 Model Context Protocol |
| 干什么 | 让 **Chrome DevTools MCP** 能发现 / 注册 / 暴露 React 相关 devtools |
| 目的 | 让 agent 在 runtime 理解 React 应用 |

## 为什么用它 / 适合什么场景

- AI agent 想 debug React 应用，需要 runtime 上下文（组件树 / props / state）。
- Chrome DevTools MCP 用户想接入 React 生态。
- 研究「**agent 理解运行时应用**」的方向。

## 关键能力

| 能力 | 说明 |
|------|------|
| CDP 发现 | 通过 Chrome DevTools Protocol 发现 React 实例 |
| Devtools 暴露 | 组件树 / props / state 暴露给 agent |
| 即将发布 | pkg 准备首次 npm 发布 |
| React 官方实验 | 官方推动 |

## 参考链接

- 项目仓库：<https://github.com/sebastienlorber/react-devtools-cdt-mcp>

## 媒体

- ![](https://pbs.twimg.com/media/HRyE0DyWYAIfRBp.jpg)

## 相关概念

- [Vercel Agent Browser](./tool-vercel-agent-browser.md) — AI agent 模拟浏览器行为
- [Browser Use Pi](./tool-browser-use-pi.md) — Browser-Use 团队轻量 Web Agent
</content>
</invoke>