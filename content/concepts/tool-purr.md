---
type: Tool
title: "Purr"
description: "macOS 菜单栏按住说话听写工具，全程本地推理不传音频，默认 Parakeet 英文模型，可换 WhisperKit 多语言，含会议录音与本地摘要。"
resource: "https://github.com/iamarunbrahma/purr"
tags: "[macos, dictation, voice-to-text, local-ai, whisper, parakeet]"
timestamp: "2026-06-29T16:00:00Z"
---

# Purr

## 它是什么
Purr 是一款 macOS Apple Silicon 上的菜单栏按住说话听写应用，主打「全程本地推理、音频不上传」。MIT 协议、菜单栏常驻、第一次启动会下载约 450 MB 的本地模型，之后可断网使用。

![](https://pbs.twimg.com/media/HL78eaebQAAGdXx.jpg)

## 为什么用它 / 适合什么场景
- **想换掉 Wispr Flow / MacWhisper 等闭源订阅工具**：本地推理、不传音频、模型本地下载。
- **想同时有听写 + 会议记录两套能力**：会议模式录麦克风 + 系统声，本地分说话人，结束自动出摘要。
- **多语言需求**：默认 Parakeet 英文（延迟低，可边说边打字），换 WhisperKit 后支持更多语言。

## 关键能力
| 能力 | 说明 |
|------|------|
| 全局热键按住听写 | 菜单栏触发，识别结果直接打当前文本框 |
| 模型可换 | Parakeet（英文低延迟）/ WhisperKit（多语言） |
| 边说边打字 | 流式识别，延迟可感 |
| 会议模式 | 录麦克风 + 系统声，本地分说话人 |
| 会议摘要 | 本地 LLM 出纪要 |
| 语音改写选中文本 | 选中一段文字，语音指令改写 |
| 离线可用 | 模型下完后断网可用 |

## 系统要求
- macOS 14+
- Apple Silicon（默认模型本地推理）
- 权限：麦克风、辅助功能、输入监控（用于键入）

## 参考链接
- [原始链接](https://x.com/QingQ77/status/2071506454834757785)
- [项目链接](https://github.com/iamarunbrahma/purr)

## 相关概念
- [Verenu](./tool-verenu.md) — 同样是按住说话桌面听写，但走的是外部 API（音频上传到所选转写服务）；Purr 强在本地推理
- [Ember](./tool-ember-hackernews.md) — 同为 macOS 优先的开源工具，但定位是 Hacker News 阅读器