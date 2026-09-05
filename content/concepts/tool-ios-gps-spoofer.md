---
type: Tool
title: "iOS-GPS-Spoofer"
description: "macOS 开源工具，通过 Apple 开发者位置模拟服务修改已配对 iPhone 的 GPS 定位，底层经 pymobiledevice3 走加密 CoreDevice 通道"
resource: "https://github.com/SegFault42/iOS-GPS-Spoofer"
tags: [ios, gps, spoof, macos, pymobiledevice3, coredevice]
timestamp: 2026-09-05T15:00:00Z
---

# iOS-GPS-Spoofer

## 它是什么
`SegFault42/iOS-GPS-Spoofer` 是一款运行在 **macOS** 上的开源工具，通过 **Apple 开发者位置模拟服务**（与 Xcode Simulate Location 同机制）修改已配对 iPhone 的 GPS 定位。底层经 `pymobiledevice3` 走加密 **CoreDevice** 通道传输，与 Xcode 走的是同一条路径。

## 为什么用它 / 适合什么场景
- QA / 测试场景：需要让 App 在不同地理位置下表现正确（不在 macOS 主机上模拟，而是改真 iPhone）。
- 自动化：批量给真机注入位置，跑地理围栏 / 区域通知测试。
- 不想依赖 Xcode Simulate Location GUI，希望命令式自动化。

## 关键能力
| 能力 | 说明 |
|------|------|
| Apple 开发者位置模拟 | 与 Xcode Simulate Location 同机制 |
| pymobiledevice3 通信 | 通过加密 CoreDevice 通道与 iPhone 通信 |
| macOS 主机 | 在 macOS 上跑，命令式控制已配对 iPhone |
| 真机定位注入 | 修改真实已配对 iPhone 的 GPS 而非模拟器 |

## 媒体
- ![](https://pbs.twimg.com/media/HRVsEo3bkAA2MVY.jpg)

## 相关概念
- [原始链接](https://github.com/SegFault42/iOS-GPS-Spoofer)