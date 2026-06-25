---
type: Tool
title: "lex-ghostty-shaders（Ghostty 终端涟漪着色器）"
description: "用 GLM-5.2 vibe-coded 的 Ghostty 终端水波纹着色器 shader 示例。"
resource: "https://github.com/lexrus/lex-ghostty-shaders"
tags: [ghostty, shader, terminal, vibe-coding]
timestamp: "2026-06-25T10:33:16Z"
---

# lex-ghostty-shaders（Ghostty 终端涟漪着色器）

## 它是什么

一份为 **Ghostty 终端**写的**水波纹 shader**，由 GLM-5.2「vibe-coded」产出——意思是开发者用自然语言驱动模型写完代码，而不是手敲 GLSL。

## 为什么关注

- **Ghostty** 是近年快速崛起的终端模拟器（用 Zig 写、GPU 加速、原生体验）。
- 「**vibe coding 出可运行 shader**」是当下 LLM 编程能力的一个有趣切片——shader 看似小众但对模型代码生成质量要求很高（语法严格、数学密集）。
- 着色器可以**拓展到**任意 GPU 加速的终端 / 桌面应用的视觉增强。

## 关键看点

| 维度 | 说明 |
|------|------|
| 目标平台 | Ghostty 终端 |
| 视觉效果 | 水波纹 |
| 实现语言 | GLSL / shader |
| 编码方式 | vibe-coded（GLM-5.2 驱动） |

## 媒体

视频：<https://video.twimg.com/amplify_video/2069999577277886464/vid/avc1/2214x1550/1qUzeT3p2_Eg2E9C.mp4?tag=28>

## 相关概念

- [Fable 5 World Demo](./tool-fable5-world-demo.md) — 同样「99% 代码由 LLM 生成」，但 Fable 5 是 21,000 行的浏览器开放世界；lex-ghostty-shaders 是几十行 shader——可以对照看 LLM 在不同规模 / 类型的产出
- [Aura-IDE](./tool-aura-ide.md) — 「AI 写代码 → 用户审批」的本地工作台；vibe coding 的落地工作台之一