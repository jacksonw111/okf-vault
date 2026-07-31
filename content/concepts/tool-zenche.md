---
type: "Tool"
title: "ZENCHE（Tauber01/ZENCHE）"
description: "跨平台本地优先的 Nikon 相机控制与影像传输工具：通过 USB/PTP 控制相机、无线接收影像，并在同一应用中预览、管理、分享；五端原生（macOS / Windows / Android / HarmonyOS / iOS-iPadOS），无 WebView 套壳，覆盖 17 款 EXPEED 6/7 机型。"
resource: "https://github.com/Tauber01/ZENCHE"
tags: "[photography, nikon, ptp, cross-platform, native-ui, image-transfer]"
timestamp: "2026-07-31T20:30:00Z"
---

# ZENCHE（Tauber01/ZENCHE）

[ZENCHE](https://github.com/Tauber01/ZENCHE) 是一套**跨平台、本地优先**的 Nikon 相机控制与影像传输工具。通过 **USB/PTP** 控制相机、无线接收影像，并在同一应用内完成**预览 / 管理 / 分享**。覆盖 macOS、Windows、Android、HarmonyOS 和 iOS/iPadOS **五个原生平台**——不是 WebView 套壳。

## 它是什么

- 控制：USB/PTP 直连 Nikon 相机，调快门、光圈、ISO、白平衡、Picture Control
- 取景：实时 LiveView 直接显示到屏幕上
- 传输：拍完的 NEF / JPEG / HEIF / TIFF 走 FTP、HTTP 或 WebDAV 无线进入应用
- 一体：控制 + 传输 + 预览 + 管理 + 分享，都在一个 app 里

## 为什么用它 / 适合什么场景

| 痛点 | ZENCHE 的回应 |
|------|----------------|
| 多平台开发常用 WebView 套壳，UX 不一致 | 五端各自原生框架 |
| 摄影师想在不掏相机的情况下控制 | 用电脑/手机当遥控取景器 |
| 拍完导入电脑繁琐 | 无线 FTP / WebDAV 直接到 app |
| 现场传输 Nikon RAW 难 | NEF / HEIF / TIFF 都支持 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 五端原生 | macOS、Windows、Android、HarmonyOS、iOS/iPadOS |
| 17 款机型覆盖 | Nikon EXPEED 6 / 7 系列 |
| USB/PTP 控制 | 调快门、光圈、ISO、白平衡、Picture Control |
| 实时取景 | LiveView 直接显示 |
| 多协议传输 | FTP / HTTP / WebDAV |
| 多格式支持 | NEF / JPEG / HEIF / TIFF |
| 一体化 app | 控制 + 预览 + 管理 + 分享 |

## 相关概念

- [herdr-browser](./tool-herdr-browser.md) — 终端里嵌浏览器，与 ZENCHE 同属「让客户端原生化不靠 WebView」的工程精神
- [Pixshell](./tool-pixshell.md) — 跨平台 SSH/SFTP 客户端，五端原生或 Swift/WPF 同源，与 ZENCHE 同属「跨平台原生工具栈」
- [Article-tools](./tool-article-tools.md) — 纯前端 HTML 工具，ZENCHE 反向：用原生而非 Web
- [Everos](./tool-everos.md) — 若相关可对照
