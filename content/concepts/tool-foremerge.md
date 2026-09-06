---
type: Tool
title: "foremerge"
description: "给并行的编码 Agent 共用一块白板：开工前每个 Agent 先写下要动哪块代码、想怎么改，状态存在项目 .git 目录下的小数据库，避免合并时才发现目标打架。"
resource: "https://github.com/naw103/foremerge"
tags: [multi-agent, coordination, git, white-board, pre-merge]
timestamp: "2026-09-06T00:00:00Z"
---

# foremerge

## 它是什么

[foremerge](https://github.com/naw103/foremerge) 是给**并行编码 Agent** 用的共享白板：开工前每个 Agent 先把自己的计划——要动哪块代码、想怎么改——登记到仓库 `.git/` 目录下的小型数据库里，**同一台机器上的 Claude、Codex、Cursor 等多个 Agent 互相可见**。

定位：

- **预防式协调**：在 Agent 真正动手之前暴露冲突，而不是合并代码时才发现白干。
- **数据留在仓库**：白板数据放在 `.git/`，不引入额外服务。

## 为什么用它 / 适合什么场景

- 多个编码 Agent 并行干活，常出现「A 改的接口被 B 重构了」「两个人同时改同一文件」的隐式冲突。
- 想让 Agent 之间互相知道对方在做什么，预先避免重写而不是事后合并。
- 不想为协调再多跑一套外部数据库 / 服务器。

## 关键能力

| 能力 | 说明 |
|------|------|
| 共享白板 | 所有 Agent 写入并读取同一份计划库 |
| 计划可见 | 开工前声明「动哪块代码、怎么改」，别人能看到 |
| 数据位置 | 存在项目 `.git/` 目录里，与仓库同生命周期 |
| 跨 Agent | 同机 Claude / Codex / Cursor 等都可读写 |

## 相关概念

- [Vicoa](./tool-vicoa.md) — 让多 Agent 各占独立 worktree/分支的并行策略（与 foremerge「共享白板」互为补充）
- [vibepod](./tool-vibepod.md) — 把多 Agent 收进统一工作区的容器化方案
- [Claude Code](./tool-claude-code.md) — foremerge 支持的典型 Agent

## 项目链接

- 项目主页：<https://github.com/naw103/foremerge>
