---
type: "Tool"
title: "hehe-industry-researcher（盒盒行业研究技能包）"
description: "面向 AI Agent 的中文行业与企业研究工作流，由总入口 hehe-industry-researcher 统筹 13 个专项 Skill，覆盖市场规模、产业链、商业模式、竞争格局、PEST、趋势、驱动力、痛点、公司画像、财务分析、治理与资本配置、估值、投资逻辑。"
resource: "https://github.com/hexiaofeier/hehe-industry-research-skill-pack"
tags: "[agent-skills, industry-research, chinese, workflow, market-analysis]"
timestamp: "2026-09-21T22:00:00Z"
---

# hehe-industry-researcher

## 它是什么

[hehe-industry-research-skill-pack](https://github.com/hexiaofeier/hehe-industry-research-skill-pack) 是一套面向 AI Agent 的**中文行业与企业研究**工作流——一个总入口 Skill（`hehe-industry-researcher`）+ 13 个专项 Skill，串起从宏观行业到微观公司的完整研究链路。

## 13 个专项 Skill 覆盖维度

| 维度 | 解决什么 |
|------|----------|
| 市场规模 | TAM / SAM / SOM 估算与口径说明 |
| 产业链 | 上中下游分工与价值环节 |
| 商业模式 | 收入结构、定价、护城河 |
| 竞争格局 | 玩家份额、集中度、差异化 |
| PEST | 政治 / 经济 / 社会 / 技术宏观环境 |
| 趋势 | 行业演进方向 |
| 驱动力 | 增长与变革的根本原因 |
| 痛点 | 客户 / 行业未解决的问题 |
| 公司画像 | 公司基本盘、定位、产品矩阵 |
| 财务分析 | 三表分析、关键比率 |
| 治理与资本配置 | 股权结构、董事会、资本运作 |
| 估值 | DCF / 相对估值 / 隐含假设 |
| 投资逻辑 | 总结买点 / 风险点 / 持有期 |

## 为什么用它 / 适合什么场景

- 想让 Agent 做**结构化行业 / 公司研究**而不是东一句西一句地堆信息。
- 跨多个研究维度保持**口径一致**——比如产业链里的「上中下游」与商业模式里的「价值环节」能互相引用。
- 总入口 Skill 负责**调度**——把行业先拆给市场规模 / 竞争格局 / 趋势，再把公司交给公司画像 / 财务 / 治理 / 估值。

## 关键能力

| 能力 | 说明 |
|------|------|
| 总入口 Skill | 协调 13 个专项 Skill，避免重复工作 |
| 中文语境 | 用语、案例、口径都面向中文用户 |
| 可单独调用 | 每个专项 Skill 都能独立跑 |
| 研究维度齐全 | 宏观 / 中观 / 微观三层次都覆盖 |

## 项目链接

- 仓库：<https://github.com/hexiaofeier/hehe-industry-research-skill-pack>

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — 这套工作流的载体形式
