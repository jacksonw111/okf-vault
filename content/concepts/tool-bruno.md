---
type: "Tool"
title: "Bruno"
description: "开源的本地优先 API 客户端：API 集合以纯文本文件存储，可纳入 Git 版本管理，与 Postman 的云端协作思路相反。"
resource: "https://www.usebruno.com/"
tags: [api-client, open-source, git-friendly, local-first, developer-tools]
timestamp: "2026-08-08T20:00:00Z"
---

# Bruno

## 它是什么

Bruno 是一款开源的本地优先 API 客户端，核心差异点是「API 集合以纯文本文件存储」。整套 collection 不是云端账户的私有数据，而是可直接 commit 进 Git、用 diff 看变更的 Markdown-like 文件。

## 为什么用它 / 适合什么场景

- 想用 Git 管理 API 集合，跟代码一起 review。
- 不想被 Postman 云端账号锁定。
- 喜欢「文件即配置」的本地优先工具。
- 团队协作：API 集合像代码一样走 PR 流程。

## 关键能力

| 能力 | 说明 |
|------|------|
| 纯文本存储 | 每个 collection 是文件夹，结构可读 |
| Git 友好 | diff 友好，PR review 自然 |
| 本地优先 | 无需云端账号，本地运行 |
| 多协议 | REST / GraphQL / gRPC / WebSocket |
| 环境变量 | 通过 .env 文件管理多环境配置 |
| CLI 版 | Bruno CLI 可在 CI 中跑 collection |

## 相关概念

- [HTTPie](./tool-httpie.md) — 终端 HTTP 客户端，但走 CLI
- [Postcat](./tool-postcat.md) — 终端 HTTP 调试 TUI