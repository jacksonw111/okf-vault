---
type: Tool
title: "transit-hub"
description: "面向 sub2api / new-api 自托管 API 服务的多上游运营管理中心，后端 Go 1.25，前端 Vue 3.5，提供 Docker Compose 一键部署。"
resource: "https://github.com/deviseo/transit-hub"
tags: [api, ops, multi-upstream, dashboard]
timestamp: "2026-07-07T12:00:00Z"
---

# transit-hub

## 它是什么
`deviseo/transit-hub` —— 面向 **sub2api / new-api 这类自托管 API 服务** 的「多上游运营管理中心」。运营一个二次转售 / 中转 API 站时，会面对多上游同步、余额跟踪、分组倍率价格活动等繁杂事务，transit-hub 提供统一面板。技术栈 **Go 1.25 + Vue 3.5 + PostgreSQL 16+ + Redis 7+**，Docker Compose 一键部署。

## 为什么用它 / 适合什么场景
- 你在运营一个自托管的 API 中转平台（new-api / sub2api 等），想摆脱手算和脚本拼凑的状态。
- 需要：上游站点同步、余额跟踪、分组倍率快照 / 历史、**定时调价活动（到期自动恢复原倍率）**。
- 想要一个后端 + 前端 + DB 完整 Docker Compose 栈，不愿自己拼。

## 关键能力
| 能力 | 说明 |
|------|------|
| 上游管理 | 添加 / 同步上游站点 |
| 余额跟踪 | 多上游统一余额面板 |
| 分组倍率快照 | 当前 / 历史倍率都能看 |
| 定时调价活动 | 设定窗口 + 到期自动恢复原倍率 |
| 一键部署 | Docker Compose 拉起后端 · 前端 · DB · Cache |

## 相关概念
- [animarouter](tool-animarouter.md) — 聚合 16+ LLM 提供商免费额度到单一 OpenAI 兼容接口
- [opencode-cc](tool-opencode-cc.md) — 高性能 API 代理，把 OpenCode Zen 协议桥接为 Anthropic / OpenAI 兼容
- [okkmax-web](tool-okkmax-web.md) — AI API 中转服务商的独立评测与目录平台
- [OPG](tool-opg-backend.md) — 一人公司多 app 后端控制面（账号 / AI 网关 / 视频 / 支付 / 计费）
