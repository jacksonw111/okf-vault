---
type: Tool
title: "dsh-ios（ZSeven-W/dsh-ios）"
description: "DSH 插件：把一台真的 iOS 模拟器塞进对话里，Agent 能构建 / 点按 / 看日志，侧边栏实时显示屏幕，连 USB 真机也用同套命令驱动"
resource: "https://github.com/ZSeven-W/dsh-ios"
tags: "[dsh, deepseek-harness, ios, simulator, agent-plugin, ui-testing]"
timestamp: "2026-08-22T11:12:00Z"
---

# dsh-ios

## 它是什么
[`ZSeven-W/dsh-ios`](https://github.com/ZSeven-W/dsh-ios) 是一个 **DeepSeek Harness (DSH)** 插件，把一台**真**的 iOS 模拟器塞进 Agent 对话里：Agent 能构建、点按、看日志，用户也能在侧边栏实时盯着屏幕上手操作；USB 插着真 iPhone 时，同一套命令能直接驱动真机。

## 为什么用它 / 适合什么场景
- Coding Agent 写完 iOS 应用却「看不见它跑起来」——把模拟器直接暴露给 Agent 即可眼见为实。
- 想做 iOS UI 自动化 / 演示，但不愿为了一个截图再切出 Xcode。
- 想让 Agent **真实交互**：点 / 滑 / 输入文本，再读屏幕状态做下一步判断。

## 关键能力
| 能力 | 说明 |
|------|------|
| 真模拟器 | 沙盒内启动真正 iOS Simulator 而非录屏 / 截图工具 |
| Agent 可交互 | Agent 能构建、点按、看日志、读屏幕 |
| 实时侧边栏 | 用户能看到屏幕与 Agent 同步操作 |
| 真机驱动 | USB 接入 iPhone 后同一命令集直接操控 |
| 统一指令 | 模拟器与真机同套命令，无需分两套脚本 |

## 媒体
- ![](https://pbs.twimg.com/media/HQT-jHAbgAADITs.jpg)

## 相关概念
- [sim-use](./tool-sim-use.md) — CLI 让 AI Agent 观察与操作 iOS 模拟器与 Android 设备屏幕，读无障碍树省 16× tokens
- [pi-computer-use](./tool-pi-computer-use.md) — 给 pi harness 加 computer-use 能力，支持 Mac / Windows
- [agent-device（Callstack）](./tool-agent-device-callstack.md) — 给 coding agent 操作 iOS / Android 真实 App 的 CLI
