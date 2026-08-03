---
type: Tool
title: "FaceLogin (EthanZer0)"
description: "让不支持 Windows Hello 的电脑也能刷脸解锁：锁屏后看一眼摄像头就进系统，本地账户和微软账户都能用，靠眨眼检测 + 静默反欺诈挡住照片和视频攻击。"
resource: "https://github.com/EthanZer0/FaceLogin"
tags: [windows, face-recognition, login, security, liveness, anti-spoofing]
timestamp: "2026-08-03T12:17:00Z"
---

# FaceLogin (EthanZer0)

## 它是什么
FaceLogin（`EthanZer0/FaceLogin`）**让不支持 Windows Hello 的电脑也能刷脸解锁**：锁屏后看一眼摄像头就进系统，本地账户和微软账户都能用，靠眨眼检测 + 静默反欺诈挡住照片和视频攻击。

![FaceLogin 截图](https://pbs.twimg.com/media/HOsyO_5aoAA32NV.jpg)

## 为什么用它 / 适合什么场景
- **老硬件解锁**：很多老款 PC / 笔记本的红外 / ToF 摄像头规格不够，Windows Hello 装不上，本工具补这块。
- **账户全兼容**：本地账户 + 微软账户都支持。
- **抗欺诈**：眨眼检测 + 静默反欺诈，对抗照片 / 视频回放攻击。

## 关键能力

| 能力 | 说明 |
|------|------|
| 刷脸解锁 | 锁屏后看一眼摄像头即登入 |
| 眨眼检测 | 活体检测，拒绝静态照片 |
| 静默反欺诈 | 视频回放 / 数字人攻击都挡 |
| 账户兼容 | 本地账户 + 微软账户 |

## 项目链接
- <https://github.com/EthanZer0/FaceLogin>

## 相关概念
- [HeartRateMonitor (Compose UI)](./tool-heart-rate-monitor-composeui.md) — 同样用 Android Compose / 桌面摄像头采集的另一类硬件交互
- [Voyage Camera Recorder](./tool-voyage-camera-recorder.md) — 摄像头 + 录制场景下的工具（同类相机硬件交互）
