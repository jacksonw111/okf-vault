---
type: Tool
title: "Covan（公司级共享 AI agent）"
description: "给全公司用的共享 AI agent，不是工程师专属的 Slack 机器人，更像「读过你们所有文档的同事」：团队把流程文档 / 合同 / 研究资料传上去汇成一个 agent 的记忆，每个人在自己私密的会话里提问，隔离靠 Postgres 行级安全而不是 API 里的检查。"
resource: "https://github.com/covan-ai/covan"
tags: [enterprise, agent, knowledge-base, postgres, rls, shared-memory]
timestamp: "2026-09-03T00:00:00Z"
---

# Covan（公司级共享 AI agent）

## 它是什么

[Covan](https://github.com/covan-ai/covan) 是给**全公司用的共享 AI agent**，定位不是工程师专属的 Slack 机器人，更像一个「**读过你们所有文档的同事**」：

- 团队把流程文档、合同、研究资料传上去，汇成一个 agent 的**记忆**；
- 每个人在自己**私密**的会话里提问；
- 隔离不是放在应用层检查里，而是**靠 Postgres 行级安全（RLS）**——数据库本身就是访问控制层。

## 为什么用它 / 适合什么场景

- 公司想把分散在 Confluence / Notion / Google Drive / 内部 Wiki 的文档变成一个能回答员工问题的 agent；
- 希望不同部门 / 员工只能看到自己有权限的内容，但又共用同一个 agent 的「记忆」；
- 厌倦了在应用层写一堆 `if (user.role === 'admin')` 的权限检查——想用数据库层 RLS 替代；
- 需要合规可追溯的问答（Postgres 行级安全让审计更直接）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 共享记忆 | 团队资料汇成一个 agent 的记忆 |
| 私密会话 | 每个用户问的都是自己的会话 |
| Postgres RLS | 隔离靠数据库行级安全，非应用层检查 |
| 多资料源 | 流程 / 合同 / 研究文档统一 |
| 公司级定位 | 不是工程师专属工具 |

## 参考链接

- 项目链接：<https://github.com/covan-ai/covan>
- 原始推文：<https://x.com/QingQ77/status/2095299231603126341>
- 媒体：<https://pbs.twimg.com/media/HRIRMoSbsAAybFY.jpg>

## 相关概念

- [second-brain-cloudflare](./tool-second-brain-cloudflare.md) — Cloudflare Workers 上的开源共享记忆层
- [TencentDB Agent Memory](./tool-tencentdb-agent-memory.md) — 腾讯云数据库驱动的 agent 长期记忆
- [EverOS](./tool-everos.md) — 统一的本地长期记忆层，让不同 agent 共享并进化记忆
