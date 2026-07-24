---
type: Tool
title: "yunxiao-mr-review-step（云效 Flow AI 自动评审流水线步骤）"
description: "阿里云云效 Flow 流水线接入的 AI 自动评审 Codeup 合并请求步骤,把模型输出的结构化结果转成行级评论,还能发飞书报告。"
resource: "https://github.com/benrenshan/yunxiao-mr-review-step"
tags: [yunxiao, code-review, ai-review, ci, feishu, codeup]
timestamp: "2026-07-24T00:00:00Z"
---

# yunxiao-mr-review-step

[yunxiao-mr-review-step](https://github.com/benrenshan/yunxiao-mr-review-step) 是给阿里云[云效](https://yunxiao.aliyun.com/) Flow 流水线用的一个**AI 自动评审步骤**,专门给 Codeup 合并请求做行级评论。

## 它解决的问题

传统 Codeup MR 评审要么靠人工 code review,要么靠 SonarQube 这种静态扫描——前者贵且慢,后者只能查风格 / bug pattern。把大模型接进流水线,通常直接得到「整段 Markdown 总结」,没法像资深 reviewer 那样把意见**精确打到具体行**。

本工具走的是结构化路径:
- 让模型按指定 JSON Schema 输出
- 把模型给的「文件 + 行号 + 评论」自动转成 Codeup 的行级评论
- 同时把评审报告发到飞书群

## 关键能力

| 能力 | 说明 |
|------|------|
| Flow 流水线原生步骤 | 作为 Flow Pipeline Step 接入,不破坏现有 CI / CD 编排 |
| Codeup 行级评论 | 模型输出按 Schema 转 inline comment,而不是堆在 MR 顶部 |
| 结构化输出 | 走 JSON Schema,避免模型「自由发挥」 |
| 飞书报告 | 评审结果可推送到飞书机器人,适合团队协作 |
| 自动评审 | 每个 MR / Push 都自动跑一遍,无需人工触发 |

## 适用场景

- 已经在用阿里云云效 / Codeup 做内部代码托管的团队
- 想要在保留 SonarQube 之类静态扫描的同时,加上 LLM 的语义评审
- 需要把评审结果同步到飞书做团队可见

## 参考链接

- 项目仓库: <https://github.com/benrenshan/yunxiao-mr-review-step>

## 媒体

![](https://pbs.twimg.com/media/HN9PmibbIAAfBYv.jpg)

## 相关概念

- [trueline-mcp](tool-trueline-mcp.md) — 同样给 AI 编码精准改文件,定位不同:一个改,一个评
- [12-Factor Agents](tool-12-factor-agents.md) — 23.5k 星 12 条让 Agent 从 demo 到实盘的工程原则