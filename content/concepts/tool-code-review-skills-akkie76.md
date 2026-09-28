---
type: "Tool"
title: "Code Review Skills（akkie76：『コードレビューの教科書』基础）"
description: "akkie76 出品的 Agent Skill：基于日文《コードレビューの教科書》，帮编码 Agent 做 Code Review 时避免「风格偏好」与「无据猜测」式指摘，要求每条意见都给具体依据与发生条件。支持 Codex / Claude Code。"
resource: "https://github.com/akkie76/code-review-skills"
tags: "[code-review, agent-skill, claude-code, codex, japanese]"
timestamp: "2026-09-28T23:45:00Z"
---

# Code Review Skills（akkie76：『コードレビューの教科書』基础）

## 它是什么

[akkie76/code-review-skills](https://github.com/akkie76/code-review-skills) 是 akkie76 出品的 **Agent Skill**，基于日文《**コードレビューの教科書**》（Code Review 教科书）。作用是帮 **Codex / Claude Code** 等编码 Agent 在做 Code Review 时：

- 避免「**风格上的好恶**」（style-based nitpicks）
- 避免「**无据的推测**」（speculative comments）
- 每条意见都给出**具体依据**与**发生条件**

## 为什么用它 / 适合什么场景

- 觉得现在的 AI Code Review 太多「个人偏好」式意见，真正有价值的反馈被淹没。
- 团队想统一 Code Review 质量标准。
- 在用 Codex / Claude Code，需要一个能让 Agent 主动收敛评论质量的 Skill。
- 日文团队 / 项目，或者想参考日文技术书的标准。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | Agent Skill（Codex / Claude Code 可加载） |
| 理论依据 | 日文《コードレビューの教科書》 |
| 设计目标 | 收敛评论质量、避免偏好 / 猜测 |
| 兼容性 | Codex / Claude Code |
| 出品 | akkie76 |

## 相关概念

- [open-code-review（阿里 AI 代码审查助手）](./tool-open-code-review.md) — 另一种 AI Code Review 思路：BYOK + Delegation 把审查委派给别的 agent
- [Perch](./tool-perch-code-review.md) — 方法级逐个 + 调用上下文的 AI Code Review 工具