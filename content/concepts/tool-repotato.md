---
type: Tool
title: "repotato（GitHub 日报 TUI 终端工具）"
description: "由 Claude 驱动的本地终端工具：在终端里浏览每日 GitHub 开源项目推荐 feed、点赞（直接给项目加星）、按 a 调用本地 Claude 帮你解释 / 安装 / 干净卸载。"
resource: "https://github.com/mnlt/repotato"
tags: [tui, github, claude, terminal, discovery]
timestamp: "2026-06-25T09:16:00Z"
---

# repotato（GitHub 日报 TUI 终端工具）

## 它是什么

一个**本地终端工具**，跑在 Claude 驱动下。它把 GitHub 仓库发现这件事**搬进 TUI**：

- **浏览日报**——左右键翻页，看每日精选 GitHub 项目 feed。
- **点赞**——`↑` 直接给该项目**点星**，计票实时拉 GitHub 数据。
- **Claude 解释 / 试用 / 卸载**——按 `a` 让本地 Claude 帮你解释这个项目是啥、装上去玩玩、或者干净地卸掉。

## 为什么用它

- 终端里就能发现 / 试用 GitHub 项目，**不需要打开浏览器**。
- 「点星」是真实操作，不是 toy——计票直接走 GitHub API。
- 让本地 Claude 帮你**真正安装 / 卸载**——避免「看到有趣项目 → 收藏 → 半年没动」。

## 关键操作

| 键 | 行为 |
|----|------|
| ← → | 翻页 |
| ↑ | 给当前项目加星（写 GitHub） |
| `a` | 调本地 Claude：解释 / 试用 / 卸载 |

## 关键能力

| 能力 | 说明 |
|------|------|
| TUI | 纯终端界面 |
| 日报 feed | 每日 GitHub 项目推荐 |
| 真实点赞 | 写 GitHub Star |
| 本地 Claude | 安装 / 解释 / 卸载 |

## 相关概念

- [Claude Code](./tool-claude-code.md) — repotato 后台的驱动模型
- [pi-task](./tool-pi-task-delegation.md) — 把「试用某个项目」作为 Pi 子任务也很自然
- [mattpocock/skills](./tool-mattpocock-skills.md) — repotato 的 Claude 解释路径可以挂载外部 SKILL
- [repotato 是本地 Claude 的「前端」](./term-agent-skills.md) — Skill 视角下的 repotato