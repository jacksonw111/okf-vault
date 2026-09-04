---
type: Tool
title: "OpenSEO（全栈跑在 Cloudflare 上的开源 SEO 平台）"
description: "开源 SEO 平台，整套系统完全运行在 Cloudflare 之上（Durable Objects、KV、R2、D1 及其 Agent 能力），托管版另用 Planetscale；直到不久前月成本仅约 5 美元。"
resource: "https://github.com/every-app/open-seo"
tags: [seo, cloudflare, durable-objects, d1, r2, kv, serverless, open-source]
timestamp: 2026-09-04T12:00:00Z
---

# OpenSEO（全栈跑在 Cloudflare 上的开源 SEO 平台）

## 它是什么

一个开源的 SEO 平台。真正值得关注的是它的**部署形态**：整套系统**完全跑在 Cloudflare 上**，托管版额外用了 Planetscale 作数据库。

## 用到的 Cloudflare 能力

| 组件 | 角色 |
|------|------|
| Durable Objects | 有状态协调 |
| KV | 键值存储 |
| R2 | 对象存储 |
| D1 | 关系型数据库 |
| Cloudflare Agent 相关能力 | Agent 运行支撑 |

## 为什么值得看

- 一个**完整生产系统只靠一家边缘平台**跑起来的真实样本，而不是 hello-world demo——想评估「全栈上 Cloudflare」可行性时，这是可读代码的参照。
- 成本参照：直到不久前，这套架构的月开销约 5 美元。

## 参考链接

- 项目链接：<https://github.com/every-app/open-seo>
- 原始链接：<https://x.com/bensenescu/status/2095688948165034134>

## 相关概念

- 暂无强关联概念。
