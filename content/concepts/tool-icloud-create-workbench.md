---
type: "Tool"
title: "iCloud Create Workbench"
description: "自建服务器控制台，把 iCloud 隐藏邮箱（Hide My Email）的批量创建、库存管理、邮件同步放进同一界面，靠账号 Cookie 自动产出，省去在网页上一个一个手工点。"
resource: "https://github.com/wmn1525/icloud-create-workbench"
tags: [icloud, hide-my-email, automation, self-hosted, dashboard]
timestamp: "2026-08-07T13:28:00Z"
---

# iCloud Create Workbench

## 它是什么

iCloud Create Workbench 是一个自建服务器控制台，专门管理 iCloud 的「隐藏邮箱（Hide My Email）」功能。它把批量创建、库存盘点、邮件同步三件事收敛到同一界面，靠账号 Cookie 自动驱动，省去用户在 iCloud 网页上一个一个手工点开的重复劳动。

## 为什么用它 / 适合什么场景

- 注册多个一次性 / 副邮箱账号，想批量生成 iCloud 隐藏邮箱。
- 想把所有用过的隐藏邮箱汇总到一张表里，避免「哪个邮箱对应哪个服务」的混乱。
- 想跟踪每个隐藏邮箱的来信 / 投递状态。
- 不希望依赖第三方代收服务，所有逻辑跑在自己服务器上。

## 关键能力

| 能力 | 说明 |
|------|------|
| 批量创建隐藏邮箱 | 一次操作产出多个 `@icloud` 隐藏邮箱地址 |
| 库存管理 | 把已生成的隐藏邮箱汇总到表格，可加标签、备注 |
| 邮件同步 | 跟踪每个隐藏邮箱的来信，便于回查服务来源 |
| Cookie 自动驱动 | 用账号 Cookie 自动操作，无需每次手动登录 |
| 自托管 | 部署在自己的服务器上，数据不出本地 |
| 控制台式 UI | Web 面板形式，可视化管理 |

## 相关概念

- [Apple Hide My Email](./term-apple-hide-my-email.md) — iCloud 内置的隐私邮箱功能，本工具的操作对象
- [SimpleLogin](./tool-simplelogin.md) — 开源自托管的邮件别名服务，是与 iCloud Hide My Email 同类的替代方案