---
type: "Tool"
title: "EasySNI（SNI / XRay / 域名前置单文件面板）"
description: "macan-dev/EasySNI —— Go 写的单文件本地网页面板，集成 SNI 隧道、XRay/sing-box 核心、域名前置代理、配置管理、扫描器和 Google 隧道。"
tags: "[proxy, sni, xray, sing-box, domain-fronting, tunnel, go]"
timestamp: "2026-06-22T16:05:00Z"
---

# EasySNI（SNI / XRay / 域名前置单文件面板）

## 它是什么

[`macan-dev/EasySNI`](https://github.com/macan-dev/EasySNI) 是一套**Go 写的单文件本地网页面板**，把一整套代理工具栈装进一个二进制：

- **SNI 隧道**
- **XRay / sing-box 核心**
- **域名前置代理**
- **配置管理**
- **扫描器**
- **Google 隧道**

> 截图：![](https://pbs.twimg.com/media/HLTvJcCaUAA4rf6.jpg)

## 为什么用它 / 适合什么场景

- **单文件部署**：一个 Go 二进制就启动整套面板，免去 docker-compose / 依赖安装。
- **多协议集成**：SNI / XRay / sing-box / 域名前置 / Google 隧道在同一 UI 配置切换。
- **扫描器内置**：可主动扫描可用节点 / 端口。
- **Google 隧道**：把 Google 域名当 CDN 中转，针对特定审查环境有效。

适合：

- 折腾代理栈的**重度用户**
- 想在路由器 / NAS / 单 VPS 上**一键起面板**的运维
- 对「单文件 Go 二进制」有偏好的极简部署爱好者

## 关键能力

| 能力 | 说明 |
|---|---|
| 单文件部署 | 一个 Go 二进制启动整套面板 |
| SNI 隧道 | SNI 协议级流量伪装 |
| XRay 核心 | 多协议（VLESS / Trojan / VMess 等） |
| sing-box 核心 | 新一代通用代理平台 |
| 域名前置 | 流量伪装成访问 CDN 域名 |
| 配置管理 | 可视化编辑配置 |
| 扫描器 | 主动扫描可用节点 / 端口 |
| Google 隧道 | 利用 Google 域名做 CDN 中转 |

## 与同类工具的差异

| 维度 | 3X-UI | EasySNI |
|---|---|---|
| 形态 | Web 面板（容器 / 二进制） | **单文件** Go 二进制 |
| 协议核心 | Xray | XRay + sing-box 双核心 |
| 隧道方式 | VLESS / Trojan | + SNI 隧道 + 域名前置 + Google 隧道 |
| 扫描 | 无 | 内置扫描器 |

## 参考链接

- [项目链接](https://github.com/macan-dev/EasySNI)

## 相关概念

- [3X-UI](tool-3x-ui.md) — Xray 图形面板（同属代理栈面板范畴）
- [Lucky](tool-lucky.md) — DDNS + ACME + 反代瑞士军刀（常配合代理栈做端口转发）
- [VLESS + WebSocket + TLS 绕过电信 QoS](playbook-vless-bypass-telecom-qos.md) — 3X-UI + Lucky 端到端绕过 QoS 的 Playbook