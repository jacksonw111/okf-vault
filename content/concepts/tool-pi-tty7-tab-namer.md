---
type: "Tool"
title: "pi-tty7-tab-namer（Pi 终端会话自动命名器）"
description: "pi-tty7-tab-namer 会在 tty7 中调用 Pi 当前会话所用的模型，为新建 / 恢复的会话生成简短名称，并双向同步到终端 Tab 和 /resume 列表。"
resource: "https://github.com/ifyour/pi-tty7-tab-namer"
tags: "[pi-coding-agent, terminal, tab-naming, automation, session-management, open-source]"
timestamp: "2026-09-25T15:55:00Z"
---

# pi-tty7-tab-namer（Pi 终端会话自动命名器）

## 它是什么

[pi-tty7-tab-namer](https://github.com/ifyour/pi-tty7-tab-namer) 是给 [Pi 编码代理](./tool-pi-coding-agent.md) 写的**终端会话自动命名器**：

- 在 **`tty7`**（Pi 默认主交互终端）中调用 **Pi 当前会话所用的模型**
- 给**新建**或**恢复**的会话生成一个**简短名称**
- 名称会**双向同步**到：
  - 终端 Tab 标题
  - `/resume` 列表里的可选项

## 为什么用它 / 适合什么场景

- 同时开多个 Pi 会话（任务 A / 任务 B / 探索 X），手动给 Tab 改名字既累又忘。
- 想让 `/resume` 列表里的会话**看一眼就知道是干嘛的**，而不是一串「session-12 / session-13」。
- 不想引入额外 LLM——直接**复用当前会话模型**，命名调用几乎零额外开销。
- 工作流重度依赖 Pi——Tab 命名的一致性会直接影响上下文切换速度。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | Pi 的终端扩展 |
| 触发时机 | 新建会话 / 恢复会话 |
| 模型来源 | 复用当前会话正在用的模型 |
| 同步范围 | 终端 Tab 标题 + `/resume` 列表 |
| 名称风格 | 简短（一两词） |
| 性能 | 几乎零开销（同进程模型调用） |

## 媒体

![](https://pbs.twimg.com/media/HTB5_HJagAAkw7X.jpg)

## 相关概念

- [Pi Coding Agent](./tool-pi-coding-agent.md) — 本项目所属的编码代理
- [pi-task](./tool-pi-task-delegation.md) — Pi 的子任务委派扩展
