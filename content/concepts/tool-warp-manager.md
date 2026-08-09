---
type: "Tool"
title: "WARP-Manager"
description: "AminMGMT 写的纯 Bash VPS 工具（不依赖 Docker）：用 nftables TPROXY 拦截服务器出站 HTTPS，交给本机 sing-box 从 TLS SNI / QUIC ClientHello 提取真实域名按域名决定是否走 Cloudflare WARP，应用换 IP 或 CDN 也不影响。"
resource: "https://github.com/AminMGMT/WARP-Manager"
tags: [warp, cloudflare, bash, nftables, tproxy, sing-box, vps]
timestamp: "2026-08-09T19:35:00Z"
---

# WARP-Manager

## 它是什么

[WARP-Manager](https://github.com/AminMGMT/WARP-Manager) 是一个**纯 Bash**（不依赖 Docker）写的 VPS 工具：用 **nftables TPROXY** 拦截服务器出站的 HTTPS 流量，交给本机 **sing-box**，从 TLS SNI 和 QUIC ClientHello 里取出**真实目标域名**，按域名决定是否走 **Cloudflare WARP** 出站。**应用换了 IP 或 CDN 也不影响**——决策是基于域名而非 IP。

## 为什么用它 / 适合什么场景

- 跑 VPS 服务（爬虫 / 自动化 / 代理节点），希望对特定域名走 WARP 出口。
- 不想依赖 Docker，希望纯 Bash + 系统服务就能跑。
- 想精细化「哪些域名走 WARP / 哪些走本地出口」，而非全量代理。
- 想用 WARP+ 解锁 AI / 流媒体 / 开发者工具等服务（内置 100+ 域名分类）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 纯 Bash | 无 Docker 依赖，systemd 服务即可运行 |
| TPROXY 透明代理 | nftables 拦截出站 HTTPS，零应用改动 |
| 域名级决策 | 从 SNI / ClientHello 提取域名，按域名单独路由 |
| 内置 100+ 服务 | AI / 流媒体 / 社交 / 游戏 / 开发者工具 13 大类 |
| 白名单 / 自定义 | 任意域名可加白名单或自定义路由规则 |
| WARP+ 授权 | 支持 WARP+ 授权、自动换 IP、定时重启 |

## 媒体

![](https://pbs.twimg.com/media/HPMUGaobAAAg_AB.jpg)

## 相关概念

（暂无直接相关概念）