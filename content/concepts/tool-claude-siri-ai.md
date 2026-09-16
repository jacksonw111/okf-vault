---
type: "Tool"
title: "claude-siri-ai"
description: "macOS 27 上给 Spotlight / Siri 加一个 Claude 问答入口，提示词走本地 Swift 桥丢给你自己登录好的 Claude Code CLI，纯文本答案流回苹果原生气泡。"
resource: "https://github.com/mpociot/claude-siri-ai"
tags: "[macos, siri, spotlight, claude, swift, integration]"
timestamp: "2026-09-16T16:01:00Z"
---

# claude-siri-ai

## 它是什么

[mpociot/claude-siri-ai](https://github.com/mpociot/claude-siri-ai) 在 macOS 27 上给 **Spotlight / Siri 加一个 Claude 问答入口**：本地 Swift 桥负责把用户提问包装好，直接丢给本机已经登录好的 **Claude Code CLI**，再把流式返回的纯文本答案写回苹果原生气泡，无需打开终端窗口。

## 为什么用它 / 适合什么场景

- 想在 macOS 系统级调起 Claude 而不切换 App。
- 把 Claude Code CLI 当作 LLM 后端，避开自己再开 API Key。
- 需要在 Spotlight 搜索结果里直接看到 AI 回答。

## 关键能力

| 能力 | 说明 |
|------|------|
| Spotlight / Siri 集成 | 系统级入口免切窗口 |
| 本地 Swift 桥 | 负责包装 prompt + 调用 CLI |
| 复用本地 Claude Code CLI | 直接接你登录好的会话，不另开 API |
| 苹果原生气泡 | 答案流式显示在系统通知样式里 |
| 纯文本输出 | 不走特殊渲染，原生 UI 即可显示 |

## 媒体

- ![](https://pbs.twimg.com/media/HSTVMmWa4AAztO9.jpg)

## 相关概念

- [Claude Code](./tool-claude-code.md) — 被该项目当 LLM 后端的终端 AI 编码 agent