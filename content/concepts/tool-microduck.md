---
type: "Tool"
title: "microduck（开源机器鸭：低成本的桌面陪伴机器人）"
description: "Pollen Robotics 开源的小型桌面机器人：可动腿、可动头、低成本舵机方案；硬件 BOM + 固件全部开源，适合做 STEM 教学、AI 代理物理外壳、个人桌面玩具。"
resource: "https://github.com/pollen-robotics/microduck"
tags: [robotics, open-source, hardware, education, ai-agent, companion-robot]
timestamp: "2026-08-30T21:50:00Z"
---

# microduck

## 它是什么
[pollen-robotics/microduck](https://github.com/pollen-robotics/microduck) 是 Pollen Robotics 开源的**小型桌面机器鸭**：可动腿、可动头，用低成本舵机实现「行走 + 扭头」动作；硬件 BOM、3D 打印文件、固件全部开源。

定位介于「桌面玩具」和「机器人开发平台」之间：

- **AI 代理的物理外壳**：可在固件层接入大模型 API，让它真的能「听 / 说 / 回应」；
- **STEM 教学**：BOM 便宜、结构简单、可全部 3D 打印，适合课堂；
- **类 Huaqiangbei 山寨版**：硬件方案公开，意味着任何人都可以低成本复刻。

## 为什么用它 / 适合什么场景
- 想给 AI agent / LLM 配一个**实体的、会动的**展示载体；
- 教机器人入门（舵机 / 步态 / 控制回路）——结构简单、零件便宜；
- 想要「陪伴型」桌面硬件但不想花几千块买 AIBO / LOQO；
- 想做产品原型 demo——硬件方案完全公开，迭代成本低。

## 关键能力

| 能力 | 说明 |
|------|------|
| 双舵机驱动 | 腿 + 头各自一个舵机，结构极简 |
| 全开源 | BOM / 3D 文件 / 固件 / 控制协议都公开 |
| 低成本 | 用通用 SG90 / MG90 舵机方案即可 |
| 可外接 AI | 固件层留出与 LLM / 本地代理对接的钩子 |
| 桌面友好 | 体积小，不占地方 |

## 媒体
- 视频：<https://video.twimg.com/amplify_video/2093884276471435264/vid/avc1/1080x1440/4akVbl8m69W8eD7M.mp4?tag=29>

## 相关概念
- [Aether Android Agent](tool-aether-android-agent.md) — 让 Android 手机变成 AI 代理的物理外壳；与 microduck 同属「AI → 实体」思路

## 参考链接
- 项目链接：<https://github.com/pollen-robotics/microduck>
