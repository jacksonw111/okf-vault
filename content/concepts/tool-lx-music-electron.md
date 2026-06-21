---
type: "Tool"
title: "LX Music Desktop（跨平台 Electron 音乐播放器）"
description: "基于 Electron 的跨平台桌面音乐播放器（Windows / macOS / Linux）：本地端扫描本地文件夹建曲库，支持按歌/专辑/歌手浏览、内嵌逐词歌词与翻译、标签编辑、下载管理；在线端依赖用户自行导入的 LX JS 音源脚本实现搜索、歌单、排行榜、每日推荐，与 lx-music-desktop 生态完全兼容。"
resource: "https://t.co/3ogtWT01Tl"
tags: "[electron, music, desktop, lx-music, lyrics, cross-platform]"
timestamp: "2026-06-21T16:06:00Z"
---

# LX Music Desktop（跨平台 Electron 音乐播放器）

## 它是什么

一个基于 **Electron** 的跨平台桌面音乐播放器（Windows / macOS / Linux）。**本地播放** 走「扫描本地文件夹建曲库」的路线，按歌曲 / 专辑 / 歌手浏览，内嵌歌词（支持逐词歌词和翻译）、标签编辑、下载管理；**在线播放** 通过用户自行导入的 LX JS 音源脚本实现搜索、歌单、排行榜、每日推荐 —— 与 [lx-music-desktop](https://github.com/lyswhut/lx-music-desktop) 生态完全兼容。

## 为什么用它 / 适合什么场景

- 想用 LX 音源体系（社区维护、覆盖各大平台），但想换一个更现代 / 更可定制的桌面壳。
- macOS / Linux 用户原来用 LX Music Desktop 体验不佳，想要 Electron 的跨平台一致性。
- 既要本地曲库管理（歌词 / 标签 / 下载），又想要在线流媒体入口。

## 关键能力

| 能力 | 说明 |
|------|------|
| 平台 | Electron，跨 Windows / macOS / Linux |
| 本地曲库 | 扫描本地文件夹，按歌 / 专辑 / 歌手浏览 |
| 歌词 | 内嵌歌词，逐词时间轴 + 翻译 |
| 标签 | 编辑本地文件元数据 |
| 下载 | 内置下载管理 |
| 在线音源 | 用户自行导入 LX JS 脚本，搜索 / 歌单 / 排行榜 / 每日推荐 |
| 生态 | 兼容 lx-music-desktop 的音源脚本生态 |

## 与 BiliMusic 的差异

- BiliMusic：把 B 站音乐内容升格为 Apple Music 风格的播放体验。
- LX Music Desktop：跨平台通用桌面壳 + 接入 LX 社区音源生态（覆盖多平台）。

## 媒体

- 截图：![](https://pbs.twimg.com/media/HLOpBsQbAAAyNWb.jpg)

## 相关概念

- [BiliMusic](tool-bili-music-electron.md) — 同样是 Electron 桌面音乐客户端，但定位在 B 站内容升格
- [Forel](tool-forel-macos.md) — 另一个 macOS 本地优先小工具