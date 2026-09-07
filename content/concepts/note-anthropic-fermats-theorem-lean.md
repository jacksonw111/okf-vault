---
type: Note
title: "Anthropic 用 Lean 形式化证明费马大定理"
description: "Anthropic 公开的费马大定理 Lean 形式化证明项目，把数学界 350 年的未解难题搬进机器可验证体系。"
resource: "https://github.com/anthropics/fermats-last-theorem"
tags: "[anthropic, lean, formal-verification, math, fermat]"
timestamp: "2026-09-07T13:03:00Z"
---

# Anthropic 用 Lean 形式化证明费马大定理

## 是什么
Anthropic 在 GitHub 上公开的费马大定理（Fermat's Last Theorem）的 Lean 形式化证明项目。费马大定理是数学界悬而未决 350 年的难题（直到 1994 年 Andrew Wiles 给出经典证明），本项目把这一定理以及关键证明步骤在 Lean 定理证明器里重新形式化，使整个证明链可被机器独立验证。

## 为什么重要
- **形式化数学的里程碑**：经典证明（如 Wiles 的证明）依赖人类专家审稿，形式化后可由 Lean 内核自动核对
- **Anthropic 出品**：少见的"AI 公司做纯数学形式化"案例，体现形式化方法对 LLM 推理可靠性的潜在价值
- **公开仓库**：整个证明链、依赖、引理都可被复现与审计

## 与传统证明的区别
| 维度 | 经典证明 | Lean 形式化证明 |
|------|---------|----------------|
| 验证方式 | 人类专家审稿 | 机器内核自动验证 |
| 错误风险 | 隐藏的逻辑缺陷 | 每一步都需内核接受 |
| 可读性 | 自然语言 + 数学符号 | Lean 策略式 + 数学声明 |
| 可执行性 | 仅作为论文 | 可在 Lean 解释器里独立跑 |

## 参考
- 项目链接：<https://github.com/anthropics/fermats-last-theorem>

## 相关概念
- [Lean 定理证明器](https://leanprover.github.io/) — 本项目使用的形式化工具