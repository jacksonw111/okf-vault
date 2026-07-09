---
type: Tool
title: "DataFoundry（企业级私有部署数据 Agent 工作台）"
description: "一个企业级、可私有部署的数据 Agent 工作台，让自然语言分析在统一的业务语义、只读边界和全程审计下可信地跑完。"
resource: "https://github.com/datagallery-lab/datafoundry"
tags: "[data-agent, enterprise, self-hosted, sql, semantic-layer, audit, nl2sql]"
timestamp: "2026-07-09T20:50:00Z"
---

# DataFoundry（企业级私有部署数据 Agent 工作台）

## 它是什么
`datagallery-lab/datafoundry` 是一个**企业级数据 Agent 工作台**：

- **私有部署**：整套系统装在自己机房，符合合规要求。
- **统一业务语义**：把"业务术语 → 表 / 字段"映射集中维护，避免幻觉拼错指标。
- **只读边界**：默认不写生产库，agent 查询动作都被限制在只读视图。
- **全程审计**：每一次自然语言分析都被审计（输入、生成的 SQL、结果、时间戳、用户）。

## 为什么用它 / 适合什么场景
- 业务团队希望"自然语言问数据"，但又不敢把生产库交给 LLM。
- 想用同一个工作台**统一多个 LLM Agent** 的数据访问边界与口径。
- 适合：金融 / 医疗 / 政企 / SaaS 数据平台——任何对"数据合规 + 业务语义一致 + 全程可溯"有要求的场景。
- 与 [Tool: second-brain-cloudflare](tool-second-brain-cloudflare.md) 形成"个人 + 团队"两端覆盖。

## 关键能力
| 能力 | 说明 |
|------|------|
| 私有部署 | 数据不出自家机房 |
| 业务语义层 | 统一指标/维度口径 |
| 只读边界 | 防止误写 / 越权 |
| 全程审计 | 操作日志可回溯 |
| 多 Agent 接入 | 不耦合单一 LLM |

## 媒体参考

产品截图：
- ![](https://pbs.twimg.com/media/HMrOEkeaAAAJ3Vg.jpg)

## 相关概念
- [second-brain-cloudflare](tool-second-brain-cloudflare.md) — Cloudflare Workers 上的开源「共享大脑」
- [Open Knowledge（Inkeep）](tool-open-knowledge.md) — WYSIWYG Markdown 编辑器 + LLM 知识库
- [Finnhub API](tool-finnhub-api.md) — 美股行情/财报/新闻 REST API（数据源接入示例）

## 参考链接
- 项目链接：<https://github.com/datagallery-lab/datafoundry>
