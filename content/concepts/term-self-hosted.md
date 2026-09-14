---
type: "Term"
title: "Self-Hosted（自托管）"
description: "把服务部署在自己控制的硬件 / 服务器 / 云账户上，而不是用 SaaS 公有云。优势是数据可控、长期成本低、可深度定制；代价是运维负担。"
tags: "[self-hosted, on-prem, saas, devops, open-source]"
timestamp: "2026-09-14T22:30:00Z"
---

# Self-Hosted（自托管）

## 它是什么

**自托管（Self-Hosted）** 指把软件部署在自己控制的硬件、服务器或私有云账户上，而不是订阅 SaaS 公有云服务。绝大多数自托管项目基于开源 + Docker / Docker Compose / Kubernetes，可在一台小型 VPS、家庭实验室甚至树莓派上跑起来。

## 为什么自托管

| 收益 | 说明 |
|------|------|
| 数据可控 | 用户数据在自己的机器上，不上传给第三方 |
| 长期成本 | 一次性硬件 + 电费 vs SaaS 按月续费 |
| 可深度定制 | 改源码 / 加插件 / 调参数不被厂商限制 |
| 隐私 / 合规 | 金融 / 医疗 / 政企场景往往必须自托管 |
| 抗供应商绑定 | SaaS 厂商改价 / 倒闭 / 改条款时不被卡住 |

## 代价

- **运维**：备份、升级、安全补丁、证书续期都得自己盯。
- **学习曲线**：Docker / 反向代理 / DNS / 备份策略都要懂。
- **可靠性**：单机部署可能因为硬件故障宕机。
- **SLA**：没有厂商的 SLA，自己就是 SRE。

## 典型自托管项目举例

- **身份认证**：authentik / Keycloak
- **邮件**：MillionSend / Stalwart
- **网盘 / 备份**：Nextcloud / Synology Hyper Backup / Immich
- **智能家居**：Home Assistant
- **媒体**：Jellyfin / Plex
- **AI / Agent**：Pi Coding Agent / Ollama / Open WebUI
- **VPN / 网络**：3X-UI / AdGuard Home

## 相关概念

- [authentik（开源身份认证平台）](./tool-authentik.md) — 自托管 SSO / 身份认证代表项目
- [Harness Engineering](./term-harness-engineering.md) — 自托管场景下 agent / 工具的运行环境治理

## 参考链接

- awesome-selfhosted：<https://github.com/awesome-selfhosted/awesome-selfhosted>
