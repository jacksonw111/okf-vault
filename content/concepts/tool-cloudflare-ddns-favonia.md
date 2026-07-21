---
type: Tool
title: "cloudflare-ddns（favonia 实现的 Cloudflare DDNS）"
description: "Cloudflare DDNS 守护进程：定期检测本机公网 IP，自动调用 Cloudflare API 更新 DNS 记录，让无固定公网 IP 的家用 / 自建服务器始终能用域名访问。"
resource: "https://github.com/favonia/cloudflare-ddns"
tags: [cloudflare, ddns, dns, self-hosted, networking]
timestamp: "2026-07-21T08:57:00Z"
---

# cloudflare-ddns（favonia 实现的 Cloudflare DDNS）

## 它是什么
[cloudflare-ddns](https://github.com/favonia/cloudflare-ddns) 是一款由 favonia 实现的 DDNS 守护进程：家里或自建服务器没有固定公网 IP 时，DNS 记录会随 IP 变化失效。这个工具 **定期检测本机公网 IP → 自动调用 Cloudflare API 更新对应 DNS 记录**，让你始终能用一个稳定域名访问自己的机器。

## 为什么用它 / 适合什么场景
- 自托管服务跑在家里 / VPS 上，公网 IP 是动态的。
- 已经把域名 NS 托管在 Cloudflare，希望由 Cloudflare 一家处理 DNS + 证书 + DDNS。
- 想要一个 **可审计、可脚本化** 的 DDNS 替代品，而不是路由器厂家的闭源固件功能。

## 关键能力
| 能力 | 说明 |
|------|------|
| 自动检测公网 IP | 定期探测，避免 IP 变化导致域名失联 |
| Cloudflare API | 直接更新 A / AAAA 记录 |
| 守护进程形态 | 后台常驻，无需手动干预 |
| 与 Cloudflare 生态贴合 | DNS / 证书 / 反代都可一并用 Cloudflare |
| 开源 | 自托管 / 可审计 |

## 相关概念
- [Lucky](tool-lucky.md) — DDNS + ACME + 反代瑞士军刀（更全的家用网关工具集）
- [EdgeMirror](tool-edge-mirror.md) — Cloudflare Workers 单域名边缘镜像网关（同生态）
- [Vortex](tool-vortex-vps.md) — 终端里的 VPS 管理工具（同为云端运维链）

## 参考链接
- 项目链接: <https://github.com/favonia/cloudflare-ddns>
