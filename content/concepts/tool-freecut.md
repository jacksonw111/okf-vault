---
type: "Tool"
title: "freecut（Moh4696/freecut）"
description: "为 video-use 这类 Agent 视频剪辑工具替换掉付费的 ElevenLabs Scribe 转录后端，改用免费、可插拔的本地转录，让你不配任何 API key 也能用 Claude Code 剪视频。"
tags: "[video, transcription, mcp, claude-code, agent, local-first]"
timestamp: "2026-07-18T20:00:00Z"
resource: "https://github.com/Moh4696/freecut"
---

# freecut（Moh4696/freecut）

## 它是什么

[`freecut`](https://github.com/Moh4696/freecut) 是 Moh4696 开源的 video-use 替代品，**专门解决「video-use 强制依赖付费 ElevenLabs Scribe 转录」**的问题：

- 原版 video-use 让 Agent（Claude Code 等）能基于视频做剪辑，但转录环节强绑 ElevenLabs Scribe（付费、要 API key）；
- freecut 把这一层**换成可插拔的本地转录后端**（例如本地 whisper 兼容服务）；
- 用 freecut 后，**完全不依赖任何云端付费服务**，全程本地、转录可控、零成本。

## 关键能力

| 能力 | 说明 |
|------|------|
| 替换付费依赖 | 解除 video-use 对 ElevenLabs Scribe 的硬绑定 |
| 可插拔转录后端 | 兼容 OpenAI Whisper API 协议即可接入 |
| 完全本地化 | 不需要 ElevenLabs 账号、不上传音频 |
| 保留 Agent 工作流 | 仍可被 Claude Code 等 Coding Agent 直接调用 |

## 适合什么场景

- 用 Claude Code / Codex / OpenCode 做 Agent 视频剪辑，又不想付费买转录服务；
- 数据敏感（视频内容不能上云）的场景；
- 想把 video-use 接入私有 ASR 服务的人。

## 参考链接

- [原始链接](https://github.com/Moh4696/freecut)

## 相关概念

- [Local LLM 硬件指南](note-local-llm-hardware-guide.md) — freecut 推荐本地转录，本地推理选型可参照该笔记