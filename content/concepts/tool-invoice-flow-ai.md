---
type: "Tool"
title: "InvoiceFlowAI（EthanYoQ/Invoice-Downloader）"
description: "开源电子发票整理工具，自动从邮箱收集 PDF / OFD / XML 发票，OCR 后分类归档并生成可复核的 Excel 汇总。"
resource: "https://github.com/EthanYoQ/Invoice-Downloader"
tags: "[invoice, ocr, email, finance, automation, tool]"
timestamp: "2026-09-29T16:00:00Z"
---

# InvoiceFlowAI（EthanYoQ/Invoice-Downloader）

## 它是什么

[InvoiceFlowAI](https://github.com/EthanYoQ/Invoice-Downloader) 是 EthanYoQ 开源的电子发票整理工具：从邮箱里把散落在各处的 PDF / OFD / XML 发票自动收下来，OCR 识别后分类归档，最后导出可复核的 Excel 汇总。

## 它解决的问题

个人 / 小团队发票管理常见痛点：
- 邮件附件散落各处（PDF / OFD / XML 多种格式）
- 手工一张张归档耗时
- 月底报销时翻找困难

## 关键能力

| 能力 | 说明 |
|------|------|
| 多格式支持 | PDF / OFD / XML 三大国内电子发票格式 |
| 邮箱抓取 | 自动从邮箱收集发票附件 |
| OCR 识别 | 文字识别后提取关键字段（金额 / 开票方 / 税号等） |
| 分类归档 | 按类型 / 时间 / 来源自动归类 |
| Excel 导出 | 导出可复核的 Excel 汇总表 |

## 媒体预览

![](https://pbs.twimg.com/media/HTRobZlaMAAupur.jpg)

## 原始链接

- 项目主页：<https://github.com/EthanYoQ/Invoice-Downloader>

## 相关概念

- [Atomic JSON Store](./tool-atomic-json-store.md) — Python 小型本地状态存储，处理 JSON 时解决并发 / 崩溃问题