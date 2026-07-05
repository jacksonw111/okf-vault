---
type: "Tool"
title: "firstmate（多 Agent 并行编排框架）"
description: "不是传统工具，是一套目录结构与规则：把终端编码 AI 变成「大副」，自动派多个 crewmate（独立工作目录 + 窗口）并行干活，完成后给你 PR 或调查报告。"
tags: "[multi-agent, orchestration, code-review, parallel, ai]"
timestamp: "2026-07-05T00:00:00Z"
resource: "https://github.com/kunchenguid/firstmate"
---

# firstmate（多 Agent 并行编排框架）

## 它是什么

[`firstmate`](https://github.com/kunchenguid/firstmate) **不是传统意义上的工具**，它是一套**目录结构 + 行为规则**的组合，把你本地的终端编码 AI（Claude Code / Codex 等）变成「大副」（first mate）。

你向 firstmate 说需求，firstmate 自己**拆任务 → 分给 crewmate（每个在独立工作目录和窗口里跑）→ 盯着执行完 → 最后给你 PR 或调查报告**。

## 关键能力

| 能力 | 说明 |
|------|------|
| 任务自动拆分 | 输入高层需求，firstmate 拆成多个可独立执行的小任务 |
| 多 Agent 并行 | 每个 crewmate 跑在独立工作目录 + 独立窗口 |
| 进程隔离 | 不同 crewmate 互不干扰，工作目录物理分开 |
| 执行监督 | firstmate 监控所有 crewmate 的完成状态 |
| 统一交付 | 完成后输出 PR 或调查报告 |
| 规则即配置 | 整套机制由目录结构 + 规则定义，不靠复杂配置文件 |

## 工作模型

```text
你（Captain）
   │
   ▼
firstmate（大副）
   │
   ├── crewmate A （独立目录 / 窗口）
   ├── crewmate B （独立目录 / 窗口）
   └── crewmate C （独立目录 / 窗口）
   │
   ▼
最终交付：PR / 调查报告
```

## 适用场景

- 一个需求需要**多角度同时研究**（性能 / 安全 / 可读性 / 测试覆盖）
- 大型重构拆给多 Agent 并行处理，节省单线程等待
- 想让 AI 像团队一样干活而不是「一个大模型从头干到尾」
- 给 AI 编码流加一层「分而治之」的人类管理风格

## 与同类工具的差异

- **vs MCO（多 CLI 编排层）**：MCO 调度多个**不同** CLI 代理（Claude Code + Codex CLI + Gemini CLI），firstmate 调度**同一个 CLI 的多个实例**
- **vs Brigade**：Brigade 是完整的「多 Agent 协作框架」（长期记忆 + 模型切换），firstmate 偏向「单任务并行」

## 参考链接

- [项目链接](https://github.com/kunchenguid/firstmate)

## 相关概念

- [MCO](tool-mco.md) — 中立的代理编排层，同时调度多种 CLI 代理
- [Brigade](tool-brigade.md) — 本地 AI 代理团队 + Tideline 共享长期记忆
- [ORGII](tool-orgii.md) — Rust + Tauri 多 Agent 协作框架