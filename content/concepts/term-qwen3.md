---
type: "Term"
title: "Qwen3（通义千问 3）"
description: "阿里通义实验室 2025 年发布的 Qwen 系列第三代基座模型——同时提供 Dense 与 MoE 两种架构、覆盖 0.6B / 4B / 8B / 14B / 32B / 235B 等多档规模，原生支持 119 种语言与 32K 上下文，是当下中文开源大模型的第一梯队。"
resource: "https://qwenlm.github.io/blog/qwen3/"
tags: "[qwen, qwen3, llm, open-source, chinese]"
timestamp: "2026-10-06T22:51:00Z"
---

# Qwen3（通义千问 3）

## 定义

**Qwen3** 是阿里通义实验室发布的第三代 Qwen 系列基座大模型，2025 年 4 月开源，**同时提供 Dense 与 MoE 两种架构**，规模覆盖 0.6B / 4B / 8B / 14B / 32B / 235B-A22B 等多档，原生支持 119 种语言，**最长 32K 上下文**，是当下中文开源大模型第一梯队的代表。

## 要点

- **博客 / 发布**：[qwenlm.github.io/blog/qwen3](https://qwenlm.github.io/blog/qwen3/)
- **架构**：Dense + MoE 双线（Qwen3-235B-A22B 是 235B 总参 / 22B 激活的 MoE）
- **能力**：推理、代码、Agent、Function Call、多语言；32K 上下文原生
- **许可**：Apache 2.0（多数规模）
- **典型场景**：本地推理 / 微调、Agent 底座、桌面端侧模型、Apple Silicon 友好（量化后）

## 相关概念

- [Apple Silicon](./term-apple-silicon.md) — Qwen3 小规模版量化后可本地跑在 M 系列芯片
- [AI Coding Agent](./term-ai-coding-agent.md) — Qwen3 可作为底座
