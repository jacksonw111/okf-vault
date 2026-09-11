---
type: "Tool"
title: "StrikeAgent / AtkBrain-Flash（自循环 AI 渗透测试控制台）"
description: "为授权红队打点 / SRC / CTF 提供自循环的 AI 渗透测试控制台：控制台 + 攻击图自循环，猎面去执行，监督只在轮次边界定方向，把管用手法沉到记忆库供下一局用。"
resource: "https://github.com/Yean-Sec/StrikeAgent_AtkBrain-Flash"
tags: "[security, pentest, redteam, ai-agent, ctf]"
timestamp: "2026-09-11T22:00:00Z"
---

# StrikeAgent / AtkBrain-Flash

## 它是什么

[Yean-Sec/StrikeAgent_AtkBrain-Flash](https://github.com/Yean-Sec/StrikeAgent_AtkBrain-Flash) 是夜安团队开源的**自循环 AI 渗透测试控制台**：面向**授权红队打点 / SRC（漏洞响应）/ CTF** 场景。

## 架构要点

| 组件 | 角色 |
|------|------|
| 控制台 | 人机交互层 |
| 攻击图 | 任务拓扑与依赖 |
| 猎面（Hunter） | 执行代理，跑具体攻击动作 |
| 监督（Supervisor） | 轮次边界定方向 |
| 记忆库 | 沉淀管用手法，给下一局复用 |

循环流程：**方向 → 执行 → 评估 → 记忆**，循环。

## 为什么用它 / 适合什么场景

- 安全研究员做授权渗透测试 / SRC 漏洞挖掘。
- CTF 选手想自动化部分侦察与攻击执行。
- 研究「**自循环 + 记忆库**」架构的 Agent 工程化范式。

## 关键能力

| 能力 | 说明 |
|------|------|
| 攻击图建模 | 把渗透任务拓扑化成图 |
| 自循环执行 | Hunter + Supervisor 协作 |
| 轮次监督 | 监督只在边界干预 |
| 记忆沉淀 | 每次成功手法进记忆库 |
| 多场景 | 红队 / SRC / CTF 共用引擎 |

## 重要边界

⚠️ **仅限授权场景**——红队打点、SRC 漏洞响应、CTF 比赛均可；未经授权使用即违法。

## 参考链接

- 项目仓库：<https://github.com/Yean-Sec/StrikeAgent_AtkBrain-Flash>

## 媒体

- ![](https://pbs.twimg.com/media/HRvlQbybsAAiJs8.jpg)

## 相关概念

- [fable-harness](./tool-fable-harness.md) — Claude Code 行为纪律协议（hooks / skill）
- [OKF Enrichment Agent](./tool-okf-enrichment-agent.md) — OKF bundle 自动补全 / 富化 agent
</content>
</invoke>