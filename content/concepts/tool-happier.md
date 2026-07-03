---
type: Tool
title: "happier"
description: "开源、端到端加密的跨设备 AI 编程代理客户端；电脑跑编码会话、手机接着干；支持 Claude Code / Codex / OpenCode / Gemini 等多种后端；三层架构：relay 服务器（可自托管）+ 守护进程 + iOS / Android / Web / Desktop 客户端。"
resource: "https://github.com/happier-dev/happier"
tags: "[ai-coding-agent, cross-device, e2ee, mobile-client, claude-code, codex, relay]"
timestamp: "2026-07-03T12:31:00Z"
---

# happier

## 它是什么
**开源、端到端加密的跨设备 AI 编程代理客户端**——电脑端跑的 Claude Code / Codex 编码会话，手机端可以无缝接着干。

三层架构：

| 层 | 说明 |
|----|------|
| **Relay 服务器** | 中转设备间消息（可自托管） |
| **守护进程** | 跑在电脑端，管会话状态与 LLM 调用 |
| **UI 客户端** | iOS / Android / Web / Desktop 多端 |

通过 E2EE 保护，会话、提示、代码内容对 Relay 服务器不可见。支持的后端包括 **Claude Code**、**Codex**、**OpenCode**、**Gemini** 等多种编码代理。

由 happier-dev 团队开发。

## 为什么用它 / 适合什么场景
- 上班通勤路上想在手机上看看 Claude Code 跑到哪了 / 改个方向。
- 不想每次换设备都要重新「描述上下文」——希望会话无缝跨设备。
- 重视隐私——不想让 AI 编码对话内容被中转服务器看见（E2EE）。
- 用多种编码代理（Claude Code / Codex / OpenCode / Gemini），想统一一个跨端客户端管全部。
- 团队 / 公司要私有化部署——Relay 服务器可自托管在自家基础设施。

## 关键能力
| 能力 | 说明 |
|------|------|
| 加密 | 端到端加密（E2EE），Relay 服务器不可见明文 |
| 跨设备 | 电脑 ↔ 手机无缝接力 |
| 多端客户端 | iOS / Android / Web / Desktop |
| 后端兼容 | Claude Code / Codex / OpenCode / Gemini 等 |
| 远程控制 | 手机端可控制电脑端会话 |
| 协作 | 支持多人协作 |
| Relay 服务器 | 可自托管 |
| 守护进程 | 跑在电脑端管会话状态与 LLM 调用 |
| 形态 | 开源 AI 编码代理跨端客户端 |

## 相关概念
- [Mux（Claude Code tmux 插件）](tool-mux-claude-tmux.md) — 本机多会话管理；happier 是跨设备
- [shuangzi-xubei（双子续杯）](tool-shuangzi-xubei.md) — iPhone 锁屏小组件看额度；happier 是完整跨端编码会话控制
- [CodexPro](tool-codexpro.md) — ChatGPT Web ↔ 本地仓库 MCP 桥；happier 是多端 ↔ 本地守护进程

## 项目链接
- 项目主页：<https://github.com/happier-dev/happier>

## 媒体
![](https://pbs.twimg.com/media/HMRQ1ITbcAAZnRC.jpg)