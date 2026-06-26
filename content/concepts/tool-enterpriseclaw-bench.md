---
type: Tool
title: "EnterpriseClawBench（真实企业工作会话的编码 Agent 基准）"
description: "FrontisAI 提出的编码 Agent 基准：要求 Agent 在持久工作区里操作文件、调用工具并交付能用的业务产出，弥补现有基准偏算法题、缺真实工作会话的不足。"
resource: "https://github.com/FrontisAI/EnterpriseClawBench"
tags: [benchmark, agent, evaluation, coding-agent, enterprise, eval]
timestamp: 2026-06-26T16:50:00Z
---

# EnterpriseClawBench

## 它是什么

EnterpriseClawBench 是 FrontisAI 提出的**编码 Agent 评估基准**，核心论点是：

> 现有编码 Agent 基准测的都是"比赛中做算法题"的水平，没有多少是从真实企业工作会话里来的。

为了填补这个空白，它把评测标准从"解 LeetCode 风格题"换成：

- **持久工作区**：Agent 必须在长生命周期的工作目录里操作（不能一次性跑完就清场）
- **真实工具调用**：要像真员工一样用文件 / Shell / 内部服务
- **业务交付物**：最后交出"能用的业务产出"（代码、文档、配置、报表等）才算过关

## 它与现有基准的差异

| 维度 | 传统算法题基准 | EnterpriseClawBench |
|------|---------------|---------------------|
| 工作区 | 临时一次性 | 持久 / 状态连续 |
| 工具 | 通常仅文本补全 | 真实文件 / Shell / API |
| 评分 | 测试用例通过 | 业务产出可用性 |
| 任务来源 | 比赛 / 教科书 | 真实企业工作会话 |
| 考察能力 | 短时推理 | 长链 + 工具 + 状态 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 真实工作流 | 模拟企业里"开个工单 → 改代码 → 跑测试 → 出报表"的完整链路 |
| 持久化评估 | 跨 step 的状态连续，避免"每个题独立"造成的过拟合 |
| 工具丰富 | Agent 必须学会选择 / 组合 / 失败重试多种工具 |
| 业务导向 | 评分锚定"产出能否被真实团队采用"，而非"代码能不能通过单元测试" |

## 原始链接

- [项目仓库](https://github.com/FrontisAI/EnterpriseClawBench)
- [原始推文剪藏](https://x.com/QingQ77/status/2070307051449040937)

## 相关概念

- [eot-bench](./tool-eot-bench.md) — LiveKit 的"话轮检测"基准，形态上是同思路（"现有基准偏 X，我们补 Y"）但聚焦对话
- [awesome-evals](./tool-awesome-evals.md) — BenchFlow 维护的 1.16 万论文评测索引，可交叉印证编码 Agent 评估趋势
- [AgentStalker](./tool-agent-stalker.md) — 从"安全视角"审视 Agent，把 LLM Agent 当系统而非模型来审计
