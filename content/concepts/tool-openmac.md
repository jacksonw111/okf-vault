---
type: "Tool"
title: "OpenMac（echosoar/openmac）"
description: "Swift 编写的 macOS 本地 HTTP 服务，把 Vision OCR、Translation、人脸识别、二维码、TTS、网页抓取等系统原生能力封装成统一 JSON API。"
resource: "https://github.com/echosoar/openmac"
tags: [macos, swift, ocr, tts, local, api]
timestamp: "2026-06-23T15:30:00Z"
---

# OpenMac（echosoar/openmac）

## 它是什么

一个跑在 macOS 上的轻量本地 HTTP 服务，把系统自带但平时需要写 Swift/Objective-C 才能调用的能力（Vision OCR、Translation 框架、人脸检测、Vision 二维码识别、AVSpeechSynthesizer TTS、WKWebView 无头抓取）打包成 RESTful JSON 接口，无需付费第三方 OCR/翻译 API。

## 为什么用它 / 适合什么场景

- **OCR 流水线**：批量识别截图、扫描件，调用 `POST /ocr` 直接拿 JSON 结果；
- **翻译工具链**：Mac 内部翻译服务无需联网，配合 Alfred / Raycast 一键翻译剪贴板；
- **Mac 变 AI 推理盒子**：把 Vision 的人脸/二维码能力开放给局域网内其它机器调用；
- **零成本原型**：Cloud Vision / DeepL 还在审批预算？先把 OpenMac 跑起来做演示。

## 关键能力

| 能力 | 底层框架 | 输入 |
|------|----------|------|
| OCR | Vision | URL / Base64 / 本地路径（图片） |
| 翻译 | Translation（macOS 15+） | 文本 |
| 网页抓取 | WKWebView 无头渲染 | URL |
| 人脸检测 | Vision | 图片 |
| 二维码识别 | Vision | 图片 |
| 文字转语音 | AVSpeechSynthesizer | 文本 |

## 媒体 / 原始链接

- 项目链接：<https://github.com/echosoar/openmac>

## 相关概念

- [Proxide](concepts/tool-proxide.md) — 同样是「让本机能力被外部代理调用」的桥接思路（这里是 ChatGPT 网页）
- [Vaultty](concepts/tool-vaultty.md) — 同样属于「macOS 本地系统能力复用」的工具