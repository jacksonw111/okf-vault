---
type: "Tool"
title: "Birth（iAmCorey/birth）"
description: "macOS 启动项管理器：把散落在 LaunchAgents / LaunchDaemons / 登录项里的项目集中到一个窗口，标出是谁装的、有没有在跑，一键停用或删掉。"
resource: "https://github.com/iAmCorey/birth"
tags: [macos, launchd, launchagents, login-items, system-tweak, cleanup]
timestamp: "2026-08-05T10:15:00Z"
---

# Birth（iAmCorey/birth）

## 它是什么

**Birth** 是 macOS 上的**启动项管理器**：把散落在 **LaunchAgents / LaunchDaemons / 登录项** 里的项目集中到一个窗口，标出：

- **是谁装的**（哪个应用 / 哪个进程注册的）
- **有没有在跑**（当前状态）
- **一键停用 / 删掉**

## 为什么用它 / 适合什么场景

- macOS 上装了太多软件后，**开机慢**、不知道是哪个在偷偷启动。
- 想**清理**可疑的 Launch Agent（很多广告软件 / 浏览器劫持会注册 LaunchAgent）。
- 想**审计**当前系统的开机自启项。

## 关键能力

| 能力 | 说明 |
|------|------|
| 集中视图 | LaunchAgents / LaunchDaemons / 登录项一窗尽览 |
| 来源标注 | 显示是哪个应用注册的 |
| 状态显示 | 当前是否在跑 |
| 一键停用 | 不用手动改 plist |
| 一键删除 | 清理无用项 |

## 参考链接

- [GitHub 仓库](https://github.com/iAmCorey/birth)

## 相关概念

- [MacTools](./tool-mac-tools.md) — 同属「macOS 菜单栏 / 系统清理工具集」，可对照
- [Worf](./tool-worf.md) — MIT 本地优先桌面应用，集成系统级工具