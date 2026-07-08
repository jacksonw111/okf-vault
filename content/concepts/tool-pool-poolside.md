---
type: "Tool"
title: "pool（Poolside 出品的编码智能体）"
description: "pool 是 Poolside 做的编码智能体，既能在终端里用，也能当 ACP（Agent Communication Protocol）服务端或客户端，还能脚本化批量跑任务。支持四种运行方式：终端交互、ACP server、ACP client、`pool exec` 非交互执行。"
resource: "https://github.com/poolsideai/pool"
tags: "[ai-coding, agent, acp, cli, batch, poolside]"
timestamp: "2026-07-08T07:05:00Z"
---

# pool

## 它是什么

[pool](https://github.com/poolsideai/pool) 是 **Poolside 出品的编码智能体**，定位与 Claude Code / Codex CLI 类似，但更强调「多形态运行 + 脚本化」。

## 四种运行方式

| 模式 | 用途 |
|------|------|
| 终端交互 | 像 Claude Code 一样在终端里跟它聊 |
| ACP Server | 跑成 Agent Communication Protocol 服务端，供其它 agent / IDE 接入 |
| ACP Client | 主动去连别人的 ACP 服务端 |
| `pool exec` | 非交互式批量跑任务（CI / 自动化） |

## 关键能力

| 能力 | 说明 |
|------|------|
| 终端交互 | 直接跑命令、问问题、看 diff |
| ACP 服务端 | 暴露标准 ACP 接口给第三方 |
| ACP 客户端 | 可作为 ACP client 调用其它 agent |
| 非交互执行 | `pool exec` 脚本化跑任务 |
| 编码任务 | 自动改文件、跑测试、提 PR 等 |

## 媒体

![pool 终端预览](https://pbs.twimg.com/media/HMoU-yXbQAAWdMv.jpg)

## 参考链接

- [项目仓库](https://github.com/poolsideai/pool)

## 相关概念

- [Claude Code](./tool-claude-code.md) — 同为终端编码 agent，但走 Anthropic 模型路线
- [Codex X](./tool-codex-x.md) — 同为编码 agent 生态