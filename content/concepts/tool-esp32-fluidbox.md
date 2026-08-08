---
type: "Tool"
title: "ESP32 FluidBox"
description: "在 Waveshare ESP32-S3 开发板上跑的 3D 粒子流体模拟：屏幕当玻璃盒的前壁，倾斜、晃动板子，液体跟着流动。"
resource: "https://github.com/V4C38/esp32-fluidbox"
tags: [esp32, embedded, simulation, 3d, fluid]
timestamp: "2026-08-08T20:30:00Z"
---

# ESP32 FluidBox

## 它是什么

ESP32 FluidBox 是一个在 Waveshare ESP32-S3 开发板上跑的 3D 粒子流体模拟项目，把屏幕当成「玻璃盒」的前壁。当你倾斜或晃动板子时，盒里的液体粒子跟着重力与惯性流动，给一块廉价嵌入式板子带来「真实流体玩具」的体验。

## 为什么用它 / 适合什么场景

- 想在 ESP32 上做有视觉冲击力的演示 / 玩具 / 桌面摆件。
- 研究嵌入式平台上的粒子 / 流体实时模拟。
- 想把加速度传感器作为模拟的物理输入。

## 关键能力

| 能力 | 说明 |
|------|------|
| 3D 粒子流体 | 在嵌入式屏幕上跑出立体粒子流体感 |
| 加速度驱动 | 倾斜 / 晃动板子改变重力方向 |
| ESP32-S3 | 跑在 Waveshare 出品的开发板上 |
| 自包含 | 一块板子 = 一个完整玩具 |

## 相关概念

- [ESPHome Guition 语音助手旋钮屏](./tool-esphome-guition-va.md) — 同属「ESP32 屏 + 单片机玩具」方向
- [Pocket Lab Power Supply](./tool-pocket-lab-power-supply.md) — 同类嵌入式 DIY 项目
- [gm-balancecar](./tool-gm-balancecar.md) — STM32 平衡车硬件项目