---
type: "Tool"
title: "OmniStudio（本地大模型一站式桌面工作台）"
description: "把本地大模型的下载、推理服务运行和对话、语音、图片、视频、OCR、翻译等应用收进一个桌面工作台，全程本地优先；模型市集基于 ModelScope，支持 GGUF / safetensors 全格式 + 队列并发 + 断点续传，推理侧统一抽象 llama.cpp / vLLM / SGLang 三引擎并可热切换。"
resource: "https://github.com/kunpengtalk/OmniStudio"
tags: "[local-llm, desktop, gguf, vllm, sglang, llama-cpp, ocr, tts]"
timestamp: "2026-09-14T22:30:00Z"
---

# OmniStudio（本地大模型一站式桌面工作台）

## 它是什么

[kunpengtalk/OmniStudio](https://github.com/kunpengtalk/OmniStudio) 把本地大模型的**下载 + 推理服务运行 + 上层应用**（对话、语音、图片、视频、OCR、翻译）都收进一个桌面工作台，**全程本地优先**。

## 关键能力

| 能力 | 说明 |
|------|------|
| 模型市集 | 基于 ModelScope 搜索 |
| 多格式下载 | GGUF / safetensors 全格式 |
| 队列并发 | 多模型同时下载 |
| 断点续传 | 大文件下载不怕断网 |
| 能力分类 | 按对话 / 语音 / 视觉 / 视频分类 |
| 三推理引擎 | llama.cpp / vLLM / SGLang 统一抽象 |
| 热切换 | 运行时切换后端 |
| 20+ 云厂商 | 内置 OpenAI 兼容厂商预设 |
| 应用收口 | 对话 / 语音 / 图片 / 视频 / OCR / 翻译 |

## 适合谁

- 想一站式跑本地大模型，不想装 Ollama / LM Studio / ComfyUI 等多个工具
- 想在不同推理引擎间切换
- 想统一管理对话 / 语音 / 视觉多个应用

## 项目链接

- 仓库：<https://github.com/kunpengtalk/OmniStudio>
