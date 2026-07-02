---
type: Tool
title: "sim-use"
description: "命令行工具，让 AI agent 观察与操作 iOS 模拟器与 Android 设备屏幕（看屏、点按、打字、滑动、硬件键）；读无障碍树输出 token 紧凑摘要（省 16× tokens）、@N 别名缓存加速点按；iOS 走模拟器 HID 管道，Android 走 AccessibilityService，接口统一。"
resource: "https://github.com/lycorp-jp/sim-use"
tags: "[mobile, automation, ai-agent, ios, android, cli, accessibility]"
timestamp: "2026-07-02T15:35:00Z"
---

# sim-use

## 它是什么
命令行工具（CLI），给 AI Agent 提供观察和操作 iOS 模拟器 + Android 设备屏幕的能力。让 Agent 能看屏幕、点按钮、打字、滑动、按硬件键。

## 为什么用它 / 适合什么场景
- 移动端自动化测试 / Agent 验证开发效果。
- Agent 自己开发的 App 在模拟器上跑，你想让 Agent「看到」并迭代 UI。
- 想把 GUI Agent 能力封装成可被任意 Agent 调用的统一 CLI。

## 关键能力
| 能力 | 说明 |
|------|------|
| 平台 | iOS 模拟器 + Android 真机 / 模拟器 |
| 操作 | 看屏 / 点按 / 打字 / 滑动 / 硬件键 |
| 无障碍读取 | 直接读无障碍树 |
| Token 优化 | 输出摘要比原始 JSON 省 16× tokens |
| 别名缓存 | `@N` 别名机制，重复点同一元素时直接复用 |
| iOS 实现 | 模拟器 HID 管道 |
| Android 实现 | AccessibilityService |
| 接口统一 | iOS / Android 共一套 CLI |
| 形态 | 命令行工具 |

## 相关概念
- [page-agent（阿里浏览器端 GUI Agent）](tool-page-agent.md) — 同类「让 AI 操作界面」思路；sim-use 专注移动端，page-agent 专注浏览器端
- [memgui-agent](tool-memgui-agent.md) — 移动端 GUI Agent（同为手机屏幕）；sim-use 偏 CLI，memgui-agent 偏 SDK + 模型架构
- [Obscura（Rust 无头浏览器）](tool-obscura-headless-browser.md) — 同类「为 Agent 提供界面交互能力」思路；sim-use 在手机端，Obscura 在浏览器端

## 项目链接
- 项目主页：<https://github.com/lycorp-jp/sim-use>