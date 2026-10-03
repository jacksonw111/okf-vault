---
type: "Tool"
title: "Jelly（dctanner/jelly：本地持久 AI Agent 容器）"
description: "把持久 AI Agent 装进自己的 Mac 或 Linux 机器：数量不限、按项目目录分组，网页登录和 sudo 审批都经用户之手，会话和浏览器配置存在本地 .jelly/ 目录。"
resource: "https://github.com/dctanner/jelly"
tags: "[ai-agent, local-first, multi-agent, ssh, open-source]"
timestamp: "2026-10-03T00:00:00Z"
---

# Jelly

## 它是什么

[Jelly](https://github.com/dctanner/jelly) 是 **dctanner** 出品的**本地持久 AI Agent 容器**——把 AI Agent 装进自己的 Mac 或 Linux 机器：

- **数量不限**：可同时跑多个 Agent
- **按项目目录分组**：每个 Agent 绑定一个项目
- **网页登录 + sudo 审批**：用户始终掌握入口与权限
- **本地存储**：会话与浏览器配置存在 `.jelly/` 目录

## 为什么用它 / 适合什么场景

- **数据不出本地**：适合金融 / 医疗 / 政企等敏感场景。
- **一个项目一个 Agent**：不让多个项目共享上下文，按目录分组。
- **审批权在用户手里**：sudo 弹窗给用户审核，避免 Agent 乱动系统。
- **典型场景**：个人 / 小团队的本地 AI 编程助手、长期维护的项目研究助理。

## 关键能力

| 能力 | 说明 |
|------|------|
| 平台 | macOS / Linux |
| Agent 数量 | 不限 |
| 分组方式 | 按项目目录 |
| 鉴权 | 网页登录 + sudo 审批 |
| 存储 | 本地 `.jelly/` 目录 |

## 参考链接

- 项目链接：<https://github.com/dctanner/jelly>

## 相关概念

- [Harness Engineering（Harness 工程）](./term-harness-engineering.md) — Jelly 是 Harness 工程方向的本地化实现
- [Comma](./tool-comma-agent.md) — 同类「多 Agent 跨设备持久」思路
