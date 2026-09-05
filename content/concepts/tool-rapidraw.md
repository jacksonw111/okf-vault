---
type: Tool
title: "RapidRaw"
description: "20MB 以内的跨平台 RAW 修图工具，Rust 后端 + WGSL 图像管线 + React + Tauri 界面，32 位全管线 GPU 即时渲染"
resource: "https://github.com/cybertimon/rapidraw"
tags: [raw, photo, editor, rust, wgsl, tauri, gpu, cross-platform]
timestamp: 2026-09-05T15:00:00Z
---

# RapidRaw

## 它是什么
`cybertimon/rapidraw` 是一款**轻量跨平台 RAW 修图工具**：作者 18 岁时为方便自己拍片所写，目标是不装臃肿的 Lightroom 也能直接开工。它用 **Rust** 做后端、**WGSL** 写 GPU 图像管线、**React + Tauri** 拼界面，二进制不到 20MB，可在 Windows / macOS / Linux / Android 四个平台运行。

## 为什么用它 / 适合什么场景
- 摄影师想快速处理 RAW，又不愿安装数百 MB 的 Lightroom / Capture One。
- 喜欢原生 GPU 实时反馈（拉曝光、压高光、调曲线都是即时更新）。
- 跨平台统一体验：Mac / Windows / Linux / Android 一份二进制搞定。

## 关键能力
| 能力 | 说明 |
|------|------|
| 体积极小 | 安装包不到 20MB，远小于 Lightroom |
| GPU 全管线 | 32 位图像管线全部跑在 GPU 上（WGSL 着色器），即时反馈 |
| 跨平台 | Windows / macOS / Linux / Android 一致体验 |
| Rust + Tauri | 后端 Rust、桌面壳 Tauri、UI React，技术栈现代且轻量 |
| 基础调参 | 曝光 / 高光 / 曲线等核心 RAW 调整 |

## 媒体
- ![](https://pbs.twimg.com/media/HRW6_bcbgAA0pt8.jpg)

## 相关概念
- [原始链接](https://github.com/cybertimon/rapidraw)