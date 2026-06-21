---
type: "Tool"
title: "PP-OCRv6 Studio（本地 OCR 工作台）"
description: "用飞桨 PP-OCRv6 三档模型（Tiny / Small / Medium）搭建的本地 OCR 工作台：一键切换模型，Apple Silicon 自动走 CoreML 硬件加速，附完整 Web 界面；可离线批量识别图片 / PDF 中的文字。"
resource: "https://github.com/andyhuo520/ppocrv6-studio"
tags: "[ocr, paddleocr, pp-ocrv6, coreml, apple-silicon, local-ai, web-ui]"
timestamp: "2026-06-21T16:04:00Z"
---

# PP-OCRv6 Studio（本地 OCR 工作台）

## 它是什么

基于**飞桨 PP-OCRv6** 三档模型（Tiny / Small / Medium）的本地 OCR 工作台：在 macOS / Apple Silicon 上自动走 CoreML 硬件加速，附带完整 Web 界面，可一键切换模型档位、按需在「速度」与「精度」间权衡。完全本地、离线可用。

## 为什么用它 / 适合什么场景

- 处理隐私敏感文档（合同、票据、身份证）不想上传云端 OCR。
- macOS Apple Silicon 用户想榨干 CoreML，对标 Apple Vision 框架但要中文识别更强。
- 想在一台机器上跑批量 OCR（扫描件归档、PDF 重排、电子书制作），又不想自己拼 PaddleOCR + PaddleServing。

## 关键能力

| 能力 | 说明 |
|------|------|
| 模型三档 | Tiny（快）/ Small（均衡）/ Medium（准），运行时一键切换 |
| 硬件加速 | Apple Silicon 上自动走 CoreML |
| 界面 | 完整 Web UI（上传 / 预览 / 结果导出） |
| 离线 | 全部计算在本地，无需联网 |
| 后端 | 飞桨 PaddlePaddle + PP-OCRv6（PP-OCRv5 之后的最新系列） |

## 适用边界

- 非中文场景下与 Tesseract / Apple Vision / EasyOCR 的对比需要自行 benchmark。
- 模型档位与速度的权衡高度依赖图像质量。

## 媒体

- 截图：![](https://pbs.twimg.com/media/HLOizZmawAAMzul.jpg)

## 相关概念

- [Single Server](tool-single-server.md) — 把它跑在自托管 VPS 上，就成了一个「OCR 微服务」
- [BiliMusic](tool-bili-music-electron.md) — 同为「Electron 桌面端跑本地 AI 模型」的同类形态