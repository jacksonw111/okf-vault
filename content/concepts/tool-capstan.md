---
type: Tool
title: "Capstan（C + Lua 的轻量可扩展终端编码 Agent）"
description: "主流终端编码 agent 多为 Node/Python 实现，启动慢、内存占用高；Capstan 用 C 加嵌入式 Lua 做出一个轻量可扩展的替代方案。"
resource: "https://github.com/theStrangeAdventurer/capstan"
tags: [c, lua, coding-agent, terminal, lightweight, embeddable]
timestamp: "2026-08-27T09:48:00Z"
---

# Capstan

## 它是什么
[theStrangeAdventurer/capstan](https://github.com/theStrangeAdventurer/capstan) 是一个**用 C + 嵌入式 Lua 实现的终端编码 Agent**。出发点很明确：

- 主流终端编码 agent（Codex CLI / Claude Code 等）多为 **Node.js 或 Python** 实现，**启动慢、内存占用高**；
- Capstan 用 **C 写核心 + 嵌入式 Lua 做扩展**，给出一个轻量、可扩展的替代方案。

## 为什么用它 / 适合什么场景
- 嫌 Node / Python 实现的 coding agent 启动慢、占内存；
- 想用一个嵌入式 Lua 做扩展的 coding agent——写业务工具脚本不必再起一门语言运行时；
- 喜欢 C / Lua 那种"几 MB 二进制就能跑"的极简范式。

## 关键能力
| 能力 | 说明 |
|------|------|
| 实现语言 | C（核心）+ 嵌入式 Lua（扩展） |
| 轻量 | 比 Node / Python 实现启动快、内存占用低 |
| 终端形态 | 命令行 agent |
| 可扩展 | Lua 写工具脚本 |
| 替代方案 | 对标主流终端编码 agent |
| 开源 | 仓库开源 |

## 相关概念
- [Claude Code](tool-claude-code.md) — 终端原生 AI 编码 agent（Node 实现）；Capstan 是其"轻量替代"路线
- [Pi Agent 编码笔记](note-pi-agent-core-book.md) — Pi 这条 JetBrains 路线编码 agent 的内核笔记；与 Capstan 都是"终端 agent"的不同实现路径

## 参考链接
- 项目链接：<https://github.com/theStrangeAdventurer/capstan>
