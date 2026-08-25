---
type: Tool
title: "Cloudflare GitHub Actions Runner"
description: "让私有仓库的 GitHub Actions 作业跑在自己 Cloudflare 账号的临时容器里，替代按分钟计费的 GitHub 托管 runner。"
resource: "https://github.com/biw/cloudflare-github-actions-runner"
tags: [github-actions, cloudflare, ci, runner, self-hosted]
timestamp: "2026-08-25T19:30:00Z"
---

# Cloudflare GitHub Actions Runner

## 它是什么

[biw/cloudflare-github-actions-runner](https://github.com/biw/cloudflare-github-actions-runner) 把私有仓库的 GitHub Actions 作业**从 GitHub 托管 runner 搬到 Cloudflare 容器**。GitHub 给私有仓库的免费 runner 分钟数有限，超出按分钟计费；这个工具让作业跑在你自己 Cloudflare 账号的 Workers / Containers 里，按 Cloudflare 的计费模型（通常是按请求 / CPU 时间）结算，账单归自己。

## 为什么用它 / 适合什么场景

- **私有仓库 CI 用量大**：不想按分钟买 GitHub 托管 runner。
- **已经重度使用 Cloudflare 生态**：希望 CI 与边缘 / 存储在同一账号下结算。
- **想绕开 GitHub runner 配额**：自托管 runner 的另一种形态——跑在 Cloudflare 而不是自己的 VM。
- **作业短、并发弹性**：Cloudflare 容器按需拉起，适合轻量、突发型 CI。

## 关键能力

| 能力 | 说明 |
|------|------|
| 自托管 runner 替代 | 用 Cloudflare 临时容器承载 Actions job |
| 私有仓库友好 | 不依赖 GitHub 托管 runner 分钟数配额 |
| 按需弹性 | 容器冷启动 / 按作业回收 |
| 统一账单 | 跑 CI 的费用进 Cloudflare 账号 |
| 与 GitHub 协议兼容 | Actions 协议层面无侵入 |

## 相关概念

- [Lucky](./tool-lucky.md) — 自托管 Swiss Army knife：DDNS + ACME + 反代

## 参考链接

- 项目链接: <https://github.com/biw/cloudflare-github-actions-runner>
- 原始链接: <https://x.com/QingQ77/status/2092109966622470256>