---
type: "Tool"
title: "NFCX（跨平台桌面 NFC 工具）"
description: "用 Go 写的跨平台桌面 NFC 工具，支持 macOS、Windows 和 Linux，主打 MIFARE Classic 卡片的读、写、dump 备份恢复和密钥管理。"
resource: "https://github.com/BennyThink/NFCX"
tags: "[nfc, mifare-classic, desktop, go, cross-platform, dump, key-management]"
timestamp: "2026-09-19T16:00:00Z"
---

# NFCX（跨平台桌面 NFC 工具）

## 它是什么

[BennyThink/NFCX](https://github.com/BennyThink/NFCX) 是一个**用 Go 写的跨平台桌面 NFC 工具**——支持 **macOS / Windows / Linux** 三平台，主打 **MIFARE Classic** 卡片场景：

- 读卡
- 写卡
- dump 备份与恢复
- 密钥管理

## 为什么用它 / 适合什么场景

- 需要在三大桌面系统上统一使用 NFC 工具（很多同类工具仅限某个平台）。
- 做 MIFARE Classic 卡片的项目（门禁 / 一卡通 / 资产标签）需要读写 / 备份 / 还原链路。
- 想要一个**单一二进制、无 GUI 依赖链**的 NFC 桌面工具。
- 想在 Linux 上跑 NFC 工具——很多 NFC 桌面软件对 Linux 支持差。

## 关键能力

| 能力 | 说明 |
|------|------|
| 跨平台 | macOS / Windows / Linux 三端统一体验 |
| MIFARE Classic 优先 | 读 / 写 / dump / 密钥管理 |
| Go 实现 | 单二进制、依赖少、便于分发 |
| 桌面 GUI | 不是 CLI 黑窗口，带可视化界面 |

## 参考

- 项目链接：<https://github.com/BennyThink/NFCX>
- 原始推文：<https://x.com/QingQ77/status/2101270830013378878>