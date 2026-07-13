---
type: Tool
title: "mithka"
description: "一个 Telegram 客户端，UI 设计看上去"似曾相识"（视觉上高度致敬 macOS / iOS 风格），开源。"
tags: "[telegram, client, messenger, open-source, tool]"
timestamp: "2026-07-13T00:00:00Z"
resource: "https://github.com/iebb/mithka"
---

# mithka

一个 **Telegram 客户端**——最大的看点是它的 UI 设计"似曾相识"，是社区里又一个用类似 macOS / iOS 视觉风格重做 Telegram 客户端的项目。

## 它是什么

- 自建的 Telegram 客户端（区别于官方客户端、Telegram Desktop、Telegram for macOS）；
- 开源，可自行部署或改造；
- 主要价值在 UI/UX 重新设计，不在功能增量。

## 为什么用它 / 适合什么场景

- 觉得官方客户端视觉风格不合心意，想用更"原生 macOS 感"的 UI 看 Telegram；
- 想研究"Telegram 协议 + 跨平台 UI 框架"组合的参考实现；
- 想拿一个"长得像 native、但其实是 web/electron 重制版"的项目做二次开发底座。

## 关键能力

| 能力 | 说明 |
|------|------|
| 协议兼容 | 走标准 Telegram 客户端协议 |
| 视觉重制 | 仿 macOS / iOS 风格的窗口、列表、消息气泡 |
| 开源 | 可 fork 自部署 |

## 预览

![](https://pbs.twimg.com/media/HNE2OVoa4AAkywC.jpg)

## 相关概念

- [Plex TUI](tool-plex-tui.md) — 同样是"为已有服务做一种新的客户端形态"的思路（TUI 版 Plex）
- [NaviTUI](tool-navitui.md) — 同类"把图形界面服务重做成终端 UI"实践（Subsonic/Navidrome）
