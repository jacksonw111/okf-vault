---
type: "Tool"
title: "Jevbridge（给 LLM 挂类型化决策层：noul / choice / score）"
description: "tacticocc/Jevbridge：在已跑的 LLM 外面再挂一层类型化决策层，用 Jev 或任意 OpenAI 兼容模型回答 noul / choice / score 三类问题，替 LLM 决定「调用哪个工具 / 要不要点那个按钮」。"
resource: "https://github.com/tacticocc/Jevbridge"
tags: "[agent, decision-engine, jev, type-safe, llm]"
timestamp: "2026-09-20T18:00:00Z"
---

# Jevbridge

## 它是什么

[tacticocc/Jevbridge](https://github.com/tacticocc/Jevbridge) 给已经在跑的 LLM「外挂一个**类型化决策层**」——这个决策层用 **Jev 模型**或**任意 OpenAI 兼容模型**回答三类结构化问题：

- `noul`：二元判断（是 / 否）
- `choice`：多选一
- `score`：打分

LLM 负责「想」，Jevbridge 负责「**定**」——决定调用哪个工具、该不该点那个按钮。

## 为什么用它 / 适合什么场景

- 已经在跑大模型，但「**这个操作该不该做 / 走哪条路**」这种**结构化判断**更适合用专用决策模型。
- 不想把决策逻辑写死在 prompt 里——给决策一个独立可替换的「决策器」。
- 想要**跨 LLM 一致**的决策标准——决策层不绑死模型。

## 关键能力

| 能力 | 说明 |
|------|------|
| 类型化决策 | noul / choice / score 三种结构化输出 |
| 模型可选 | Jev 模型或任意 OpenAI 兼容模型 |
| 与 LLM 解耦 | LLM 换不换，决策层都接得住 |
| 工具调用决策 | 决定调用哪个工具 / 要不要执行某动作 |

## 项目链接

- 仓库：<https://github.com/tacticocc/Jevbridge>

## 相关概念

- [Laya](./tool-laya-decision-engine.md) — 同为编码器式决策引擎
- [SemIf](./tool-semif.md) — 同为「让小模型做 if 决策」的思路
- [kev（Qwen 底座决策模型）](./tool-kev-decision-model.md) — 同为复刻 Jev 架构的开源实现
- [jev-mcp](./tool-jev-mcp.md) — 同基于 Jev 的 MCP server
