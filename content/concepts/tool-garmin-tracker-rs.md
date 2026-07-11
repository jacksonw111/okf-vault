---
type: Tool
title: "Garmin Tracker RS"
description: "Emiliopg91 开源的 Tauri 2 跨平台桌面应用，Rust 后端 + React 19 + TypeScript 前端，通过 USB（MTP）从 Garmin 手表下载活动 .FIT 文件，全程无需云端账号。"
resource: "https://github.com/Emiliopg91/garmin-tracker-rs"
tags: "[garmin, fitness, tauri, rust, react, mtp, desktop]"
timestamp: "2026-07-11T20:00:00Z"
---

# Garmin Tracker RS

## 它是什么

`Emiliopg91/garmin-tracker-rs` 是一个**离线的 Garmin 手表活动导出工具**：用 Tauri 2 构建的跨平台桌面应用，Rust 后端 + React 19 + TypeScript 前端。

连接 Garmin 手表后，通过 USB（MTP 协议）直接读取手表里的 `.FIT` 活动文件，全程**不走 Garmin Connect 云端**。

## 为什么用它 / 适合什么场景

- 不想把跑步 / 骑行 / 游泳等训练数据交给 Garmin 云。
- 对隐私 / 数据主权敏感，希望活动文件**本地直传**到 Strava / TrainingPeaks / 自建分析工具。
- 想要一个轻量 GUI，而不是 CLI。
- 已有 Garmin Connect 账号但希望「备份一份到本地」。

## 关键能力

| 能力 | 说明 |
|------|------|
| USB 直连 | MTP 协议读 `.FIT` 文件，不走云端 |
| 跨平台 | Tauri 2 同时支持 macOS / Windows / Linux |
| 离线 | 全程无云端账号 / 无 token / 无登录 |
| 现代栈 | Rust + React 19 + TypeScript |
| 活动文件 | `.FIT`（Garmin 标配，可被 Strava / TrainingPeaks 接受） |

## 媒体参考

- 项目截图：

![Garmin Tracker RS UI](https://pbs.twimg.com/media/HM1bt7IasAEDlgX.png)
![Garmin Tracker RS 运行截图](https://pbs.twimg.com/media/HM1buCwaMAArUbO.png)

## 相关概念

- [Smart Remarkable](tool-smart-remarkable.md) — 同样走「本地直连硬件」路线的工具
- [MacMTP](tool-macmtp.md) — macOS 通过 MTP 协议与 Android 互传文件

## 项目链接

- 项目仓库：<https://github.com/Emiliopg91/garmin-tracker-rs>