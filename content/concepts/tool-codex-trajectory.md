---
type: Tool
title: "codex-trajectory"
description: "把本地 Codex 编码会话日志解析成结构化事件账本 + 交互时间线的只读插件：轮次、模型步数、推理摘要、助手消息、工具耗时、子代理、压缩、token 用量、失败记录全可见，原日志不被改动"
resource: "https://github.com/icesixgod/codex-trajectory"
tags: [codex, agent, observability, trajectory, ledger, timeline, privacy]
timestamp: 2026-08-17T16:00:00Z
---

# codex-trajectory

## 它是什么

`icesixgod/codex-trajectory` 是一个**只读**的本地 Codex 任务日志分析插件：把 Codex 在本机写入的原始任务日志**解析**成结构化事件账本（event ledger）和交互时间线（interaction timeline），供事后审阅、复盘与回溯使用——**原日志保持不变**。

典型用途：写完代码发现中间某一步走了错路 / 想统计 token / 想看每个工具调用的耗时 / 想把会话生成可视化回顾。

## 为什么用它 / 适合什么场景

- 想要一个**事后审计层**：Codex 默认日志只读不便分析，需要事件化视图。
- 想看每个回合的「推理摘要 + 助手消息 + 工具调用」完整链条。
- 想统计子代理触发次数、压缩事件、模型步数与失败记录。
- 不想让日志上云——**全本地、隐私友好**。
- 想做 CodeX 会话可视化（仪表盘 / 时间轴 / 统计图）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 事件账本 | 把原始日志拆解为「轮次 / 模型步 / 推理摘要 / 助手消息 / 工具耗时 / 子代理 / 压缩 / token / 失败」等字段 |
| 交互时间线 | 按时间顺序渲染会话全过程，类似 IDE debug 时间轴 |
| 只读 | 永远不修改原 Codex 日志，可放心跑在生产目录 |
| 隐私友好 | 全本地运行，不上传任何遥测 |
| 子代理可见 | 区分主会话与子代理调用关系 |
| 失败记录 | 把每次失败 / 中断 / 重试单独提取 |

## 媒体

- ![](https://pbs.twimg.com/media/HPzMlE5bsAAP2fR.jpg)

## 原始链接

- [项目仓库](https://github.com/icesixgod/codex-trajectory)

## 相关概念

- [Codex](./tool-codex.md) — codex-trajectory 是给 Codex 日志的事后分析插件，没有 Codex 就没有它
- [kcap-cli](./tool-kcap-cli.md) — 同样面向编码会话可观测性，但 kcap-cli 捕获实时调用而非离线解析
- [quickai](./tool-quickai-claude-cost.md) — 类似的 transcript 剖析思路，但 quickai 聚焦 Claude Code 与 token 成本