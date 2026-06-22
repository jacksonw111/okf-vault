---
type: "Tool"
title: "Loops（jwangkun/loops，100 个 AI 自动化循环模板）"
description: "jwangkun/loops —— 100 个精心策划的 AI 驱动自动化循环（loop engineering）模板，覆盖软件开发、数据科学、内容创作、产品运营、学习管理等领域；让 AI 助手按「干→查→修→再干」的循环自己把活干完。"
tags: "[ai, agent, automation, loop-engineering, prompt-engineering]"
timestamp: "2026-06-22T07:35:00Z"
---

# Loops（jwangkun/loops，100 个 AI 自动化循环模板）

## 它是什么

[`jwangkun/loops`](https://github.com/jwangkun/loops) 是一个**精心策划的 AI 自动化循环模板合集**——收录 **100 个**「**loop engineering**」套路，覆盖软件开发、数据科学、内容创作、产品运营、学习管理等场景。每个模板描述一种「**干 → 查 → 修 → 再干**」的闭环结构，让 AI 助手自己反复迭代，**不需要人一步步盯着**。

## 为什么用它 / 适合什么场景

- **一次性 prompt 干不了复杂任务**：让 AI 「写一个完整 web 应用」一次就跑好的概率很低；但让它「写 → 跑测试 → 看错误 → 改」循环起来，质量会显著提升。
- **Loop engineering 是 agent 写法的核心模式**：本质就是把"失败→重试"做到结构化、可见、可调试。
- **100 个模板**横跨多领域，提供现成的循环骨架，省得自己设计。

适合：

- 让 AI 写代码并自动跑测试 / 修复 lint / 修类型错误。
- 让 AI 写内容并自动校稿 / 改风格 / 改长度。
- 让 AI 做数据分析并自动验证假设 / 重选模型。
- 任何「希望 AI 自己闭环、不想频繁打断」的工作。

## 关键能力

| 能力 | 说明 |
|---|---|
| 100 个模板 | 覆盖软件 / 数据 / 内容 / 产品 / 学习多领域 |
| Loop engineering 思路 | 「干 → 查 → 修 → 再干」结构化闭环 |
| 开箱即用 | 模板即 prompt / script，照搬可用 |
| 跨工具 | 适用于 Claude Code / Codex / Pi / Cursor 等任意 agent |
| 持续增长 | 仓库仍在维护，模板数会继续上升 |

## 典型循环结构（以"代码自动化"为例）

```
目标：实现 feature X
  ↓
1. 干：让 AI 写实现
  ↓
2. 查：跑测试 / lint / typecheck，收集错误
  ↓
3. 修：把错误喂回 AI，让它修复
  ↓
4. 评估：是否满足退出条件（测试全过 / lint 干净）
  ├─ 是 → 返回
  └─ 否 → 回到 1（限定最大迭代次数）
```

模板化 = 把这个循环的"目标 / 退出条件 / 反馈格式 / 工具调用"具体化。

## 与"loop engineering"概念合集的关系

本仓库是 [loops.elorm.xyz](tool-loops-elorm-xyz.md) 的**具体模板实现**——前者收录"几十位大神的 loop engineering 思路"（理念合集），本仓库提供"100 个开箱即用的具体模板"（实现合集）。两者配合阅读：先理解思路，再抄模板。

## 适用人群

- **Claude Code / Codex / Pi / Cursor 等 agent 的重度用户**。
- 想给 agent 加「自动循环 / 失败重试 / 自我修正」能力的人。
- 在写「AI 自动跑 KAGGLE / AI 自动写周报 / AI 自动出报告」之类系统的人。

## 参考链接

- [项目链接](https://github.com/jwangkun/loops)
- [原始链接](https://t.co/0qQJefuRvb)

## 相关概念

- [loops.elorm.xyz](tool-loops-elorm-xyz.md) — 几十位大神的 loop engineering 思路集合（理念合集）
- [Agent Skills 是什么](term-agent-skills.md) — 代理技能包元概念
- [pi-task](tool-pi-task-delegation.md) — Pi Agent 子任务委派扩展（前 / 后台 + TUI 进度条）
- [Repo→Agent](tool-repo-agent-generator.md) — 把任意 GitHub 仓库生成为带 CLI / MCP / 签名的 Agent 包