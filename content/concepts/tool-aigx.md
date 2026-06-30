---
type: Tool
title: "AIGX（AI 编码代理上下文格式）"
description: "开放的 AI 编程代理上下文格式——把代码库规则集中存到 .aigx/ 目录，通过 per-file 边界索引精确绑定约束，零源码注入，且经过基准测试验证。"
resource: "https://github.com/Lolner95/AIGX"
tags: "[ai-coding, context, format, mcp, vscode]"
timestamp: "2026-06-30T15:30:00Z"
---

# AIGX（AI 编码代理上下文格式）

## 它是什么

AIGX 是一个开放的、面向 AI 编程代理的上下文格式：把代码库的规则集中存到 `.aigx/` 目录，通过 per-file（按文件）的边界索引精确地把约束「绑定」到对应位置，让代理在编辑某文件时直接拿到相关约束，**无需把约束作为注释注入源码**。

## 关键能力

| 能力 | 说明 |
|------|------|
| 集中式规则库 | 全部约束放 `.aigx/` 目录，源码不被污染 |
| per-file 边界索引 | 约束按文件精确绑定，编辑该文件时自动加载 |
| 零源码注入 | 不需要在源代码里加 AI 注释，保留代码整洁 |
| 基准测试验证 | 是首个（也是目前唯一）经过基准测试验证的同类格式 |
| 多语言实现 | Node / Python / Rust 三套参考实现 |
| 编辑器集成 | 提供 VS Code 扩展 |

## 适用场景

- 想给 AI 代理「喂」项目特定约束（命名 / 错误处理 / 测试覆盖 / 风格），又不想污染源码。
- 团队需要一套统一的「代理友好」约束管理规范。
- 替代散落在 `CLAUDE.md` / `AGENTS.md` / `codex.md` 里的临时约束。

## 相关概念

- [codebase-memory-mcp](./tool-codebase-memory-mcp.md) — 同为面向 AI 编码代理的结构化「代码记忆」
- [claude-code](./tool-claude-code.md) — 终端 AI 编码代理，协议开放
- [claude-code-best-practice](./tool-claude-code-best-practice.md) — Claude Code 60k+ 星资源合集
- [Aura-IDE](./tool-aura-ide.md) — Planner/Worker 双智能体本地编码工作台

## 参考链接

- 项目链接：<https://github.com/Lolner95/AIGX>