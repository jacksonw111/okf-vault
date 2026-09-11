---
type: "Tool"
title: "Roam-Control（iPhone 开发测试位置模拟工具）"
description: "给 iPhone 提供开发测试用的位置模拟工具：在一个 Apple Maps 界面里选点、测步行路线并切换上报位置。"
resource: "https://github.com/seanhowarthdev/Roam-Control"
tags: "[ios, location, mock, testing, swift, devtool]"
timestamp: "2026-09-11T22:00:00Z"
---

# Roam-Control

## 它是什么

[seanhowarthdev/Roam-Control](https://github.com/seanhowarthdev/Roam-Control) 是一个**iOS 端的位置模拟工具**，专为开发 / 测试场景设计：把模拟功能包进一个 **Apple Maps** 风格的界面，可在地图上选点、画步行路线、并随时切换当前上报位置，覆盖大部分需要「假装在别处」的 iOS 测试用例。

## 为什么用它 / 适合什么场景

- 开发 LBS / 出行 / 外卖 / 健身路线类 App 时模拟用户位置。
- 在不同位置回归测试地图 UI、定位权限逻辑、距离提示等。
- 不愿用 Xcode 自带的 GPX 路线模拟（需要重启模拟器 / 改文件）。

## 关键能力

| 能力 | 说明 |
|------|------|
| Apple Maps UI | 熟悉的原生地图界面，选点 / 路线交互直观 |
| 模拟位置上报 | 一键切换当前上报坐标 |
| 路线模拟 | 画一条步行路线，沿线逐步移动 |
| 测试友好 | 开发调试期注入位置，无需改 GPX 文件 |
| 开源 | Swift 实现，可二次定制 |

## 参考链接

- 项目仓库：<https://github.com/seanhowarthdev/Roam-Control>

## 媒体

- ![](https://pbs.twimg.com/media/HRvhCYaaIAAp90E.jpg)

## 相关概念

- [docker-android](./tool-docker-android.md) — Android 端的远程模拟器 + adb 容器化方案
- [mobile-harness](./tool-mobile-harness.md) — 安卓端 AI 编码套件
</content>
</invoke>