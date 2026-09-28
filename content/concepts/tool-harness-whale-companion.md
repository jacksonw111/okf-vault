---
type: "Tool"
title: "harness-whale-companion（DSH 状态 + 单选题 ESP32-C3 蓝牙小屏）"
description: "1ikeMcFlurry 出品：让 DeepSeek Harness 的运行状态、任务进度和 API 余额显示在一块 ESP32-C3 蓝牙小屏上；普通单选题也能在屏上作答。"
resource: "https://github.com/1ikeMcFlurry/harness-whale-companion"
tags: "[esp32, bluetooth, dsh, deepseek-harness, hardware, status-display]"
timestamp: "2026-09-28T23:50:00Z"
---

# harness-whale-companion（DSH 状态 + 单选题 ESP32-C3 蓝牙小屏）

## 它是什么

[harness-whale-companion](https://github.com/1ikeMcFlurry/harness-whale-companion) 是 1ikeMcFlurry 出品的**蓝牙小屏配套**：让 **DeepSeek Harness** 的**运行状态、任务进度、API 余额**显示在一块 **ESP32-C3 蓝牙小屏**上——你不用打开电脑也能瞥一眼 DSH 在不在干活、还剩多少额度。

另外支持**普通单选题作答**：在屏上也能点选选项。

## 为什么用它 / 适合什么场景

- 想给 DSH 配一块**桌面小副屏**，随时瞥一眼进度 / 余额。
- 想把 DSH 状态外置到一块**低成本蓝牙小屏**（ESP32-C3 便宜 + 通用）。
- 想用物理屏做轻量交互（如单选题问答）。
- 喜欢给 AI 代理配一块「**物理仪表盘**」。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | ESP32-C3 蓝牙小屏 + 配套固件 |
| 数据源 | DeepSeek Harness（运行状态 / 任务进度 / API 余额） |
| 交互 | 单选题屏上作答 |
| 连接 | 蓝牙 |
| 出品 | 1ikeMcFlurry |

## 媒体

- ![](https://pbs.twimg.com/media/HTRlZaIboAAibIp.png)

## 相关概念

- [DeepSeek Harness](./term-deepseek-harness.md) — 数据来源（DSH 的运行状态）
- [moto-gps](./tool-moto-gps.md) — 同为「ESP32 蓝牙 + 圆屏」硬件方案（harness-whale-companion 用的 ESP32-C3 更通用）