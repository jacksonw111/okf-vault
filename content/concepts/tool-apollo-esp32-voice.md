---
type: Tool
title: "Apollo (ESP32 + Cloudflare Workers 语音助手)"
description: "桌面级 ESP32 硬件装置 + Cloudflare Workers 后端的语音代理：按住即说，云端跑推理 / 调工具 / 记记忆 / 处理语音，设备端只负责收声与手势。"
resource: "https://github.com/galfrevn/apollo"
tags: "[esp32, cloudflare-workers, voice-assistant, hardware, agent, open-source]"
timestamp: "2026-08-13T19:53:00Z"
---

# Apollo (ESP32 + Cloudflare Workers 语音助手)

## 它是什么
一个**桌面语音助手装置**，由两部分组成：

- **设备端**：ESP32 小硬件，负责**收声**与**手势识别**（按住说话）。
- **云端**：**Cloudflare Workers** 跑**推理 / 调工具 / 记记忆 / 处理语音**——把所有「重活」都放在 Cloudflare 的边缘运行时上。

形态上是一个**硬件 + 云端协同的语音 agent**：本地极简（只负责 IO），云端极丰富（智能 / 工具 / 状态）。

## 为什么用它 / 适合什么场景
- 想要桌面一个永远待命的语音装置，不想给本地装大模型。
- 偏好 Cloudflare 生态（边缘 / Workers / Sandbox / D1 等）而非自家服务器。
- 把设备当「瘦客户端」，所有智能都集中放在 Cloudflare 那一侧，便于一处升级、所有设备同步。
- 用作 IoT / Home Assistant 类项目的语音入口。

## 关键能力
| 能力 | 说明 |
|------|------|
| 硬件 | ESP32（小型、低功耗） |
| 输入 | 语音 + 手势（按住说话） |
| 云端 | Cloudflare Workers（推理 / 工具 / 记忆 / 语音处理） |
| 设备职责 | 仅收声与手势 |
| 云端职责 | 全部智能 |
| 部署 | 硬件装置 + Workers 后端 |

## 相关概念
- [Cloudflare Workers](tool-cloudflare-workers.md) — Apollo 后端运行所在平台

## 项目链接
- 项目主页：<https://github.com/galfrevn/apollo>