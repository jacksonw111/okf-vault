---
type: "Tool"
title: "QuestLHSync（Quest / Steam Frame 无 tracker 对齐 Lighthouse）"
description: "CreoleVR 开源：让 Quest 或 Steam Frame 用自身摄像头看到 SteamVR 基站的激光闪光，把 lighthouse 空间与头显空间对齐——不需要在头上绑 tracker，也不需要 SpaceCalibrator。"
resource: "https://github.com/CreoleVR/QuestLHSync"
tags: "[vr, quest, steamvr, lighthouse, tracking, calibration]"
timestamp: "2026-10-07T10:25:00Z"
---

# QuestLHSync

## 它是什么

[QuestLHSync](https://github.com/CreoleVR/QuestLHSync) 是 **CreoleVR** 开源的 **VR 跨空间校准工具**——让 **Quest** 或 **Steam Frame** 用自身摄像头看到 **SteamVR 基站（lighthouse）** 的激光闪光，把 **lighthouse 空间** 与 **头显空间** 对齐。

定位是「**无 tracker 的跨生态校准**」——传统方案需要在头上绑 tracker 或装 SpaceCalibrator 才能把 SteamVR 的基站定位数据接入 Quest / Steam Frame，这套方案完全省掉。

## 为什么用它 / 适合什么场景

- **Quest 用户** 想用 SteamVR 的 lighthouse 基站定位（精度高、追踪范围大）
- **Steam Frame 用户** 想跟现有的 SteamVR 生态设备（控制器 / 第三方 tracker）共享同一空间
- **不想在头上绑额外硬件** 的 VR 玩家
- **VR 跨平台玩家** 想统一追踪坐标系

## 关键能力

| 能力 | 说明 |
|------|------|
| 输入 | 头显摄像头 + SteamVR 基站激光闪光 |
| 输出 | lighthouse 空间与头显空间对齐 |
| 硬件要求 | 无需头显外接 tracker |
| 软件要求 | 无需 SpaceCalibrator |
| 支持设备 | Quest / Steam Frame |

## 参考链接

- 项目仓库：<https://github.com/CreoleVR/QuestLHSync>

## 媒体

- ![](https://pbs.twimg.com/media/HUADxeoaYAAvv9A.png)

## 相关概念

无相关概念需要链入。
