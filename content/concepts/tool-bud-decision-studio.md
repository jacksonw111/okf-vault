---
type: "Tool"
title: "Bud Decision Studio（本地决策模型运行台）"
description: "Bud Ecosystem 开源：让用户在本地电脑上跑自家的开源决策模型，把一段情况和若干带类型的问题交给模型，毫秒级拿到每个候选答案的概率。"
resource: "https://github.com/BudEcosystem/Bud-Decision-Studio"
tags: "[decision-model, on-device, local-llm, bud, ml, classification]"
timestamp: "2026-10-08T23:50:00Z"
---

# Bud Decision Studio

## 它是什么

[Bud Decision Studio](https://github.com/BudEcosystem/Bud-Decision-Studio) 是 **Bud Ecosystem** 开源的「**本地决策模型运行台**」：

- 在本地电脑上跑 Bud 开源的决策模型
- 输入：**一段情况 + 若干带类型的问题**
- 输出：**每个候选答案的概率**
- **毫秒级**响应

## 为什么用它 / 适合什么场景

- **要快**：毫秒级响应，可放进交互式应用
- **数据敏感**：决策不上云
- **分类 / 路由**：让 LLM Agent 做高吞吐的轻量决策
- **想给小模型找落地**：把决策模型嵌进产品

## 关键能力

| 能力 | 说明 |
| ------ | ------ |
| 形态 | 本地运行台（desktop / CLI） |
| 模型 | Bud Ecosystem 开源决策模型 |
| 输入 | 自由文本 + 类型化问题列表 |
| 输出 | 每个候选的概率 |
| 速度 | 毫秒级 |
| 隐私 | 全本地 |

## 参考链接

- 项目链接：<https://github.com/BudEcosystem/Bud-Decision-Studio>

## 媒体

![](https://pbs.twimg.com/media/HUAID7JbUAENFjq.jpg)

## 相关概念

- [Jev（决策小模型范式）](./term-jev.md) — 同属「本地决策模型」范式
- [OneJev](./tool-onejev.md) — 另一款本地多模态决策框架