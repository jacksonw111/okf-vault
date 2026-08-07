---
type: "Tool"
title: "Salience (macOS)"
description: "macOS 桌面应用：跟踪 git 分支把 PR、工单、CI、容器、部署等上下文自动连成一张图，按紧急程度生成 situations 提醒，免去开发者来回切十几个标签页拼凑「工作状态」。"
resource: "https://github.com/clegginabox/salience-macos"
tags: [macos, developer-tools, situational-awareness, git, ci, devops]
timestamp: "2026-08-07T04:37:00Z"
---

# Salience (macOS)

## 它是什么

Salience 是一款跑在 macOS 上的桌面应用，跟踪 git 分支并自动把 PR、工单、CI、容器、部署这些相关数据连成一张图，推到副屏上看。它刻意不做收件箱、不弹弹窗，而是由推导引擎把值得注意的变化聚合成「situations」，按紧急程度决定提醒强度。

## 为什么用它 / 适合什么场景

- 经常同时维护多个 git 分支 / 多个项目，需要随时知道「现在最该看哪个 PR」。
- 不想被一堆悬浮通知打断，但需要被动感知「上下文变了」。
- 想把开发状态放到副屏做「持续可见」的工作仪表盘，而不是打开浏览器挨个看 GitHub / GitLab / Jenkins。
- 喜欢图（graph）而不是列表（list）作为信息组织方式。

## 关键能力

| 能力 | 说明 |
|------|------|
| Git 分支锚定 | 跟随当前分支拉取相关 PR / Issue 关联 |
| 自动关系建模 | PR、工单、CI、容器、部署彼此自动连成图 |
| 副屏常驻 | 主视图适合放副屏做态势展示，不抢主屏焦点 |
| 无收件箱 / 无弹窗 | 不用 inbox 模式管理推送，避免噪声 |
| Situations 推导 | 由引擎判断「现在该关注什么」，按紧急度分级提醒 |
| macOS 原生体验 | 用系统通知中心，遵守 macOS 通知权限与勿扰设置 |

## 媒体

- ![Salience 工作流示意图](https://pbs.twimg.com/media/HPBPP_waEAAAvuW.jpg)

## 相关概念

- [GitButler](./tool-gitbutler.md) — 同样以 git 为中心的桌面协作 / 工作流工具，与本工具在「git 即工作状态」的设计哲学上同源
- [terminal-browser](./tool-terminal-browser.md) — 把终端 / 编辑 / Agent 收进同一界面，是另一种「消除标签页切换」的思路