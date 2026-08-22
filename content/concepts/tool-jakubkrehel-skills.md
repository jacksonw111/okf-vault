---
type: Tool
title: "jakubkrehel Skills（含 /explain-interface）"
description: "jakubkrehel 维护的 Agent Skills 仓库，首发 `/explain-interface`：用 DevTools 风格的手段拆解任意网页交互与渐变等视觉技术如何被实现，Agent 跑一遍给出拆解。"
resource: "https://github.com/jakubkrehel/skills"
tags: [agent, skills, devtools, web, explain, design]
timestamp: 2026-08-21T03:56:03Z
---

# jakubkrehel Skills（含 /explain-interface）

## 它是什么
jakubkrehel 在 GitHub 开源的个人 Agent Skills 仓库，按 Claude Code / Codex 等支持「斜杠命令 Skill」的 agent 通用格式发布，主打「用 DevTools 风格工具拆解别人网页是怎么搭的」。首发命令 `/explain-interface`，回答类似「`https://interfere.com` 的渐变是用什么技术实现的？」

## 为什么用它 / 适合什么场景
- 想搞清楚一个具体网页交互 / 视觉细节（CSS 渐变、滚动联动、动画曲线、WebGL shader 等）是怎么搭的，但不想装浏览器扩展自己扒。
- 想在评审里引用「xx 网站用了 xx 技术」佐证设计决策，又不想手敲一长串 DevTools 操作。
- 教学 / 写作场景：让 agent 把别人页面的工程做法读出来再给你复盘一遍。

## 关键能力
| 能力 | 说明 |
|------|------|
| `/explain-interface <url>` | 给定网址，agent 像用 DevTools 一样逐元素拆解交互与渐变等视觉技术实现 |
| Skill 格式开放 | 命令作为 Skill 单元分发，可挂到 Claude Code / Codex 等支持的 agent |
| DevTools 风格抓取 | 复用 agent 自身的网页抓取能力，把"按 F12 看 elements / computed"翻译成自然语言 |
| 个人轻量仓库 | jakubkrehel 个人发布，按 Issue / PR 持续补充新 Skill 命令 |

## 一句话总结
**「别人网站是怎么搭的」用一条 `/explain-interface` 让 AI 自己开 DevTools 拆给你看。**

## 原始链接
- [jakubkrehel/skills 仓库](https://github.com/jakubkrehel/skills) — 原始仓库

## 相关概念
- [Jakub 设计 Skills](./note-jakub-design-skills.md) — Jakub 早期发布的设计 Skill 合集（同名不同项目）
- [Agent Skills 是什么](./term-agent-skills.md) — Skill 文件的通用约定