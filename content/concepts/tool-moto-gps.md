---
type: "Tool"
title: "MOTO GPS（摩托车导航：圆屏 + iPhone BLE 协议）"
description: "Maler X（Glimpse）做的摩托车导航硬件 + 软件：Waveshare ESP32-S3-Touch-AMOLED-1.75C 圆屏固件 + iOS App，BLE 自定义 GATT 协议，iPhone 放包里、出发前选路线、骑行中圆屏只显下一路口 / 转向动作 / 距离。"
resource: "https://github.com/mx3353672833-debug/moto-gps-waveshare"
tags: "[motorcycle, gps, esp32, waveshare, ble, ios, round-display, navigation]"
timestamp: "2026-09-27T21:55:00Z"
---

# MOTO GPS（摩托车导航：圆屏 + iPhone BLE 协议）

## 它是什么

[MOTO GPS](https://github.com/mx3353672833-debug/moto-gps-waveshare) 是 **Maler X（Glimpse）** 做的**摩托车导航硬件 + 软件**套装：

- **硬件端**：**Waveshare ESP32-S3-Touch-AMOLED-1.75C** 圆屏固件（车把上装的 1.75 寸圆形触控屏）
- **软件端**：**iOS App**
- **协议**：**BLE 自定义 GATT 协议**

骑行场景设计：

- iPhone 装包里
- 出发前在 iPhone 上**选路线**
- 骑行中**圆屏只显示下一路口、转向动作、距离**——减少手机操作、提升安全

## 为什么用它 / 适合什么场景

- **摩托车骑行**——手持手机既不方便又不安全，圆屏 + 腕动 = 一瞥就懂。
- 想**自建导航硬件**而不是买 Garmin 等商业产品。
- 喜欢 **ESP32 + AMOLED** 折腾的开源硬件玩家。
- 想**自定义 GATT 协议**——把手机 / 圆屏解耦，方便后续扩展。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | 硬件 + 软件套装 |
| 屏幕 | Waveshare ESP32-S3-Touch-AMOLED-1.75C（1.75 寸圆形触控） |
| 主控 | ESP32-S3 |
| App | iOS |
| 通信 | BLE 自定义 GATT |
| 场景 | 摩托车骑行导航 |
| 设计原则 | 圆屏只显必要信息（下一路口 / 转向 / 距离） |

## 媒体

- ![](https://pbs.twimg.com/media/HTH5yQHbAAAv7gw.jpg)
- ![](https://pbs.twimg.com/media/HTH5zboaIAAvlDa.jpg)

## 相关概念

- [ESPHome Guition 语音助手旋钮屏](./tool-esphome-guition-va.md) — 同样是 ESP32 + 圆屏 / 旋钮屏的家居场景
- [Home Assistant](./tool-homeassistant.md) — 智能家居生态（视情况联动）