---
type: "Tool"
title: "DevSpace（自托管 MCP 编程工作台）"
description: "让 ChatGPT 通过 MCP 协议安全连接本地开发环境，实现读取、编辑、搜索和运行代码的能力 —— 相当于把 ChatGPT 变成 Codex CLI 那样的编程助手，但数据和操作都在自己机器上。"
resource: "https://github.com/Waishnav/devspace"
tags: "[mcp, chatgpt, dev-mode, self-hosted, coding-assistant]"
timestamp: "2026-06-21T00:00:00Z"
---

# DevSpace（自托管 MCP 编程工作台）

## 它是什么

由 `@QingQ77` 在 2026-06 推荐的 GitHub 仓库：**DevSpace** —— 一个自托管的 MCP 编程工作台。让 ChatGPT 通过 MCP 协议安全连接到你的**本地开发环境**，直接读 / 写 / 搜 / 运行代码。

## 核心定位

> 相当于把 ChatGPT 变成 Codex CLI 那样的编程助手，但**数据和操作都在自己机器上**。

不走云端中转、不上传源码。

## 关键能力

| 能力 | 说明 |
|------|------|
| 读取 | 浏览本地仓库文件 |
| 编辑 | 修改代码（带安全限制） |
| 搜索 | 跨文件 grep / 符号搜索 |
| 运行 | 跑安全命令（白名单内） |
| 协议 | MCP 标准，Claude Desktop / Cursor / Continue 等也能用 |

## 与 CodexPro 的差异

| 维度 | DevSpace | CodexPro |
|------|----------|----------|
| 部署 | 自托管 | 全局 npm + 自动隧道 |
| 接入 | 任意 MCP 客户端 | 专攻 ChatGPT Developer Mode |
| 数据流向 | 全部本地 | 本地 → 隧道 → ChatGPT |

## 适用场景

- 不想把代码上传到云端，但想用 ChatGPT 的编程能力 —— 自托管。
- 已经在用 MCP 客户端（Claude Desktop / Cursor / Continue）—— 直接 `add` 即可。
- 在企业内网开发，需要数据本地化。

## 媒体

![DevSpace 截图](https://pbs.twimg.com/media/HLJR8I7aIAAZ0AV.jpg)

## 相关概念

- [CodexPro](tool-codexpro.md) — 同样做 ChatGPT ↔ 本地仓库 MCP 桥，但走自动隧道路线
- [Codex Control Plane MCP](tool-codex-control-plane-mcp.md) — Codex Desktop 端的队列 MCP
- [ngrok / webernetes](tool-ngrok-webernetes.md) — 公网隧道集成（DevSpace 自托管场景的反面参考）