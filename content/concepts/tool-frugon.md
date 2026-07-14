---
type: "Tool"
title: "frugon（Rodiun/frugon）"
description: "本地开源的 LLM 费用分析器:把 OpenAI 格式 JSONL 调用日志喂进去,在本机用分词器 + 价目表把成本拆解、给出换模型 / 路由建议,全程不联网也不发模型请求。"
resource: "https://github.com/Rodiun/frugon"
tags: "[llm, cost-analysis, log-analysis, self-hosted, privacy, cli]"
timestamp: "2026-07-14T07:06:00Z"
---

# frugon

[frugon](https://github.com/Rodiun/frugon) 是一个**本地、开源、MIT** 协议的 **LLM 费用分析器**:喂入 OpenAI 格式 JSONL 调用日志,在本机算出**换模型 / 换路由能省多少**。全程**不联网、不发模型请求**。

## 关键能力

| 能力 | 说明 |
|------|------|
| 本地运行 | 计算全在本地,不联网 |
| OpenAI 格式兼容 | JSONL 调用日志直接吃 |
| 分词器统计 | 真实 token 计数 |
| 价目表拆解 | 把成本按模型 / 调用 / token 维度拆开 |
| 路由建议 | 提示换模型 / 换路由能省多少 |
| 不发请求 | 只算历史日志,不发新模型请求 |

## 适合什么场景

- LLM 应用 / 副业项目想**对账** API 成本。
- 选型阶段:对比「同一 prompt 用 GPT-4o-mini vs Claude Haiku vs 自建模型」的真实开销。
- 隐私敏感场景:账单日志不能上云,只能本地分析。
- 配合 budget / 配额告警,实现「超支前先看到」。

## 与同类资源的差别

| 资源 | 特征 | frugon |
|------|------|--------|
| tokenscope | 实时菜单栏 token 显示 | 实时;frugon 是事后日志分析 |
| retok | 分析 Claude Code / Codex 日志给省 token 建议 | 专攻 CC/Codex;frugon 通吃 OpenAI 协议 |
| quickai / retok 类比 | 工具 | frugon 偏「成本计算 + 路由建议」,不只省 token |
| token-diet | 编码 agent 省 token Skill | 技能;frugon 是事后分析 |

## 参考链接

- [项目仓库](https://github.com/Rodiun/frugon)

## 相关概念

- [tokenscope](./tool-tokenscope.md) — 实时 token / 费用菜单栏,frugon 是离线日志分析
- [retok](./tool-retok.md) — CC / Codex 日志省 token 建议,也是同类工具
- [token-tracker](./tool-token-tracker.md) — 本地统计各 AI CLI Token 消耗,可视化成本
