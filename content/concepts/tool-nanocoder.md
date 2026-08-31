---
type: "Tool"
title: "Nanocoder（终端编码 Agent，社区集体维护）"
description: "Nano Collective 社区集体（非公司）维护的终端编码 Agent，npm 全局装完直接 `nanocoder` 即可启动，也支持 Homebrew 与 Nix Flakes。"
resource: "https://github.com/Nano-Collective/nanocoder"
tags: [ai, agent, coding-agent, terminal, community, npm, homebrew, nix]
timestamp: "2026-08-31T16:00:00Z"
---

# Nanocoder

## 它是什么

[Nanocoder](https://github.com/Nano-Collective/nanocoder) 是 **Nano Collective** 社区集体（非公司组织）维护的**终端编码 Agent**。不像主流商业 CLI 编码 Agent 背后是公司，Nanocoder 的开发由社区集体贡献。

安装路径多样：

- **npm**：`npm i -g nanocoder`，直接敲 `nanocoder` 运行
- **Homebrew**：`brew install ...`
- **Nix Flakes**：`nix profile install ...`

## 为什么用它 / 适合什么场景

- **想要社区治理的 CLI 编码 Agent**：不喜欢单一公司主导的工具链；
- **跨平台安装**：Nix 用户可直接用 flake 接入；
- **极简**：默认配置即可上手，无需复杂账号 / 计费。

## 关键能力

| 能力 | 说明 |
|------|------|
| 终端优先 | TUI 界面，跑在 shell 里 |
| 三种安装方式 | npm / Homebrew / Nix Flakes |
| 社区治理 | Nano Collective 集体维护 |
| MIT 协议 | 完全开源 |

## 相关概念

- [Claude Code](tool-claude-code.md) — 同类终端 AI 编码 agent，由商业公司 Anthropic 维护
- [DeepSeek Harness Core](tool-deepseek-harness-core.md) — 同类 agent harness 框架，可插拔智能体平台

## 参考链接

- 项目链接：<https://github.com/Nano-Collective/nanocoder>