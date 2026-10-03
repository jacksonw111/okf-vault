---
type: "Tool"
title: "Ponytail（DietrichGebert/ponytail）"
description: "DietrichGebert 出品的 Agent Skill：把「尾巴 (logs / trailing state)」相关工作流沉淀成可加载的 Skill，让 Claude / Cursor 等编码代理在长任务中正确处理输出流与历史。"
resource: "https://github.com/DietrichGebert/ponytail"
tags: "[agent-skills, log, trailing-state, claude-code]"
timestamp: "2026-10-03T00:00:00Z"
---

# Ponytail

## 它是什么

[Ponytail](https://github.com/DietrichGebert/ponytail) 是 **DietrichGebert** 出品的 Agent Skill——专门处理**输出流 / 历史尾巴**相关的工作流，让 Claude / Cursor 等编码代理在长任务 / 多回合场景下不丢上下文、正确处理尾部状态。

## 为什么用它 / 适合什么场景

- **长任务容易「断尾」**：编码 Agent 跑 30 分钟以上，trailing log / 文件 diff 尾巴 / 输出末尾 容易丢失或错位。
- **把流式工作流装进 Skill**：不必每次手写 trailing 处理逻辑，让 Skill 接管。
- **多 Agent 协作时统一尾巴语义**：让多个 Agent 都按 Ponytail 的约定输出末尾。

## 关键能力

| 能力 | 说明 |
|------|------|
| 主题 | Trailing state / 输出尾部处理 |
| 形态 | Agent Skill（Claude / Cursor 等可加载） |
| 开源 | GitHub 公开维护 |
| 作者 | DietrichGebert |

## 参考链接

- 项目链接：<https://github.com/DietrichGebert/ponytail>

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — Skill 装载机制
- [Matt Pocock Skills](./tool-mattpocock-skills.md) — 同作者出品的另一类工程师风格 Skills
