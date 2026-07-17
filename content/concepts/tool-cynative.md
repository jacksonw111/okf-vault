---
type: "Tool"
title: "cynative（cynative/cynative）"
description: "跑在你自己云、代码和运行时上的安全研究智能体——用大模型把「我哪里暴露了不该暴露的东西」这类问题, 在 GitHub/AWS/K8s 等一堆系统里并行查一遍, 全程只读、沙箱化, 最后给出能追到源头的结论。"
resource: "https://github.com/cynative/cynative"
tags: "[security, cloud-security, agent, read-only, devsecops]"
timestamp: "2026-07-17T06:42:00Z"
---

# cynative

[cynative](https://github.com/cynative/cynative) 是一个「**跑在你自己的云、代码和运行时上**」的**安全研究智能体**。它用大模型来回答「我哪里暴露了不该暴露的东西」这类问题, 在 GitHub、AWS、K8s 等一堆系统里**并行**查一遍; 全程**只读、沙箱化**, 最终给出可追到源头的结论。

## 它和「自动扫描器」的差别

| 维度 | 自动扫描器 | cynative |
|------|------|------|
| 行为 | 跑规则 → 出风险项 | 用 LLM 推理 → 给「为什么 + 怎么修」 |
| 数据源 | 单一系统 (比如 CodeQL) | 跨 GitHub / AWS / K8s / 运行时联合查 |
| 输出 | 列表 | 上下文叙事结论 + 引用源头 |
| 权限 | 通常需要写 / 安装 agent | **只读 + 沙箱**, 不需要代理常驻 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 跨系统并行查询 | GitHub、AWS、K8s、运行时一起看, 不只是单一系统快照 |
| 大模型推理 | 不只是规则匹配, 还能根据语义推断「这里可能暴露了 X」 |
| 只读 + 沙箱 | 在用户自己的云里运行, 但只读不写, 不污染生产 |
| 可追溯结论 | 每条结论都给出可追溯到源头 (commit / IAM / deployment 等) 的指针 |

## 媒体

![](https://pbs.twimg.com/media/HNRP0eFbwAArDtF.jpg)
![](https://pbs.twimg.com/media/HNRP3fvb0AABaXC.jpg)

## 参考链接

- [项目仓库](https://github.com/cynative/cynative)

## 相关概念

- [Strix](./tool-strix.md) — 自主 AI 渗透测试 agent, cynative 偏「防御视角的自查」, Strix 偏「攻击视角的 PoC」
- [AgentStalker](./tool-agent-stalker.md) — 把 LLM Agent 当成系统来审计 (污点图 → 攻击链 → 沙箱重放), cynative 输出形态与之互补
- [Cliare](./tool-cliare.md) — CLI 工具的 Agent 就绪评分 + 安全报告, 三者从不同层切入「Agent 时代的安全」主题
