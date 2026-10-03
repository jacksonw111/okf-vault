---
type: "Tool"
title: "Cloudflare Artifacts（Git 兼容的代码仓库平台底座）"
description: "Cloudflare BirthdayWeek 发布的 Git 兼容系统：专为「成百上千 AI Agent 同时编码」时代设计，支持从 Worker 创建 / fork / clone 仓库；Cloudflare 还配套发起「在 Artifacts 之上重建下一代 Git 平台」开发者竞赛。"
resource: "https://blog.cloudflare.com/next-git-platform-on-cloudflare/"
tags: "[cloudflare, git, artifacts, ai-agent, dev-platform, birthdayweek]"
timestamp: "2026-10-03T00:00:00Z"
---

# Cloudflare Artifacts

## 它是什么

[Cloudflare Artifacts](https://blog.cloudflare.com/next-git-platform-on-cloudflare/) 是 Cloudflare 在 **BirthdayWeek** 发布的 **Git 兼容代码仓库平台底座**——为「成百上千 AI Agent 同时编码」这一新场景重新设计：

- 从 **Worker** 里直接创建 / fork / clone Git 仓库
- 已有 Git 工具链可直接对接（兼容 Git 协议）
- 为大规模并发仓库操作做了基础设施层优化

Cloudflare 还配套发起 **「在 Artifacts 之上重建下一代 Git 平台」开发者竞赛**——邀请开发者在底座之上构建面向 AI Agent 时代的 Git 托管形态。

## 为什么用它 / 适合什么场景

| 场景 | 价值 |
|------|------|
| 多 Agent 协同编码 | 传统 GitHub 为「人写人审人合」设计，Agent 海量并发时不匹配 |
| Worker 内创建仓库 | 让 Agent 自己 fork / 试错 / 提交，不必绕道外部服务 |
| 自托管 Git 平台底座 | 不必从零搭 Git 后端，直接基于 Artifacts 构建 |
| 边缘代码资产 | 与 Workers / R2 / Workers AI 同生态 |

## 关键能力

| 能力 | 说明 |
|------|------|
| Git 兼容 | 已有 Git CLI / 工具可直接对接 |
| Worker 原生 | 从 Worker 直接创建 / fork / clone |
| 大规模并发 | 为多 Agent 同时编码优化 |
| 生态一致性 | 与 Workers / R2 / Workers AI 同账号 / 同计费 |

## 参考链接

- 项目链接：<https://blog.cloudflare.com/next-git-platform-on-cloudflare/>

## 相关概念

- [Cloudflare Clef](./tool-cloudflare-clef.md) — 同为 BirthdayWeek 发布
- [Cloudflare K2 Streams](./tool-cloudflare-k2-streams.md) — 同为 BirthdayWeek 发布
