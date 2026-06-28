---
type: "Tool"
title: "Kanarenshu（假名练习 TUI）"
description: "Go 写的终端 TUI 日语假名练习工具，提供平假名 / 片假名 / 混合三种模式，基于权重自适应算法——答错的字符出现频率更高，掌握后自动减少。"
tags: "[tui, japanese, learning, go, spaced-repetition]"
timestamp: "2026-06-28T00:45:00Z"
resource: "https://github.com/nuixyz/kanarenshu"
---

# Kanarenshu（假名练习 TUI）

## 它是什么

Kanarenshu（仮名練習，「假名练习」的罗马字）是 **Go** 写的**终端 TUI 日语假名练习工具**，帮用户熟悉平假名（ひらがな）与片假名（カタカナ）。三种模式：

- **平假名** 单独练习
- **片假名** 单独练习
- **混合** 模式

## 自适应权重算法

核心特点是**基于权重的字符调度**：

- 答错的字符 → 出现频率自动提高
- 答对的字符 → 频率逐渐降低
- 整个过程在终端里实时调整

相比传统「50 音图死背」省去大量重复劳动，把练习时间集中在薄弱字符上。

## 关键能力

| 能力 | 说明 |
|------|------|
| 三模式 | 平假名 / 片假名 / 混合 |
| 权重自适应 | 答错多练、答对少练 |
| 终端 TUI | 全键盘交互，零依赖 |
| Go 单二进制 | 一份 go install 即可使用 |

## 启动

```bash
go install github.com/nuixyz/kanarenshu@latest
kanarenshu
```

## 界面预览

![Kanarenshu 练习界面](https://pbs.twimg.com/media/HL26_7haIAAOPTJ.jpg)

## 参考链接

- [项目仓库](https://github.com/nuixyz/kanarenshu)
- [原始链接](https://x.com/QingQ77/status/2071032079224013191)

## 相关概念

- [ExamPrep-AI](tool-exam-prep-ai.md) — PDF 笔记转闪卡，与 Kanarenshu 同属「间隔重复学习」家族但面向通用备考
- [happy-figure-skill](tool-happy-figure-skill.md) — 学术场景的 AI Skill，与 Kanarenshu 互补