---
type: "Note"
title: "Advent of Agents Season 3（Google Cloud 31 天生产级 Agent 实战系列）"
description: "Google Cloud 在 2026 年 10 月推出的 31 天免费动手教程系列：每天一篇覆盖 agent identity、guardrails、sandboxing、observability、evaluations、MCP security、cost controls、fleet management——每篇以客户和安全团队的真实问题为入口，配可运行代码。"
resource: "https://adventofagents.com"
tags: "[google-cloud, agent, security, observability, mcp, course, tutorial, free]"
timestamp: "2026-10-02T01:15:00Z"
---

# Advent of Agents Season 3（Google Cloud 31 天生产级 Agent 实战系列）

## 它是什么

[Advent of Agents Season 3](https://adventofagents.com) 是 Google Cloud 在 2026 年 10 月推出的**免费 31 天动手教程系列**，定位「把 AI agent 安全、可控地带到生产环境」。每天解锁一篇实战教程 + 可运行代码，覆盖安全与治理的方方面面。

## 每天的主题（30 天 + 收官）

| 类别 | 代表主题 |
|------|---------|
| 身份 / 鉴权 | agent identity、API key、service account |
| 隔离 / 沙箱 | sandboxing、tool-call blast radius |
| 守门 | guardrails、输入输出审查、prompt injection 防御 |
| 可观测 | observability、trace、log、cost analytics |
| 评测 | evals、回归、red-team、行为评分 |
| MCP 安全 | MCP server 鉴权、工具毒化检测 |
| 成本 | cost controls、rate limiting、budget alert |
| 编队 | fleet management、多 agent 调度、failover |

## 为什么值得关注

- **真实问题驱动**——每篇教程的标题就是「客户 / 安全团队真正会问的那个问题」，再给出可跑代码作答，不是 PPT 演讲。
- **覆盖完整的「生产级」维度**——身份 / 沙箱 / 守门 / 可观测 / 评测 / 成本 / 编队一次扫完。
- **MIT 可改可用**——所有教程仓库都开源，code 在 Cloud 账户上跑就行。
- **学完能写简历**——一口气拿到生产级 agent 安全的一手图谱。

## 学习建议

1. **按顺序刷**——每天一篇大约 30-60 分钟，10 月跑完。
2. **每篇动手跑**——教程结尾都有 deploy 按钮 / 链接，把代码粘到自己的 GCP 项目里跑一遍。
3. **对照已有项目**——每篇都问自己：「我手上的 agent 这块做得怎样？」，把短板补齐。
4. **建一份本地 cheat sheet**——把 31 篇的「做与不做」总结成 1 页 markdown，贴到团队 wiki。

## 参考链接

- 原始链接：<https://x.com/_avichawla/status/2105739515382165728>
- 项目链接：<https://adventofagents.com>

## 相关概念

- [Harness Engineering](./term-harness-engineering.md) — 大伞概念，本系列是它在「生产级安全 / 治理」维度的具体落地
- [MCP](./term-mcp.md) — 本系列里 MCP 安全是单独一讲
- [Sandbox](./term-sandbox.md) — sandboxing 是本系列的独立主题
- [Cloudflare security-audit-skill](./tool-cloudflare-security-audit-skill.md) — 另一份多阶段安全审计 Skill，可与本系列搭配学习
