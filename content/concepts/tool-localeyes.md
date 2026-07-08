---
type: "Tool"
title: "LocalEyes（Claude Code 本地视觉能力补齐）"
description: "让 Claude Code 中的纯文本 LLM（如 DeepSeek、CodeLlama、Qwen-Coder）通过本地 Ollama 视觉模型获得视觉能力。支持描述剪贴板截图、截取全屏并描述、读取已保存的图片文件三种模式。所有图像处理本地完成，不上传云端，无需 API key。"
resource: "https://github.com/NoPainNullGain/LocalEyes"
tags: "[claude-code, vision, ollama, local-llm, screenshot, mcp, privacy]"
timestamp: "2026-07-08T01:15:00Z"
---

# LocalEyes

## 它是什么

[LocalEyes](https://github.com/NoPainNullGain/LocalEyes) 是一个**让 Claude Code 中的纯文本 LLM「长出眼睛」**的工具——通过本地 Ollama 跑的视觉模型，给 DeepSeek / CodeLlama / Qwen-Coder 这类**没有原生视觉能力**的模型补上图像理解。

核心场景：你想让本地跑的开源模型能「看」截图 / 全屏 / 图片文件。

## 三种模式

| 模式 | 用途 |
|------|------|
| 描述剪贴板截图 | 读剪贴板里刚截的图 |
| 截取全屏并描述 | 截图当前屏幕 → 描述 |
| 读取已保存的图片文件 | 读磁盘上的图片 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 本地视觉 | 全部走本地 Ollama 视觉模型 |
| 隐私安全 | 图像不上传云端 |
| 无 API key | 无需 OpenAI / Anthropic 等云端 key |
| 安装极简 | 两条命令：`ollama pull` + `pip install` |
| 代码极简 | 核心 `vision` 脚本约 150 行 |
| 三种模式 | 截图 / 全屏 / 文件 |

## 适合谁

- 用本地开源 LLM（DeepSeek / Qwen-Coder 等）跑 Claude Code 的用户。
- 对「截图发云端」有隐私顾虑的开发者。
- 想低成本给本地 LLM 加视觉能力的极客。

## 参考链接

- [项目仓库](https://github.com/NoPainNullGain/LocalEyes)

## 相关概念

- [Local LLM Hardware Guide](./note-local-llm-hardware-guide.md) — 同为本地 LLM 玩法，但偏硬件选型
- [Claude Code](./tool-claude-code.md) — LocalEyes 的主要使用场景载体