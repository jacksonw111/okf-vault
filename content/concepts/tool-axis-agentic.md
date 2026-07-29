---
type: Tool
title: "AxisAgentic（Agent 运行不可篡改记录与回放 / 评测 / 训练数据导出）"
description: "长时间跑的 Agent 难重现、不好评估、收集训练数据也麻烦。AxisAgentic 给每次执行做一份不可篡改的运行记录，回放、评测、导出训练数据全用同一份。"
resource: "https://github.com/XYZ-AI-Lab/AxisAgentic"
tags: [agent, observability, reproducibility, evaluation, training-data]
timestamp: "2026-07-29T05:41:00.000Z"
---

# AxisAgentic

## 它是什么

**长时间跑**的 Agent 存在三类工程难题：

1. **难重现**——同样的 prompt + 同样的工具，结果可能漂移
2. **不好评估**——评测要回放执行轨迹，传统日志不全
3. **训练数据散落**——高质量 Agent 轨迹是训练素材，但散在各处

AxisAgentic 的解法：**给每次执行生成一份不可篡改的运行记录**——回放、评测、导出训练数据全用同一份。

![示意图](https://pbs.twimg.com/media/HOSQw4cbIAEqKu_.jpg)

## 它做了什么

| 步骤 | 说明 |
|------|------|
| 执行 Agent 任务 | 完整记录每个 tool call / message / decision |
| 不可篡改存档 | append-only / 哈希链 / 类区块链结构 |
| 回放 | 用同一份记录驱动 UI 重演 |
| 评测 | 按 step 打分、对比基准 |
| 训练数据导出 | 直接吐成 SFT 格式（messages / tools） |

## 与「传统日志」的差异

| 维度 | 传统日志 | AxisAgentic |
|------|---------|-------------|
| 完整性 | 可能丢消息 | 全量不可篡改 |
| 可回放 | 通常不能 | 原生支持 |
| 评测 | 难自动化 | 按 step 评分 |
| 训练数据 | 需手动 ETL | 一键导出 |
| 时序一致性 | 不保证 | 哈希链锚定 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 不可篡改记录 | append-only + 哈希链 |
| 同一份数据三种用途 | 回放 / 评测 / 训练数据 |
| 长 Agent 任务友好 | 不丢失中间状态 |
| 训练数据导出 | 解决 Agent 后训练的数据来源问题 |

## 原始链接

- [项目仓库](https://github.com/XYZ-AI-Lab/AxisAgentic)
- [推文剪藏](https://x.com/QingQ77/status/2082340593837969422)

## 相关概念

- [AgentStalker](./tool-agent-stalker.md) — 把 LLM Agent 当系统而非模型来审计
- [kcap-cli](./tool-kcap-cli.md) — 给 AI 编码助手的可观测性 CLI
- [AgentLock](./tool-agent-lock.md) — eBPF LSM 把 AI 代理限制在指定目录
- [12-Factor Agents](./tool-12-factor-agents.md) — Agent 工程原则，提到状态管理