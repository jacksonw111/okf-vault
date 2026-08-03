---
type: Tool
title: "Chartr"
description: "Go + Svelte 写的 agent 多路复用器，侧边栏管项目，标签页跑各种 agent CLI；规划 agent 把 .plan/maps/ 落盘的 Markdown 渲染成星图，从图的前沿取无阻塞 ticket 自动派发到会话。"
resource: "https://github.com/rengwu/chartr"
tags: [agent, multiplexer, go, svelte, planning, ticket, star-map]
timestamp: "2026-08-03T09:47:00Z"
---

# Chartr

## 它是什么
Chartr（`rengwu/chartr`）是一个 Go + Svelte 写的 agent 多路复用器。**侧边栏管项目，标签页跑各种 agent CLI**，不用来回切窗口——多个 agent 会话（Claude Code / Codex / OpenCode / Kimi / Grok / Pi）共享同一个 UI 容器。

主要玩法是「地图」：规划 agent 往 `.plan/maps/` 里写的 Markdown 一落盘就渲染成星图，从图的前沿取一张没被阻塞的 ticket，选好角色和 agent，会话会自动带上地图、ticket 和前置问题的答案。任何在 `PATH` 上的 CLI 都能注册，开箱即识别 claude、codex、opencode、kimi、grok、pi。

![Chartr 星图 + 标签页](https://pbs.twimg.com/media/HOsrGx8a0AARxp4.jpg)

## 为什么用它 / 适合什么场景
- **多 agent 并行 ≠ 多个窗口**：一个 UI 管多个 agent 项目，会话、项目、地图、ticket 四个层级一目了然。
- **规划即图**：把 `.plan/maps/*.md` 自动渲染为可点击星图，DRY 化「规划文档 ↔ 任务派发」流程。
- **零接入门槛**：不绑定特定 agent CLI；只要在 PATH 里能找到的 CLI 都能注册。
- **角色 × agent 解耦**：每个 ticket 单独选角色（前端 / 后端 / 校验 / 文档）和所用的 agent CLI。

## 关键能力

| 能力 | 说明 |
|------|------|
| 项目侧边栏 | 左侧栏聚合所有项目，每个项目有自己的 .plan/maps |
| 标签页会话 | 多 agent CLI 并行运行，按标签页切换 |
| Markdown 星图 | 规划 Markdown 自动渲染成可点星图 |
| Ticket 派发 | 从图的前沿取无阻塞 ticket，自动带入上下文 |
| CLI 自动注册 | PATH 内任意 agent CLI 自动识别 |

## 项目链接
- <https://github.com/rengwu/chartr>

## 相关概念
- [agent-manager (tmux)](./tool-agent-manager-tmux.md) — TUI 架在 tmux 上统一管 Claude Code / Codex / OpenCode / Grok Build
- [session-manager (Tauri v2)](./tool-session-manager-tauri.md) — Tauri v2 + React + Rust 桌面应用，三栏浏览 AI 编程助手历史会话
- [opencode-fusion](./tool-opencode-fusion.md) — OpenCode 多模型协作，主代理只规划 / 审查，副手改代码
- [Pi Extensible Workflows](./tool-pi-extensible-workflows.md) — Pi 终端 AI 助手的确定性多代理工作流编排，支持并行 / 审批 / 断点恢复
