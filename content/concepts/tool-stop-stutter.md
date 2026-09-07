---
type: Tool
title: "Stop Stutter"
description: "macOS 原生 SwiftUI 应用，串流游戏时自动关闭 AWDL 点对点 Wi-Fi，消除 Moonlight / GeForce NOW / Punktfunk / Parsec / Steam Link 等客户端的周期性卡顿。"
resource: "https://github.com/burakgon/stop-stutter"
tags: "[macos, swiftui, gaming, streaming, awdl, network]"
timestamp: "2026-09-07T13:00:00Z"
---

# Stop Stutter

## 它是什么
macOS 原生应用（SwiftUI），解决 macOS 串流游戏时画面周期性卡顿的问题。根因是 AWDL（Apple Wireless Direct Link）点对点 Wi-Fi 与路由器的 Wi-Fi 连接争抢同一块无线网卡。

## 怎么用
- 启动后驻留菜单栏
- 检测到 Moonlight / GeForce NOW / Punktfunk / Parsec / Steam Link 任一串流客户端启动 → 自动开启 Boost（关闭 AWDL）
- 串流客户端退出 → 自动恢复

## 适用场景
- macOS 串流玩游戏（GeForce NOW、Steam Link、Sunshine/Moonlight 等）周期性卡顿
- 其他依赖实时低延迟 Wi-Fi 的应用（远程桌面、AR/VR 串流）

## 关键能力
| 能力 | 说明 |
|------|------|
| 自动触发 | 监听五个主流串流客户端启动/退出事件 |
| 串流 Boost | 关 AWDL 释放无线网卡给 AP 模式连接 |
| 自动恢复 | 退出串流客户端后自动复原 |
| SwiftUI 原生 | 轻量，无外部依赖 |

## 参考
- 原始链接：<https://github.com/burakgon/stop-stutter>

## 相关概念
- [GeForce NOW](https://en.wikipedia.org/wiki/GeForce_NOW) — 主流云游戏服务之一，受 AWDL 干扰
- [Moonlight](https://moonlight-stream.org/) — 开源游戏串流客户端