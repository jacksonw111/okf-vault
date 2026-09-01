---
type: "Tool"
title: "MoneyPrinterTurbo（一站式 AI 短视频生成器）"
description: "输入主题或关键词，自动写脚本、找素材、配音、加字幕，合成竖屏或横屏的高清短视频——一站式的「按主题出片」AI 流水线。"
resource: "https://github.com/stophobia/moneyprinterturbo"
tags: [ai-video, short-video, tiktok, content-automation, python, ffmpeg]
timestamp: "2026-09-01T04:15:00Z"
---

# MoneyPrinterTurbo

## 它是什么
[MoneyPrinterTurbo](https://github.com/stophobia/moneyprinterturbo) 是一个**一站式 AI 短视频生成器**：用户只需要给一个主题或关键词，工具自己负责——**写脚本 → 找素材 → 配音 → 加字幕 → 合成竖屏 / 横屏高清视频**。整个流水线被打包在一个 Python 应用里，目标是「按主题出片」的最低摩擦路径。

与单纯的「AI 文生视频」模型不同，MoneyPrinterTurbo 走的是**整段工作流自动化**——从文案、检索、配音到合成都有现成实现，更像「AI 视频剪辑台」而不是单点模型。

## 为什么用它 / 适合什么场景
- 想要**按主题批量出短视频**（自媒体、矩阵号、营销号、知识口播）；
- 不想自己拼脚本模型 + 素材检索 + TTS + 字幕 + FFmpeg 的长链路；
- 想要**横屏 / 竖屏**两种比例都能直接产出（适配 YouTube + 抖音 / TikTok）；
- 想要可本地部署的开源方案，不依赖单一商业 SaaS。

## 关键能力

| 能力 | 说明 |
|------|------|
| 主题 → 脚本 | LLM 自动生成视频文案 |
| 素材检索 | 根据脚本自动找匹配素材 |
| AI 配音 | TTS 配音，多音色可选 |
| 自动字幕 | 时间轴对齐的字幕 |
| 横屏 / 竖屏 | 同时支持 16:9 与 9:16 输出 |
| 高清合成 | FFmpeg 流水线最终合成 |
| 一键出片 | 给主题 → 出完整视频，最少人工介入 |
| 开源可改 | Python 全栈，方便接入私有模型 / 素材源 |

## 媒体
![](https://pbs.twimg.com/media/HRBPPCMa8AABpYc.jpg)

## 相关概念

## 参考链接
- 项目链接：<https://github.com/stophobia/moneyprinterturbo>