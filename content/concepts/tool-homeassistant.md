---
type: "Tool"
title: "Home Assistant（开源智能家居自动化平台）"
description: "开源的家庭自动化平台：把各种厂商的智能设备统一接入、做本地化的自动化规则与仪表盘，是自托管智能家居的事实标准。"
resource: "https://www.home-assistant.io/"
tags: "[home-assistant, smart-home, open-source, self-hosted, automation]"
timestamp: "2026-09-27T21:55:00Z"
---

# Home Assistant（开源智能家居自动化平台）

## 它是什么

[Home Assistant](https://www.home-assistant.io/) 是开源的家庭自动化平台（[GitHub: home-assistant/core](https://github.com/home-assistant/core)）——把不同厂商、不同协议的智能设备（灯、开关、传感器、空调、摄像头等）统一接入，用本地优先的规则做自动化，并提供仪表盘 / 语音 / 移动端 App 等交互界面。

## 为什么用它 / 适合什么场景

- **本地优先**：核心逻辑跑在用户自己的硬件（树莓派 / NAS / 小主机）上，不被厂商云服务绑架。
- **跨生态接入**：支持 Zigbee、Z-Wave、Matter、Wi-Fi、Bluetooth、Thread 等数百种设备 / 服务。
- **可扩展**：通过 [HACS](https://hacs.xyz/) 安装社区自定义组件（如 [ha-spatial-context](./tool-ha-spatial-context.md)）来补足官方功能。
- **可编程**：YAML / UI / Python 都能写自动化；能与 AI 助手 / Agent 联动，给自动化提供「物理上下文」。
- **隐私**：数据留在本地，不卖给云厂商。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | Python 应用 + 前端 + 移动端 |
| 接入 | 1000+ 集成（Integration），覆盖主流智能家居品牌与协议 |
| 自动化 | trigger / condition / action 三段式，可写脚本 / 场景 |
| 生态 | HACS 社区自定义组件 / 主题 / App 等 |
| 部署 | Raspberry Pi / NAS / Docker / 虚拟机均可 |

## 相关概念

- [ha-spatial-context](./tool-ha-spatial-context.md) — Home Assistant 的空间上下文自定义组件
- [Self-Hosted（自托管）](./term-self-hosted.md) — Home Assistant 是经典自托管场景