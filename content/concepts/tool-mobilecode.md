---
type: Tool
title: "mobilecode"
description: "opencode 的移动端开源 fork：在 AI 编码会话旁边嵌入实时 iOS Simulator 与 Android emulator，由 serve-avd / serve-sim 提供底层模拟器托管能力。"
resource: "https://github.com/hsandhu/mobilecode"
tags: [mobile, opencode, ios-simulator, android-emulator, ai-coding]
timestamp: "2026-09-06T00:00:00Z"
---

# mobilecode

## 它是什么

[hsandhu/mobilecode](https://github.com/hsandhu/mobilecode) 是 **opencode 的移动端开源 fork**：把 opencode（AI 编码代理）的使用场景带到**移动设备**，并在其旁边嵌入**实时 iOS Simulator 和 Android emulator**，让用户可以在 AI 编码会话里直接看到 App 在 iOS / Android 上的运行效果。

定位：

- **opencode 移动版**：核心是「在手机上 / 平板上用 opencode 编码」。
- **嵌入式模拟器**：底层由作者另外两个开源项目 `serve-avd`（Android 模拟器服务化）和 `serve-sim`（iOS Simulator 服务化）支撑。

## 为什么用它 / 适合什么场景

- 移动端开发者想用 opencode 类 AI 编码工具，但又不能丢下模拟器调试。
- 想从一台设备同时发起编码会话 + 实时看移动端运行结果。
- 关注开源移动端编码工具链——而不是云端 IDE / 在线沙盒。

## 关键能力

| 能力 | 说明 |
|------|------|
| opencode 移动 fork | 在移动设备运行 AI 编码代理 |
| 嵌入式 iOS Simulator | 编码会话旁直接看 iOS 运行效果 |
| 嵌入式 Android emulator | 编码会话旁直接看 Android 运行效果 |
| serve-avd | Android 模拟器的服务化托管 |
| serve-sim | iOS Simulator 的服务化托管 |
| 开源 | 与 opencode 生态一致 |

## 相关概念

- [Claude Code](./tool-claude-code.md) — 同类「终端原生 AI 编码 agent」，mobilecode 是移动端 opencode
- [opencode](https://github.com/sst/opencode) — mobilecode 的上游项目（外部链接）

## 项目链接

- 项目主页：<https://github.com/hsandhu/mobilecode>
