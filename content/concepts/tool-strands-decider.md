---
type: "Tool"
title: "strands-labs/strands-decider（19 亿参数决策小模型）"
description: "strands-labs 出品：19 亿参数的快模型，专门接 Agent 里「选哪个模型 / 调哪个工具 / 这句话紧不紧急」之类小判断——一次前向出结果附带置信度，不必每次都调 LLM。"
resource: "https://github.com/strands-labs/strands-decider"
tags: "[ai-agent, small-model, decision-model, routing, classifier]"
timestamp: "2026-10-04T06:00:00Z"
---

# strands-decider

## 它是什么

[strands-decider](https://github.com/strands-labs/strands-decider) 是 **strands-labs** 出品的**决策小模型**——19 亿参数，专门接 Agent 里的小判断任务：

- 选哪个模型
- 调哪个工具
- 这句话紧不紧急
- 分类 / 打分 / 答是否

## 关键特点

| 特点 | 说明 |
|------|------|
| 体积 | 19 亿参数（足够小，能本地跑 / 边缘部署） |
| 输出 | 一次前向出**类型化答案 + 置信度** |
| 替代 | 不必每次都为这类小判断调大 LLM |
| 速度 | 单次推理极快 |

## 适合场景

- Agent 工作流里有大量「是 / 否 / 选 A / 选 B」小判断
- 想把「调 LLM」换成「调本地小模型」省成本 / 延迟
- 边缘 / 离线部署 Agent 的分类 / 路由需求

## 参考链接

- 项目链接：<https://github.com/strands-labs/strands-decider>

## 相关概念

- [Jev 类决策模型（10 级分层示例）](./note-ten-levels-of-jev.md) — 决策模型在架构中的层级位置