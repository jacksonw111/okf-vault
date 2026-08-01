---
type: Tool
title: "ai-code-evaluation-suite"
description: "BuddyDew/ai-code-evaluation-suite，给 AI 或人写的 Python 代码跑隔离评分：丢进一次性 Docker 容器（无网络 / 非 root / 资源限制），跑可见 + 隐藏测试，返回带分数分解的可复现评分。"
resource: "https://github.com/BuddyDew/ai-code-evaluation-suite"
tags: "[python, docker, sandbox, code-eval, scoring, ai-coding, benchmark]"
timestamp: "2026-08-01T20:30:00Z"
---

# ai-code-evaluation-suite

## 它是什么

[`BuddyDew/ai-code-evaluation-suite`](https://github.com/BuddyDew/ai-code-evaluation-suite) 是一个**Python 代码评分套件**：把提交的代码扔进**一次性 Docker 容器**（无网络 / 非 root / 资源限制），跑一遍**可见测试 + 隐藏测试**，返回一个**带分数分解的可复现评分**。它解决的是「AI / 人写的 Python 到底能不能跑、对不对、稳不稳」的客观评判问题。

## 关键设计

| 设计点 | 说明 |
|--------|------|
| 一次性容器 | 每次提交用全新容器跑，**结果可复现**，不污染环境 |
| 沙箱隔离 | 无网络 / 非 root / 资源限制（CPU / 内存），防止恶意 / 失控代码 |
| 双层测试 | 可见测试 + 隐藏测试，避免「针对测试集优化」 |
| 分数分解 | 不只给总分，还按维度拆解（正确性 / 性能 / 边界 / 风格等） |

## 解决什么痛点

- LLM / Agent 生成代码后没法判断「是否真的能跑 / 跑通」
- 人工 review 太慢、benchmark 跑分脱离真实场景
- 普通 `pytest` 跑 AI 生成代码有安全风险（执行任意代码）

## 适合什么场景

- **AI 编程评测**：用本工具给不同模型 / 不同 prompt 的代码产出打分对比
- **教学 / 招聘**：自动给候选人代码打分，避免人工 review 主观偏差
- **CI 中的代码质量门禁**：PR 提交后自动跑隔离评测

## 与同类工具的差异

| 工具 | 范围 | 差异 |
|------|------|------|
| [better-harness](./tool-better-harness.md) | AI 编码工作流审计 | 流程审计五维框架，不直接打分 |
| [AxisAgentic](./tool-axis-agentic.md) | Agent 执行记录 | 不可篡改运行记录 + 回放 |
| [awesome-evals](./tool-awesome-evals.md) | LLM 评测榜单合集 | 评测集 / 榜单聚合 |
| ai-code-evaluation-suite | 单文件代码评分 | 真跑代码 + 隔离容器 + 双层测试 |

## 媒体

![ai-code-evaluation-suite 截图](https://pbs.twimg.com/media/HOhWnzZbIAAtN0f.jpg)

## 原始链接

- [项目仓库](https://github.com/BuddyDew/ai-code-evaluation-suite)
- [原始推文](https://x.com/QingQ77/status/2083392273480581442)

## 相关概念

- [better-harness](./tool-better-harness.md) — AI 编码工作流的「五维审计」框架，与本工具可串联（评测阶段使用）
- [awesome-evals](./tool-awesome-evals.md) — LLM 评测数据集 / 榜单合集，可作为评测维度参考