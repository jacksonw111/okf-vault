---
type: "Tool"
title: "PocketWatch（自由职业者自托管时间记录）"
description: "给自由职业者的自托管时间记录工具：点一下开始计时，再点一下导出 PDF 就能拿去开票；数据就存在本地两个 JSON 文件里，无账号、无订阅、无统计上报，连字体都内置在容器中，运行时不向外发任何请求。"
tags: "[time-tracking, freelancer, self-hosted, privacy, docker]"
timestamp: "2026-08-15T15:37:00Z"
resource: "https://github.com/winnicodes/pocketwatch"
---

# PocketWatch（自由职业者自托管时间记录）

## 它是什么

`winnicodes/pocketwatch` 是一个面向自由职业者 / 独立咨询师的自托管时间记录工具。核心流程是：

- 点击「开始」 → 进入计时状态。
- 工作完成 → 点击「结束」。
- 选一段时间 → 一键导出 PDF 拿去开票 / 报工时。

所有数据存在本地两个 JSON 文件里；**没有账号、没有订阅、没有统计上报**；连字体都内置在容器中，**运行时完全不发任何外部网络请求**。

> ![](https://pbs.twimg.com/media/HPrgpb9aQAAhsyW.jpg)

## 为什么用它 / 适合什么场景

- **隐私优先**：客户项目时长这种数据不想被 SaaS 收集。
- **离线可用**：网络断了也能继续计时。
- **直接出 PDF**：导出的 PDF 拿去给客户开票 / 内部报销。
- **零基础设施**：两个 JSON 文件 + 一个容器，部署只需 `docker run`。

## 关键能力

| 能力 | 说明 |
|------|------|
| 一键计时 | 开始 / 停止按钮，简单直接 |
| 本地 JSON 存储 | 数据透明、可备份、易迁移 |
| PDF 导出 | 选时间段 → 生成可直接开票的 PDF |
| 字体内置 | 容器内自带字体，PDF 在任何环境渲染一致 |
| 零网络请求 | 运行时完全离线 |
| 无账号 / 无订阅 | 自托管、无第三方依赖 |
| Docker 部署 | 一条命令拉起 |

## 与相关工具的差异

| 工具 | 思路 | 差异 |
|------|------|------|
| Toggl / Clockify | SaaS 时间记录 | 功能全，但数据在他方 |
| Time Tracker（自托管） | 多用户 Web 工具 | 重，需数据库 |
| **PocketWatch** | **单用户 + 隐私优先 + PDF 直出** | **极简、自托管、零网络** |

## 适用人群

- 自由职业者 / 独立咨询师。
- 对时间数据隐私敏感的开发者 / 设计师。
- 想用最小工具解决「计时 + 开票」的人。

## 参考链接

- [项目链接](https://github.com/winnicodes/pocketwatch)

## 相关概念

- [Single Server](tool-single-server.md) — 一台 Linux 服务器串 Cloudflare + Tailscale + Docker 一键部署
- [Plex TUI](tool-plex-tui.md) — 同类极简单工具示例