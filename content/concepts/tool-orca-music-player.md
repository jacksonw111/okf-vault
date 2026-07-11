---
type: Tool
title: "Orca Music Player（Svelte 5 + Tauri 本地音乐播放器）"
description: "shubham-pathak1 用 Svelte 5 + Tauri 2 + Rust 构建的本地音乐播放器，alpha 阶段，本地目录扫描建库，支持 MP3 / FLAC / M4A / WAV / OGG / OPUS / AIFF 等格式，rodio 音频引擎支持交叉淡入。"
resource: "https://github.com/shubham-pathak1/orca"
tags: "[music, audio, svelte, tauri, rust, desktop, local]"
timestamp: "2026-07-11T20:00:00Z"
---

# Orca Music Player（Svelte 5 + Tauri 本地音乐播放器）

## 它是什么

`shubham-pathak1/orca` 是一个**本地音乐播放器**，用 Svelte 5（前端）+ Tauri 2（壳）+ Rust（后端）构建，目前处于 **alpha 阶段**。

把本地音乐目录加进来，它会即时扫描建库，识别：

- MP3 / FLAC / M4A / WAV / OGG / OPUS / AIFF / AIF

音频引擎由 **rodio** 驱动，**支持交叉淡入**（cross-fade），切换歌时不会硬切。

> ⚠️ 同名项目区分：本仓库作者是 `shubham-pathak1`，定位是「音乐播放器」。另有 [`stablyai/orca`](tool-orca-coding-ide.md) 是「Coding IDE 套壳」。两者同名但完全无关。

## 为什么用它 / 适合什么场景

- 想要一个**完全本地、不联网、不上传歌单**的桌面音乐播放器。
- 想用现代栈（Svelte 5 + Tauri 2）替代老旧的 Electron 音乐 App。
- 库不大（Windows 上日常使用 OK，但**未在 5,000+ 曲目曲库上压测**）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 现代栈 | Svelte 5 + Tauri 2 + Rust |
| 格式全 | MP3 / FLAC / M4A / WAV / OGG / OPUS / AIFF / AIF |
| 即时建库 | 本地目录扫描立即出库 |
| 交叉淡入 | rodio 引擎切歌淡入淡出 |
| 本地优先 | 不联网、不上传 |

## 媒体参考

- 项目截图：

![Orca Music Player UI](https://pbs.twimg.com/media/HM1-EzibcAAPMyN.jpg)

## 相关概念

- [Orca（stablyai）](tool-orca-coding-ide.md) — 同名但不同作者的 Coding IDE 套壳
- [Lx Music (Electron)](tool-lx-music-electron.md) — 另一款本地音乐播放器，可对比选型

## 项目链接

- 项目仓库：<https://github.com/shubham-pathak1/orca>