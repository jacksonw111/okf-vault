---
type: "Tool"
title: "personal-edge-proxy（个人自建梯子的清晰路由：Hysteria2 + WARP + SOCKS5）"
description: "yding-git 出品的个人自建代理仓库：把「日常 Hysteria2 入口 + AI 流量走 WARP + Claude/Anthropic 单独挂固定 SOCKS5」这套路由思路完整摆出来——1 核 1G 小鸡能跑，明确不保证账号安全。"
resource: "https://github.com/yding-git/personal-edge-proxy"
tags: "[proxy, hysteria2, warp, socks5, self-hosted, edge, ai-routing]"
timestamp: "2026-09-26T21:55:00Z"
---

# personal-edge-proxy（个人自建梯子的清晰路由：Hysteria2 + WARP + SOCKS5）

## 它是什么

[personal-edge-proxy](https://github.com/yding-git/personal-edge-proxy) 是 yding-git 开源的**个人自建代理方案**——把整套**路由思路**完整摆到台面上，不藏着掖着：

1. **日常流量**走 **Hysteria2** 当主入口——图稳
2. **AI 流量**单独走 **WARP** 出口——和廉价 VPS 机房 IP 隔开
3. **Claude / Anthropic** 等不够稳时，再单独挂**固定 SOCKS5** 兜底

## 为什么用它 / 适合什么场景

- 想自己搭代理、但一直被「**哪类流量走哪个出口**」绕晕的人。
- 想把**普通流量**和**AI / Claude 调用**分开走不同出口——降低「廉价 VPS IP 被 AI 服务风控」的机率。
- 拥有 1 核 1G 小鸡，想立刻能跑的低门槛方案。
- 喜欢**作者明说「不保证账号安全，条款得自己守」** 这种不忽悠的细致活儿。

## 关键能力

| 能力 | 说明 |
|------|------|
| 主入口 | Hysteria2（基于 UDP 的 QUIC，抗 QoS） |
| AI 出口 | Cloudflare WARP（独立 IP 段） |
| 兜底 | 固定 SOCKS5（给 Claude / Anthropic 用） |
| 硬件门槛 | 1 核 1G 小鸡即可 |
| 文档 | 写得白话，可直接丢给 AI 跑 |
| 风险说明 | 作者明确不保证账号安全 |

## 媒体

示意图：
- ![](https://pbs.twimg.com/media/HTHj12VbwAArhfD.png)

## 相关概念

- [VLESS + WebSocket + TLS 绕过电信 QoS](./playbook-vless-bypass-telecom-qos.md) — 同为「绕过运营商 QoS / 自建代理」思路的另一份 Playbook
- [Self-Hosted（自托管）](./term-self-hosted.md) — 个人边缘代理 = 自托管的一种