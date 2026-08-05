---
type: "Tool"
title: "LongHorizon-Harness（AMAP-ML/LongHorizon-Harness）"
description: "高德地图 AMAP-ML 团队开源的「长程代理」脚手架/评测框架，用「认知回路 + 经验记忆 + 工具/技能」三件套让模型在多步任务里保持目标感，并自带真实业务评测集。"
resource: "https://github.com/AMAP-ML/LongHorizon-Harness"
tags: [long-horizon, harness, agents, amap, amap-ml, eval, framework]
timestamp: "2026-08-05T16:00:00Z"
---

# LongHorizon-Harness（AMAP-ML/LongHorizon-Harness）

## 它是什么

`AMAP-ML/LongHorizon-Harness` 是高德地图 AMAP-ML 团队开源的**长程代理脚手架**：面向「一个任务需要几十几百步、跨工具/跨数据源才能完成」的场景，给出参考实现 + 评测集。

核心理念是让代理具备三条能力：

1. **认知回路**：明确规划 → 执行 → 验证 → 反思的循环，而不是一次 prompt 直出；
2. **经验记忆**：把历史轨迹 / 成功失败案例沉淀下来，下次同类任务直接复用，避免每次从零开始；
3. **工具/技能库**：把可用能力抽象成可注册的 skill，代理按需调用。

项目主页同步展示了文档、案例与可视化。

## 为什么用它 / 适合什么场景

- **长程任务**：单次工具调用搞不定的复杂流程（多轮检索 + 多步修改 + 验证）；
- **业务评测**：自带真实业务场景的评测集，不只是学术 benchmark；
- **脚手架而非新模型**：直接基于现有 LLM，专注 harness 设计。

## 关键能力

| 能力 | 说明 |
|------|------|
| 认知回路 | 规划-执行-验证-反思循环，避免一次直出 |
| 经验记忆 | 任务轨迹 / 案例沉淀，跨会话复用 |
| 工具/技能注册 | 统一管理可用能力，agent 按需调度 |
| 真实业务评测集 | 不只是学术 benchmark，含高德实际业务样本 |
| 可视化主页 | 文档 / 演示 / 案例统一展示 |

## 参考链接

- [GitHub 仓库](https://github.com/AMAP-ML/LongHorizon-Harness)
- [项目主页](https://lh-harness.pages.dev/)

## 相关概念

- [Awesome Long-Horizon Agents](./tool-awesome-long-horizon-agents.md) — 同主题（长程代理）的论文清单 + H1/H2/H3 分层，可与本框架互相参照
- [Codexloom](./tool-codexloom.md) — 同属「把单次线程延续为领域 agent」的思路
- [Agent Skills（代理技能包）](./term-agent-skills.md) — 通用「技能包」术语，与本项目的 skill 注册机制同源