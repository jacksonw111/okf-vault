---
type: "Tool"
title: "EdgeMirror（边缘镜像网关）"
description: "跑在 Cloudflare Workers / Vercel 上的单域名边缘镜像网关，把 PyPI / PyTorch / Hugging Face / GitHub / Docker / npm / Go / Maven / crates 等开发者源统一加速到一个干净域名下。"
resource: "https://github.com/tianrking/EdgeMirror"
tags: "[edge, mirror, cdn, python, npm, docker, github]"
timestamp: "2026-07-20T20:20:00Z"
---

# EdgeMirror（边缘镜像网关）

## 它是什么

[tianrking/EdgeMirror](https://github.com/tianrking/EdgeMirror) 是部署在 **Cloudflare Workers / Vercel** 之上的**单域名边缘镜像网关**——把 PyPI、PyTorch、Hugging Face、GitHub、Docker、npm、Go、Maven、crates 等开发者源统一映射到一个干净的自有域名下，企业 / 个人做开发环境加速用。

## 关键能力

| 能力 | 说明 |
|------|------|
| 边缘部署 | 跑在 Cloudflare Workers / Vercel，天然 CDN 加速 |
| 多源统一 | 一份配置覆盖 9+ 主流开发源 |
| 单一域名 | 把多源合到同一个自有域名下，免去逐个配 / 各记各的 mirror |
| 零运维 | Serverless，按流量计费，零服务器维护 |

## 支持的开发源

PyPI / PyTorch / Hugging Face / GitHub / Docker / npm / Go / Maven / crates（*总 9 类*）

## 相关概念

- [Docker Images Sync](./tool-docker-images-sync.md) — 用 GitHub Actions 把海外 Docker 镜像同步到国内可达源
- [VLESS Bypass Telecom QoS](./playbook-vless-bypass-telecom-qos.md) — 网络加速参考手册

## 参考链接

- 项目链接: <https://github.com/tianrking/EdgeMirror>
