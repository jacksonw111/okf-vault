---
type: Tool
title: "cordis-mini（DeepSeek Harness 五机制迷你版）"
description: "adpanru 开源：把 deepseek-harness 五个核心机制（插件注册、ctx.llm 加载、上下文传递等）各写一份约 600 行的 Python 迷你版，跑一遍 demo 就能看见完整数据流。"
resource: "https://github.com/adpanru/cordis-mini"
tags: [agent, dsh, deepseek-harness, learning, mini, python, open-source]
timestamp: 2026-08-21T09:23:00Z
---

# cordis-mini（DeepSeek Harness 五机制迷你版）

## 它是什么
cordis-mini 是一个为「想读懂 deepseek-harness 源码但无从下手」的人准备的迷你实现：把 dsh 核心的五个机制（插件如何注册、`ctx.llm` 从哪里冒出来、上下文如何传递、加载顺序由谁决定、子代理怎么派发）各用约 600 行 Python 重写一遍，总共不到 3000 行就能跑 demo 把完整数据流跑出来。

## 为什么用它 / 适合什么场景
- 想给 deepseek-harness 写插件 / 二次开发，但直接读源码被层层抽象劝退。
- 教学 / 培训：把 dsh 的核心抽象「对应到一份能跑的小代码」，比看 1000 行业务代码高效。
- 想理解其他 harness（Codex / Claude Code / Hermes / Pi）也都能借鉴的同类核心机制。

## 关键能力
| 能力 | 说明 |
|------|------|
| 600 行 ×5 机制 | 5 份迷你实现，每份对应 dsh 一个核心抽象 |
| 完整数据流 | 跑一遍 demo 看见从插件加载到模型调用的完整链路 |
| Python 实现 | 用 Python 简化 boilerplate，让读者专注机制本身 |
| 可调试 | 单文件 / 小代码量，单步跟进零阻力 |
| 开源学习用 | Apache / MIT 类许可，可自由学习与扩展 |

## 一句话总结
**想读懂 deepseek-harness？先跑一遍这五份 600 行 Python 迷你版，看清数据流再回去啃源码。**

## 原始链接
- [adpanru/cordis-mini](https://github.com/adpanru/cordis-mini) — 原始仓库

## 相关概念
- [DeepSeek Harness 中文手册](./note-deepseek-harness-handbook.md) — 与本仓库互为「读源码前后的两本参考书」
- [DeepSeek Harness 橙皮书](./note-deepseek-harness-orange-book.md) — 非开发者实测第一手体验