---
type: Tool
title: "dsh-crew (ZSeven-W/dsh-crew)"
description: "把 DeepSeek Harness 的 agent 作为子代理接到 Claude Code 和 Codex 里使用，子任务进度同步显示在宿主自己的面板上"
resource: "https://github.com/ZSeven-W/dsh-crew"
tags: [deepseek-harness, dsh, claude-code, codex, subagent, multi-agent]
timestamp: 2026-08-20T06:14:00Z
---

# dsh-crew (ZSeven-W/dsh-crew)

## 它是什么
[`ZSeven-W/dsh-crew`](https://github.com/ZSeven-W/dsh-crew) 把 **DeepSeek Harness (DSH)** 的 agent 当作**子代理**接到 **Claude Code** 与 **Codex** 里使用：当主代理（宿主）派活给子代理时，子代理的执行进度**继续显示在宿主自己的面板**里，不用来回切窗口。

## 为什么用它 / 适合什么场景
- 你日常用 Claude Code / Codex，但希望某些任务（多文件搜索 / 长上下文总结 / 大块代码改动）交给专门化 agent 跑。
- 想让多 agent 协作保留「在一个 UI 里看进度」的连贯体验，不切到 DSH 自己的 Web UI。
- 想直接复用 DSH 已有生态的子代理能力，不必在 Claude Code 里重新实现一遍。

## 关键能力
| 能力 | 说明 |
|------|------|
| 宿主集成 | 以插件形式接入 Claude Code / Codex |
| 子代理调度 | DSH agent 作为子代理被宿主调用 |
| 进度回传 | 子代理进度回流到宿主自己的 UI 面板 |
| DSH 生态复用 | 直接复用 dsh-* 系列插件与工具，不重复实现 |

## 媒体
- ![dsh-crew 截图](https://pbs.twimg.com/media/HQDMxnDaMAAZvsw.png)

## 相关概念
- [项目仓库](https://github.com/ZSeven-W/dsh-crew) — 原始仓库
- [dsh-agent-teams](./tool-dsh-agent-teams.md) — dsh 自身的多代理编排（同一生态、不同实现）
- [pi-agent-core-book](./note-pi-agent-core-book.md) — 关于 Pi / agent 调度体系的阅读笔记，可作为子代理模式的概念背景
