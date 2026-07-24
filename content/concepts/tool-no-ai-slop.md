---
type: Tool
title: "no-ai-slop（去 AI 套话味儿扫描器）"
description: "把 AI 文本里 20 多种常见套话模式一把扫干净——「不是 A 而是 B」二元对比、冒号披露句、「作为一个什么中心」虚词、同义词轮换等等。"
resource: "https://github.com/petergyang/no-ai-slop"
tags: [writing, ai-humanizer, linter, prose]
timestamp: "2026-07-24T00:00:00Z"
---

# no-ai-slop

[no-ai-slop](https://github.com/petergyang/no-ai-slop) 是一个**专门识别并扫除 AI 套话味儿**的扫描工具。它能识别 20 多种「典型 LLM 输出味道」的模式，让作者在保持内容的同时剥离那种「一眼就是 AI 写的」感。

## 它识别哪些 AI 套话

| 模式 | 示例 |
|------|------|
| 「不是 A 而是 B」二元对比 | "不是工具，而是伙伴" |
| 冒号披露句 | "关键在于：xxx" |
| 「作为一个 XX 中心」虚词 | "作为一个开放中心" |
| 同义词轮换 | 反复换「重要 / 关键 / 核心 / 首要」 |
| （更多 20+ 种）| … |

## 它解决的问题

- **作者**：Lerect 写完初稿后跑一遍，能看到所有「AI 味儿」位置。
- **编辑 / 出版方**：批量审稿时自动标记「需要人工润色」段落。
- **写作工具**：在 LLM 输出回灌给用户前先过一遍，去掉最扎眼的套话。

## 关键能力

| 能力 | 说明 |
|------|------|
| 20+ 模式识别 | 覆盖最常见的 AI 套话句式 |
| 规则化 | 不依赖模型调用，纯规则扫描，可离线、可批量 |
| 写作辅助 | 让作者主动避开这些「AI 标记句式」 |
| 与 AI Humanizer 互补 | AI Humanizer 是「润色让它更像人」，no-ai-slop 是「先去掉最明显的 AI 句式」 |

## 参考链接

- 项目仓库: <https://github.com/petergyang/no-ai-slop>

## 相关概念

- [AI Humanizer Handbook](tool-ai-humanizer-handbook.md) — AI 文本人性化实操指南（手动润色 + 工具对比 + Skill）
- [vibecoded-design-tells](tool-vibecoded-design-tells.md) — AI 生成视觉的「AI 网站视觉痕迹」排行榜，本工具是其文本侧版本