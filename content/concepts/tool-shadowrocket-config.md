---
type: Tool
title: "shadowrocket-config（防 DNS 泄露配置）"
description: "基于 ACL4SSR 规则集的 Shadowrocket 配置文件：国内 UDP（阿里/腾讯）+ 境外 DoH（Cloudflare/Google）四路并发 DNS，附 URL 重写 / IPv6 禁用 / DNS rebinding 防护，并生成 v2rayN (Xray-core) 兼容 JSON 路由规则。"
resource: "https://github.com/DuskWander87/shadowrocket-config"
tags: [shadowrocket, proxy, dns, acl4ssr, anti-leak]
timestamp: "2026-06-25T00:06:00Z"
---

# shadowrocket-config（防 DNS 泄露配置）

## 它是什么

基于 **ACL4SSR 规则集**的 Shadowrocket 配置文件，目标是**防止 DNS 泄露**，同时兼顾「**国内直连 / 境外代理分流**」的稳定调度。

## 核心方案：四路并发 DNS

| 路线 | 协议 | 用途 |
|------|------|------|
| 国内 1 | UDP | 阿里 DNS——保 CDN 调度精度 |
| 国内 2 | UDP | 腾讯 DNS——保 CDN 调度精度 |
| 境外 1 | DoH | Cloudflare——加密防污染 |
| 境外 2 | DoH | Google——加密防污染 |

思路：

- **国内走 UDP**——UDP 解析延迟低，CDN 调度精准（同一域名返回最近的 CDN 节点）。
- **境外走 DoH**——加密通道防污染，避免被 GFW 注入假 IP（这是 DNS 泄露的常见源头）。

## 附带硬化

| 措施 | 作用 |
|------|------|
| URL 重写 | 抹掉泄露 query string |
| IPv6 禁用 | 防止 IPv6 走代理外导致泄露 |
| DNS rebinding 防护 | 拦下内网 IP 解析结果 |

## 多端兼容

同一份规则源同时生成 **Shadowrocket** 与 **v2rayN (Xray-core)** 兼容的路由规则 JSON（含 QUIC 阻断）。

## 相关概念

- [ClashOmega](./tool-clash-omega.md) — Clash 代理规则管理 Chrome 扩展；shadowrocket-config 是 iOS/macOS 端的规则源
- [3X-UI](./tool-3x-ui.md) — Xray 图形面板；shadowrocket-config 也为其生成兼容 JSON
- [EasySNI](./tool-easysni.md) — SNI 隧道 / XRay 单二进制面板，与 shadowrocket-config 共用 Xray-core 生态
- [HypoMux](./tool-hypomux.md) — Windows 多网卡带宽聚合下载加速；与 shadowrocket-config 的「分流」思路互补
- [VLESS + WebSocket + TLS 绕过电信 QoS](./playbook-vless-bypass-telecom-qos.md) — 同样围绕代理 / 隧道做文章