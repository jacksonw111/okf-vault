---
type: Tool
title: "Highball（Apple Silicon 一键运行 Windows 游戏 + 兼容性数据库）"
description: "gauthierpiarrette/Highball：让 Apple Silicon Mac 用户免于手动配置 Wine / DXMT / D3DMetal / DXVK，一键装好引擎 + Steam 运行 Windows 游戏；配套开放兼容性数据库，下载前就能知道哪些游戏能跑、该用哪个渲染器。"
resource: "https://github.com/gauthierpiarrette/highball"
tags: [apple-silicon, macos, gaming, wine, dxmt, dxvk, steam, compatibility-db]
timestamp: "2026-08-27T07:29:00Z"
---

# Highball

## 它是什么
[gauthierpiarrette/highball](https://github.com/gauthierpiarrette/highball) 是给 **Apple Silicon Mac** 用户的 Windows 游戏运行工具，主要做两件事：

1. **一键安装引擎与 Steam**——免去手动配 **Wine / DXMT / D3DMetal / DXVK** 的折腾；
2. **开放兼容性数据库**——下载前就能查到「这个游戏在 Apple Silicon 上能不能跑 + 该用哪个渲染器（DXMT / DXVK / D3DMetal）」。

相当于 macOS 上的「游戏兼容性 + 自动配置」管家。

## 为什么用它 / 适合什么场景
- 想在 M1 / M2 / M3 / M4 Mac 上跑 Windows 游戏但被 Wine 配置劝退；
- 不想装一个游戏就查一遍"哪个渲染器支持"；
- 想要社区维护的"游戏 × Mac"兼容性数据，而不是 Reddit 帖子瞎猜。

## 关键能力
| 能力 | 说明 |
|------|------|
| 引擎一键安装 | Wine / DXMT / D3DMetal / DXVK 自动配置 |
| Steam 安装 | 一并装好 |
| 兼容数据库 | 开放、下载前可查 |
| 渲染器建议 | 针对每个游戏推荐 DXMT / DXVK / D3DMetal |
| Apple Silicon 优先 | 专为 M 系列芯片优化 |
| 社区驱动 | 兼容性数据由社区维护 |

## 相关概念
- [Apple Hide My Email](term-apple-hide-my-email.md) — Apple 生态工具；Highball 是 Apple Silicon 的"游戏兼容层"工具
- [Tabminal](tool-tabminal.md) — 终端工具，思路不同但都属"为命令行体验省事"的同类工具

## 参考链接
- 项目链接：<https://github.com/gauthierpiarrette/highball>
