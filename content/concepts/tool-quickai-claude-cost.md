---
type: "Tool"
title: "quickai（Claude Code 本地 transcript 剖析工具）"
description: "直接从磁盘上的 Claude Code transcript 文件统计 token、花费与时间去向，按任务 / 子代理 / 模型维度呈现，无需埋点、无需联网，纯本地分析。"
resource: "https://github.com/AlexGladkov/quickai"
tags: "[claude-code, analytics, token-cost, transcript, self-hosted, devtools]"
timestamp: "2026-07-08T12:30:00Z"
---

# quickai

## 它是什么

[quickai](https://github.com/AlexGladkov/quickai) 是一个 **Claude Code 的本地剖析工具**——直接读取磁盘上的 transcript 文件，统计：

- **Token 用量**
- **花费**（按模型计费折算）
- **时间分布**

按「任务」「子代理」「模型」等维度呈现，**无需埋点、无需联网**。

## 为什么需要它

- Claude Code 本身没提供详细的成本 / 时长仪表盘。
- 想看哪个任务 / 哪个子代理最烧钱 / 最耗时，只能自己解析 transcript。
- 联网分析有隐私顾虑，本地读取最安全。

## 关键能力

| 能力 | 说明 |
|------|------|
| 本地读取 transcript | 直接解析磁盘上的 JSONL |
| Token 统计 | 按模型、任务、会话维度切分 |
| 成本折算 | 按模型定价算钱 |
| 时长统计 | 看每个任务 / 子代理耗时 |
| 多维下钻 | 任务 → 子代理 → 模型逐层看 |
| 离线 | 无任何网络请求 |

## 媒体

![quickai 仪表盘预览](https://pbs.twimg.com/media/HMq4qUlbQAAOIzx.jpg)

## 参考链接

- [项目仓库](https://github.com/AlexGladkov/quickai)

## 相关概念

- [AI Usage Dashboard](./tool-ai-usage-dashboard.md) — 同为「AI 使用量 / 成本」仪表盘，但走云端聚合路线
- [Claude Code Tipsy Skill](./tool-claude-code-tipsy-skill.md) — 同为 Claude Code 增强工具，偏使用技巧