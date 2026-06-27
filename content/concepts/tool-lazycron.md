---
type: "Tool"
title: "lazycron（Linux cron TUI 管理器）"
description: "Go 写的终端 TUI 工具，让你在 Linux 上方便地管理 cron 任务：列表 / 增删改 / 开关（禁用时注释掉不删除）/ 计划校验 / 详情展开；vim 风格快捷键（j/k / g/G / :N 跳行）；无需 root，无需配置文件。"
tags: "[cli, tui, cron, linux, vim]"
timestamp: "2026-06-27T07:57:00.000Z"
resource: "https://github.com/Domenez-dev/lazycron"
---

# lazycron（Linux cron TUI 管理器）

## 它是什么

[`lazycron`](https://github.com/Domenez-dev/lazycron) 是一个**用 Go 写的终端 TUI 工具**，让你在 Linux 上**方便地管理 cron 定时任务**。它能列出任务、新增 / 删除 / 修改、开关任务（**禁用时注释掉而不删除**），还带计划校验和详情展开。操作风格贴近 vim：j/k 上下翻、g/G 到头尾、:N 跳到指定行。**不需要 root 权限也不用配置文件**，直接读写当前用户的 crontab。

![lazycron 界面](https://pbs.twimg.com/media/HLuKu4YbEAACln9.jpg)

## 关键能力

| 能力 | 说明 |
|------|------|
| 列表浏览 | TUI 列表展示所有 cron 任务 |
| 增删改 | 在 TUI 内完成 CRUD |
| 开关任务 | 禁用时注释掉，不删除原配置 |
| 计划校验 | 检查 cron 表达式是否合法 |
| 详情展开 | 展开查看任务完整定义 |
| vim 风格 | j/k / g/G / :N 等快捷键 |
| 零配置 | 无需 root、无需配置文件 |
| 直读 crontab | 直接操作当前用户的 crontab |

## 适用场景

- Linux 用户嫌 `crontab -e` 不直观
- 经常需要临时启用 / 禁用某些定时任务，又怕删错配置
- 习惯 vim 快捷键的开发者 / 运维
- 在共享服务器上没 root 但需要管理个人 cron

## 参考链接

- [项目链接](https://github.com/Domenez-dev/lazycron)

## 相关概念

- [Plaza](tool-plaza.md) — 同样是 Go 写的 TUI 工具，面向包管理
- [tabiew](tool-tabiew.md) — 同样是 TUI 工具，面向表格数据查看