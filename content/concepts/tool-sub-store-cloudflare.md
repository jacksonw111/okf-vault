---
type: Tool
title: "sub-store-cloudflare"
description: "Cloudflare Workers 上部署的订阅聚合与规则配置工具，把订阅源管理、节点处理、分流模板放在云端；同作者 FlareMo / cfnew-deployer 等作品的同类 Cloudflare Worker 部署形态。"
resource: "https://github.com/realchendahuang/sub-store-cloudflare"
tags: "[cloudflare-workers, subscription, proxy, rule-engine]"
timestamp: "2026-07-02T05:00:00Z"
---

# sub-store-cloudflare

## 它是什么
在 Cloudflare Workers 上部署的**订阅聚合与规则配置**工具。把订阅源管理、节点处理、分流模板放在云端。

## 为什么用它 / 适合什么场景
- 想用 Cloudflare 全球边缘节点托管自己的订阅聚合服务，零服务器运维。
- 想把多个机场 / 自建节点合并到一份订阅里给客户端用。
- 想要云端的分流规则配置（地区、域名、应用级）。

## 关键能力
| 能力 | 说明 |
|------|------|
| 部署平台 | Cloudflare Workers（无服务器） |
| 订阅源管理 | 多订阅聚合 |
| 节点处理 | 节点过滤 / 重命名 / 排序 |
| 分流模板 | 规则配置（地区 / 域名 / 应用级） |
| 形态 | Cloudflare Worker 单仓库部署 |

## 相关概念
- [FlareMo](tool-flaremo.md) — 同作者 realchendahuang，Cloudflare Worker 部署的 Flomo 风格时间线笔记
- [cfnew-deployer](tool-cfnew-deployer.md) — 同作者另一 Cloudflare 部署器面板
- [EasySNI](tool-easysni.md) — 单文件 SNI/XRay/域名前置面板，定位相似但部署形态不同（独立二进制）
- [VLESS + WebSocket + TLS 绕过电信 QoS](playbook-vless-bypass-telecom-qos.md) — 自建代理节点端到端教程，sub-store-cloudflare 是订阅分发端

## 项目链接
- 项目主页：<https://github.com/realchendahuang/sub-store-cloudflare>