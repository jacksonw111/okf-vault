---
type: Tool
title: "wsrv.nl（开源图像 CDN / 图像代理）"
description: "免注册、免 API Key 的开源图像 CDN：往原图 URL 后拼参数即可在服务端做缩放 / 裁剪 / 格式转换 / 压缩 / 缓存，支持 GIF / animated WebP / PDF，号称每小时处理约两千万张图；可自托管 Docker。"
resource: "https://news.hada.io/topic?id=32915"
tags: [image-cdn, image-proxy, optimization, docker, self-hosted]
timestamp: "2026-08-27T09:16:00Z"
---

# wsrv.nl

## 它是什么
[wsrv.nl](https://news.hada.io/topic?id=32915) 是一个**开源的图像 CDN / 图像代理服务**。使用方式极其简单：**任何原图 URL 后面拼几个查询参数**（缩放、裁剪、格式、压缩），服务端处理后缓存到 CDN，再返回前端。**无需注册、无需 API Key**。

特性：

- **格式广泛**：静态图、**GIF、animated WebP、PDF** 均处理；
- **高吞吐**：号称每小时处理约 **2000 万张图**；
- **可自托管**：开源 + Docker 镜像，本地 / 私有云都能跑。

## 为什么用它 / 适合什么场景
- 网站 / 博客 / Wiki 中大量图片需要按设备 / 上下文动态出图（缩放、WebP 压缩、裁剪）；
- 不想签商业 CDN 合同、不想管 API Key、不想把图片传第三方；
- 想完全自托管一套「类 Cloudflare Images」的图像优化层；
- 内容站需要把 GIF / animated WebP 转成静态帧或更小的格式省带宽。

## 关键能力
| 能力 | 说明 |
|------|------|
| URL 参数驱动 | 改查询参数即可变换，不改原图 |
| 缩放 / 裁剪 | width / height / fit 参数 |
| 格式转换 | 输出 WebP / AVIF / JPEG / PNG 等 |
| 压缩 | 自动按目标质量压缩 |
| 缓存 | CDN 层缓存，重复请求直返 |
| 零注册 | 无需账号 / API Key |
| 多格式 | GIF / animated WebP / PDF |
| 高吞吐 | 公开实例 ~ 2000 万图/小时 |
| 可自托管 | Docker 一键起 |

## 相关概念
- [Cloudflare Kumo](tool-kumo.md) — Cloudflare 官方 UI 组件库与文档框架；wsrv 是更轻的「图像处理基础设施」，Kumo 是更厚的「界面组件库」
- [Next-shadcn-admin-dashboard](tool-next-shadcn-admin-dashboard.md) — Next.js 16 + shadcn UI 仪表盘模板，常配 wsrv 这类图像 CDN 处理头像 / 卡片图

## 参考链接
- 项目介绍：<https://news.hada.io/topic?id=32915>
