---
type: "Term"
title: "Home Assistant"
description: "开源的家庭自动化平台——把灯光 / 空调 / 安防 / 能源 / 传感器 / 音箱 / 媒体中心等几百种设备 / 协议统一到本地实例，支持 YAML / UI / Node-RED 多种自动化编辑方式，是当下自托管智能家居的事实标准。"
resource: "https://www.home-assistant.io"
tags: "[home-assistant, home-automation, iot, self-hosted, smart-home]"
timestamp: "2026-10-06T22:51:00Z"
---

# Home Assistant

## 定义

**Home Assistant**（简称 HA）是开源的家庭自动化平台，**完全本地运行**（不上云），把灯光 / 空调 / 安防 / 能源 / 传感器 / 音箱 / 媒体中心 / ESP32 设备 等几百种品牌 / 协议（Zigbee / Z-Wave / MQTT / Matter / Wi-Fi / Bluetooth）统一到一个 dashboard，让用户以 YAML / UI / Node-RED / Python Script 编写自动化规则。

## 要点

- **官网**：[home-assistant.io](https://www.home-assistant.io)
- **核心**：本地优先（Local-first）+ 几百种集成（Integrations）+ 强大的自动化引擎
- **硬件友好**：与 ESP32 / ESPHome / Tasmota / Zigbee2MQTT 等深度集成
- **扩展**：HACS 商店收录第三方自定义集成 / 前端组件
- **典型场景**：自托管智能家居、能源管理、安防、3D 户型图集成（如 [`tool-neonplan3d`](tool-neonplan3d.md)）、ESP32 设备中控

## 相关概念

- [ESP32](./term-esp32.md) — 主流硬件终端
- [Self-Hosted](./term-self-hosted.md) — 部署形态
- [Meta Muse Gadget SDK](./tool-muse-gadget-sdk.md) — 同为家庭智能设备中控生态
