---
type: "Tool"
title: "light-ocr（arcships/light-ocr）"
description: "为原生应用和 Node.js 应用准备的离线 OCR 引擎，单图 100ms 以内，模型加包约 30MB，适合 desktop/native 客户端内嵌。"
resource: "https://github.com/arcships/light-ocr"
tags: "[ocr, offline, native, nodejs, desktop, on-device]"
timestamp: "2026-07-14T09:03:10Z"
---

# light-ocr

[light-ocr](https://github.com/arcships/light-ocr) 是 **arcships** 开源的离线 OCR 库,面向**原生应用**和 **Node.js** 客户端,主打**轻量、低延迟**。

## 关键指标

| 指标 | 数值 |
|------|------|
| 单图耗时 | ≤ 100 ms |
| 模型 + 包体积 | 约 30 MB |
| 网络依赖 | 零(完全离线) |
| 接入面 | 原生 (iOS/Android/桌面) + Node.js |

## 适合什么场景

- 桌面 / native 客户端里需要**实时截图翻译 / 题目识别 / 名片录入**等轻量 OCR。
- 不希望引入云 API、又嫌传统 PaddleOCR / Tesseract 包体过大的场景。
- 对延迟敏感(用户敲下快捷键就要结果),需要本地推理的流水线。

## 与已有方案的差别

| 方案 | 特征 | light-ocr 定位 |
|------|------|----------------|
| 云 OCR(腾讯/百度/Google) | 高精度、要联网、要 API key | 离线、低延迟的客户端替代 |
| Tesseract | 成熟、但体积大、速度慢 | 更小、更快,精度仍可接受 |
| PaddleOCR/PP-OCRv6 | 高精度、本地 | 模型通常更大,30MB 是更激进的瘦身方案 |

## 参考链接

- [项目仓库](https://github.com/arcships/light-ocr)
- [原始推文](https://x.com/ashfold/status/2076937753993122239)

## 相关概念

- [PP-OCRv6 Studio](./tool-ppocrv6-studio.md) — 飞桨 PP-OCRv6 本地 OCR,同样面向 Apple Silicon CoreML 加速
- [claude-real-video](./tool-claude-real-video.md) — 视频抽帧做 AI 视频理解的工具,与 OCR 共同构成「本地视觉输入」栈
