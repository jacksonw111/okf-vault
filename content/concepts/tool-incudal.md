---
type: "Tool"
title: "Incudal（基于 Incus 的 NAT VPS 销售 / 交付面板）"
description: "qwer-xyz/incudal —— 基于 Incus 的 LXC / KVM NAT VPS 销售、交付与管理面板。Vue 3 + Fastify 前后端分离，宿主 Agent 用 Go 写，Docker Compose 一键部署。"
tags: "[vps, incus, lxc, kvm, nat, sales, panel, docker-compose]"
timestamp: "2026-06-22T16:09:00Z"
---

# Incudal（基于 Incus 的 NAT VPS 销售 / 交付面板）

## 它是什么

[`qwer-xyz/incudal`](https://github.com/qwer-xyz/incudal) 是一套**基于 Incus 的 VPS 销售管理系统**，能自动创建和交付 LXC / KVM 实例，支持 NAT 网络。

技术栈：

- **前端**：Vue 3
- **后端**：Fastify
- **宿主机 Agent**：Go
- **部署**：Docker Compose 一键启动

核心功能：

- **实例生命周期管理**：自动创建 / 删除 / 启停 LXC / KVM 实例
- **NAT 网络支持**：适合 IPv4 紧缺场景（NAT VPS 业务）
- **用户后台**：客户自助查实例 / 重启 / 重装
- **管理后台**：管理员审核 / 工单 / 套餐配置
- **套餐镜像管理**：维护可售卖的 OS 镜像库
- **余额充值**：账户余额系统
- **VIP 等级**：差异化服务
- **工单系统**：用户问题跟进

## 为什么用它 / 适合什么场景

- **NAT VPS 业务**：针对 IPv4 紧缺场景，NAT 出口 + 端口映射是核心。
- **小型 VPS 服务商**：自己跑一套，开卖 NAT VPS，无需付费商业面板（如 SolusVM）。
- **Incus 生态**：相比 LXD，Incus 是社区维护的活跃分支，长期更稳。
- **学习 / 内部用**：把 Incus 集群抽象成「可售卖资源」做 PoC。

适合：

- 小型 NAT VPS 服务商
- 想 DIY VPS 销售面板的运维
- 在 Incus 上做「资源池化」研究的工程师

## 关键能力

| 能力 | 说明 |
|---|---|
| Incus 集成 | 基于 Incus 集群 |
| LXC / KVM | 同时支持容器与虚拟机 |
| NAT 网络 | 端口映射 + 共享 IPv4 |
| 销售面板 | 套餐 / 余额 / VIP |
| 用户后台 | 自助操作实例 |
| 工单系统 | 客户支持 |
| Docker Compose | 一键部署 |

## 工作流

```
客户下单  ──→  分配余额  ──→  选套餐 / 镜像  ──→  Agent 创建 Incus 实例
                  │                                    │
                  └──→  管理员后台审核 / VIP 处理  ────┘
                                                      │
                                              NAT 端口映射 + 资源隔离
```

## 与商业面板对比

| 维度 | SolusVM / Virtualizor 等商业面板 | Incudal |
|---|---|---|
| 授权费 | 商业付费 | **开源免费** |
| 后端 | 闭源 | Fastify + Go Agent |
| 生态 | 成熟 | 早期但活跃 |
| NAT 支持 | 需插件 | **原生** |

## 参考链接

- [项目链接](https://github.com/qwer-xyz/incudal)

## 相关概念

- [Single Server](tool-single-server.md) — 一台 Linux 服务器串 Cloudflare + Tailscale + Kamal 一键部署
- [OPG](tool-opg-backend.md) — 一人公司多 app 后端控制面（账号 / AI 网关 / 视频 / 支付）
- [3X-UI](tool-3x-ui.md) — Xray 图形面板（同样针对自托管场景）