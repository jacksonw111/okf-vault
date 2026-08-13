---
type: Tool
title: "claudish-to-english"
description: "Claude Code 插件，用本地 ollama 模型把每条消息重写成通俗英语——只改屏幕上看到的输出，会话记录与推理过程保持原样。"
resource: "https://github.com/gvzdv/claudish-to-english"
tags: "[claude, claude-code, ollama, plugin, localization, open-source]"
timestamp: "2026-08-13T19:53:00Z"
---

# claudish-to-english

## 它是什么
**Claude Code 插件**：调用本地 ollama 模型，把 Claude Code 的每条消息**实时重写成更通俗的英语**，再呈现给用户。

关键约束是**只改显示层**——屏幕看到的是改写后的版本，但：
- 会话记录 / 日志保持 Claude 原话
- 推理过程 / 工具调用链不受影响
- 上下文不被改写污染

## 为什么用它 / 适合什么场景
- Claude Code 默认回复常又长又绕，技术词汇 / 学术化措辞密集；用本地模型做一层「白话翻译」提速扫读。
- 不希望污染模型上下文（避免降级后续推理质量）。
- 已有 ollama 本地环境，不想再为翻译单独付费云端。
- 想保留 Claude 原话留档，事后审计 / 回溯。

## 关键能力
| 能力 | 说明 |
|------|------|
| 部署形态 | Claude Code 插件 |
| 翻译模型 | 本地 ollama（自选） |
| 作用范围 | 仅屏幕输出 |
| 不污染 | 会话记录 / 推理链 / 上下文 |
| 离线 | 翻译侧不依赖云端 |

## 相关概念
- [Claude Code](tool-claude-code.md) — 被增强的宿主；插件安装在该工具上
- [Attention Span](tool-attention-span.md) — 同样瞄准「让 Claude 输出更易扫读」，但 Attention Span 改的是「输出样式 / 说话方式」，claudish-to-english 改的是「语言简化 / 通俗化」

## 媒体
- 截图参考：<https://pbs.twimg.com/media/HPfXI2AaUAANkuO.jpg>

## 项目链接
- 项目主页：<https://github.com/gvzdv/claudish-to-english>