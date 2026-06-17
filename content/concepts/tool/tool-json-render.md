---
type: "Tool"
title: "JSON-Render / HarnessAgent（生成式 UI）"
description: "为 Claude Code / Codex / Pi 等编码 agent 设计的「在沙盒里渲染真实 UI」方案：代理输出结构化 JSON → 沙盒里的渲染器把它变成图表 / 表单 / 3D / 任意组件；用户看到的是真组件而不是终端文本。"
tags: "[ai, agent, ui, generative-ui, json-render, ai-sdk]"
timestamp: "2026-06-17T00:00:00Z"
---

# JSON-Render / HarnessAgent（生成式 UI）

## 它是什么

`JSON-Render`（也写作 `json-render`）是配合 Vercel **AI SDK** 的 **实验性 `HarnessAgent`** 提出的一种「**生成式 UI**（Generative UI）」范式：让编码 / 通用 agent（[Claude Code](tool-claude-code.md)、Codex、Pi）在**沙盒中**为用户**渲染真实的 UI 组件**——图表、表单、3D、可交互组件——而不是把结果以纯文本 / Markdown 形式打印到终端。

核心思想：**代理输出结构化 JSON schema，渲染器把它变成真组件**。和 [Archify](tool-archify.md) 同源思路：让 LLM 负责「画什么」、让确定性渲染器负责「画对」。

## 为什么这个范式重要

传统 agent 跑完任务只能用 `print` 输出一段 Markdown，用户看到的是「日志」。一旦代理能渲染真实 UI：

- **数据探索**：代理读完 CSV 不是给一段统计文字，而是直接出可点 / 可筛选的图表。
- **配置向导**：代理问 5 个问题不是用输入框收答案，而是渲染 step-by-step 表单。
- **可视化报告**：代码审计 / 性能分析结果用「卡片 + 进度条 + 颜色」呈现，比纯文本直观。
- **跨端一致**：JSON schema 一次定义，桌面 / 移动 / 嵌入式都能渲染。

## 关键能力

| 能力 | 说明 |
|------|------|
| 真实 UI 渲染 | 图表、表单、3D、任何 React/Vue/Svelte 组件 |
| 沙盒隔离 | 代理代码在沙盒里跑，不污染用户环境 |
| 结构化 JSON | 代理输出契约明确，可测试、可 diff |
| 多 agent 兼容 | Claude Code、Codex、Pi 都能接 |
| 实验性 | 由 Vercel AI SDK 的 `HarnessAgent` 提供，仍在演进 |

## 工作流（简化版）

```
代理（Claude Code / Codex / Pi）
    ↓ JSON schema 描述「我想画什么」
HarnessAgent 沙盒
    ↓ 解析 + 渲染
浏览器内真实 UI（图表 / 表单 / 3D / 任意）
    ↓
用户操作
    ↓ 回传
代理
```

## 与 [Archify](tool-archify.md) 的同与不同

| 维度 | Archify | JSON-Render / HarnessAgent |
|------|---------|---------------------------|
| 目标产物 | 静态架构图（SVG） | 可交互 UI（图表、表单、3D） |
| 渲染器 | Node.js + 几何算法 | 浏览器 / 沙盒 + React 组件 |
| 交互性 | 无 | 有 |
| 用途 | 系统拓扑、架构图 | 数据探索、配置向导、报告 |

## 相关概念

- [Agent Skills 是什么](../term/term-agent-skills.md)
- [Claude Code](tool-claude-code.md)
- [Archify](tool-archify.md)
- [Vercel AI SDK](https://sdk.vercel.ai/)
- [OKF 是什么](../term/term-okf.md) — 同属「LLM 可消费的结构化文本」范式，可作 OKF 概念的渲染端
