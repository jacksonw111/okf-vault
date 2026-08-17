---
type: Tool
title: "GraphShield-Fraud"
description: "面向图算法 / 风控 / 反欺诈岗位的时序图欺诈检测项目：在严格时间切分、杜绝未来信息泄漏的前提下，比较因果 Temporal GraphSAGE 与树基基线，并交付离线调查工件 + 事件级在线评分演示"
resource: "https://github.com/nikashen/GraphShield-Fraud"
tags: [fraud-detection, graph, temporal, graphsage, risk-control, ml]
timestamp: 2026-08-17T16:00:00Z
---

# GraphShield-Fraud

## 它是什么

`nikashen/GraphShield-Fraud` 是一个**面向图算法 / 风控 / 反欺诈岗位的时序图欺诈检测项目**：以**交易为节点、资金关联为边**构建时序图，在**严格时间切分**（杜绝未来信息泄漏）的前提下，对比非图基线（树模型）与**因果 Temporal GraphSAGE** 的欺诈识别能力，并交付：
- 离线调查工件（哪些节点被判定为高风险、依据是什么）
- 事件级在线评分 demo（新交易实时打分）

## 为什么用它 / 适合什么场景

- 想学 / 复现**时序图欺诈检测**的标准做法。
- 想对比「传统树模型 vs. 时序 GNN」在反欺诈上的差距。
- 想拿到**可演示的端到端工件**（离线 + 在线），而不是论文里的孤立模型。
- 风控 / 反欺诈岗位面试 / 学习参考项目。

## 关键能力

| 能力 | 说明 |
|------|------|
| 时序图构建 | 交易为节点、资金关联为边 |
| 严格时间切分 | 杜绝未来信息泄漏，避免回测作弊 |
| Temporal GraphSAGE | 因果时序图神经网络 |
| 树基基线 | LightGBM / XGBoost 等传统模型做对比 |
| 离线调查工件 | 输出高风险节点 + 依据 |
| 在线评分演示 | 单事件实时打分 API / 接口 |

## 媒体

- ![](https://pbs.twimg.com/media/HPvTJKDbAAA1fhE.jpg)

## 原始链接

- [项目仓库](https://github.com/nikashen/GraphShield-Fraud)

## 相关概念

- [Vibe-Trading](./tool-vibe-trading.md) — 同属金融 AI 生态，但 Vibe-Trading 偏投研多代理流水线