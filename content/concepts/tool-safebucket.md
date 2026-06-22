---
type: "Tool"
title: "SafeBucket（预签名 URL 直传直下的自托管文件共享）"
description: "safebucket/safebucket —— 开源自托管文件共享平台，文件通过预签名 URL 直传直下，绕过服务器中转。Go + React 架构，存储 / 数据库 / 事件 / 缓存 / 通知组件皆可插拔。"
tags: "[file-sharing, self-hosted, presigned-url, go, react, s3-compatible]"
timestamp: "2026-06-22T16:06:00Z"
---

# SafeBucket（预签名 URL 直传直下的自托管文件共享）

## 它是什么

[`safebucket/safebucket`](https://github.com/safebucket/safebucket) 是一套**开源的自托管文件共享平台**。文件通过**预签名 URL 直传直下**，**绕过服务器中转**。

技术栈：

- **后端**：Go
- **前端**：React
- **存储**：S3 / 兼容对象存储（通过预签名 URL）
- **数据库**：可插拔
- **事件 / 缓存 / 通知**：组件化，可单独替换

> 截图：![](https://pbs.twimg.com/media/HLT0GdJaYAAlcb9.jpg)

## 为什么用它 / 适合什么场景

- **服务器不碰文件内容**：上传 / 下载走预签名 URL，**带宽与存储压力全在对象存储上**，应用服务器只签发 URL。
- **隐私 / 合规**：服务器只持 URL 签名能力，不持文件明文；文件内容直接落到 S3 / MinIO / 阿里 OSS。
- **可插拔**：存储、数据库、事件、缓存、通知每个组件都能换，团队按已有基建选型。
- **替代 WeTransfer / Dropbox 自托管版**：团队 / 客户之间临时共享大文件。

适合：

- 想要「类 WeTransfer」体验又不想用 SaaS 的团队
- 已用对象存储（S3 / MinIO / OSS）的工程团队
- 关心**文件隐私**与**服务器带宽成本**的运维

## 关键能力

| 能力 | 说明 |
|---|---|
| 直传直下 | 文件不经服务器中转 |
| 预签名 URL | S3-style 临时访问凭证 |
| Go + React | 后端 Go，前端 React |
| 组件可插拔 | 存储 / DB / 事件 / 缓存 / 通知均可替换 |
| 自托管 | 完全私有部署 |

## 工作流

```
上传方 (浏览器) ──→  SafeBucket 申请预签名 URL  ──→  直接 PUT 到 S3 / MinIO
下载方 (浏览器) ──→  SafeBucket 申请预签名 URL  ──→  直接 GET 到 S3 / MinIO
                                                                  │
SafeBucket 服务器只签 URL，不过文件内容 ────────────────────────┘
```

## 参考链接

- [项目链接](https://github.com/safebucket/safebucket)

## 相关概念

- [Cloud Mail](tool-cloud-mail.md) — 单域名无限收发的邮件服务（同样「轻量自托管邮件 / 文件」方向）
- [OPG](tool-opg-backend.md) — 一人公司多 app 后端控制面（账号 / AI 网关 / 视频 / 支付）
- [Single Server](tool-single-server.md) — 一台 Linux 服务器一键部署