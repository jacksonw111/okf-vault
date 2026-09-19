---
type: "Tool"
title: "Mobile-Jev（Mobilerun 云真机执行手机操作的 agent）"
description: "让 Jev 模型直接在 Mobilerun 云真机上执行手机操作指令的独立 agent，无需 ADB 连接。"
resource: "https://github.com/droidrun/mobile-jev"
tags: "[jev, mobile-agent, cloud-device, mobilerun, android, automation]"
timestamp: "2026-09-19T16:00:00Z"
---

# Mobile-Jev（Mobilerun 云真机执行手机操作的 agent）

## 它是什么

[droidrun/mobile-jev](https://github.com/droidrun/mobile-jev) 是一个**让 Jev 模型在云端真机（不是模拟器、不是 ADB 链接的本机）上完成手机操作指令**的独立 agent。它把「Jev 风格的并行打分决策」嫁接到 droidrun 的 Mobilerun 真机云上，让 agent 直接调用远端 Android 真机去执行「打开 XX 应用 → 点 YY 按钮」这类指令。

## 为什么用它 / 适合什么场景

- 需要在**云上批量操作真机 Android**（测试 / 数据采集 / 演示），又不想自己拉 USB 连 ADB。
- 想把 Jev 模型当打分器，配合 droidrun 的真机调度框架做 phone-use。
- 不想为单次自动化任务在本地维护一套 Android 调试链路的人。

## 关键能力

| 能力 | 说明 |
|------|------|
| 云端真机执行 | 走 Mobilerun 真机云，不需要 ADB / 本地设备 |
| Jev 决策打分 | 用 Jev 并行打分范式选下一步动作 |
| 独立 agent 形态 | 与 browser-use jev-ultrafast 同源思路，但目标从浏览器换到手机 |
| 适合远程调度 | 后台任务、CI / 持续集成场景都能接入 |

## 与相关概念的关系

- [JEV Ultrafast（browser-use 极速浏览器自动化）](./tool-jev-ultrafast.md) — 同一个 Jev「打分式」决策家族，但目标从浏览器自动化换到了云端真机操作
- [DSH Mobile（移动端 AI agent）](./tool-dsh-mobile.md) — 与 mobile-jev 同样把 AI 操作落到手机，但 dsh-mobile 偏本机/远程执行链，不依赖云真机

## 参考

- 项目链接：<https://github.com/droidrun/mobile-jev>
- 原始推文：<https://x.com/QingQ77/status/2101141225944252731>