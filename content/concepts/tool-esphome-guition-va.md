---
type: "Tool"
title: "ESPHome Guition 语音助手旋钮屏"
description: "无需写自定义 C 固件，在 Guition JC3636K718C 圆形旋钮触控屏上跑一个完整的 Home Assistant 语音助手：唤醒词、音乐播放、定时器、设备控制、LED 灯环与两个内置游戏，全部用纯 ESPHome YAML 配出来。"
resource: "https://github.com/MichalZaniewicz/esphome-guition-jc3636k718c-va"
tags: "[esphome, home-assistant, voice-assistant, knob-screen]"
timestamp: "2026-06-21T00:00:00Z"
---

# ESPHome Guition 语音助手旋钮屏

## 它是什么

由 `@QingQ77` 在 2026-06 推荐的 ESPHome 项目：在 **Guition JC3636K718C** 圆形旋钮触控屏上跑一个完整的 **Home Assistant 语音助手**，**不需要写一行 C 固件**，全部用 ESPHome YAML 配出来。

## 内置能力

| 能力 | 说明 |
|------|------|
| 唤醒词 | 支持本地唤醒词识别 |
| 音乐播放 | 通过 HA 媒体服务 |
| 定时器 | 厨房 / 工作流定时 |
| 设备控制 | 联动 HA 下任何设备 |
| LED 灯环 | 旋钮外圈 LED 反馈 |
| 游戏 | 内置两个小游戏（旋钮操作） |

## 适用场景

- 想给厨房 / 工作台放一个 **物理旋钮 + 屏 + 语音** 三合一的 Home Assistant 控制终端。
- 不喜欢 Arduino / 自定义固件 —— 想用纯 YAML 配置。
- 已经在跑 ESPHome 生态 —— 直接加一个设备节点即可。

## 媒体

![Guition 旋钮屏截图](https://pbs.twimg.com/media/HLJKTuoa8AA0Ooa.jpg)

## 相关概念

- [3X-UI](tool-3x-ui.md) — 同为「GUI 设备控制 + 自动化」思路的对照（Web 端）
- [Monorepo 代码质量体系搭建](playbook-monorepo-code-quality-setup.md) — 同为「YAML 配置驱动」哲学