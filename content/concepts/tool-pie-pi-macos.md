---
type: "Tool"
title: "Pie（Pi Coding Agent 的 macOS 桌面客户端）"
description: "hieunc229 写的 SwiftUI 原生 macOS 客户端，为 Pi Coding Agent 当桌面外壳；每个活跃会话跑一个 pi --mode rpc 进程。"
resource: "https://github.com/hieunc229/Pie"
tags: "[pi-coding-agent, macos, swiftui, native-app, rpc, agent-shell, desktop-client]"
timestamp: "2026-09-17T09:57:00Z"
---

# Pie（Pi Coding Agent 的 macOS 桌面客户端）

## 它是什么

[hieunc229/Pie](https://github.com/hieunc229/Pie) 是 **hieunc229** 写的 SwiftUI 原生 macOS 客户端。它**不是 fork**，而是为 [Pi Coding Agent](./tool-pi-coding-agent.md) 当桌面外壳——让长跑的编码会话、文件审查不必挤在终端里。

## 关键架构

- 每个活跃会话启动一个 `pi --mode rpc` 子进程（RPC 模式）
- 消息、凭据、扩展**全归 Pi 管**
- 应用自身**只存**：
  - 最近项目列表
  - 置顶（pinned）会话
  - 草稿
  - 窗口布局

## 关键能力

| 能力 | 说明 |
|------|------|
| 原生 SwiftUI | 非 Electron / Tauri，体积小、跟手 |
| 多会话并行 | 每个会话独立 RPC 进程，互不干扰 |
| 不 fork Pi | 升级 Pi 时 Pie 自动跟随，零维护成本 |
| 本地优先 | 没有云端依赖，凭据不离开本机 |

## 适合什么场景

- 经常跑长会话（多步编码 / 长上下文审查）、不想一直盯终端的开发者。
- 想给 Pi Coding Agent 一个「正经桌面应用」外观的 macOS 用户。
- 想学习 SwiftUI + RPC 架构组合的 macOS 开发者。

## 与相关概念的关系

- [Pi Coding Agent](./tool-pi-coding-agent.md) — Pie 是 Pi 的桌面外壳，两者关系是「外壳 vs 内核」。

## 参考

- 项目链接：<https://github.com/hieunc229/Pie>

![preview](https://pbs.twimg.com/media/HSYvpBVb0AATQPG.jpg)
