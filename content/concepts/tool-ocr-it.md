---
type: "Tool"
title: "ocr-it（浏览器离线 OCR 翻页阅读扩展）"
description: "thiagotigaz 出品的 Chrome 扩展，针对「翻页阅读器里无法复制的扫描书 / 幻灯片 / PDF」做截图 OCR：⌥⇧R 框选区域 → ⌥⇧S 截屏识别 → ⌥⇧A 自动托管翻页跑完整本书，全程本地 Tesseract。"
tags: "[ocr, chrome-extension, tesseract, offline, scanner, reading]"
timestamp: "2026-08-26T16:30:00Z"
resource: "https://github.com/thiagotigaz/ocr-it"
---

# ocr-it（浏览器离线 OCR 翻页阅读扩展）

## 它是什么

[`ocr-it`](https://github.com/thiagotigaz/ocr-it) 是 thiagotigaz 出品的 **Chrome 扩展**，专为「**翻页阅读器里的扫描内容无法复制**」场景设计——把扫描书 / 幻灯片 / 翻页 PDF **按页面逐张截图 → 本地 OCR → 输出文本**：

| 快捷键 | 行为 |
|--------|------|
| `⌥⇧R` | 在页面上拖框选一个区域（只需设一次） |
| `⌥⇧S` | 每按一次就截屏当前区域、丢给本地 **Tesseract** 识别，文字按页攒着 |
| `⌥⇧A` | 一键托管——自己截图、自己翻页，跑到文档末尾自动停 |

识别**完全离线**，扩展**一个出站请求都不发**，**不用 API key**。

## 为什么用它 / 适合什么场景

- 翻页式电子书 / 扫描版 PDF / 文献截图，无法右键复制
- 想做 PDF / 扫描教材的批量转写，且不愿意把内容发到 Google Vision / OCR.space 等闭源服务
- 想完全本地跑（避免扫描内容过网）

## 关键能力

| 能力 | 说明 |
|------|------|
| 本地 OCR | 内置 Tesseract |
| 区域选择 | ⌥⇧R 拖框定一次即可 |
| 半自动模式 | ⌥⇧S 手动逐页 |
| 自动翻页 | ⌥⇧A 托管跑整本 |
| 零出站 | 扩展不发任何外网请求 |
| 零 API key | 全本地跑 |
| 跨平台 | Chromium 内核（Chrome / Edge / Brave 等） |

## 媒体

![](https://pbs.twimg.com/media/HQiBps2bYAAittb.jpg)

## 参考链接

- [项目链接](https://github.com/thiagotigaz/ocr-it)
