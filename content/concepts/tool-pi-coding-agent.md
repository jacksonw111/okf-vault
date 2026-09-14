---
type: "Tool"
title: "Pi Coding Agent（earendil-works 的 pi 编码代理）"
description: "earendil-works 出品的终端原生 AI 编码代理：一个 agent 循环被做成可被代码直接调用的库，支持多家 LLM provider，强调扩展（Skills / Skills / 插件）与可复现的沙箱环境。"
resource: "https://github.com/earendil-works/pi"
tags: "[pi, coding-agent, terminal, earendil, agent-loop, provider]"
timestamp: "2026-09-14T22:30:00Z"
---

# Pi Coding Agent

## 它是什么

[earendil-works/pi](https://github.com/earendil-works/pi) 是 **earendil-works** 出品的**终端原生 AI 编码代理**。它不做成 IDE / 网页应用，而是一个**终端里跑的 agent 循环**：把「读上下文 → 调模型 → 执行工具 → 更新上下文」这套核心循环实现成一个可被代码直接调用的库。

最关键的定位是 **「一个 agent 循环被做成一个库」**——其它项目可以用 Pi 当基础，把 agent 循环嵌入到自己的桌面 / IDE / 多 agent 框架里。

## 核心特点

| 特点 | 说明 |
|------|------|
| 终端原生 | 装好就 `pi` 启动，零 IDE / 浏览器依赖 |
| agent 循环 = 库 | 不是 CLI 工具而是可嵌入的库 |
| 多 provider | 兼容 OpenAI / Anthropic / 其它 LLM 的统一接口 |
| 插件 / Skills 体系 | `pi install git:...` 一行装扩展（review / sandbox / 子任务委派…） |
| 桌面端扩展 | 社区版（pi-agent-desktop）、官方版（ThinkRail）都基于它 |
| 沙箱可叠加 | pi-env / SoL-Pi 等扩展把宿主隔离 / 省 token 旁挂进来 |

## 与同类对比

| 维度 | Pi Coding Agent | Claude Code |
|------|----------------|-------------|
| 形态 | 终端 CLI + 可嵌入库 | 终端 CLI |
| 模型 | 多 provider 自选 | Anthropic 优先 |
| 扩展 | `pi install git:...` 插件生态 | settings.json / skills |
| 桌面端 | 社区 / 官方都有 | 官方 IDE 集成 |

## Pi 生态扩展（节选）

- **pi-review** — 官方 review 插件
- **SoL-Pi**（NVIDIA）— 省 token 旁挂扩展
- **pi-env** — 沙箱运行环境
- **pi-desktop / pi-agent-desktop** — 桌面外壳
- **pi-claude-bridge** — 把 Claude Code 作为 provider 接入
- **pi-task-delegation** — 子任务委派

## 项目链接

- 仓库：<https://github.com/earendil-works/pi>

## 相关概念

- [Claude Code](./tool-claude-code.md) — 终端原生 AI 编码 agent；与 Pi 同类定位
- [Pi Review（earendil 团队）](./tool-pi-review.md) — Pi 的官方 review 插件
- [SoL-Pi（NVIDIA 给 Pi 的省 token 扩展）](./tool-sol-pi.md) — 在 Pi 之外加四个省 token 招数
- [pi-env（Pi 沙箱）](./tool-pi-env.md) — Pi 的隔离运行环境
- [Farcaster（多 coding agent 统一桌面）](./tool-farcaster-multi-agent-desktop.md) — 把 Pi / Codex / Claude Code 接入同一个桌面
