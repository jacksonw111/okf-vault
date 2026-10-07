---
type: "Tool"
title: "Gyotaku（截图 OCR 全文检索）"
description: "xevrion 开源：用 PaddleOCR PP-OCRv6 模型（跑在 ONNX Runtime 上）读取截图里的文字，写进 SQLite FTS5 三元组索引，按快捷键唤出搜索窗口敲几个字母即可定位对应截图，匹配词在原图上高亮。"
resource: "https://github.com/xevrion/gyotaku"
tags: "[ocr, paddleocr, sqlite-fts5, onnx-runtime, screenshot, search]"
timestamp: "2026-10-07T15:43:00Z"
---

# Gyotaku（截图 OCR 全文检索）

## 它是什么

[Gyotaku](https://github.com/xevrion/gyotaku) 是 **xevrion** 开源的截图 OCR 全文检索工具。用 **PaddleOCR 的 PP-OCRv6 模型**（跑在 **ONNX Runtime** 上）读取截图里的文字，写进 **SQLite FTS5 三元组索引**，按快捷键唤出搜索窗口敲几个字母即可定位到对应截图，**匹配词在原图上高亮**。

定位是「**Mac / Windows / Linux 通用**」的截图内容检索器——专门解决「我记得截图里出现过那句话，但忘了文件名」的痛点。

## 为什么用它 / 适合什么场景

- **截图为王**：现代人靠截图保存信息，但文件名 / 时间戳检索经常失效
- **OCR + 全文索引**：把图变文本，再走 SQLite FTS5 高性能三元组检索
- **匹配词高亮**：找到后直接在原图上画高亮框，省一步二次确认
- **跨平台**：ONNX Runtime 跨 macOS / Windows / Linux 一致

## 关键能力

| 能力 | 说明 |
|------|------|
| OCR | PaddleOCR PP-OCRv6 |
| 推理 | ONNX Runtime（跨平台） |
| 索引 | SQLite FTS5（三元组） |
| 触发 | 快捷键唤出搜索 |
| 高亮 | 匹配词在原图上标注 |
| 平台 | macOS / Windows / Linux |

## 参考链接

- 项目仓库：<https://github.com/xevrion/gyotaku>

## 媒体

- ![](https://pbs.twimg.com/media/HUAHt34bYAA-Qfi.jpg)

## 相关概念

无相关概念需要链入。
