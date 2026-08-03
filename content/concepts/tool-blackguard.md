---
type: Tool
title: "Blackguard"
description: "把 Zach Gage 和 Kurt Bieg 的 Scoundrel 桌面扑克牌 roguelike 搬进终端的 Rust + ratatui 实现，牌堆就是地牢：黑桃梅花是怪兽，方块是武器，杀掉一只就变钝一档，红心回血，每间房只有第一瓶药水管用。"
resource: "https://github.com/ElnurBDa/blackguard"
tags: [rust, ratatui, tui, game, roguelike, card]
timestamp: "2026-08-03T05:13:00Z"
---

# Blackguard

## 它是什么
Blackguard（`ElnurBDa/blackguard`）把 Zach Gage 和 Kurt Bieg 的 Scoundrel 桌面扑克牌 roguelike 游戏搬进了终端。**牌堆就是地牢**：黑桃梅花是怪兽，方块是武器，杀掉一只就变钝一档，红心回血，每间房只有第一瓶药水管用。

Rust + ratatui 实现，全键盘操作。

![Blackguard 截图](https://pbs.twimg.com/media/HOpHnOjbQAAtD5H.jpg)

## 为什么用它 / 适合什么场景
- **移植经典牌游**：把单机桌游「Scoundrel」复刻为纯终端游戏。
- **极简资源占用**：Rust + ratatui，运行几乎不吃资源。
- **TUI 教学样例**：ratatui 实现状态机 + 卡片交互的范本。

## 关键能力

| 能力 | 说明 |
|------|------|
| Rust + ratatui | 纯 TUI，无 GUI 依赖 |
| Scoundrel 规则 | 完整复刻牌组当作地牢的桌面 roguelike |
| 键盘操作 | 全键鼠脱离，终端直接玩 |
| 状态机清晰 | 房间 / 战斗 / 武器损耗 / 药剂规则简化 |

## 项目链接
- <https://github.com/ElnurBDa/blackguard>

## 相关概念
- [archwiki-tui](./tool-archwiki-tui.md) — Go 写的终端 Arch Wiki 浏览器，全键盘查阅
- [hop (SSH TUI)](./tool-hop-ssh-tui.md) — Go 写的终端 SSH 多服务器切换 TUI
- [docksurf](./tool-docksurf.md) — 终端里用键盘操作 Docker 的 TUI
