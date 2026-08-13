---
type: Tool
title: "conform-desktop"
description: "音频对轨工具，把一段音轨按参考视频时间轴重新落位——自动识别剪辑 / 插入 / 删减 / 恒定偏移 / PAL 变速 / 3:2 电视电影痕迹，把残余偏移清零后输出 FLAC + 质量报告。"
resource: "https://github.com/wolfram0108/conform-desktop"
tags: "[audio, conform, video, post-production, open-source]"
timestamp: "2026-08-13T19:53:00Z"
---

# conform-desktop

## 它是什么
一个**音频对轨（conform）工具**。给定：

- 一段**源音频**
- 一段**参考视频**（已知时间轴）

工具自动分析源音频里**到底做了什么修改**，然后把音频**重排**到参考视频的时间线上：

- **剪辑点**（cuts）：哪里被切
- **插入 / 删减**：哪里多了 / 少了
- **恒定偏移**：整体偏多少毫秒
- **PAL 变速**：PAL 制式拉伸（音频变调 / 时长变化）
- **3:2 电视电影（telecine）痕迹**：胶片转视频的帧模式

把残余偏移**清零**，最终输出：

- **FLAC** 音频文件（无损）
- 一份**质量报告**（做了什么处理、偏移量多少）

## 为什么用它 / 适合什么场景
- 影视后期：把粗剪音频 / 临时音乐重对到精剪时间线。
- 修复老素材：把被人为剪辑 / 变速过的音轨还原回原始对齐。
- 跨格式工作流（NTSC / PAL / 胶片 / 数字）——自动识别并补偿。
- 想要「可审计的对轨」：附质量报告。

## 关键能力
| 能力 | 说明 |
|------|------|
| 任务 | 音频对轨（conform） |
| 输入 | 源音频 + 参考视频 |
| 自动识别 | cuts / insert / delete / offset / PAL speed / 3:2 pulldown |
| 输出 1 | 对齐后的 FLAC |
| 输出 2 | 质量报告 |
| 适配 | 多制式（NTSC / PAL / 胶片） |

## 相关概念
- （暂无强相关概念——独立的后期工具）

## 媒体
- 工具截图：<https://pbs.twimg.com/media/HPfUssOasAAMZL9.png>

## 项目链接
- 项目主页：<https://github.com/wolfram0108/conform-desktop>