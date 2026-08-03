---
type: Tool
title: "HalalDL"
description: "Windows 本地优先、基于 yt-dlp 的桌面媒体下载工具，Tauri v2 + React + TypeScript 搭界面，把「粘贴链接、选预设、点下载」做成图形界面；不设账号、不做追踪、不依赖云端，直接亮 yt-dlp 原始输出。"
resource: "https://github.com/Asdmir786/HalalDL"
tags: [windows, tauri, youtube-dl, media-downloader, local-first, react]
timestamp: "2026-08-03T14:09:00Z"
---

# HalalDL

## 它是什么
HalalDL（`Asdmir786/HalalDL`）给 Windows 用户一个**本地优先、基于 yt-dlp 的媒体下载工具**，把命令行那套操作收进「粘贴链接、选预设、点下载」的图形界面。

界面由 Tauri v2 + React + TypeScript 搭起来，**不设账号、不做追踪、不依赖云端**。它内置常见画质和设备预设，支持托盘快速下载和剪贴板自动识别，并把 yt-dlp 的原始输出直接亮出来，不拿模糊的进度条糊弄人。

![HalalDL 界面](https://pbs.twimg.com/media/HOtLzhWakAAkup1.jpg)

## 为什么用它 / 适合什么场景
- **本地优先 + 无追踪**：下载工具本应只发请求给目标网站，不该追踪用户。
- **所见即所得**：把 yt-dlp 原始输出亮出来，进度 / 错误 / 警告全透明。
- **桌面托盘集成**：粘贴链接自动识别 + 托盘菜单快捷下载。
- **Tauri 极小占用**：相比 Electron 应用，启动更快、内存更省。

## 关键能力

| 能力 | 说明 |
|------|------|
| 本地优先 GUI | Tauri v2 + React + TypeScript 桌面应用 |
| 剪贴板识别 | 复制链接后自动捕获，一键下载 |
| 画质 / 设备预设 | 常用画质与设备内建，无需记 yt-dlp 参数 |
| 原始输出 | 直接展示 yt-dlp 输出，不包装模糊进度条 |
| 托盘快捷 | 托盘菜单触发，零窗口切换 |

## 项目链接
- <https://github.com/Asdmir786/HalalDL>

## 相关概念
- [OpenBrowser](./tool-openbrowser.md) — 浏览器代理模式（与「下载 URL 抓取」互补）
- [Pi-Hive](./tool-pi-hive.md) — Pi 扩展的另一种「前端化代理」
- [LightMarkit](./tool-lightmarkit.md) — 同样 Tauri v2 + React + TypeScript 桌面应用形态
