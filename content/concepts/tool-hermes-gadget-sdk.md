---
type: "Tool"
title: "Hermes Gadget SDK（按住说话的 Hermes Agent 硬件终端）"
description: "AdnanQuazi 开源——给 Hermes Agent 配一个「按住说话」的实体语音终端：ESP32 固件 + Linux 客户端 + 桌面模拟器，让设备接入 Agent 的工具、记忆和技能。"
resource: "https://github.com/Adolanium/hermes-gadget-sdk"
tags: "[agent, esp32, voice, hardware, hermes, sdk]"
timestamp: "2026-10-06T22:51:00Z"
---

# Hermes Gadget SDK（按住说话的 Hermes Agent 硬件终端）

## 它是什么

**Hermes Gadget SDK** 是 AdnanQuazi 出品的开源项目——给 **Hermes Agent** 配一个**「按住说话」的实体语音终端**。SDK 包含三件套：

1. **ESP32 固件**：跑在低成本 Wi-Fi/BLE 芯片上，做麦克风采集 + 按键触发
2. **Linux 客户端**：把音频流推到 Agent
3. **桌面模拟器**：无硬件时也能在桌面软件上试

设备接入 Agent 后可调用 Agent 的工具、记忆和技能。

## 为什么用它 / 适合什么场景

- **语音即界面**：按住设备按键说话，松开就完成一轮 Agent 任务
- **低成本硬件**：ESP32 几美元，可量产做家庭 / 办公终端
- **三件套齐全**：硬件 / Linux / 桌面模拟器，无硬件也能开发

## 关键能力

| 能力 | 说明 |
|------|------|
| ESP32 固件 | 麦克风 + 按键 + Wi-Fi 推流 |
| Linux 客户端 | 接收音频 + 转给 Agent |
| 桌面模拟器 | 无硬件时调试 |
| 工具/记忆/技能接入 | Hermes Agent 全栈 |
| 开源 | 可二次开发自定义触发词 |

## 参考链接

- 项目链接：<https://github.com/Adolanium/hermes-gadget-sdk>

## 相关概念

- [ESP32](./term-esp32.md) — 硬件底座
- [Muse Gadget SDK](./tool-muse-gadget-sdk.md) — 同为「Agent + 设备端 SDK」形态
