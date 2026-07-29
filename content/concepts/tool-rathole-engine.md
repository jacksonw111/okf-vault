---
type: Tool
title: "RatholeEngine（基于 rathole + Nginx 的多地点反向隧道编排系统）"
description: "用 rathole + Nginx 做多地点反向隧道的编排系统：一个域名、一个端口、一张证书，把多个境外节点的流量统一路由回境内。"
resource: "https://github.com/loopy-iri/RatholeEngine"
tags: [rathole, nginx, reverse-tunnel, networking, proxy, orchestration]
timestamp: "2026-07-28T08:16:00.000Z"
---

# RatholeEngine

## 它是什么

一个把 **rathole + Nginx** 组合起来的多地点反向隧道编排系统：原本零散的境外节点（每节点一个 rathole client）通过编排统一收口，**只需一个域名、一个端口、一张证书**，就能让所有节点流量按规则路由回境内。

![示意图](https://pbs.twimg.com/media/HONpjRWaYAAItDE.jpg)

## 解决的痛点

- **多节点管理麻烦**：每个境外节点单独暴露端口、单独申请证书、单独配 DNS，节点一多就乱
- **TLS 分散**：每个节点都要维护证书，过期 / 更新全要逐个处理
- **路由不统一**：流量分发靠手工 NAT / iptables，规则散落各处

## 关键能力

| 能力 | 说明 |
|------|------|
| 单域名单端口单证书 | 入口收口到一张证书 |
| 多地点反向隧道编排 | 节点多但配置只写一份 |
| Nginx 做 7 层路由 | 根据 host / path 把流量分发到对应后端 |
| rathole 负责内网穿透 | 客户端轻量、易部署 |
| 适合跨境 / 混合云 | 境外节点回境内 / 边缘回中心皆可 |

## 架构

```
[境外节点 A]──┐
[境外节点 B]──┼──rathole──→ [境内 nginx :443 :证书] ──路由→ [内网服务]
[境外节点 C]──┘
```

## 原始链接

- [项目仓库](https://github.com/loopy-iri/RatholeEngine)
- [推文剪藏](https://x.com/QingQ77/status/2082017212823490902)

## 相关概念

- [3X-UI](./tool-3x-ui.md) — Xray 图形面板
- [Lucky](./tool-lucky.md) — DDNS + ACME + 反代瑞士军刀
- [Single Server](./tool-single-server.md) — 一台 Linux 服务器串 Cloudflare + Tailscale + Docker 一键部署
- [Cloudflare DDNS Favonia](./tool-cloudflare-ddns-favonia.md) — Cloudflare 守护进程做动态 DNS