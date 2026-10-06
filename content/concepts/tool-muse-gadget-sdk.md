---
type: "Tool"
title: "Muse Gadget SDK（Meta 开源硬件 + AI SDK）"
description: "Meta 开源的 Muse 设备端 SDK：分 ESP32 固件与 Linux 服务两条线，把闲置开发板 / 旧电脑变成听 Muse AI 助手指挥的硬件设备，17 款 ESP32 板卡清单 + 家庭网络隧道摸局域网设备。"
resource: "https://github.com/facebookincubator/muse-gadget-sdk"
tags: "[esp32, linux, ai-assistant, hardware, iot, meta]"
timestamp: "2026-10-06T00:35:00Z"
---

# Muse Gadget SDK

## 它是什么

[Muse Gadget SDK](https://github.com/facebookincubator/muse-gadget-sdk) 是 **Meta** 把 Muse 的设备端 SDK 开源到 GitHub——分 **ESP32 固件** 与 **Linux 服务** 两条线：让闲置开发板和旧电脑变成听 Muse AI 助手指挥的硬件设备。

## 关键能力

| 能力 | 说明 |
|------|------|
| 硬件支持 | 17 款可刷 ESP32 板卡，其中 7 款跑得动完整 UI（动画头像、按键对讲、设置菜单） |
| 网络隧道 | 带 PSRAM 的板卡可开家庭网络隧道，摸局域网里已有设备 |
| 形态 | 两条线：ESP32 固件 + Linux 服务，可分别部署也可联动 |
| 协议 | 与 Muse AI 助手配套，把设备端能力桥接到云端对话 |

## 适合场景

- 把抽屉里吃灰的 ESP32 重新拿出来做 AI 控制节点
- 把退役的旧 Linux 机器 / NAS 变成家庭 AI 助手执行体
- 想搭一套「云上 LLM ↔ 本地硬件」的端到端实验台

## 参考链接

- 项目链接：<https://github.com/facebookincubator/muse-gadget-sdk>

## 相关概念

- [ESP32](./term-esp32.md) — SDK 主战场芯片
- [Home Assistant](./term-home-assistant.md) — 同为家庭智能设备中控生态