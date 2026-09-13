---
type: "Tool"
title: "mobai-dev（云端 coding agent 跑 iOS 开发）"
description: "让 Cloud coding agent 从 Linux 沙箱里开发 iOS App：预览 SwiftUI / RN / Flutter、用 CI 跑 Xcode 构建、驱动 iOS 模拟器、装到真机驱动，全程都在 Linux 云上。"
resource: "https://github.com/MobAI-App/mobai-dev"
tags: "[ios, linux, cloud-agent, swiftui, react-native, flutter, xcode]"
timestamp: "2026-09-12T23:25:00Z"
---

# mobai-dev（云端 coding agent 跑 iOS 开发）

## 它是什么

[MobAI-App/mobai-dev](https://github.com/MobAI-App/mobai-dev) 让 **Cloud coding agent 从 Linux 沙箱里开发 iOS App**——预览 SwiftUI / RN / Flutter、用 CI 跑 Xcode 构建、驱动 iOS 模拟器、装到真机驱动，**全程都在 Linux 云上**。

## 为什么用它 / 适合什么场景

- 团队都用 Linux / WSL，但 iOS 工程传统上要 Mac。
- 想让 coding agent 在云端沙箱里完成 iOS 开发全链路，不必为它准备 Mac。
- 远程 / 多 agent 协作时统一在 Linux 沙箱里跑。

## 关键能力

| 能力 | 说明 |
|------|------|
| SwiftUI 预览 | Linux 沙箱里跑 |
| React Native 预览 | Linux 沙箱里跑 |
| Flutter 预览 | Linux 沙箱里跑 |
| Xcode CI 构建 | Linux 触发 |
| iOS 模拟器 | Linux 远程驱动 |
| 真机驱动 | 把 app 装到 iPhone 跑测试 |

## 项目链接

- 仓库：<https://github.com/MobAI-App/mobai-dev>

## 相关概念

- [Cloud coding agent](./term-cloud-coding-agent.md) — mobai-dev 是这一类在 iOS 域的扩展（term 暂未独立收录，留概念链接占位）
- [Sandbox / 沙箱](./term-sandbox.md) — mobai-dev 的核心依赖（term 暂未独立收录，留概念链接占位）