---
type: Tool
title: "clawd-conduit"
description: "Claude Code 卡在权限确认时不至于傻等——卡片直接弹到桌面，Cmd+Shift+Y 批 / Cmd+Shift+N 拒，同时把 15 个 hook 事件都变成宠物状态。"
resource: "https://github.com/ssssssanjiu/clawd-conduit"
tags: "[claude-code, hooks, desktop, ui, open-source]"
timestamp: "2026-09-22T00:00:00Z"
---

# clawd-conduit

## 它是什么
一个**Claude Code 桌面权限确认桥**：当 Claude Code 卡在权限确认界面等用户回复时：

- 权限确认卡片直接弹到桌面（不盯着终端）
- 快捷键：`Cmd+Shift+Y` 批 / `Cmd+Shift+N` 拒
- 同时把 15 个 Claude Code hook 事件映射成「宠物状态」——把干巴巴的事件流变成可视化反馈

## 为什么用它 / 适合什么场景
- 经常让 Claude Code 跑长任务，又不想一直在终端面前等权限确认。
- 想用全局快捷键秒批 / 秒拒权限请求。
- 想把 hook 事件流变成宠物状态/动画反馈，把 agent 跑的过程「可视化」。

## 关键能力
| 能力 | 说明 |
|------|------|
| 桌面卡片 | 权限确认弹出到桌面 |
| 快捷键 | Cmd+Shift+Y 批 / Cmd+Shift+N 拒 |
| Hook 覆盖 | 15 个 Claude Code hook 事件 |
| 宠物状态 | 把 hook 事件映射成宠物状态 |

## 相关概念
- [Claude Code](tool-claude-code.md) — 该工具的宿主
- [Agent Skills（代理技能包）](term-agent-skills.md) — Claude Code 的 hook / skill 机制

## 项目链接
- 项目主页：<https://github.com/ssssssanjiu/clawd-conduit>

## 媒体
- 截图：<https://pbs.twimg.com/media/HSyLTUyaQAAlhMl.jpg>
