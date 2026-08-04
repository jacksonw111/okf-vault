---
type: "Tool"
title: "qr-data-transfer (deedy)"
description: "两台都不能上网的设备间倒文件太麻烦，让发送端把文件编码成一组动态二维码，接收端对着屏幕扫一遍就能收下来——纯视觉通道传输，不依赖任何网络。"
resource: "https://github.com/deedy/qr-data-transfer"
tags: "[qr-code, air-gap, file-transfer, no-network, p2p, offline]"
timestamp: "2026-08-04T20:30:00Z"
---

# qr-data-transfer (deedy)

## 它是什么

[qr-data-transfer](https://github.com/deedy/qr-data-transfer) 解决**两台都不能上网的设备间倒文件**太麻烦的问题——**让发送端把文件编码成一组动态二维码，接收端对着屏幕扫一遍就能收下来**。

![qr-data-transfer 截图](https://pbs.twimg.com/media/HOw3ikNbMAAV400.jpg)

## 为什么用它 / 适合什么场景

- **纯空气隔离传输**：两台都不上网 / 不在同一网段时仍能传文件。
- **零网络依赖**：只靠屏幕 + 摄像头。
- **安全敏感场景**：内网隔离 / 涉密设备间单向/双向倒文件。

## 关键能力

| 能力 | 说明 |
|------|------|
| 文件 → 动态二维码 | 发送端编码 + 循环播放 |
| 摄像头扫码接收 | 接收端扫码并拼回原文件 |
| 零网络 | 纯视觉通道 |
| 跨平台 | 只要有屏幕和摄像头即可 |

## 参考链接

- [项目仓库](https://github.com/deedy/qr-data-transfer)

## 相关概念

- [TermPair](./tool-termpair.md) — 浏览器里端到端加密的远程终端共享
- [Sunshine Send](./tool-sunshine-send.md) — Android TV 端 NanoHTTPD 局域网快传（基于局域网，与本工具互补）
