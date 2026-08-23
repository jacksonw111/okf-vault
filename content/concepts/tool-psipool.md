---
type: Tool
title: "psipool（终端多地区 Psiphon 代理池管理工具）"
description: "在终端里一键管理多地区 Psiphon 代理池，每个国家一条隧道，各自提供 SOCKS5 和 HTTP 本地端口"
resource: "https://github.com/xHossein/psipool"
tags: [psiphon, proxy-pool, terminal, socks5, http-proxy]
timestamp: "2026-08-23T14:23:00Z"
---

# psipool（终端多地区 Psiphon 代理池管理工具）

## 它是什么

[xHossein/psipool](https://github.com/xHossein/psipool) 是一个**终端**工具，让你**一键管理多地区 Psiphon 代理池**：每个国家一条隧道，各自提供 **SOCKS5 和 HTTP 本地端口**，按需启动 / 关闭。

适合需要按国家切换出口 IP 的抓取 / 测试 / 跨境访问场景。

## 为什么用它 / 适合什么场景

- 想在终端里管多国 Psiphon 隧道，不想每个国家手动起一个进程。
- 抓取 / 测试 / 跨境访问需要按国家切换 IP。
- 想用 SOCKS5 / HTTP 端口方便本地工具链（curl、Playwright、Python requests）接入。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多地区代理池 | 一条命令起多个国家隧道 |
| SOCKS5 + HTTP 双端口 | 兼容本地工具链 |
| 终端管理 | CLI 操作，无需图形界面 |
| 按需启停 | 不需要的国家不开隧道 |

## 媒体

- 视频：<https://video.twimg.com/tweet_video/HQYDvCzaQAAtIW-.mp4>

## 相关概念

- [sub-store-cloudflare](./tool-sub-store-cloudflare.md) — 订阅聚合与规则配置
- [ClashOmega](./tool-clash-omega.md) — 代理规则管理 Chrome 扩展

## 参考链接

- [项目链接](https://github.com/xHossein/psipool)
