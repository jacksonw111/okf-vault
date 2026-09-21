---
type: "Tool"
title: "tax-doc-classifier（IRS 税表 PDF 页面级分类器）"
description: "把税表 PDF 的每一页自动识别成对应的 IRS 表格编号，并给出可卡阈值的置信度，替代每页把 PDF 丢给 Claude Sonnet 的高成本流水线。"
resource: "https://github.com/kyotofin/tax-doc-classifier"
tags: "[pdf, classification, irs, tax, document-ai, cost-saving]"
timestamp: "2026-09-21T22:00:00Z"
---

# tax-doc-classifier

## 它是什么

[kyotofin/tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier) 把**税表 PDF 的每一页自动识别成对应的 IRS 表格编号**——并给出**置信度**，方便按阈值做后续路由。

## 解决的问题

传统流程是把**每一页 PDF 丢给 Claude Sonnet**，让它判断这一页是哪个表格。**Sonnet 按 token 计费**——一份上百页的税表扫描件算下来账单不低。

## 它的做法

- 用**专用分类模型**替代通用大模型——只判断「页 → 表格编号」，范围极窄。
- 输出**置信度**，业务侧可按**阈值**决定是直接采用分类结果还是再走 Sonnet 复核。

## 为什么用它 / 适合什么场景

- 税务 SaaS / 报税代理处理**大量 PDF 税表**的归档 / 入库。
- 想把**高成本 LLM 调用**缩到只有「置信度不够」的少数页。

## 关键能力

| 能力 | 说明 |
|------|------|
| 页面级识别 | 每一页独立输出 IRS 表格编号 |
| 置信度输出 | 可按阈值路由：置信度高直接采用，低置信度再上 LLM |
| 替代通用 LLM | 分类专用模型，成本远低于 Sonnet |

## 项目链接

- 仓库：<https://github.com/kyotofin/tax-doc-classifier>

## 相关概念

- [Datalab LIFT（视觉文档 JSON 抽取模型）](./tool-datalab-lift.md) — 同为「专用小模型替代通用 LLM 做文档任务」
