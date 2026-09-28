---
type: "Tool"
title: "recall-mac（macOS 语义剪贴板管理器）"
description: "cnazk 出品：给 macOS 做能按语义检索历史的剪贴板管理器。同时把密码 / 助记词这类复制过的东西判为高危——不写盘、不喂模型、60 秒后自己消失。"
resource: "https://github.com/cnazk/recall-mac"
tags: "[macos, clipboard, semantic-search, privacy, security]"
timestamp: "2026-09-28T23:50:00Z"
---

# recall-mac（macOS 语义剪贴板管理器）

## 它是什么

[recall-mac](https://github.com/cnazk/recall-mac) 是 cnazk 出品的 **macOS 剪贴板管理器**：能**按语义检索历史**——你不需要记准确的字符串，想起「上次复制的那段关于……」就能搜出来。

隐私设计是它最大的卖点：识别出**密码 / 助记词 / API key 等敏感内容**时，**不写盘**、**不喂模型**、**60 秒后自动消失**。

## 为什么用它 / 适合什么场景

- macOS 原生剪贴板只能保留最近一项，需要**历史可检索**。
- 经常复制大段文字（链接 / 代码片段 / 长引用），想按语义找回。
- **对隐私敏感**——不愿让剪贴板历史 / 模型看到密码、助记词。
- 想用一个**本地**的剪贴板工具，不上传云端。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | macOS 剪贴板管理器 |
| 检索 | 语义搜索（不依赖精确字符串） |
| 隐私 | 密码 / 助记词等敏感内容不写盘、不喂模型 |
| 自动清理 | 敏感内容 60 秒后自动消失 |
| 出品 | cnazk |

## 相关概念

- [Apple Hide My Email](./term-apple-hide-my-email.md) — 同属 macOS 隐私工具生态（一个管邮箱、一个管剪贴板）
- [Self-Hosted（自托管）](./term-self-hosted.md) — recall-mac 偏本地优先、不联网的设计哲学