---
type: "Tool"
title: "LawLink（开源自部署律师案件管理）"
description: "为中小律所和独立律师设计的开源自部署案件管理全流程系统，技术栈 Next.js 16 + TypeScript + PostgreSQL，律师办案主线：收案登记 → 冲突检索 → 转正式案件 → 持续跟进 → 财务记录 → 结案归档 → 数据导出。Docker Compose 一键部署，UI 走深色科技感风格。"
resource: "https://github.com/lawflow-boop/LawLink"
tags: [legal, case-management, self-hosted, nextjs, postgresql]
timestamp: "2026-06-24T15:30:00Z"
---

# LawLink（开源自部署律师案件管理）

## 它是什么

[`lawflow-boop/LawLink`](https://github.com/lawflow-boop/LawLink) 是**专门给中小律所和独立律师用的开源案件管理系统**。

技术栈：Next.js 16 + TypeScript + PostgreSQL。

律师日常办案的主线被它一锅端：

> 收案登记 → 冲突检索 → 转正式案件 → 持续跟进 → 财务记录 → 结案归档 → 数据导出

## 为什么用它 / 适合什么场景

- **独立律师 / 中小律所**需要一套轻量但完整的案件管理；
- 关注**数据自主** —— 自托管部署，客户/案件数据不出本机；
- 不想用 SaaS（如 Clio / MyCase）按席位付费；
- 部署门槛低 —— Docker Compose 一键拉起来；
- UI 走深色科技感风格，适合年轻律所 / 内部工具审美。

## 关键能力

| 能力 | 说明 |
|---|---|
| 收案登记 | 潜在客户 / 线索录入 |
| 冲突检索 | 接案前利益冲突自动查重 |
| 案件转正 | 线索 → 正式案件的转换 |
| 持续跟进 | 时间线 / 任务 / 文件管理 |
| 财务记录 | 工时 / 账单 / 收款 |
| 结案归档 | 一键归档 + 文档打包 |
| 数据导出 | 案件数据可批量导出 |
| Docker 一键部署 | docker-compose up 即可 |
| Next.js 16 | 最新版 Next.js App Router |

## 媒体 / 参考链接

- [项目链接](https://github.com/lawflow-boop/LawLink)

## 相关概念

- [Seeder](tool-seeder.md) — 小团队自托管项目管理 + MCP，看板任务管理可作为律所内部协作补充
- [OPG](tool-opg-backend.md) — 一人公司多 app 后端控制面，账户/权限/计费基础设施可与本系统组合
- [Single Server](tool-single-server.md) — 一台 Linux 服务器串 Cloudflare + Tailscale + Docker + Kamal，本系统的部署形态参考
