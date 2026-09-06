---
type: Tool
title: "usque-custom-pro"
description: "基于 Cloudflare WARP / MASQUE 的可视化配置工具，支持 Cloudflare Pages 与 Workers 双部署；打开页面注册、生成密钥，一键导出 Clash / Mihomo / Shadowrocket / sing-box / 本地 VLESS 桥接配置。"
resource: "https://github.com/KJGX66F/usque-custom-pro"
tags: [warp, masque, cloudflare, proxy-config, clash, sing-box]
timestamp: "2026-09-06T00:00:00Z"
---

# usque-custom-pro

## 它是什么

[KJGX66F/usque-custom-pro](https://github.com/KJGX66F/usque-custom-pro) 是**基于 Cloudflare WARP / MASQUE 的可视化配置工具**，支持 **Cloudflare Pages 与 Workers 双部署**。

定位：

- **零门槛 WARP 配置**：打开页面就能注册、生成密钥，`config.json` 存好以后直接导入复用。
- **多客户端输出**：节点数 1～500 任意指定，QUIC / H2 都支持，一键吐出 Clash / Mihomo / Shadowrocket / sing-box 与本地 VLESS 桥接的配置。

## 为什么用它 / 适合什么场景

- 想用 Cloudflare WARP / MASQUE 跑代理，但不想自己研究 `wireproxy`、注册流程、密钥生成。
- 需要把同一份配置分发给多平台客户端（Clash 系、sing-box 系、Shadowrocket 等）。
- 想自己部署一份到 Pages / Workers，给小团队共享节点。

## 关键能力

| 能力 | 说明 |
|------|------|
| 可视化注册 | 打开页面即可注册、生成密钥 |
| 配置持久化 | `config.json` 可保存复用 |
| 双部署 | 支持 Cloudflare Pages 与 Workers |
| 多客户端输出 | Clash / Mihomo / Shadowrocket / sing-box / 本地 VLESS 桥接 |
| 节点数可调 | 1～500 任意 |
| 协议覆盖 | QUIC / H2 都支持 |

## 相关概念

- [3X-UI](./tool-3x-ui.md) — 同样是「把代理配置变可视化」的工具，3X-UI 走 Docker 自托管 + Web 面板
- [Lucky](./tool-lucky.md) — DDNS / 反代 / ACME 瑞士军刀，与 usque-custom-pro 形成「客户端配置 + 公网入口」组合

## 项目链接

- 项目主页：<https://github.com/KJGX66F/usque-custom-pro>
