---
type: Tool
title: "MeterEye"
description: "电表被封铅印、无数据口、供应商月度刷新的场景：装个摄像头对着电表，每 7 秒自动解一次 LCD 读数。"
resource: "https://github.com/epynic/MeterEye"
tags: [ocr, webcam, meter-reading, computer-vision, home-automation]
timestamp: "2026-08-25T19:30:00Z"
---

# MeterEye

## 它是什么

[epynic/MeterEye](https://github.com/epynic/MeterEye) 是一个**摄像头 + 视觉识别**解决「**铅封电表无数据口**」问题的小工具。现实痛点：

- 电表被铅印封死，没有任何数据口导出。
- 电力公司网站一个月才刷新一次读数。
- 用户想看到本月用了多少电——只能出门盯着那块小 LCD 看。

MeterEye 的解法：**装一个摄像头对着电表，每 7 秒跑一次 OCR，把读数落到本地 / 推送给用户**，相当于「DIY 智能电表」。

![](https://pbs.twimg.com/media/HQiBftEbcAAfP0u.jpg)

![](https://pbs.twimg.com/media/HQiBgiobMAA_Hzi.jpg)

## 为什么用它 / 适合什么场景

- **租户 / 老旧住宅的电表无数据口**：想看到更细粒度的用电数据。
- **电力公司只月度刷新**：想自己高频采集、做用电分析。
- **自动化 / 节能研究**：高频读数才能跑异常检测、峰谷分析。
- **DIY 智能家居**：不想买昂贵的智能电表方案。

## 关键能力

| 能力 | 说明 |
|------|------|
| 摄像头 + OCR | 每 7 秒对 LCD 跑一次识别 |
| 本地采集 | 数据落到本地，不依赖云 |
| 高频读数 | 7 秒粒度，远比月度刷新精细 |
| 历史记录 | 可绘制用电曲线、导出 CSV |
| 低成本 | 用普通 USB / IP 摄像头即可 |

## 相关概念

- [BetterVoice](./tool-better-voice.md) — 同样把摄像头 / OCR 用在「语音 + 视觉结合」的桌面场景
- [Toolcraft](./tool-toolcraft.md) — 创意类应用 starter kit，MeterEye 这类小工具也能在其上拓展

## 参考链接

- 项目链接: <https://github.com/epynic/MeterEye>
- 原始链接: <https://x.com/QingQ77/status/2092275809457496234>