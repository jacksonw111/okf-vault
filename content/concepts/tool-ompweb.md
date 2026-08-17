---
type: Tool
title: "ompweb"
description: "给 omp（oh-my-pi）编码代理加一个本地 Web 界面：直接在浏览器里浏览会话、实时聊天、改配置、管技能、预览项，免去命令行 + 编辑器来回切换"
resource: "https://github.com/kahme247/ompweb"
tags: [agent, web-ui, omp, oh-my-pi, coding-agent, local]
timestamp: 2026-08-17T16:00:00Z
---

# ompweb

## 它是什么

`kahme247/ompweb` 是给 `omp`（oh-my-pi）编码代理的**本地 Web 控制台**：在浏览器里就能完成「**浏览会话 / 实时聊天 / 改配置 / 管技能 / 预览项**」等原本需要切到终端或编辑器的操作。

相当于把 oh-my-pi 的 CLI 后端套了一个轻量 web 前端，本地起服务、浏览器访问。

## 为什么用它 / 适合什么场景

- 想给 oh-my-pi 一个**图形化界面**，而不是每次都进终端。
- 想**远程**操作 omp（同一网络内），比如另一台机器访问。
- 想在 Web 里管「技能」与「配置项」，而不是改文件。
- 想实时看 omp 的会话历史与运行状态。

## 关键能力

| 能力 | 说明 |
|------|------|
| 会话浏览 | 在 Web 里查看所有历史会话 |
| 实时聊天 | 浏览器直接与 omp 对话 |
| 配置管理 | GUI 修改 omp 配置 |
| 技能管理 | 启用 / 停用 / 改 omp skill |
| 项目预览 | 在 Web 里预览 omp 当前工作目录产物 |
| 本地起服 | 一次启动，浏览器即用 |

## 媒体

- ![](https://pbs.twimg.com/media/HPxVnVwaAAAFWN8.jpg)

## 原始链接

- [项目仓库](https://github.com/kahme247/ompweb)

## 相关概念

- [pi-desktop](./tool-pi-desktop.md) — Pi 的原生桌面 GUI 外壳；ompweb 是 omp 的 Web 外壳——同一个「给 CLI agent 加 GUI」的思路
- [peakcode](./tool-peakcode.md) — 同为多代理统一 GUI，但 peakcode 偏多会话统一管理而非单 agent 增强