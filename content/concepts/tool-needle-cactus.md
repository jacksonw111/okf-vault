---
type: "Tool"
title: "Needle（cactus-compute：8–29 MB 端侧超微型自动化模型）"
description: "cactus-compute/needle 是专门跑在端侧的超微型自动化模型：体积只有 8 MB 到 29 MB，专精两件事——理解用户指令然后调用工具、提取结构化 JSON。本地离线运行，零网络延迟，零 API 账单，设备断网也能秒级执行自动化；搞不定的复杂任务还能输出置信度分数，自动转交云端大模型兜底。"
resource: "https://github.com/cactus-compute/needle"
tags: "[edge-ai, on-device, tool-use, json-extraction, small-model]"
timestamp: "2026-09-21T22:00:00Z"
---

# Needle（cactus-compute）

## 它是什么

[cactus-compute/needle](https://github.com/cactus-compute/needle) 是**专门跑在端侧的超微型自动化模型**——**8 MB 到 29 MB** 体量。

## 两件专精事

| 任务 | 说明 |
|------|------|
| 理解用户指令后**调用工具** | 端侧 tool use |
| **提取结构化 JSON** | 端侧 NLU → 结构化输出 |

## 运行形态

- **本地离线**运行。
- **零网络延迟**。
- **零 API 账单**。
- **设备断网也能秒级执行自动化**。

## 复杂任务的兜底

遇到搞不定的复杂任务时，**输出置信度分数**，**自动转交给云端大模型兜底**。

## 为什么用它 / 适合什么场景

- **智能家居 / 硬件折腾**——想在本地通过自然语言触发控制、调接口。
- 做**客户端 / 本地小工具**——想做自然语言意图识别，又不想每次都调云端 API 烧钱。
- **网络受限**场景——设备没网也想有 agent。

## 关键能力

| 能力 | 说明 |
|------|------|
| 8–29 MB 体量 | 嵌入式硬件、IoT 都能跑 |
| 离线运行 | 不依赖网络 |
| 零 API 成本 | 本机推理 |
| 工具调用 | 端侧 tool use |
| JSON 提取 | 端侧结构化输出 |
| 云端兜底 | 置信度低时自动升级 |

## 项目链接

- 仓库：<https://github.com/cactus-compute/needle>

## 相关概念
