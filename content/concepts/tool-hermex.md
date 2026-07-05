---
type: "Tool"
title: "Hermex（iOS 上的 Hermes AI 控制端）"
description: "用 SwiftUI 写的 iOS 应用，让你从 iPhone 操控自托管的 Hermes AI 代理：实时流式聊天、管理定时任务、浏览技能与文件系统、查看内存与用量分析。"
tags: "[ios, swiftui, mobile, ai-agent, hermes, remote-control]"
timestamp: "2026-07-05T00:00:00Z"
resource: "https://github.com/uzairansaruzi/hermex"
---

# Hermex（iOS 上的 Hermes AI 控制端）

## 它是什么

[`Hermex`](https://github.com/uzairansaruzi/hermex) 是一个用 **SwiftUI** 写的 iOS 应用，作为 [Hermes AI 代理](https://github.com/uzairansaruzi/hermes) 的**移动端控制端**——在 iPhone 上即可与自托管的 Hermes 代理进行实时聊天，并管理它的定时任务、技能、文件系统与用量。

![Hermex 截图](https://pbs.twimg.com/media/HMbc96uasAACyxy.jpg)

## 关键能力

| 能力 | 说明 |
|------|------|
| 实时流式聊天 | 与自托管 Hermes 代理对话，响应流式返回 |
| 定时任务管理 | 在手机上创建 / 暂停 / 删除代理的定时任务 |
| 技能浏览 | 查看代理装载的所有 skill，可启用 / 禁用 |
| 文件系统浏览 | 远程查看代理工作目录的文件树 |
| 内存与用量分析 | 监控代理的内存占用、token 用量等指标 |
| SwiftUI 原生 | iOS 14+ 原生体验，适配 iPhone / iPad |

## 适用场景

- 出门在外用 iPhone 让家里的 Hermes 代理跑任务
- 在通勤路上快速查看昨晚定时任务的执行结果
- 临时想给代理加个新 skill，不想开电脑
- 跟踪代理的健康指标（内存 / 用量），及时发现异常

## 参考链接

- [项目链接](https://github.com/uzairansaruzi/hermex)
- [Hermes 代理原项目](https://github.com/uzairansaruzi/hermes)

## 相关概念

- [happier](tool-happier.md) — 跨设备 AI 编码客户端（电脑 ↔ 手机），与 Hermex 同样解决「离开电脑也要管 AI 代理」的问题，但面向编码场景
- [shuangzi-xubei](tool-shuangzi-xubei.md) — iPhone 桌面小组件，锁屏看 Claude Code / Codex 额度