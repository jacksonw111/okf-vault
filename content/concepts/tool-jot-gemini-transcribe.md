---
type: "Tool"
title: "Jot（Gemini macOS 语音输入）"
description: "google-gemini 官方出的 macOS 工具：按住 fn 键说话，松开后把标点齐整、去掉口头禅的文字直接输入到光标处。"
resource: "https://github.com/google-gemini/jot-gemini-transcribe-macOS"
tags: "[macos, voice-input, dictation, fn-key, gemini, punctuation-cleanup, google]"
timestamp: "2026-09-17T05:35:00Z"
---

# Jot（Gemini macOS 语音输入）

## 它是什么

[google-gemini/jot-gemini-transcribe-macOS](https://github.com/google-gemini/jot-gemini-transcribe-macOS) 是 **google-gemini** 官方出的 macOS 语音输入工具。它的交互极简：

> 按住 `fn` 键 → 说话 → 松开 → 把标点齐整、去掉口头禅的文字**直接输入到光标处**。

全程无需切换窗口、无需复制粘贴、无需打开独立应用。

## 关键能力

| 能力 | 说明 |
|------|------|
| fn 按住说话 | 单键触发，松开即停止录音 |
| Gemini 转写 | 后端用 Gemini 模型做语音识别 |
| 自动加标点 | 输出文本自带合理标点，不需要事后补 |
| 去口头禅 | 过滤「嗯 / 那个 / 然后」之类口水词 |
| 直接键入 | 转写结果写到当前光标所在的应用，不需要切换 |

## 适合什么场景

- 写代码时不想打断思路、用说话代替打字的开发者（写注释 / commit message / 文档尤其顺手）。
- 长篇写作时用「口述 → 文字」提速的内容创作者。
- 想找一个「比 macOS 自带 Dictation 更智能、能去口语毛刺」的工具的 macOS 用户。

## 参考

- 项目链接：<https://github.com/google-gemini/jot-gemini-transcribe-macOS>

![preview](https://pbs.twimg.com/media/HSWFtjTa8AAj4nZ.jpg)
