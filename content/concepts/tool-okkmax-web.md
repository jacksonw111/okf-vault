---
type: Tool
title: "okkmax-web（AI API 中转服务商评测目录）"
description: "AI API 中转服务商的独立评测与目录平台，帮助用户在大量真假混杂的中转服务商中做甄别。"
resource: "https://github.com/fanbidog/okkmax-web"
tags: [ai, api, aggregator, review]
timestamp: "2026-07-07T12:00:00Z"
---

# okkmax-web（AI API 中转服务商评测目录）

## 它是什么
独立第三方平台 `okkmax-web`：把市面上众多 AI API 中转 / 代理服务商聚合到一份**带评测榜单的目录**里——核心价值不在"中介 API"本身，而在**目录 + 评测**这一层信息差：哪些是真供应商、哪些是套壳皮包、跑路历史、可靠度，让用户在选型时有一份独立参考。

## 为什么用它 / 适合什么场景
- API 中转市场常年真假混杂，普通用户很难仅凭网站外观判断。
- 需要为团队 / 项目**选型一个长期可用的 API 上游**。
- 需要第三方评测视角，而不仅是服务商自吹。

## 关键能力
| 能力 | 说明 |
|------|------|
| 服务商目录 | 聚合列出大量 AI API 中转供应商 |
| 独立评测 | 第三方视角下的真伪判断与可靠度评分 |
| 用户识别帮助 | 把"看起来像真供应商"和"实际有真实量"分开 |
| Web 形态 | 直接浏览 + 搜索比读帖子效率高 |

## 相关概念
- [animarouter](tool-animarouter.md) — 聚合 16+ LLM 提供商免费额度到单一 OpenAI 兼容接口，9 种路由策略
- [opencode-cc](tool-opencode-cc.md) — 高性能 API 代理，把 OpenCode Zen 协议桥接为 Anthropic / OpenAI 兼容
- [transit-hub](tool-transit-hub.md) — 面向 sub2api / new-api 自托管 API 服务的多上游运营管理中心
- [akshare / a-stock-data](tool-a-stock-data.md) — 同为"聚合多家数据源成统一接口"的金融数据 Skill
