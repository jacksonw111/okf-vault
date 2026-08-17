---
type: Tool
title: "agent-vision-toolkit"
description: "给跑在纯文本模型（如 DeepSeek）上的 coding agent 加视觉能力：CLI 工具 + skill + 本地透明代理，让只能读文字的模型也能看图、问答、OCR、还原 UI、操作 GUI"
resource: "https://github.com/Anionex/agent-vision-toolkit"
tags: [vision, ocr, coding-agent, deepseek, multimodal, proxy]
timestamp: 2026-08-17T16:00:00Z
---

# agent-vision-toolkit

## 它是什么

`Anionex/agent-vision-toolkit` 是给**纯文本 coding agent**（如 DeepSeek）配的「眼睛」：由 **CLI 工具 + Skill + 本地透明代理**三件套组成，让**只能读文字的模型**也能完成：
- **看图问答**（截图 → 推理）
- **OCR**（图片 → 文本）
- **UI 还原**（截图 → 可执行操作）
- **操作 GUI**（点击 / 输入）

透明代理的模式：agent 发出「看图」请求 → 透明拦截 → 调用本地视觉模型 → 把结果回填 → agent 继续推理。整个过程对 agent 透明，相当于无感升级。

## 为什么用它 / 适合什么场景

- 主模型是 DeepSeek 等便宜纯文本模型，但任务里夹了截图。
- 想保留**纯文本模型的可控性 + 计费粒度**，只把视觉能力外挂。
- 想让 DSH / pi / Codex 等编码 agent 在不改内核的前提下获得视觉。
- 想做 UI 自动化 / 视觉回归 / OCR 数据清洗，又想跑本地小模型省钱。

## 关键能力

| 能力 | 说明 |
|------|------|
| 图片问答 | 截图 + 问题 → 文本模型可消费的描述 |
| OCR | 截图 / 文档 → 文字 |
| UI 还原 | 截图 → 结构化 UI 操作列表 |
| GUI 操作 | 截图 + 指令 → 点击 / 输入 |
| 透明代理 | 对 agent 透明拦截，无需改 agent 内核 |
| CLI + Skill | 既可命令行调用，也可作为 skill 注册 |

## 媒体

- ![](https://pbs.twimg.com/media/HPvT1dKaEAAou_J.jpg)

## 原始链接

- [项目仓库](https://github.com/Anionex/agent-vision-toolkit)

## 相关概念

- [dsh-vision-toolkit](./tool-dsh-vision-toolkit.md) — 同样是「给纯文本 DeepSeek 加视觉」的思路，但 dsh-vision-toolkit 专为 DSH 设计；agent-vision-toolkit 更通用（CLI + skill + 透明代理）