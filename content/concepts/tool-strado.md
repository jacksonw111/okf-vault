---
type: Tool
title: "Strado（多 AI 编码代理工作台：独立 worktree + 内置浏览器 / IDE）"
description: "多 AI 编码代理并行协作平台：每个代理给一个独立 git worktree，互不踩改；内置浏览器与 IDE，盯着页面就能确认代理说"改好了"是不是真的生效。"
resource: "https://github.com/strado-io/strado"
tags: [multi-agent, coding-agent, worktree, ide, browser, collaboration]
timestamp: "2026-08-27T06:28:00Z"
---

# Strado

## 它是什么
[strado-io/strado](https://github.com/strado-io/strado) 是**同时跑多个 AI 编码代理的协作平台**。痛点：当你同时开好几个 AI 编码代理时，终端窗口满天飞、改动互相踩、验证只能靠代理自己说"改好了"——这根本没法信。

Strado 的解法：

- **每个 AI 代理拿一个独立 git worktree**——互不踩改、各自一份；
- **内置浏览器 + IDE**——你盯着页面就能确认改的是不是真的生效；
- **统一调度**——多代理在一个工作台里并行协作。

## 为什么用它 / 适合什么场景
- 团队里同时跑多个 coding agent（Codex / Claude Code / Cursor 等）做并行任务；
- 想给 AI 代理之间做物理隔离（独立 worktree）防止互相覆盖；
- 想亲眼看着页面 / 测试结果，而不是只看代理的「文字回报」；
- 关心"代理说改完了"的可信度问题，需要可视化兜底。

## 关键能力
| 能力 | 说明 |
|------|------|
| 独立 worktree | 每个代理独占 git worktree |
| 隔离改动 | 代理之间互不踩改 |
| 内置浏览器 | 直接看 UI 真实变化 |
| 内置 IDE | 直接看代码变化 |
| 可视化验证 | 盯页面就能判代理有没有"嘴硬" |
| 多代理并行 | 一个工作台跑多个 coding agent |
| 统一调度 | 多代理状态集中查看 |

## 相关概念
- [Claude Code](tool-claude-code.md) — 终端原生 AI 编码 agent；Strado 是它的「多实例协作 + 可视化兜底」层
- [FyAgent](tool-fyagent.md) — 统一多 AI 代理的配置；Strado 是统一多 AI 代理的**工作环境**——一条管配置、一条管运行时
- [Multi-AI-Coding-Config-Panel](tool-multi-ai-coding-config-panel.md) — 多代理配置面板；Strado 是配置 + 工作台一体化

## 参考链接
- 项目链接：<https://github.com/strado-io/strado>
