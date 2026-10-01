---
type: Tool
title: "tunnl.gg（自部署 SSH 反向隧道 + 自动 HTTPS 子域名）"
description: "klipitkas 开源的自部署 SSH 隧道服务：客户端一行 SSH 反向隧道命令就能把本地端口暴露到公网，服务端自动分配子域名、签发通配符 HTTPS 证书、提供实时请求日志——比 ngrok 免费版少绕几圈。"
resource: "https://github.com/klipitkas/tunnl.gg"
tags: [ssh, tunnel, reverse-proxy, https, self-hosted, dev-tooling]
timestamp: 2026-10-01T05:16:00Z
---

# tunnl.gg

## 它是什么

**tunnl.gg** 是 [klipitkas](https://github.com/klipitkas) 开源的**自部署 SSH 反向隧道**方案：客户端用一条 SSH 反向隧道命令把本地端口暴露到公网，**服务端自动**：

- 分配子域名
- 签发 HTTPS（通配符证书）
- 提供实时请求日志

定位类似 **ngrok** 的自托管替代，但底层用 SSH 而不是 ngrok 私有协议，安装与服务端维护更轻量。宣传点：「比 ngrok 免费版少绕几圈」。

## 为什么用它 / 适合什么场景

- 本地开发服务希望临时公网可访问（Webhook 调试、远程 demo、移动端测试）。
- 不希望被 ngrok 免费版的限速 / 域名占用 / 流量上限卡住。
- 想自己掌握流量路径与日志，避开第三方中转。
- 已有一台固定公网 VPS / 服务器，想跑一个稳定隧道服务。

## 关键能力

| 能力 | 说明 |
|------|------|
| 隧道方式 | SSH 反向隧道 |
| 客户端 | 一行命令（ssh -R） |
| 服务端 | 自托管（Docker / 二进制） |
| HTTPS | 自动签发通配符证书 |
| 子域名 | 自动分配 |
| 日志 | 实时请求日志 |
| 对比 | 替代 ngrok 免费版 |

## 参考链接

- 仓库：<https://github.com/klipitkas/tunnl.gg>

## 媒体

- ![](https://pbs.twimg.com/media/HTc1iMRasAAAFWs.jpg)

## 相关概念

- [Cloudflared](https://github.com/cloudflare/cloudflared) — Cloudflare Tunnel 官方客户端，同类「暴露本地」思路
- [frp](https://github.com/fatedier/frp) — 内网穿透老牌自托管工具
