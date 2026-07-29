---
type: Tool
title: "Endpoint Evolution Atlas（FDA 主要终点变化跟踪工具）"
description: "纯前端工具，覆盖 161 个适应症、15 个治疗领域，跟踪 FDA 主要终点的变化。亮点是 Whitespace Explorer 评分——把终点放宽程度、竞争稀疏度、罕见病路径综合起来按 log 尺度打分。"
resource: "https://github.com/sherryyyyang/FDA_endpoint_tracking"
tags: [fda, clinical-trials, endpoints, frontend, biostatistics, pharma]
timestamp: "2026-07-28T06:10:00.000Z"
---

# Endpoint Evolution Atlas

## 它是什么

**纯前端工具**，覆盖：

- 161 个适应症
- 15 个治疗领域
- 跟踪 FDA 主要终点的历史变化

核心亮点是 **Whitespace Explorer 评分**——把三个维度综合到一个 log 尺度的分数：

1. **终点放宽程度**：FDA 在该适应症上是否放松了终点要求
2. **竞争稀疏度**：竞争对手少
3. **罕见病路径**：是否走罕见病捷径

低分 = 红海内卷，高分 = FDA 信号 + 竞争空白 + 罕见病通道并存 = 战略机会窗。

![截图示例](https://pbs.twimg.com/media/HONpIsZacAAtJLs.jpg)

## 适用场景

- **临床策略**：寻找新药 / 新疗法的「战略机会窗」
- **投资 / BD**：评估某适应症的竞争烈度与监管变化方向
- **学术研究**：追踪 FDA endpoint 政策的演化
- **生物统计师**：发现被低估的细分适应症

## 关键能力

| 能力 | 说明 |
|------|------|
| 161 适应症覆盖 | 广度足以横向扫 |
| 15 治疗领域 | 跨领域比较 |
| Whitespace Explorer | log 尺度综合打分，识别空白窗口 |
| 纯前端 | 可静态部署，无后端依赖 |
| FDA 主要终点变化追踪 | 监管角度的视角 |

## 原始链接

- [项目仓库](https://github.com/sherryyyyang/FDA_endpoint_tracking)
- [推文剪藏](https://x.com/QingQ77/status/2081985503868620958)

## 相关概念

- [Datalab LIFT（视觉文档 JSON 抽取）](./tool-datalab-lift.md) — 把 Schema 直接吐成 JSON 的 VLM
- [gold-pan](./tool-gold-pan.md) — 隐私优先多模态数据提取 + 本地 RAG 工作台
- [Systematic Review LLM Screener](./tool-systematic-review-llm-screener.md) — 系统综述文献筛选的本地 LLM 工具
- [Awesome Scientific LLM Benchmarks](./tool-awesome-scientific-llm-benchmarks.md) — 精选科学 LLM 基准清单