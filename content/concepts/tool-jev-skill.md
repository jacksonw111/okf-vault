---
type: "Tool"
title: "jev-skill"
description: "把 Jev 判断模型的使用方式整理成 5 个可直接装进编码 agent 的技能和 108 个可复制改写的场景，让 agent 把分类、排序、打分这类判断题交给 Jev。"
resource: "https://github.com/wuyoscar/jev-skill"
tags: "[agent-skills, jev, classification, decision, open-source, claude-code]"
timestamp: "2026-09-23T22:35:00Z"
---

# jev-skill

## 它是什么

[jev-skill](https://github.com/wuyoscar/jev-skill) 是把 **Jev 判断模型**用法打包成**编码 Agent 可直接调用的 Skills 集合**：

> 把 Jev 判断模型的使用方式整理成 5 个可直接装进编码 agent 的技能和 108 个可复制改写的场景，让 agent 把分类、排序、打分这类判断题交给 Jev。

## 为什么用它 / 适合什么场景

- 想让 Claude Code / Codex / Cursor 等 agent 在「**判断题**」场景自动调用 Jev，而不是让前沿模型自己答。
- 想直接复用别人整理好的 **108 个场景模板**，不必从零写。
- 想知道「**Jev 适合哪些问题**」的具体清单。

## 关键能力

| 能力 | 说明 |
|------|------|
| Skills 数 | 5 个直接可装 |
| 场景模板 | 108 个可复制改写 |
| 适配 | Claude Code / Codex / Cursor 等编码 Agent |
| 任务类型 | 分类 / 排序 / 打分等判断题 |

## 与同类 Jev 集成的差异

| 工具 | 形态 |
|------|------|
| jev-skill | Agent Skills + 场景模板（适合编码 Agent） |
| hermes-jev-skills | 每轮小决策路由 |
| jev-cli | CLI 命令行 + jev-mcp |

## 项目链接
- 项目主页：<https://github.com/wuyoscar/jev-skill>

## 媒体
![jev-skill 截图](https://pbs.twimg.com/media/HSyh51MaUAAsvBp.png)
