---
type: Tool
title: "whoiz（域名 / 子域 → 路径级 CDN 与托管商归属图）"
description: "给一个域名，自动画出用户访问每个路径和子域背后各是哪家 CDN 和托管商在顶——是 Cloudflare、AWS、Fastly、Netlify、自建 Nginx？识别不到就直说不认识。"
resource: "https://github.com/jkup/whoiz"
tags: [dns, cdn, hosting, observability, devops, recon, domain]
timestamp: "2026-08-28T00:00:00Z"
---

# whoiz

## 它是什么
[jkup/whoiz](https://github.com/jkup/whoiz) 是**把域名 / 子域 / 路径级别的 CDN 与托管商归属自动识别并画成关系图的工具**。

常规 whois 只能告诉你**这个域名是谁注册的**，但现代网站的结构往往是：

- `example.com` 主站放在某 CDN；
- `cdn.example.com` 用 Cloudflare；
- `api.example.com` 走 AWS CloudFront；
- `static.example.com` 又是另一家。

whoiz 的解法是**主动探测 + 模式识别**——给定一个域名，自动扫描每个路径与子域，识别背后各是哪家 CDN / 托管商在顶，识别不到就直说「不认识」而不是强行猜测。

## 为什么用它 / 适合什么场景
- **运维 / SRE** 接手一个新域名，想立刻知道全栈用了哪些 CDN / 边缘节点；
- **安全 / 蓝队** 排查某个组织的资产边界、CDN 暴露面；
- **前端 / 性能** 工程师分析目标网站的边缘架构、缓存层位置；
- **采购 / 谈判** 时想了解竞品把哪些服务交给了哪些供应商。

## 关键能力
| 能力 | 说明 |
|------|------|
| 路径级识别 | 不只查主域，还深入到具体路径与子域 |
| CDN 识别 | Cloudflare / AWS CloudFront / Fastly / Netlify / Akamai 等 |
| 托管商识别 | Vercel / Netlify / Render / 自建 Nginx 等 |
| 不假装 | 识别不到就明说，不强行贴标签 |
| 可视化 | 把多层归属关系画成图 |
| 主动探测 | 通过 HTTP 探测 + 头部特征判断 |

## 相关概念
- [PgBot](tool-pgbot.md) — Postgres 健康诊断 CLI；whoiz 是**外部网络资产**的同思路诊断工具
- [Checkfleet](tool-checkfleet.md) — 单静态二进制内网服务检查（TLS / NATS / PG）；whoiz 是面向**公网资产**的同类轻量诊断

## 参考链接
- 项目链接：<https://github.com/jkup/whoiz>
- 原始推文：<https://x.com/QingQ77/status/2093153341585170542>
- 媒体：<https://pbs.twimg.com/media/HQskM0vaIAAhHn0.png>
