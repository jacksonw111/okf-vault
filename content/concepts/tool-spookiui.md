---
type: "Tool"
title: "SpookiUI（Ghostty 终端配置 TUI）"
description: "mattj85/SpookiUI，Ghostty 终端配置 TUI——改完自动写进配置文件、验证语法、触发 Ghostty 重载，不用离开终端界面就能改完即时生效。"
resource: "https://github.com/mattj85/SpookiUI"
tags: "[terminal, ghostty, tui, config, dotfiles]"
timestamp: "2026-07-23T05:48:00Z"
---

# SpookiUI（Ghostty 终端配置 TUI）

## 它是什么

[`mattj85/SpookiUI`](https://github.com/mattj85/SpookiUI) 是 **Ghostty 终端的配置 TUI**——解决「Ghostty 改了配置不会自动重载，每次都得手动触发」的痛点。

## 它做什么

| 步骤 | 说明 |
|------|------|
| 浏览配置项 | TUI 列出 Ghostty 全部配置 |
| 修改 | 直接在 TUI 里改 |
| 写回 | 自动写回 Ghostty 配置文件 |
| 验证 | 改完先验证语法，避免坏配置 |
| 触发重载 | 通过 socket 触发 Ghostty 重新加载 |

## 关键能力

| 能力 | 说明 |
|------|------|
| TUI | 不离开终端界面 |
| 全部配置项 | 浏览 + 修改 Ghostty 全部配置 |
| 验证 | 写回前校验语法 |
| 自动重载 | 触发 Ghostty 重载无需重启 |

## 为什么用它

- **省去重启**：改了立即生效，不退出终端
- **避免改坏**：写回前先验证语法，坏配置不会保存
- **不离开 TUI**：可视化编辑，比手动 vim 改 .conf 友好

## 适用场景

- 经常调 Ghostty 配色 / 字体 / 快捷键的用户
- 想用「配置面板」思路管理 dotfiles 的用户
- 给 Ghostty 新手降低上手门槛

## 媒体

![](https://pbs.twimg.com/media/HNzmgdxbcAAxQjt.jpg)

## 相关概念

- [Tork](./tool-tork.md) — 同类「终端里的工具箱」，但聚焦 BT / ISO 下载
- [Aether Android Agent](./tool-aether-android-agent.md) — 终端里跑 AI Agent
- [Loop.js](./tool-loop-js.md) — 给目标 + 标准驱动 Agent 干活

## 原始链接

- [项目仓库](https://github.com/mattj85/SpookiUI)