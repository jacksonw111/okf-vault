---
type: Tool
title: "Tasks–To Do Sync（Google Tasks ↔ Microsoft To Do 双向同步桥）"
description: "跑在私人 Google Apps Script 项目里的双向同步工具，把 Google Tasks 与 Microsoft To Do 两个生态的待办事项统一起来，每 10 分钟一轮同步创建 / 编辑 / 完成 / 重开 / 备注 / 截止日期，列表与任务以 ID 映射，重命名不打断既有同步。"
resource: "https://github.com/simonchai-tw/tasks-todo-sync"
tags: [productivity, sync, google-tasks, microsoft-to-do, apps-script, bidirectional, tasks]
timestamp: "2026-08-28T00:00:00Z"
---

# Tasks–To Do Sync

## 它是什么
[simonchai-tw/tasks-todo-sync](https://github.com/simonchai-tw/tasks-todo-sync) 是**同时使用 Google Tasks 和 Microsoft To Do 的用户的双向同步桥**。

痛点：很多人一边用 Google Calendar 嵌着的 Google Tasks，一边又用 Outlook / Microsoft 365 里的 To Do，**两边都要手动维护同一份任务清单**——很容易漏、改、重建。

Tasks–To Do Sync 跑在**用户自己的 Google Apps Script** 里（私域，不经过第三方服务器），每 10 分钟跑一轮同步：

- **任务创建 / 编辑 / 完成 / 重开**全部双向同步；
- **备注、截止日期**也跟着走；
- **配对关系基于列表与任务 ID 映射**，重命名列表不会打断既有同步关系。

## 为什么用它 / 适合什么场景
- 同时用 Google Tasks（手机日历 / Gmail 圈圈）和 Microsoft To Do（Outlook / Win11）的人；
- 想**自己控制同步**——脚本跑在自家 Google 账户，任务数据不经过第三方服务；
- 需要稳定的双向同步（不仅单向推送）——一边勾掉，另一边也立刻完成；
- 重命名待办列表时不希望同步链路断掉。

## 关键能力
| 能力 | 说明 |
|------|------|
| 双向同步 | Google Tasks ↔ Microsoft To Do |
| 同步字段 | 创建 / 编辑 / 完成 / 重开 / 备注 / 截止日期 |
| 同步频率 | 每 10 分钟一轮 |
| 部署方式 | 私人 Google Apps Script 项目（无第三方中转） |
| 标识策略 | 列表与任务以 ID 映射，重命名不打断 |
| 隐私 | 任务数据全在用户自己的 Google 账户和 Microsoft 账户之间往返 |

## 相关概念
- [Open Sheet](tool-open-sheet.md) — 同样面向「跨生态引用统一」的思路，但作用于电子表格
- [iCloud MD](tool-icloud-md.md) — Apple Notes ↔ 本地 Markdown 双向同步；Tasks–To Do Sync 是**待办事项领域**的同类思想

## 参考链接
- 项目链接：<https://github.com/simonchai-tw/tasks-todo-sync>
- 原始推文：<https://x.com/QingQ77/status/2093268098501796055>
- 媒体：<https://pbs.twimg.com/media/HQsn2-BaAAA3XJ7.jpg>
