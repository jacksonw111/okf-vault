---
type: Tool
title: "OneSend（扫传：无账号 / 无配对 / 无服务器，屏幕当传输线）"
description: "解决无账号、无配对、无服务器环境下两台设备互传文件的问题——发送端把文件编码成持续变化的光学码显示在屏幕，接收端用摄像头连续扫描在本地还原，全程不需要网络传输。"
resource: "https://github.com/makerjackie/onesend"
tags: [file-transfer, offline, optical, no-account, p2p, qrcode, screen-camera]
timestamp: "2026-08-28T00:00:00Z"
---

# OneSend（扫传）

## 它是什么
[makerjackie/onesend](https://github.com/makerjackie/onesend) 是一种**完全脱离网络、账户、配对流程的设备间文件传输方案**。痛点：在机场、会议室、内网隔离等没有网络、没有 Wi-Fi、没有蓝牙权限的环境下，传统互传工具（AirDrop / 蓝牙 / Wi-Fi Direct）全失效。

OneSend 的解法：

- **发送端**把待传文件编码成**持续变化的光学码**（多帧 QR 风格）显示在屏幕上；
- **接收端**用摄像头**连续扫描**这些光学码，**本地解码还原**为原始文件；
- 整个过程**不需要网络传输**——屏幕就是传输线，摄像头就是接收器。

## 为什么用它 / 适合什么场景
- 在**无网 / 内网隔离**场景下临时给同事发一份文档、配置、截图；
- 不想注册账号 / 配对码 / 蓝牙可见性的临时文件交换；
- 跨平台（任何能显示 + 任何能扫的设备）即可互传；
- 适合**敏感小文件**（密钥、配置、临时成果）的一次性外带，因为链路全本地、不可被中间人嗅探。

## 关键能力
| 能力 | 说明 |
|------|------|
| 零账号 | 不需要注册、不需要登录 |
| 零配对 | 无需扫码加好友 / 输入配对码 |
| 零服务器 | 不依赖任何中转 / 云服务 |
| 零网络 | 屏幕 → 摄像头即传输链路 |
| 跨平台 | 任何能显示屏幕 + 任何能扫的设备组合即可 |
| 本地还原 | 接收端本地解码，文件不出本机 |
| 抗窃听 | 物理视线外的中间人无法拦截 |

## 相关概念
- [FileApex](tool-fileapex.md) — 同局域网 Android / macOS / Windows 设备互传，OneSend 是**连局域网都不要的极简版**
- [SSClip](tool-ssh-clipboard.md) — SSH 点对点原生剪贴板同步；OneSend 是更彻底的「无网络」剪贴板 / 文件替代

## 参考链接
- 项目链接：<https://github.com/makerjackie/onesend>
- 原始推文：<https://x.com/QingQ77/status/2093281687610564853>
