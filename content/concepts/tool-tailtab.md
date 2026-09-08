---
type: Tool
title: "Tailtab"
description: "浏览器扩展：给每个浏览器 profile 配一个独立 Tailscale 节点，不用系统级 VPN、不用 root，不同 profile 同时挂在不同 tailnet 上，默认只把 tailnet 流量走隧道。"
resource: "https://github.com/Stocist/Tailtab"
tags: [tailscale, browser-extension, vpn, profile, networking]
timestamp: "2026-09-08T00:00:00Z"
---

# Tailtab

## 它是什么
Tailtab 是一款浏览器扩展（按项目说明以浏览器扩展形态发布），为**每一个浏览器 profile 绑定一个独立的 Tailscale 节点**：不同 profile 可以同时挂在不同 tailnet 上，默认只有 tailnet 流量走隧道，普通上网不受影响。

## 为什么用它 / 适合什么场景
- 想在不同浏览器身份下走不同地区 / 不同身份的 Tailscale 出口。
- 不希望装系统级 VPN、不要 root 权限。
- 想在同一个浏览器里多 profile 同时跑多个 tailnet，互不串扰。

## 关键能力
| 能力 | 说明 |
|------|------|
| Profile 独立节点 | 每个 profile 一个 Tailscale 节点 |
| 零系统 VPN | 浏览器扩展即可，不动 OS 网络栈 |
| 多 tailnet 并存 | 同一浏览器多 profile 同时挂在不同 tailnet |
| 流量分轨 | 默认 tailnet 流量走隧道，其余走原网络 |

## 参考
- 原始链接：<https://github.com/Stocist/Tailtab>

## 媒体
- ![](https://pbs.twimg.com/media/HRqIeOmboAAROPI.jpg)

## 相关概念
- [Tailscale](https://tailscale.com/) — mesh VPN 底层
