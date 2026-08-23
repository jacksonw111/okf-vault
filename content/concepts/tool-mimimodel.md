---
type: Tool
title: "mimimodel（45M 参数的 ESP32-S3 端侧工具调用小模型）"
description: "memovai/mimimodel，不用联网、不用 Linux，一个 45M 参数的小模型就能在 5 美元的 ESP32-S3 芯片上完成工具调用和设备控制"
resource: "https://github.com/memovai/mimimodel"
tags: [edge-ai, esp32, tiny-llm, function-calling, iot]
timestamp: "2026-08-23T05:24:00Z"
---

# mimimodel（45M 参数的 ESP32-S3 端侧工具调用小模型）

## 它是什么

[memovai/mimimodel](https://github.com/memovai/mimimodel) 是一个**只有 45M 参数**的微型 LLM，**不用联网、不用跑 Linux**，直接部署到 5 美元的 **ESP32-S3** 芯片上就能完成**工具调用（function calling）和设备控制**。

## 为什么用它 / 适合什么场景

- 做 IoT / 智能硬件项目时，不想为每一个小设备挂云端 LLM API。
- 需要「在芯片上、毫秒级、可解释」的意图解析 → 动作触发链路。
- 想把"语音 / 传感器 → 动作"这类低延迟场景完全本地化，保护隐私。

## 关键能力

| 能力 | 说明 |
|------|------|
| 极小参数 | 45M 参数，能装进 ESP32-S3 这种 8MB PSRAM 的 MCU |
| 离线推理 | 完全本地跑，不依赖云端 API |
| 工具调用 | 支持 function calling 风格的指令输出 |
| 设备控制 | 适合嵌入式 GPIO / 传感器 / 串口场景 |
| 便宜硬件 | 5 美元芯片即可承载，开发门槛低 |

## 媒体

- ![](https://pbs.twimg.com/media/HQX_0JWawAAOHZs.jpg)

## 相关概念

- [ESPHome Guition 语音助手旋钮屏](./tool-esphome-guition-va.md) — 同类端侧语音 + 嵌入式硬件场景

## 参考链接

- [项目链接](https://github.com/memovai/mimimodel)
