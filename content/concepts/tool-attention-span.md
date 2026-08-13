---
type: Tool
title: "Attention Span"
description: "Claude Code 插件，提供三种「输出样式」，只改变模型的说话方式、不改变编码行为——让回答先给结论、短句分点、加粗关键句，便于扫读。"
resource: "https://github.com/alexgreensh/attention-span"
tags: "[claude, claude-code, plugin, output-style, readability, open-source]"
timestamp: "2026-08-13T19:53:00Z"
---

# Attention Span

## 它是什么
一个 **Claude Code 插件**，给 Claude 的回复换「说话方式」。Claude Code 默认输出常是**一整段难以扫读的文字墙**——Attention Span 提供三种**输出样式**让用户切换，目标是：

- 先给结论（首句即答案）
- 短句分点（一行一个意思）
- 加粗关键句（视觉锚点）

关键约束：**只改说话方式，不改编码行为**——不会改变模型的代码生成能力、工具调用链或上下文策略。

## 为什么用它 / 适合什么场景
- Claude Code 默认回复篇幅长、信息密度低，难扫读。
- 想要「不同任务用不同风格」——比如调试要详细，设计讨论要简练。
- 不想自己写一堆「请先给结论再展开」的提示词。
- 与编码相关的工作流保留完整性，只是阅读体验升级。

## 关键能力
| 能力 | 说明 |
|------|------|
| 形态 | Claude Code 插件 |
| 样式数 | 三种「输出样式」 |
| 改的范围 | 说话方式（结构 / 长度 / 重点） |
| 不改的范围 | 编码行为 / 工具调用 / 上下文策略 |
| 用户切换 | 可在会话中切换样式 |

## 相关概念
- [Claude Code](tool-claude-code.md) — 宿主；插件安装在该工具上
- [claudish-to-english](tool-claudish-to-english.md) — 同样面向「让 Claude 输出更易读」；Attention Span 改结构 / 样式，claudish-to-english 改语言通俗度

## 项目链接
- 项目主页：<https://github.com/alexgreensh/attention-span>