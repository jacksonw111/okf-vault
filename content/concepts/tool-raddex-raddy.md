---
type: Tool
title: "Raddy / Raddex（按书写顺序执行的 Pingora 反向代理）"
description: "Raddy 用一份按书写顺序执行的 Raddyfile 配置，基于 Cloudflare Pingora 提供 HTTP/HTTPS 反代、自动 HTTPS 证书、静态文件托管、负载均衡与 TCP/UDP 四层转发，避免手写 Pingora 原生代码或依赖隐式排序的配置模型。"
resource: "https://github.com/chulingera2025/raddex"
tags: [cloudflare, pingora, reverse-proxy, http, tcp, udp, load-balancer]
timestamp: "2026-09-03T00:00:00Z"
---

# Raddy / Raddex（按书写顺序执行的 Pingora 反向代理）

## 它是什么

[Raddy / Raddex](https://github.com/chulingera2025/raddex) 用一份**按书写顺序执行**的 Raddyfile 配置，**基于 Cloudflare Pingora** 提供：

- HTTP/HTTPS 反向代理
- 自动 HTTPS 证书
- 静态文件托管
- 负载均衡
- TCP/UDP 四层转发

设计上避免两件事：
1. **手写 Pingora 原生代码**；
2. **依赖隐式排序**的配置模型（你写啥就按啥顺序跑）。

## 为什么用它 / 适合什么场景

- 想用 Cloudflare Pingora 的高性能代理但不想写 Rust；
- 用过 Nginx 但配置隐式 / 难调，希望按书写顺序直白生效；
- 需要四层（TCP/UDP）+ 七层（HTTP/HTTPS）混部；
- 想自动 HTTPS 证书管理 + 静态文件 + 负载均衡一次配齐。

## 关键能力

| 能力 | 说明 |
|------|------|
| Pingora 内核 | Cloudflare 出品的高性能代理 |
| Raddyfile | 按书写顺序执行的配置文件 |
| HTTP/HTTPS | 反向代理 + 自动 HTTPS 证书 |
| 四层 | TCP/UDP 转发 |
| 七层 | 反代 + 静态文件 + 负载均衡 |

## 参考链接

- 项目链接：<https://github.com/chulingera2025/raddex>
- 原始推文：<https://x.com/QingQ77/status/2095362901011747045>
- 媒体：<https://pbs.twimg.com/media/HRLiSv3aUAAYjbG.jpg>

## 相关概念

- [Mihari Proxy CLI](./tool-mihari-proxy-cli.md) — 终端管 mihomo 内核的订阅 / 系统代理 / TUN / Web 面板
- [Lucky](./tool-lucky.md) — DDNS+ACME+反代瑞士军刀
