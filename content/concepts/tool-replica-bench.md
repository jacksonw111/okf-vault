---
type: Tool
title: "RealReplicaBench"
description: "阿里国际 Accio 团队开源的智能体业务流程度评测集：107 个真实业务流程任务（53 CLI / 28 浏览器 / 16 文件 / 10 API/MCP），按需求切成纯文本 / 浏览器可读文本 / 必须看得懂图三档；每个任务开一个干净容器跑，统一用确定性脚本 + LLM 裁判给分。"
resource: "https://github.com/Accio-Lab/RealReplicaBench"
tags: [agent-evaluation, benchmark, alibaba, accio, llm-judge, container, agent-benchmark]
timestamp: 2026-08-06T03:30:00Z
---

# RealReplicaBench

## 它是什么

阿里国际（Alibaba International）Accio 团队开源的智能体业务流程度评测集，专门测「agent 能不能完整跑通一整套真实业务流程」，而不是单个工具调用的能力。

## 为什么用它 / 适合什么场景

- 想评测自家 agent 在「端到端业务」上的体力，而不是单点 tool call 准确率。
- 想用任务异质性（CLI / 浏览器 / 文件 / API/MCP）+ 输入模态（文本 / 浏览器读文本 / 看图）做两维拆解，分析 agent 短板。
- 想用「干净容器 + 确定性脚本 + LLM 裁判」的标准化评分流程，避免自家评测管线与开源榜跑分不可比。

## 关键能力

| 能力 | 说明 |
|------|------|
| 107 个真实业务任务 | 53 CLI + 28 浏览器 + 16 文件 + 10 API/MCP，跨度够广 |
| 三档输入模态 | 纯文本 / 浏览器能读文本 / 必须看得懂图，对应 agent 多模态能力 |
| 干净容器跑任务 | 每个任务开新容器执行，互不干扰 |
| 双层评分 | 确定性脚本校验可机器验证的产物 + LLM 裁判打分主观部分 |

## 相关概念
- [AI Code Evaluation Suite](./tool-ai-code-evaluation-suite.md) — 提交 Python 代码丢进一次性 Docker 隔离评分，可见 + 隐藏测试 + 分数分解
- [Long Horizon Agents (awesome-long-horizon-agents)](./tool-awesome-long-horizon-agents.md) — 长程代理论文清单，H1/H2/H3 三层 + harness/模型双分类