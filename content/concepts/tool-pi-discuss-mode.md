---
type: "Tool"
title: "pi-discuss-mode（Pi Coding Agent 只读讨论模式扩展）"
description: "给 Pi Coding Agent 加的扩展：开启后所有编辑 / 写入工具全禁用，bash 只能跑 cat / grep / ls 等安全命令，可以在不改一行代码的前提下看代码、聊架构、审 PR，灵感来自 Claude Code 的 plan mode。"
resource: "https://github.com/zwrong/pi-discuss-mode"
tags: "[pi, coding-agent, read-only, plan-mode, extension]"
timestamp: "2026-07-20T20:20:00Z"
---

# pi-discuss-mode（Pi Coding Agent 只读讨论模式扩展）

## 它是什么

[zwrong/pi-discuss-mode](https://github.com/zwrong/pi-discuss-mode) 是 [Pi Coding Agent](./tool-pi-env.md) 的一个**只读讨论模式扩展**。一旦开启：

- 写入 / 编辑类工具全部禁用
- Bash 只能跑 `cat`、`grep`、`ls` 之类的安全只读命令
- 用户可以安心跟 agent 聊架构、审 PR、看代码，agent 不会偷偷改文件

灵感来自 Claude Code 的 **plan mode**。

## 关键能力

| 能力 | 说明 |
|------|------|
| 写工具零授权 | 任何修改类操作都被拦截 |
| 受限 bash | 只允许只读命令 |
| 适合场景 | 聊架构、审 PR、看代码、复盘历史改动 |
| 切换方便 | 一条命令开 / 关，不影响其它会话 |

![pi-discuss-mode 截图](https://pbs.twimg.com/media/HNgOLynaUAAwBMI.jpg)

## 相关概念

- [Pi Coding Agent](./tool-pi-env.md) — 宿主 Agent
- [Pi Hive](./tool-pi-hive.md) — Pi 的层次化多智能体扩展
- [Pi Smart Web Search](./tool-pi-smart-web-search.md) — Pi 的多查询批量检索扩展

## 参考链接

- 项目链接: <https://github.com/zwrong/pi-discuss-mode>
