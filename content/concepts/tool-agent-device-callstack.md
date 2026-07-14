---
type: "Tool"
title: "agent-device（callstack/agent-device）"
description: "Callstack 开源的移动端自动化 CLI,给 coding agent 操作真实 iOS / Android App 的能力:打开 App、读无障碍快照、按语义 ref 点击 / 输入、截图、录屏、抓日志 / 性能,还可存成可复放的 .ad 脚本。"
resource: "https://github.com/callstack/agent-device"
tags: "[mobile-automation, ios, android, coding-agent, accessibility, verification, replay]"
timestamp: "2026-07-14T15:42:46Z"
---

# agent-device

[agent-device](https://github.com/callstack/agent-device) 是 **Callstack** 开源的「面向 AI coding agent 的移动端自动化 CLI」。官方定位: **Mobile app verification for AI agents**——不是取代传统测试框架,而是给 agent 操作真实 App 的能力。

## 关键能力

| 能力 | 说明 |
|------|------|
| 启动 App | 直接拉起目标 App(原生 + Expo + Flutter) |
| 无障碍快照 | 读 accessibility tree,获语义结构 |
| 语义 ref 点击 / 输入 | 不靠坐标,直接定位 ref 元素 |
| 截图 / 录屏 | 给 VLM agent 当眼睛 |
| 日志 / 性能采集 | 排错与压测证据 |
| .ad 脚本 | 把探索过程存成可复放脚本,后续可重跑 |

## 适用平台

| 平台 | 支持 |
|------|------|
| iOS 真机 | ✓ |
| iOS 模拟器 | ✓ |
| Android 真机 | ✓ |
| Android 模拟器 | ✓ |
| Expo App | ✓ |
| Flutter App | ✓ |
| 原生 App | ✓ |

## 适合什么场景

- 给 coding agent 加**真机 / 模拟器视觉验证**:自动截图 + OCR 比对。
- Coding agent 改完前端的 RN / Flutter 代码,自动跑「点击 X → 验证页跳到 Y」闭环。
- 把**人工回归测试**脚本化:录制一次,后续 agent 可反复播放。

## 与同类资源的差别

| 资源 | 特征 | agent-device |
|------|------|--------------|
| Appium / XCTest | 传统测试框架 | 官方说「不是替代品」,专为 agent 设计 |
| sim-use | 模拟器 / 设备屏幕观察 | 同类,但 sim-use 强调「读无障碍树省 token」;agent-device 强调「.ad 复放 + iOS/Android Expo/Flutter 全平台」 |
| Detox | RN 端到端测试 | 偏向测试工程师;agent-device 偏向 AI agent |

## 参考链接

- [项目仓库](https://github.com/callstack/agent-device)

## 相关概念

- [sim-use](./tool-sim-use.md) — 让 AI agent 观察 iOS / Android 模拟器屏幕,读无障碍树省 16× tokens;agent-device 是更「行动版」的同类工具
- [page-agent](./tool-page-agent.md) — 浏览器端的 GUI Agent,agent-device 是其在移动端的对应物
