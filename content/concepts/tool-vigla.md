---
type: Tool
title: "Vigla"
description: "跨厂商编程 Agent 统一运营面板：把 Claude Code / Codex CLI / Antigravity 等本地并行运行的 agent 收进同一界面，划好授权边界后由监督器代审 diff，结果不对可一键回退整次任务。"
resource: "https://github.com/Kilbex/Vigla"
tags: [agent-orchestration, dev-tools, claude-code, codex, antigravity, multi-agent, ops-panel]
timestamp: 2026-08-06T12:30:00Z
---

# Vigla

## 它是什么

Kilbex 开源的本地多 Agent 运营面板，解决「本机同时跑多个编程 agent 时，每个终端各审各的 diff、各合各的」这一局面。

## 为什么用它 / 适合什么场景

- 你日常同时开 Claude Code、Codex CLI、Antigravity 跑不同项目，嫌终端窗口切来切去麻烦。
- 想给每个 agent 划清授权边界（哪些目录 / 命令 / 危险操作允许 / 拒绝），由统一的监督器代审，而不是每个 agent 各自请求确认。
- 出问题想一键回退整次任务（不只是单个文件），避免 agent 半路留下的中间状态污染仓库。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多 Agent 面板 | 把 Claude Code / Codex CLI / Antigravity 等跨厂商 agent 收进同一 UI |
| 授权边界 | 给每个 agent 划清允许范围，监督器代审，不依赖 agent 自身的确认弹窗 |
| 一键回退 | 任务结果不对时一键回退整次操作留下的所有变更 |

## 相关概念
- [Claude Code Router](./tool-claude-code-router.md) — 本地网关统一管 Claude Code / Codex / Grok 凭据 / 路由 / 故障切换
- [Cyvisguard](./tool-cyvisguard.md) — Agent 工具调用授权层，zero-trust 风格
- [Agent Manager (tmux)](./tool-agent-manager-tmux.md) — TUI 架在 tmux 上统一管 Claude Code / Codex / OpenCode / Grok Build