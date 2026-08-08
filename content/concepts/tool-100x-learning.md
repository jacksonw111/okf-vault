---
type: "Tool"
title: "100x Learning"
description: "按 Agent Skills 开放格式写的学习与内容 Skill：把任务分成材料理解 / 主题研究 / 概念解释 / 实践 / 内容审查 / 写作 / 持续选题 / 知识沉淀八类，每类都有明确「停手位置」，放进兼容工具的 Skills 目录即可跑。"
resource: "https://github.com/CheshireMew/100x-learning"
tags: [agent-skill, learning, content, openclaw, claude-skill]
timestamp: "2026-08-08T20:30:00Z"
---

# 100x Learning

## 它是什么

100x Learning 是一款按 Agent Skills 开放格式（兼容 Codex / Claude Code / 其他 Skills 协议工具）写的学习与内容工作 Skill。它把「学习 + 内容生产」拆成八类任务：材料理解、主题研究、概念解释、实践、内容审查、写作、持续选题、知识沉淀。每类任务都有明确的「停手位置」——读懂材料就停在解释，审查就不许顺手改稿，没说要成品就不会自动写帖。

## 为什么用它 / 适合什么场景

- 想用 Agent 把「学 + 写」流水线化，又不希望 agent 越界（擅自写帖、改稿）。
- 需要把 Skill 拆得足够细，便于在多工具间复用。
- 关心长期学习 / 内容工作的可持续迭代。

## 关键能力

| 能力 | 说明 |
|------|------|
| 八类任务分工 | 材料理解 / 主题研究 / 概念解释 / 实践 / 内容审查 / 写作 / 持续选题 / 知识沉淀 |
| 停手位置明确 | 每类任务明确边界，agent 不越权 |
| 长期迭代 | 真实反馈可接入下一轮循环 |
| 开放 Skill 格式 | 兼容 Codex / Claude Code 等 Agent 工具 |
| 模块化 | 可单独使用某一类任务的 Skill |

## 相关概念

- [Agent Skills](./term-agent-skills.md) — Agent Skills 标准协议
- [CoLearning Loop](./tool-loop-engineering.md) — 把 AI agent 编成自动循环的方法论
- [OpenClaw Marketing Skills](./tool-openclaw-marketing-skills.md) — 同属 Skill 协议下的内容生产集