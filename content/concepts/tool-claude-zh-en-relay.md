---
type: Tool
title: "Claude-ZH-EN-Relay（Chrome 中文翻译中继）"
description: "ZhiqiaoGong 写的 Chrome 扩展，让用户用中文与 Claude 聊天——输入时把中文译为英文发送、Claude 回复时再译回中文，从而节省 token 用量。"
resource: "https://github.com/ZhiqiaoGong/Claude-ZH-EN-Relay"
tags: "[chrome-extension, claude, translation, token-saving, chinese]"
timestamp: "2026-07-11T20:00:00Z"
---

# Claude-ZH-EN-Relay（Chrome 中文翻译中继）

## 它是什么

`ZhiqiaoGong/Claude-ZH-EN-Relay` 是一个**Chrome 扩展**，用「中文 ↔ 英文」翻译做中继，让用户**用中文与 Claude 聊天**：

- 用户在 Claude.ai 输入中文 → 扩展自动译为英文发送。
- Claude 用英文回复 → 扩展自动译为中文显示。

这样做的**副作用是节省 token 用量**（中文字符 vs 英文 token 的经济性差异）。

## 为什么用它 / 适合什么场景

- 想用中文与 Claude 对话，但担心中文 token 偏贵。
- 想保留 Claude 英文原版的「聪明度」（很多模型对英文 prompt 表现更好）。
- 想把 Claude.ai 网页版直接当作「中文版」用。

## 关键能力

| 能力 | 说明 |
|------|------|
| 双向翻译 | 中文输入 → 英文发送；英文回复 → 中文显示 |
| Token 节省 | 中文字符 → 英文 token 通常更划算 |
| Chrome 扩展 | 装上即用，无侵入 |
| 模型选择 | 翻译引擎可配置 |

## 媒体参考

- 演示视频：<https://video.twimg.com/tweet_video/HM1UHsYaIAAAf59.mp4>

## 相关概念

- [Claude Code](tool-claude-code.md) — Claude Code CLI 形态，本扩展是 Claude.ai 网页版的中文化方案
- [Token Diet](tool-token-diet.md) — 编码代理的 token 减肥技能
- [Wenyi Translator](tool-wenyi-translator.md) — Claude 多语种长篇翻译 CLI

## 项目链接

- 项目仓库：<https://github.com/ZhiqiaoGong/Claude-ZH-EN-Relay>