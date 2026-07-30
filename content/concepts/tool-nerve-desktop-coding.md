---
type: Tool
title: "Nerve（本地优先桌面编码工具集）"
description: "Nerve 是开源的本地优先桌面编码工具集，刚好填在命令行工具和重型 IDE agent 之间的空白。它把消息流、工具调用、审批、计划、任务日志全部暴露在界面上，而不是藏在进度条后面。"
resource: "https://github.com/ThilinaTLM/nerve"
tags: [ai-coding, desktop, gui, agent, approval, local-first, task-log]
timestamp: "2026-07-30T13:04:00.000Z"
---

# Nerve

## 它是什么

**本地优先桌面编码工具集**——CLI agent 太黑盒（看不到中间过程），重型 IDE 太重（启动慢 / 占资源 / 订阅贵）。

Nerve 定位中间地带：桌面 GUI，但跑得起来、轻、本地优先。

把所有「AI 在干什么」暴露出来：

- **消息流**——对话历史可视化
- **工具调用**——每一步工具都看得见
- **审批**——危险操作必须用户确认
- **计划**——agent 提的计划可看可改
- **任务日志**——所有动作留痕

![截图](https://pbs.twimg.com/media/HOWa17AaoAAOXzT.jpg)

## 关键能力

| 能力 | 说明 |
|------|------|
| 消息流 | 透明对话历史 |
| 工具调用可视化 | 每个工具的输入 / 输出 |
| 审批机制 | 关键操作需确认 |
| 计划视图 | agent 计划可编辑 |
| 任务日志 | 全程审计 |
| 本地优先 | 数据不出本机 |
| 桌面 GUI | 不开浏览器 |

## 与同类对比

| 工具 | 形态 | Nerve 优势 |
|------|------|-----------|
| Claude Code CLI | 终端 | 暴露 GUI + 审批 |
| Cursor / Windsurf | IDE | 更轻、本地优先 |
| Pi / OpenCode | 终端 + 轻 GUI | 更完整的工具可视化 |

## 适合谁

- 想要 GUI 透明度但不想订阅 IDE 的人
- 想给 AI 编码加审批 / 审计的团队
- 觉得 CLI 太黑盒但 IDE 太重的独立开发者

## 原始链接

- [项目仓库](https://github.com/ThilinaTLM/nerve)
- [推文剪藏](https://x.com/QingQ77/status/2082814466643972204)

## 相关概念

- [Aura-IDE](./tool-aura-ide.md) — Planner/Worker 双智能体本地编码工作台，写文件前先显示 diff 审批
- [PeakCode](./tool-peakcode.md) — 多代理会话统一 GUI + Git 工作流整合
- [Comando](./tool-comando.md) — 本地优先多智能体协作代码编辑器（Electron + Rust）