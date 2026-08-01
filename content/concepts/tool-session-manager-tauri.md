---
type: Tool
title: "session-manager (Tauri v2)"
description: "CatheadOwl/session-manager，基于 Tauri v2 + React + Rust 的桌面应用，统一管理本地 AI 编程助手的会话日志，按项目文件夹分组，提供三栏工作区浏览会话、分支树与消息详情。"
resource: "https://github.com/CatheadOwl/session-manager"
tags: "[tauri, react, rust, desktop, ai-coding, session-manager, claude-code, codex]"
timestamp: "2026-08-01T20:30:00Z"
---

# session-manager (Tauri v2)

## 它是什么

[`CatheadOwl/session-manager`](https://github.com/CatheadOwl/session-manager) 是一个**桌面端 AI 编程助手会话管理器**：用 Tauri v2 + React + Rust 构建，自动扫描本地的 AI 编程助手会话目录（Claude Code / Codex 等），按项目文件夹分组，提供**三栏工作区**（文件夹 → 会话列表/分支树 → 消息详情）让你快速在多个项目之间切换、翻历史对话、看分支走向。

## 三栏工作区

| 列 | 内容 |
|----|------|
| 左 | 项目文件夹树（按 git repo 或目录分组） |
| 中 | 会话列表 + 分支树（一个项目内的多次会话、checkout / fork 关系） |
| 右 | 单条会话的消息详情（user / assistant 消息、工具调用记录） |

## 解决什么痛点

- 同时跑 5 个 AI 编程会话（项目 A 改需求、项目 B 修 bug、项目 C 探索新方案），想「回到上次 Claude 说的那段话」
- 默认的会话日志藏在 `~/.claude/projects/...` 或 `~/.codex/sessions/...`，手动翻文件很蠢
- 不同 AI 助手（Claude Code / Codex / Cursor）的会话格式各异，没法统一看

## 核心能力

| 能力 | 说明 |
|------|------|
| 自动扫描 | 已知会话目录（Claude Code / Codex 等）按项目文件夹分组 |
| 三栏 UI | 文件夹 → 会话/分支树 → 消息详情，键盘流友好 |
| Tauri v2 + React + Rust | 原生窗口性能 + Web 前端灵活度 |
| 本地优先 | 会话日志全程不出本机 |

## 适合什么场景

- 多项目并行 + 多 AI 助手混用，需要快速切到「昨天那条对话」
- 想可视化会话的分支结构（同一会话里多次 checkout）
- 想要一个**比 IDE 内置会话 UI 更通用**的统一入口

## 与同类工具的差异

| 工具 | 形态 | 差异 |
|------|------|------|
| [ccsessions](./tool-ccsessions.md) | 终端 TUI | 只管 Claude Code，无分支树视图 |
| [ccmux](./tool-ccmux.md) | tmux 状态栏 | 监控运行中会话，不读历史日志 |
| session-manager | 桌面 GUI | 跨助手 + 分支树 + 桌面三栏视图 |

## 媒体

![session-manager 截图](https://pbs.twimg.com/media/HOha5Y6bUAALFNh.jpg)

## 原始链接

- [项目仓库](https://github.com/CatheadOwl/session-manager)
- [原始推文](https://x.com/QingQ77/status/2083528169156423849)

## 相关概念

- [ccsessions](./tool-ccsessions.md) — 终端里浏览 Claude Code 会话，session-manager 是它的桌面 GUI 版本
- [ccmux](./tool-ccmux.md) — 同时跑多个 Claude Code 会话时的 tmux 状态栏指示器