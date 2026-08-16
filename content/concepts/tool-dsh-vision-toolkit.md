---
type: Tool
title: "dsh-vision-toolkit"
description: "DeepSeek Harness 视觉插件：让纯文本 DeepSeek 模型在 DSH 里做视觉任务（图片问答、长截图 OCR、UI 还原、像素级比对），无需切换到多模态模型"
resource: "https://github.com/Anionex/dsh-vision-toolkit"
tags: [deepseek, harness, dsh, vision, ocr, agent]
timestamp: 2026-08-16T16:00:00Z
---

# dsh-vision-toolkit

## 它是什么
`Anionex/dsh-vision-toolkit` 是 **DeepSeek Harness (DSH)** 的一个插件（toolkit），给纯文本 DeepSeek 模型**外挂一个「眼睛」**：在 agent 链路里串入 OCR、目标定位、UI 还原、像素级比对等**视觉工具**，让 DSH 端到端完成「看图 → 推理」任务，**不用把模型换成多模态 DeepSeek**。

## 为什么用它 / 适合什么场景
- 团队 / 流水线主模型是 DeepSeek 文本版本（便宜、稳定），但任务里夹了截图。
- 想保留文本模型可控性、可观察性、可计费粒度，视觉能力外挂解决。
- UI 自动化 / 视觉回归测试 / OCR 数据清洗：让 agent 看一眼就能判断。
- 想把视觉工具做成 DSH 的「第一类工具」，跟其它 MCP 工具混用。

## 关键能力
| 能力 | 说明 |
|------|------|
| 带意图的图片问答 | 给定截图 + 提问，工具先抽信息再交给文本模型 |
| 长截图 OCR | 整页 / 长滚动截图 → 纯文本，配合上下文 |
| UI 还原 | 把截图里的 UI 结构反推成可执行操作列表 |
| 像素级比对 | 两张图差异区域定位，适合视觉回归 / UI 检查 |
| 作为 DSH 工具挂载 | 不需要改 DSH 内核，按标准工具协议注册 |

## 媒体
- ![](https://pbs.twimg.com/media/HPvJ5-AbkAAHCgl.jpg)

## 相关概念
- [项目链接](https://github.com/Anionex/dsh-vision-toolkit)