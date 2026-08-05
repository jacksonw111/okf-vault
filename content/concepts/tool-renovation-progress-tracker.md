---
type: "Tool"
title: "Renovation Progress Tracker（JeasonLoop/筑记）"
description: "面向个人装修的进度/验收/预算/现场记录监控工具：Next.js 19 + Cloudflare Workers + D1 + KV 全栈，开箱即部署。"
resource: "https://github.com/JeasonLoop/renovation-progress-tracker"
tags: [renovation, home, project-tracker, nextjs, cloudflare-workers, d1, kv, tool]
timestamp: "2026-08-05T12:20:00Z"
---

# Renovation Progress Tracker（JeasonLoop/筑记）

## 它是什么

**筑记（Renovation Progress Tracker）** 是一套面向**个人装修**场景的进度/验收/预算/现场记录监控工具，把散落在各节点的进度、验收单、账单收进一份**可直接托管**的数据清单。

技术栈是「**全 Cloudflare**」：

- 前端：**Next.js App Router + React 19**
- 后端：**Cloudflare Workers**
- 数据：**D1**（SQLite 兼容）
- 私有图片附件：**KV**

## 为什么用它 / 适合什么场景

- 装修涉及水电 / 瓦木油 / 验收 / 延期 / 整改等多个节点，传统用 Excel / 微信群 / Excel 都容易丢。
- 一屏摊开**阶段、任务、延期、完成情况**，适合业主、工长同时盯。
- 水电这类**关键验收**可留照片证据，不合格项跟着**整改闭环**。
- 全 Cloudflare 部署意味着**零服务器运维**、成本极低。

## 关键能力

| 能力 | 说明 |
|------|------|
| 进度页 | 阶段、任务、延期、完成情况一屏摊开 |
| 验收记录 | 水电等关键节点留照片证据 |
| 整改闭环 | 不合格项跟着整改清单走 |
| 预算跟踪 | 各节点账单汇总 |
| 私有附件 | 图片走 Cloudflare KV，不暴露 |
| 全栈托管 | Next.js + Workers + D1 + KV 整套 Cloudflare，无服务器 |

## 参考链接

- [GitHub 仓库](https://github.com/JeasonLoop/renovation-progress-tracker)

## 相关概念

- [CloudflareBase](./tool-cloudflarebase.md) — 同属「Cloudflare 全家桶自托管」思路，可参考其 Auth + 文档数据库架构