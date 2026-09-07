---
type: Tool
title: "omapager"
description: "Omarchy 桌面环境的通知守护进程插件（QML），按来源把通知收进卡片堆，悬停展开，每张卡片可直接操作。"
resource: "https://github.com/njpatel/omapager"
tags: "[omarchy, linux, notification, qml, tiling-wm]"
timestamp: "2026-09-07T13:12:00Z"
---

# omapager

## 它是什么
Omarchy 桌面环境的通知守护进程插件，用 QML 写成。"Pager" 原指分页器，这里借指"按应用分组、卡片堆叠"的通知中心。

## 工作方式
- 监听系统通知总线
- 按应用来源把通知收进卡片堆（同一应用多条通知堆在一起）
- 鼠标悬停展开卡片
- 每张卡片内可直接操作（回复、标记已读、关闭等）

## 关键能力
| 能力 | 说明 |
|------|------|
| 卡片堆分组 | 按应用聚合通知 |
| 悬停展开 | 鼠标悬停即展开 |
| 可直接操作 | 卡片内可回复 / 标记 / 关闭 |
| Omarchy 集成 | 与 Omarchy 桌面深度集成 |
| QML 实现 | Qt Quick 跨平台 |

## 参考
- 项目链接：<https://github.com/njpatel/omapager>

## 相关概念
- [Squawk](tool-squawk.md) — macOS 智能通知代理，针对 Claude Code 场景
- [Omarchy](https://omarchy.org/) — omapager 所在的桌面环境