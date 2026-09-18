---
type: Tool
title: "FNext（CFNext，Cloudflare Workers 代理订阅面板）"
description: "部署在 Cloudflare Workers / Pages 上的代理订阅管理面板，单个 JS 文件同时实现 VLESS / Trojan / XHTTP 三种协议，访问 /UUID 进面板、/sub 出订阅，配一次能躺很久。"
resource: "https://github.com/PAICNI/CFNext"
tags: [cloudflare, workers, vless, trojan, xhttp, subscription, proxy, single-file]
timestamp: 2026-09-18T08:35:00Z"
---

# FNext（CFNext，Cloudflare Workers 代理订阅面板）

## 它是什么

[PAICNI/CFNext](https://github.com/PAICNI/CFNext) 是一个**部署在 Cloudflare Workers / Pages 上的代理订阅管理面板**（又称 FNext）。它用**单个 JS 文件**实现 VLESS、Trojan、XHTTP 三种代理协议，访问 `/<UUID>` 进入面板、访问 `/sub` 拿到订阅。

特点：**把 Cloudflare 免费额度用到底**，单文件贴进 Worker 即用，内置 bestcf IP 池加轮询下发，配一次可以躺很久。

## 关键能力

| 能力 | 说明 |
|------|------|
| 三协议合一 | 同一个 Worker 同时支持 VLESS / Trojan / XHTTP |
| 单文件部署 | 整面板就一个 JS 文件，复制即可 |
| 面板 + 订阅 | `/UUID` 进面板管理、`/sub` 出订阅链接 |
| 九种客户端格式 | 自动产出九种常见代理客户端的订阅格式 |
| IP 池 + 轮询 | 内置 bestcf 池并轮询下发 |
| 零服务器成本 | 跑在 Cloudflare 免费额度上 |

## 适合什么场景

- 想用 Cloudflare Workers 自托管一个代理订阅面板、又不想被服务器运维拖住的人。
- 需要 VLESS / Trojan / XHTTP 协议可同时下发、按客户端选择格式的小团队。
- 希望部署一次后长时间稳定运行、不必反复维护 Cloudflare 配置的运维人员。

## 参考

- 项目链接：<https://github.com/PAICNI/CFNext>

![面板截图](https://pbs.twimg.com/media/HSdmhFIaEAApchc.jpg)
