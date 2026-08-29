---
type: Tool
title: "Lody（ACP 驱动的团队多 Agent 共享工作空间）"
description: "通过 ACP（Agent Communication Protocol）把任意机器上的 Claude Code / Codex / Kimi / OpenCode 等编码 Agent 接入同一个共享工作空间，团队成员从桌面 / 手机 / 网页 / CLI 打开同一段对话、调度任务、审阅代码改动。"
resource: "https://github.com/LodyAI/Lody"
tags: [multi-agent, team-collaboration, acp, claude-code, codex, opencode, kimi, cross-platform]
timestamp: "2026-08-28T00:00:00Z"
---

# Lody

## 它是什么
[LodyAI/Lody](https://github.com/LodyAI/Lody) 是**让团队里所有机器上跑的编码 Agent 协作起来的共享工作空间**。痛点：现在团队里有人用 Claude Code、有人用 Codex、有人用 Kimi、有人用 OpenCode，每个 Agent 跑在各自的机器上、对话进度散落各处、改动互不可见。

Lody 通过 **ACP（Agent Communication Protocol）** 把这些 Agent 全部接进同一片空间：

- **任意机器上的任意 Agent** 都能注册到 Lody；
- 团队成员从**桌面 / 手机 / 网页 / CLI** 任何一种客户端打开同一段对话；
- 任务调度、代码改动审阅都集中在共享工作区里。

## 为什么用它 / 适合什么场景
- 团队里有 3+ 人各自跑不同编码 Agent（Claude Code / Codex / OpenCode / Kimi），希望**对话历史和代码改动统一可见**；
- 远程协作者不想装全套开发环境也能在 Lody 网页 / 手机里**旁观或介入** Agent 任务；
- 需要**审计 / 复盘**整个团队一段时间的 Agent 行为；
- 想从 CLI 端用一行命令接入 Lody，无需打开 GUI 也能被同事看到。

## 关键能力
| 能力 | 说明 |
|------|------|
| 多 Agent 接入 | Claude Code / Codex / Kimi / OpenCode 等本地编码 Agent |
| 协议层 | ACP（Agent Communication Protocol）统一通信 |
| 跨端客户端 | 桌面 / 手机 / 网页 / CLI 同源访问 |
| 任务调度 | 在共享工作空间里派发、跟进、收回任务 |
| 改动审阅 | 代码改动集中展示，团队成员可即时反馈 |
| 跨机器 | 任意成员任意机器上的 Agent 都能注册 |

## 相关概念
- [Strado](tool-strado.md) — 单机多 AI 编码代理工作台（独立 worktree + 浏览器 / IDE 验证）；Lody 则是**跨机器跨工具**的协作层
- [Multi-AI-Coding-Config-Panel](tool-multi-ai-coding-config-panel.md) — 多代理配置面板；Lody 是「配置 + 协作 + 审阅」一体化
- [FyAgent](tool-fyagent.md) — 多 AI 编码代理的配置同步工具；Lody 在配置之上又叠了一层**共享对话 + 改动审阅**

## 参考链接
- 项目链接：<https://github.com/LodyAI/Lody>
- 原始推文：<https://x.com/QingQ77/status/2093184044125053355>
- 媒体：<https://pbs.twimg.com/media/HQskk85boAAxRQN.jpg>
