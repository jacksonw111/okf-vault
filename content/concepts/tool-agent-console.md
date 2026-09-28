---
type: "Tool"
title: "agent-console（LockedIn Labs：Claude Code / Codex 用量面板）"
description: "LockedIn Labs 出品：本地读取 Claude Code 和 Codex 的会话记录，把 token、模型和费用摊在一张自建面板上，多台机器汇到同一个 hub。可看 cache read / write / output / uncached input 拆分、每分钟 token 与每小时美元数、会话 lane、上下文增长与缓存断裂告警。"
resource: "https://github.com/LockedinLabs-AI/agent-console"
tags: "[claude-code, codex, observability, cost, dashboard, self-hosted, multi-machine]"
timestamp: "2026-09-28T23:50:00Z"
---

# agent-console（LockedIn Labs：Claude Code / Codex 用量面板）

## 它是什么

[agent-console](https://github.com/LockedinLabs-AI/agent-console) 是 **LockedIn Labs** 出品的**本地自建面板**：读取 **Claude Code** 与 **Codex** 的会话记录，把 **token / 模型 / 费用**摊在一张可观测面板上，多台机器汇到同一个 hub。

## 关键能力

- **token 拆分** — 看 cache read / cache write / output / uncached input 各自占比
- **多机器汇总** — 各机器 + 各模型分别花了多少钱
- **实时速率** — 当下每分钟吃掉多少 token，折合每小时几美元
- **会话 lane** — 每条会话一行泳道，可视化进度
- **告警** — 上下文增长 + 缓存断裂的告警
- **时间窗口** — 最近 1 小时到 30 天可选

## 为什么用它 / 适合什么场景

- 想**自托管**一个 Claude Code / Codex 用量仪表盘（数据不外传）。
- 团队 / 多机器场景，想把用量**集中汇总**。
- 想精细控制**AI 编码预算**——实时看速率、知道哪台机器 / 哪个模型在烧钱。
- 想看**缓存命中**情况——优化 prompt 工程。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | 本地自建面板 |
| 数据源 | Claude Code / Codex 会话记录 |
| 汇总 | 多机器 → 同一个 hub |
| 时间窗 | 1 小时 ~ 30 天 |
| 拆分 | cache read / write / output / uncached input |
| 告警 | 上下文增长 / 缓存断裂 |
| 出品 | LockedIn Labs |

## 媒体

- ![](https://pbs.twimg.com/media/HTRuku4bUAA2h9c.jpg)

## 相关概念

- [DSH Usage Stats](./tool-dsh-usage-stats.md) — DSH 的用量统计（agent-console 跨 Claude Code + Codex，更广覆盖）
- [Self-Hosted（自托管）](./term-self-hosted.md) — agent-console 的部署形态