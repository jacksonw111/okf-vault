---
type: Tool
title: "VibePod"
description: "统一命令行 vp，把 Claude / Gemini / Codex / Copilot 等编码 agent 跑在 Docker 或 Podman 容器中，开箱即用，YAML 可写自定义配置"
resource: "https://github.com/VibePod/vibepod-cli"
tags: [cli, coding-agent, docker, podman, yaml, sandbox]
timestamp: 2026-09-05T15:00:00Z
---

# VibePod

## 它是什么
`VibePod/vibepod-cli` 是一个**统一命令行工具 `vp`**，把 Claude / Gemini / Codex / Copilot 等编码 agent **跑在 Docker 或 Podman 容器中**，开箱即用，需要自定义时通过 YAML 写配置即可。

## 为什么用它 / 适合什么场景
- 想让编码 agent 在隔离、可复现的容器里跑，避免污染主机环境。
- 团队需要「同一个 agent 跑法」——容器化保证队友之间环境一致。
- 不想为每个 agent 各写一套启动脚本，希望一个 `vp` 命令统一调度。

## 关键能力
| 能力 | 说明 |
|------|------|
| 容器化执行 | 在 Docker / Podman 内启动 agent，主机干净 |
| 多 agent 支持 | Claude / Gemini / Codex / Copilot 等 |
| YAML 配置 | 想自定义就写 YAML，不用动代码 |
| 单一 CLI | `vp` 一条命令调度所有 agent |
| 开箱即用 | 默认配置已能直接跑 |

## 媒体
- ![](https://pbs.twimg.com/media/HRa6S5Za0AAq9c2.jpg)

## 相关概念
- [原始链接](https://github.com/VibePod/vibepod-cli)