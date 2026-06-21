---
type: "Tool"
title: "BiliMusic（B 站音乐 → Apple Music 风格桌面播放器）"
description: "用 Electron 把 B 站音乐内容包装成 Apple Music 风格的桌面听歌体验：搜视频、进 UP 主空间、看排行榜全以「曲目」呈现，附歌单 / 歌词 / 播放队列 / 沉浸播放器 / 托盘控制，并适配鸿蒙 PC。"
resource: "https://github.com/qingq77/bilimusic"
tags: "[electron, bilibili, music, desktop, apple-music]"
timestamp: "2026-06-21T00:00:00Z"
---

# BiliMusic（B 站音乐 → Apple Music 风格桌面播放器）

## 它是什么

由 `@QingQ77` 在 2026-06 推荐的 Electron 桌面应用：把 B 站（Bilibili）上散落的「音乐向视频」重新组织成 **Apple Music 风格**的听歌体验 —— 视频被升格为「曲目」，搜索 / UP 主空间 / 排行榜统一以「曲目列表」呈现，而不是塞满视频缩略图。

## 关键能力

| 能力 | 说明 |
|------|------|
| 渲染 | Electron 桌面端，原生体验 |
| 数据源 | B 站视频 / UP 主空间 / 排行榜 |
| 呈现 | 全部映射为「曲目」（track）而不是视频（video） |
| 播放 | 歌单、歌词匹配、播放队列、沉浸式播放器 |
| 系统 | 托盘控制；适配鸿蒙 PC 的 Electron 环境 |

## 适用场景

- 喜欢在 B 站听独立音乐、翻唱、Looper，但嫌弃 B 站官方播放器「视频感」太重。
- 想要一个本地桌面客户端，而不是浏览器 Tab。
- 想在鸿蒙 PC 上统一听歌体验（专门适配）。

## 相关概念

- [Obsidian](tool-obsidian.md) — 另一个「本地优先 + 桌面客户端」的同类思路
- [Forel（macOS 文件夹自动化）](tool-forel-macos.md) — 另一个 Electron 友好的 macOS 小工具