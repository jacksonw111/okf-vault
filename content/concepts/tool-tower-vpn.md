---
type: "Tool"
title: "Tower (VPN Subscription)"
description: "iPhone 上的机场订阅与节点管理 App：把订阅 / 自有节点转成 Surge / Clash / Shadowrocket / Loon / Quantumult X 等代理工具的配置，转换全程在本机完成，不上传节点。"
resource: "https://github.com/pengchujin/tower"
tags: [vpn, ios, subscription, surge, clash, shadowrocket]
timestamp: "2026-08-08T20:30:00Z"
---

# Tower (VPN Subscription)

## 它是什么

Tower 是一款 iPhone 上的机场订阅与自有节点管理 App，专门解决「拿到一段机场订阅 URL 之后还要手动转成各家代理客户端能识别的配置」这件事。它支持把订阅和节点转成 Surge / Clash / Shadowrocket / Loon / Quantumult X 等主流客户端的配置格式，且转换全程在本机完成，不会把节点上传到第三方。

## 为什么用它 / 适合什么场景

- 在 iPhone 上同时管多个机场订阅 + 自有节点。
- 想在多家代理客户端之间快速切换配置。
- 关心隐私：节点信息只在本地转换，不希望经过第三方服务器。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多订阅管理 | 同时管理多个机场订阅链接 |
| 多客户端导出 | Surge / Clash / Shadowrocket / Loon / Quantumult X |
| 本机转换 | 转换全程在 iPhone 本地完成 |
| 节点不上传 | 不向第三方服务器泄露节点 |
| 自有节点 | 支持把自建节点一并管理 |

## 相关概念

- [shadowrocket-config](./tool-shadowrocket-config.md) — 防 DNS 泄露的 Shadowrocket 配置
- [sub-store-cloudflare](./tool-sub-store-cloudflare.md) — Cloudflare Workers 上的订阅聚合工具
- [ClashOmega](./tool-clash-omega.md) — Clash 规则管理 Chrome 扩展