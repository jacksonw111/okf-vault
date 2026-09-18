---
type: Tool
title: "PrintFilm（剧本→成片自托管 AI 流水线平台）"
description: "把「主题/剧本 → 分镜 → 生图 → 生视频 → 成片」这条流水线做成一整套可自托管的开源平台，省去自己串模型和 FFmpeg 的功夫。"
resource: "https://github.com/yi1108/printfilm"
tags: [ai-video, storyboard, self-hosted, pipeline, ffmpeg, t2i, t2v, open-source]
timestamp: 2026-09-18T10:35:00Z"
---

# PrintFilm（剧本→成片自托管 AI 流水线平台）

## 它是什么

[yi1108/printfilm](https://github.com/yi1108/printfilm) 是一个**自托管的 AI 影视后期 / 短视频流水线平台**。它把从一段主题或剧本到最终成片的完整链路——剧本 → 分镜 → 生图 → 生视频 → 成片——全部串成一个可一键部署的开源平台，免去用户自己拼模型、写胶水代码、跑 FFmpeg。

## 关键能力

| 能力 | 说明 |
|------|------|
| 全链路流水线 | 剧本 / 分镜 / 生图 / 生视频 / 成片一站到底 |
| 自托管 | 整套平台自己部署，数据 / 模型 / 出片全在自己机器上 |
| 模型编排 | 不用自己写代码把多个生成模型接起来 |
| FFmpeg 内建 | 成片阶段的拼接 / 转码由平台处理 |
| 主题驱动 | 从一段文字主题起步即可开始走流程 |

## 适合什么场景

- 想做 AI 短视频 / 微电影 / 概念片、但不想为每一步都自己写脚本的研究者 / 创作者。
- 已经熟悉分镜与 FFmpeg、希望把「串模型」这件事自动化的团队。
- 希望把整套流水线部署在自己的机器 / 内网、对数据出域有要求的团队。

## 参考

- 项目链接：<https://github.com/yi1108/printfilm>

![平台界面](https://pbs.twimg.com/media/HSdmliqbEAA-bIu.jpg)
