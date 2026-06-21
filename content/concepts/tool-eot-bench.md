---
type: "Tool"
title: "eot-bench（LiveKit 语音 AI 话轮结束检测基准）"
description: "LiveKit 做的开源话轮结束检测（End-of-Turn）基准：放出首个公开的真实人机对话数据集（覆盖 14 种语言），评测方式是模拟真实场景下「每次用户停顿都让模型判断说完了没」，核心指标是「误切断率」与「响应延迟」的权衡曲线，而非单看准确率。"
resource: "https://github.com/livekit/eot-bench"
tags: "[livekit, eot, voice-ai, benchmark, eval]"
timestamp: "2026-06-21T00:00:00Z"
---

# eot-bench（LiveKit 语音 AI 话轮结束检测基准）

## 它是什么

**LiveKit 开源基准**：`eot-bench` —— 专门评测语音 AI 的「话轮结束检测」（End-of-Turn, EOT）能力。

## 它要解决的问题

> 各家模型的 EOT 用不同私有数据集、不同方法论，**难以横向比较**。

## 关键设计

| 设计点 | 说明 |
|--------|------|
| 数据集 | **首个公开的真实人机对话数据集**，覆盖 **14 种语言** |
| 评测方式 | 模拟真实场景：每次用户停顿都让模型判断「说完了没」 |
| 核心指标 | **误切断率 vs 响应延迟** 的权衡曲线（不是单看准确率） |
| 协议 | 公开、可复现 |

## 为什么是「权衡曲线」

> 单看「准确率」无法反映真实语音体验。EOT 的本质是「该切时切、不该切时不切」与「用户停顿后多快响应」之间的权衡。eot-bench 把这条曲线作为核心可视化指标。

## 适用场景

- 做实时语音 AI（电话机器人 / 会议助理 / Voice Agent）—— 选型 / 优化 EOT 模型。
- 学术研究 —— 首个公开跨语言 EOT 基准。
- LiveKit 用户的内部评测 —— 集成到自有 pipeline。

## 媒体

![eot-bench 截图](https://pbs.twimg.com/media/HLJYD67agAAnTPA.jpg)

## 相关概念

- [a-stock-data](tool-a-stock-data.md) — 同为「数据 → 评测 / 决策」的聚合工具思路
- [ShipSwift](tool-shipswift.md) — 同样面向 AI 语音 / 实时通讯场景的工具