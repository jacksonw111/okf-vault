---
type: "Tool"
title: "AgentVerse-OS（一键个人云操作系统）"
description: "agentverse-os/AgentVerse-OS：在 Ubuntu 服务器上一条命令装好个人云操作系统，浏览器里跑窗口桌面、隔离开发工作区和 944 个自托管应用，对外只走 Tailscale 不暴露公网。"
resource: "https://github.com/agentverse-os/AgentVerse-OS"
tags: "[self-hosted, homelab, tailscale, runtipi, cloud-os]"
timestamp: "2026-09-15T04:45:00Z"
---

# AgentVerse-OS（一键个人云操作系统）

## 它是什么

[AgentVerse-OS](https://github.com/agentverse-os/AgentVerse-OS) 把一台 Ubuntu 服务器在**一条命令**内改造成「**个人云操作系统**」：通过浏览器就能跑窗口化桌面、隔离的开发工作区，并预装 **944 个自托管应用**。

## 三个核心组件

1. **浏览器里的窗口桌面**：远程桌面在浏览器里启动，无需装客户端。
2. **隔离的开发工作区**：每个工作区独立环境，避免「全栈互相污染」。
3. **944 个自托管应用**：开箱即用的应用目录，覆盖笔记、文件同步、AI、监控、媒体等常见自托管场景。

## 为什么用它

- 「**对外只走 Tailscale**」是默认安全模型——不暴露公网 IP，攻击面只剩 Tailscale 网络。
- 「**一条命令装好**」把自托管最大的劝退点（满网找 compose）抹掉。
- 应用目录的 944 个看着唬人，实质是把 Runtipi 等成熟自托管目录拼一锅，胜在「**装起来省的是找 compose 的时间**」。

## 关键能力

| 能力 | 说明 |
|------|------|
| 一键部署 | Ubuntu 服务器一条命令启动整套栈 |
| 浏览器桌面 | 无客户端远程桌面 |
| 隔离工作区 | 多套环境互不污染 |
| 应用目录 | 944 个预装应用，开箱即用 |
| Tailscale 默认 | 对外仅 Tailscale 私网，不暴露公网 |
| Runtipi 兼容 | 应用目录以 Runtipi 等成熟方案为基础 |

## 媒体

![](https://pbs.twimg.com/media/HSOK_CNaoAANufI.jpg)

## 项目链接

- 仓库：<https://github.com/agentverse-os/AgentVerse-OS>