---
type: Tool
title: "Claude Vibe Squad"
description: "多模型编排工具：协调者 Chrono 把目标拆成计划并分派给 71 个专家角色执行，支持 Codex/Claude/Gemini/Grok/Kimi 五家；规则与每个任务都用 Markdown 描述。"
resource: "https://github.com/mtarcure/claude-vibe-squad"
tags: [agent, orchestration, multi-model, markdown, vibe-coding]
timestamp: "2026-09-08T00:00:00Z"
---

# Claude Vibe Squad

## 它是什么
Vibe Squad 是 mtarcure 开源的**多模型编排工具**：你只跟协调者 Chrono 打交道，Chrono 把目标拆解成计划，从 71 个专家简介里挑合适角色与对应模型（Codex / Claude / Gemini / Grok / Kimi）去执行。所有规则、计划、任务契约**都用 Markdown 写**——能看能改。

## 为什么用它 / 适合什么场景
- 想做 vibe coding 又想保留结构化流程感（谁负责、能改什么、什么算完成）。
- 想在多个 LLM 之间按"任务类型"分配角色，而不是把所有事塞给同一个模型。
- 想让 agent 团队的协作规则可读、可审计、可手改。

## 关键能力
| 能力 | 说明 |
|------|------|
| 协调者 Chrono | 中央拆解 + 分派 |
| 71 个专家 | 角色与简介独立维护 |
| 五家模型 | Codex / Claude / Gemini / Grok / Kimi |
| Markdown 契约 | 每个任务一份 Markdown：谁做、用什么模型、能改什么、什么算做完 |
| 透明可改 | 规则全文可见可改 |

## 参考
- 原始链接：<https://github.com/mtarcure/claude-vibe-squad>

## 媒体
- ![](https://pbs.twimg.com/media/HRn2f9JasAAVIYj.png)

## 相关概念
- [Claude Code](./tool-claude-code.md) — 同生态的终端 agent
- [vibe coding](./term-vibe-coding.md) — 玩法背景
