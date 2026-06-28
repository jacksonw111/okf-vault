---
type: "Tool"
title: "MCO（多 AI 编程代理编排层）"
description: "中立的 AI 编程代理编排层，可在任意 IDE 或终端同时调度 Claude Code、Codex CLI、Gemini CLI 等多个 AI 编程代理，支持并行执行、跨代理代码审查、自动修 bug 与自动建文件。"
tags: "[ai-agent, orchestration, cli, codex, claude-code, gemini-cli]"
timestamp: "2026-06-28T14:36:00Z"
resource: "https://github.com/mco-org/mco"
---

# MCO（多 AI 编程代理编排层）

## 它是什么

MCO（Multi-CLI Orchestrator）是一个**中立的 AI 编程代理编排层**，通过 `npm` 包安装，在终端里用 `mco` 命令统一调度多种 CLI 形态的 AI 编程代理。它不绑定特定模型或 IDE，而是把已经流行的 CLI 代理（Claude Code、Codex CLI、Gemini CLI 等）当成「可插拔的执行单元」同时拉起，让它们并行执行或接力协作。

内置 7 家 AI 提供商，覆盖主流闭源与开源模型。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多代理并行 | 一条命令同时拉起 Claude Code + Codex CLI + Gemini CLI 各自处理子任务 |
| 跨代理代码审查 | 不同代理互为 reviewer，把同一份 diff 丢给另一个模型挑刺 |
| 自动修 bug | 解析 CI/测试输出后自动让代理定位修复并提 PR |
| 自动建文件 | 根据高层意图（如「加个 API」）直接生成多文件改动 |
| 提供商中立 | 任意 CLI 代理都能以适配器形式接入，不锁死单家厂商 |
| 终端原生 | 安装后直接 `mco <task>`，无需启 GUI 或 IDE 插件 |

## 典型使用场景

- 同一项需求**多模型对照**：让 Claude 与 Gemini 各自写一份实现，再交叉评审。
- 大型重构拆给多个代理**并行处理**，节省单线程等待时间。
- 在 CI 流水线里挂上 MCO，让失败时自动派代理读日志 → 改代码 → 提 PR。

## 安装与运行

```bash
npm install -g mco
mco "为这个项目补 README 并修复 #12 的 bug"
```

## 参考链接

- [项目仓库](https://github.com/mco-org/mco)
- [原始链接](https://x.com/QingQ77/status/2071179551011467600)

## 相关概念

- [Claude Code](tool-claude-code.md) — MCO 编排的主要代理之一
- [Orgii](tool-orgii.md) — Rust + Tauri 多 Agent 协作框架，与 MCO 同样强调「把 AI 当同事」
- [PeakCode](tool-peakcode.md) — 多代理会话统一 GUI，与 MCO 的「多代理」理念互补
- [Brigade](tool-brigade.md) — 本地多 AI 代理协作框架 + Tideline 长期记忆