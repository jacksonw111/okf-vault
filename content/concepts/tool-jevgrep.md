---
type: "Tool"
title: "jevgrep（用自然语言在仓库里找代码块）"
description: "不记得符号名的时候，用一句「这块逻辑在哪」把仓库里对得上的代码捞出来，原样带路径和行号丢给 agent 接着读。"
resource: "https://github.com/nassim-arifette/jevgrep"
tags: "[code-search, agent-tool, semantic-search, repository]"
timestamp: "2026-09-21T22:00:00Z"
---

# jevgrep

## 它是什么

[nassim-arifette/jevgrep](https://github.com/nassim-arifette/jevgrep) 是用**自然语言**在仓库里**找代码块**的工具——不记得符号名的时候，用一句「这块逻辑在哪」就把对得上的代码捞出来。

## 与传统 grep 的差别

| 维度 | `grep` | `jevgrep` |
|------|--------|-----------|
| 输入 | 关键字 / 正则 | 自然语言 |
| 输出 | 行 | 代码块（带路径 + 行号） |
| 匹配方式 | 字面 / 词法 | 语义 |
| 适用 | 知道要找什么 | 只记得大致意图 |

## 为什么用它 / 适合什么场景

- 接手**陌生仓库**，不知道符号命名风格。
- 写完代码忘了**当时把它放在哪**——「这个校验逻辑在哪」。
- 配合 agent：先 grep 出代码块**带行号丢给 agent**，让 agent 接着读、解释、改。

## 关键能力

| 能力 | 说明 |
|------|------|
| 自然语言检索 | 一句描述即可 |
| 带路径 + 行号输出 | 直接喂给 agent |
| 仓库级 | 在整个代码库里找 |

## 项目链接

- 仓库：<https://github.com/nassim-arifette/jevgrep>

## 媒体

视频：<https://video.twimg.com/tweet_video/HSs4Rr-aQAAyYvE.mp4>

## 相关概念
