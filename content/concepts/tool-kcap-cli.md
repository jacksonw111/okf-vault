---
type: Tool
title: "kcap-cli"
description: "kcap-cli 是给 AI 编码助手(Claude Code / Codex CLI 等)用的可观测性 CLI:捕获整个会话生命周期、对话记录、子代理树、工具调用细节、token 用量,通过实时仪表盘展示。"
resource: "https://github.com/kurrent-io/kcap-cli"
tags: [kcap-cli, observability, ai-coding, claude-code, codex, token]
timestamp: "2026-07-04T15:00:00Z"
---

# kcap-cli

## 它是什么

`kurrent-io/kcap-cli` 是给 AI 编码助手(Claude Code、Codex CLI 等)做的可观测性工具。它**捕获**整个 AI 编码会话的四类信息:

1. 整个会话生命周期(开始 / 中断 / 恢复 / 结束)
2. 完整对话记录(用户消息 ↔ Agent 回复)
3. **子代理树**(sub-agent tree)— 哪个任务被拆给了子 Agent,子 Agent 又调了哪些工具
4. **工具调用细节** + **token 消耗**

然后通过一个**实时仪表盘**展示出来 — 给 AI 编码会话一个 DevTools / APM 视角。

![配图](https://pbs.twimg.com/media/HMTOPVma8AAR59X.jpg)

项目链接：<https://github.com/kurrent-io/kcap-cli>

## 为什么用它 / 适合什么场景

- **AI 编码会话是黑盒**:以前你只知道「Agent 跑完了」,不知道这次花了多少 token、调用了什么工具、子 agent 是否在循环里打转。kcap 把这块从盲区变成可观测。
- **Code Review 上下文**:PR 时附上一段 kcap 输出,审稿人能看 Agent 的思考路径而非只看最终 diff。
- **成本审计**:跑完一段 Agent 工作,直接出 token 用量与按模型 / MCP 拆解的成本。

## 关键能力

| 能力 | 说明 |
|------|------|
| 会话捕获 | 全生命周期 hook 进 AI 编码 CLI |
| 对话记录 | 用户消息 / Agent 回复的可重放流 |
| 子代理树 | 多 Agent 协作时的父子 / 兄弟关系可视化 |
| 工具调用 | 每个工具调入参 + 出参 + 耗时 |
| Token 用量 | 按模型 / 阶段拆解统计 |
| 实时仪表盘 | Web 端 / 终端 TUI 实时刷新 |

## 适用命令

- Claude Code:使用 kcap 包裹的 `claude` 调用,所有会话自动捕获。
- Codex CLI:同样可包装。

## 相关概念

- [tokenscope](tool-tokenscope.md) — macOS / Windows 菜单栏实时显示 Claude CLI token 用量(更轻,只关注成本)
- [DataBuff](tool-databuff.md) — AI Native OpenTelemetry APM,与 kcap-cli 在 APM 方向同源但侧重点不同
- [DataBuff / OpenTelemetry](tool-databuff.md) — 传统 APM 链路追踪
- [kcap-cli 仓库](https://github.com/kurrent-io/kcap-cli) — 项目链接
