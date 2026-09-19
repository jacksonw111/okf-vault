---
type: "Tool"
title: "is-gpt-nerfed（macOS Codex 缩水检测器）"
description: "常驻菜单栏的 macOS 工具，检测 Codex 实际回答的模型是否与所选模型一致，发现静默降级、推理力度降低、隐藏模型和小上下文窗口。"
resource: "https://github.com/kiyoakii/is-gpt-nerfed"
tags: "[codex, macos, model-verification, menu-bar, observability, llm-nerfing]"
timestamp: "2026-09-19T16:00:00Z"
---

# is-gpt-nerfed（macOS Codex 缩水检测器）

## 它是什么

[kiyoakii/is-gpt-nerfed](https://github.com/kiyoakii/is-gpt-nerfed) 是一个**常驻 macOS 菜单栏的 Codex 缩水检测器**——它逐轮读取 Codex 的会话记录，**零 token 开销地**对照「你选的模型」与「实际回答的模型」，发现：

- 模型被静默切换 / 降级
- 推理力度被偷偷调低
- 用了未公开的隐藏模型
- 上下文窗口比预期小

## 为什么用它 / 适合什么场景

- 长期用 Codex 编码、但**怀疑背后可能被偷偷降本**而回答质量下滑的开发者。
- 想验证「付费档位真的拿到对应模型 vs 被换到轻量变体」的对照实验。
- 关心 AI 工具可观测性 / 模型供应链透明度的工程师。

## 关键能力

| 能力 | 说明 |
|------|------|
| 菜单栏常驻 | macOS 状态栏直接看，不用开 App |
| 零 token 开销 | 读本地会话记录，不发额外请求 |
| 模型切换告警 | 检测所选 vs 实际回答的模型是否一致 |
| 推理力度 / 隐藏模型 | 识别"低调参数 / 隐藏变体" |
| 上下文窗口核对 | 对照声称的窗口大小与实际可用 |

## 与相关概念的关系

- [Codex](./tool-codex.md) — 检测对象就是 Codex；is-gpt-nerfed 帮你判断「你点选的 Codex 模型」背后有没有被换

## 参考

- 项目链接：<https://github.com/kiyoakii/is-gpt-nerfed>
- 原始推文：<https://x.com/QingQ77/status/2101159351151165908>