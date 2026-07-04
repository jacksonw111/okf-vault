---
type: Tool
title: "LinkBreeze"
description: "LinkBreeze 是自托管的 link-in-bio 平台:一条 Docker 命令部署,不用每月付 15 美元给 Linktree。拖拽管理链接、隐私分析(无 Cookie)、5 套主题、二维码、定时发布。"
resource: "https://github.com/Manak-hash/LinkBreeze"
tags: [linkbreeze, linktree, bio, self-hosted, docker, nextjs]
timestamp: "2026-07-04T15:00:00Z"
---

# LinkBreeze

## 它是什么

LinkBreeze(`Manak-hash/LinkBreeze`)是给「不想给 Linktree / Beacons / Bento 付月费」的人准备的自托管 link-in-bio 平台。它把「一条 URL 收纳所有社交链接」这件事做到了极致简单:一条 Docker 命令部署,基于 Next.js 16 + SQLite,启动后页面加载 < 300ms。

![截图](https://pbs.twimg.com/media/HMWoAXVaYAEUZBz.jpg)

项目链接：<https://github.com/Manak-hash/LinkBreeze>

## 为什么用它 / 适合什么场景

- **Linktree 个人版每月 5-24 美元,Bento / Beacons 更贵**;LinkBreeze 完全免费,数据在你自己的服务器。
- **隐私优先**:无 Cookie / 无第三方追踪器。
- **轻量**:Next.js 16 + SQLite + 单镜像,几十 MB 启动。

## 关键能力

| 能力 | 说明 |
|------|------|
| 拖拽链接管理 | 按喜好顺序排,不需要重写代码 |
| 隐私分析 | 页面浏览/点击计数有,但不带 Cookie,不追踪用户 |
| 5 套主题 + 自定义 | 内置主题 + CSS 变量覆盖 |
| 自动二维码 | 每个页面 URL 自动出 PNG/SVG 二维码 |
| 链接定时发布 | 「明天上午 9 点自动上线」这种调度 |
| Next.js 16 + SQLite | 部署简单;性能高于「页面加载 < 300ms」的目标 |

## 部署形态

```bash
git clone https://github.com/Manak-hash/LinkBreeze
cd LinkBreeze
docker compose up -d
# 默认监听 :3000
```

## 相关概念

- [Linktree 风格收费](https://linktr.ee/) — 它要替代的产品(参考链接)
- [FlareMo](tool-flaremo.md) — Cloudflare Workers + D1 + R2 上的个人笔记,与 LinkBreeze 同属「个人数据自托管」方向
- [SafeBucket](tool-safebucket.md) — 另一个自托管小工具
- [LinkBreeze 仓库](https://github.com/Manak-hash/LinkBreeze) — 项目链接
