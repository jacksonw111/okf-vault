---
type: "Tool"
title: "Datalab LIFT（视觉文档 JSON 抽取模型）"
description: "datalab-to/lift —— 9B 参数的视觉语言模型，专门做文档信息提取：给定 JSON Schema（如发票需要号码 / 金额 / 明细），看完 PDF 或图片直接吐出符合该 Schema 的结构化 JSON。"
tags: "[ai, vision-model, document-ai, ocr, json-schema, pdf-extraction]"
timestamp: "2026-06-22T07:30:00Z"
---

# Datalab LIFT（视觉文档 JSON 抽取模型）

## 它是什么

[`datalab-to/lift`](https://github.com/datalab-to/lift) 是 Datalab 出品的 **9B 参数视觉语言模型**（VLM），专门做**文档信息提取**（Document Information Extraction）。用法是：

1. 喂一个 **JSON Schema**（比如发票要 `invoice_no` / `amount` / `line_items`）；
2. 喂一份 **PDF 或图片**（发票 / 合同 / 报表 / 收据）；
3. 模型**看一眼**文档，直接吐出**严格符合该 Schema** 的 JSON。

> 截图：<https://pbs.twimg.com/media/HLTYXjDakAEl9lT.jpg>

## 为什么用它 / 适合什么场景

- **传统 OCR + 正则的两步法** 脆弱：版面变了正则就废。
- **GPT-4V / Claude 直接抽** 能用但**输出格式不可控**：需要靠 prompt 约束，再加 retry / 后处理校验 schema。
- **LIFT 把"输出 schema"变成一等公民**：模型本身在训练时见过大量 schema-conditional generation 任务，输出稳定性显著高于通用 VLM。

适合：

- 发票 / 收据 / 银行流水 → 结构化入账。
- 合同关键字段提取（甲方 / 金额 / 有效期）。
- 研报 / 公告关键指标抽取（对应 OKF 知识库的资料入站场景）。
- 任何「我有大量非结构化文档想批量入库」的场景。

## 关键能力

| 能力 | 说明 |
|---|---|
| 9B 参数 VLM | 单卡可跑（4090 / A100 / Apple Silicon 32G+） |
| Schema-conditional | 给定 JSON Schema 直接吐出符合的 JSON |
| 多格式输入 | PDF + 常见图片格式（PNG / JPG / WebP） |
| 文档专精 | 训练目标就是「文档理解 + 结构化输出」 |
| 开源 | GitHub 公开，可自托管 / 二次微调 |

## 工作流

```
JSON Schema  ─┐
              ├─→  LIFT 9B VLM  ──→  结构化 JSON（schema-valid）
PDF / 图片  ──┘
```

下游：JSON 直接喂给数据库 / 表格 / 业务系统，不再需要 regex / 手工模板。

## 与通用 VLM 的对比

| 维度 | GPT-4V / Claude | LIFT 9B |
|---|---|---|
| 输出格式稳定性 | 需 prompt + 后处理校验 | 模型本身训练时见过 schema 约束 |
| 部署 | 云端 API（成本 + 数据外流） | 自托管（开源、9B 可单卡） |
| 成本 | 按 token 计费 | 一次部署，推理成本 ≈ 电费 |
| 通用视觉能力 | 强（覆盖广泛任务） | 弱（专精文档提取） |
| 速度 | API 延迟 + 网络 | 本地推理，无网络依赖 |

## 适用人群

- 在做**文档自动化**（发票 / 合同 / 报告）的工程师。
- 需要 **GDPR / 数据本地化** 但又想要 GPT-4V 级别抽取精度的团队。
- 手里有 4090 / 5090 / A100，想跑本地 SOTA 文档 AI 的人。

## 参考链接

- [项目链接](https://github.com/datalab-to/lift)
- [原始链接](https://t.co/0qQJefuRvb)

## 相关概念

- [PP-OCRv6 Studio](tool-ppocrv6-studio.md) — 飞桨 PP-OCRv6 三档模型本地 OCR，Apple Silicon CoreML 加速（同属「本地文档识别」范畴）
- [a-stock-data](tool-a-stock-data.md) — A 股全栈数据 Skill（13 源 / 28 端点）
- [JSON-Render / 生成式 UI](tool-json-render.md) — 与「结构化 JSON 输出」方向互补的工具