---
type: Tool
title: "xdp-dns-evadeproxy"
description: "DNS 代理：当运营商整段封锁 anycast IP 时，在 DNS 响应中把被封锁的 Cloudflare IP 悄悄替换成同一前缀中未封锁的邻居 IP，让服务照常可达。"
resource: "https://github.com/Oihalitz/xdp-dns-evadeproxy"
tags: [dns, proxy, xdp, censorship-circumvention, cloudflare, anycast]
timestamp: 2026-09-02T12:00:00Z
---

# xdp-dns-evadeproxy

## 它是什么

当 ISP / 运营商对 Cloudflare 等 anycast IP 整段封锁时，传统代理方案都失效。`xdp-dns-evadeproxy` 的解法是工作在 DNS 解析层：在 DNS 响应中将"被封锁 IP"悄悄替换成同前缀里"未封锁的邻居 IP"，让上层 TCP 连接握手仍能落在一个可达的同前缀节点上。代理本身基于 XDP（在网卡驱动层 hook），性能开销低、绕过封锁粒度细。

## 关键能力

| 能力 | 说明 |
|------|------|
| DNS 层透明替换 | 把被封锁 IP 改成同前缀未封锁的邻居 IP |
| XDP 高速路径 | 在网卡驱动层 hook，性能开销极低 |
| anycast 友好 | 解决 anycast IP 整段封锁问题 |

## 项目链接

- [项目主页](https://github.com/Oihalitz/xdp-dns-evadeproxy)

## 相关概念

- [3x-ui](./tool-3x-ui.md) — 另一种代理面板形态
