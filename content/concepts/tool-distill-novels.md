---
type: "Tool"
title: "distill-novels"
description: "CloudLiu1008 开源的 AI 写作 Skill：把一本或多本小说拆成可按维度复用的世界观 / 人物 / 情节 / 文风等写作知识库，供 AI 写作助手调用，用来构思 / 润色 / 检查原创小说。"
resource: "https://github.com/CloudLiu1008/distill-novels"
tags: ["writing", "novel", "skill", "agent", "knowledge-base", "open-source"]
timestamp: "2026-08-14T19:50:00Z"
---

# distill-novels

## 它是什么
distill-novels 是一个给 AI 写作助手的 Skill：把一本或多本小说拆成结构化的「写作知识库」（世界观、人物、情节、文风等多个维度），让 AI 写作助手在构思 / 润色 / 一致性检查时调用这些知识做参考。

## 为什么用它 / 适合什么场景
- 写长篇小说时 AI 容易「失忆」或前后矛盾，把参考小说拆成结构化知识库就能让 AI 持续参考。
- 学习某作者文风时，先蒸馏对方的代表作，再让 AI 在该风格基础上模仿 / 改良。
- 想做「多人设多世界观」写作项目时，把每个世界观独立蒸馏后再合并调用。

## 关键能力
| 能力 | 说明 |
|------|------|
| 输入 | 一本或多本小说 |
| 拆解维度 | 世界观 / 人物 / 情节 / 文风 |
| 输出 | 可复用的写作知识库 |
| 形态 | AI 写作 Skill |
| 用途 | 构思 / 润色 / 一致性检查 |

## 相关概念
- [Novel Studio](./tool-novel-studio.md) — Go 写的本地优先 AI 长篇小说引擎，distill-novels 是其知识侧的「外部资料处理」配套
- [LiYuan](./tool-liyuan.md) — AI Agent 架构重构角色扮演：记忆账本 + 决策卡 + 自建面板 + 世界线存档，distill-novels 与其思路有重合（角色 / 世界观结构化）
- [Hearth](./tool-hearth-nl-game.md) — 自然语言描述游戏，AI 现场建游戏并跑起来；distill-novels 是文学版的「知识驱动生成」
