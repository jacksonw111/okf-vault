---
type: "Tool"
title: "iCloud Prime（本地 Hide My Email 控制台）"
description: "本地架一个苹果「隐藏我的邮箱」控制台：网页 + HTTP API 都能操作多个 iCloud 账号、生成别名、收发别名邮件，Windows 提供便携版，开箱即用。"
tags: "[icloud, hide-my-email, self-hosted, api, privacy]"
timestamp: "2026-08-15T01:10:00Z"
resource: "https://github.com/forever94yu/icloud-prime"
---

# iCloud Prime（本地 Hide My Email 控制台）

## 它是什么

`iCloud Prime` 是一个本地运行的苹果 iCloud「隐藏我的邮箱（Hide My Email）」控制台。它同时提供：

- **网页界面**：浏览器里登录、管理多个 iCloud 账号、生成别名、读 / 发到别名的邮件。
- **HTTP API**：让脚本 / CI / AI agent 通过接口调用所有功能。

Windows 用户可直接拿到便携版（绿色版，无需安装）开箱使用；macOS / Linux 也能本地部署。

## 为什么用它 / 适合什么场景

- 想把多个 iCloud 账号的隐藏邮箱收归一处统一管理。
- 想用 API 把「生成别名 → 写入登记表 → 自动收信」的流程自动化。
- 在 Windows 上不想折腾 iCloud 官方客户端（必须装 iCloud for Windows 才能用隐藏邮箱）。
- 想自己掌控邮件流量，不走第三方代收服务。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多 iCloud 账号 | 单实例下挂多个账号，统一面板切换 |
| 生成别名 | Web 按钮 / API 调用，按需产出 `@icloud.com` 隐藏邮箱 |
| 读 / 发邮件 | 收件箱列表 + 撰写 / 发送（走别名），无需走 Apple 邮件客户端 |
| HTTP API | 与 Web 界面同源能力，外部脚本可直接驱动 |
| Windows 便携版 | 不需安装，解压即用，对 Windows 用户友好 |
| 本地优先 | 数据在自己机器上，便于备份 / 审计 |

## 与相关工具的差异

| 工具 | 定位 | 关键差异 |
|------|------|----------|
| [iCloud Create Workbench](tool-icloud-create-workbench.md) | 专注批量创建隐藏邮箱 | 偏「批量产出 + 库存管理」，不发信 |
| iCloud Prime | 控制台 + API | 覆盖「创建 + 收发 + 多账号 + API」，更接近完整客户端 |

## 适用人群

- Windows 上的 iCloud+ 用户（避开官方客户端的依赖）。
- 想用脚本 / agent 自动化别名管理的开发者。
- 想脱离 Apple 邮件 App，但还要保留 Hide My Email 能力的人。

## 参考链接

- [项目链接](https://github.com/forever94yu/icloud-prime)

## 相关概念

- [Apple Hide My Email](term-apple-hide-my-email.md) — iCloud+ 内置的隐私邮箱别名功能，本工具的操作对象
- [iCloud Create Workbench](tool-icloud-create-workbench.md) — 围绕 Hide My Email 批量创建与库存管理的自建控制台
- [SimpleLogin](tool-simplelogin.md) — 开源自托管的同类邮件别名服务