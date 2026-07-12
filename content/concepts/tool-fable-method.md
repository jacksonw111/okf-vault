---
type: Tool
title: "fable-method（think / act / prove 解题 Skill）"
description: "把 Claude Fable 5 在停服前对自己解题方式的提炼整理成一套任何模型都能照做的 skill（think / act / prove），并配一套对抗式 eval 来验证它真的有用，而不是只在嘴上喊\"要仔细\"。"
resource: "https://github.com/Sahir619/fable-method"
tags: [tool, agent-skill, prompt-engineering, eval, claude, fable]
timestamp: 2026-07-12T16:30:00Z
---

# fable-method（think / act / prove 解题 Skill）

## 它是什么
开源项目，把 Anthropic 旗下 Claude Fable 5 模型在「停服」前对自己解题方式的内部分析（think → act → prove 三阶段）整理成一套**通用 Skill**，让任何 LLM（不仅限于 Fable 5）都能照做；并配套一套对抗式 eval，用真实基准验证这个 Skill 真能提升解题质量，而不是停留在"提示词好听"的层面。

## 为什么用它 / 适合什么场景
- 想给团队里所有 LLM（Opus / Sonnet / GPT / Gemini / 本地模型）统一一套经过验证的解题流程，而不是各凭 prompt 摸索。
- 已尝试过自写"先想清楚再动手"类 prompt，但缺少对抗式 eval 验证效果。
- 想学习 Fable 5 模型的内部解题策略并应用到下游任务。

## 关键能力
| 能力 | 说明 |
|------|------|
| think → act → prove 三段式 | 把解题流程拆成"先想清楚、再动手、最后用真实证据证明有效"三步 |
| 模型无关 | 不绑死 Claude，任何支持指令遵循的 LLM 都能加载 |
| 对抗式 eval | 配套 eval 套件验证 Skill 是否真的提升模型表现，不只是"听起来对" |
| Skill 协议打包 | 按 Agent Skills 协议打包，便于 Claude Code / Codex / Cursor 等加载 |

## 参考链接
- [项目链接](https://github.com/Sahir619/fable-method)
- [原始链接](https://x.com/QingQ77/status/2076204662483771849)

## 相关概念
- [Fable Harness（先取证 / 明说假设 / 求反对意见）](tool-fable-harness.md) — 同一思路（"用协议约束 agent 行为"）的另一实现，差别在 Harness 偏"行为纪律"，fable-method 偏"解题流程"
- [Agent Skills（代理技能包）](term-agent-skills.md) — 项目本身按 Agent Skills 协议打包
- [Frontier 21（Fable 5 编写 / 审计的 21 项质量标准方法包）](tool-frontier-21.md) — 同样源自 Fable 5 训练经验的质量方法集