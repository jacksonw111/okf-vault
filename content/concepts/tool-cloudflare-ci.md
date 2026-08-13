---
type: Tool
title: "cloudflare/ci"
description: "Cloudflare 官方维护的开源 CI 引擎——把安装 / 检查 / 部署等流水线步骤直接跑在自家 Workflows 与 Sandbox 运行时上，省掉自建 runner 集群。"
resource: "https://github.com/cloudflare/ci"
tags: "[cloudflare, ci-cd, workflow, sandbox, open-source]"
timestamp: "2026-08-13T19:53:00Z"
---

# cloudflare/ci

## 它是什么
**Cloudflare 官方维护的开源 CI 引擎**。把 CI 流水线（install / check / deploy 等步骤）**直接跑在 Cloudflare 自家的 Workflows 与 Sandbox 运行时上**——不再需要单独运维 runner 集群。

定位上是 Cloudflare 生态的「**自家 CI**」方案：

- 开源（GitHub 上 cloudflare/ci）
- 跑在 Cloudflare 边缘
- 用 Workers / Sandbox / Workflows 这些已有原语当 runtime

## 为什么用它 / 适合什么场景
- 已在 Cloudflare 生态（Workers / Pages / R2 / D1 等）部署——想用同一家基础设施做 CI。
- 不想运维自建 runner（k8s runner fleet / GitHub Actions self-hosted 等）。
- 想从开源而非 SaaS 控制 CI 流水线。
- 对延迟敏感：CI 与生产部署同在 Cloudflare 边缘。

## 关键能力
| 能力 | 说明 |
|------|------|
| 维护方 | Cloudflare 官方 |
| 形态 | 开源 CI 引擎 |
| 运行时 | Cloudflare Workflows + Sandbox |
| 覆盖步骤 | install / check / deploy 等 |
| 替代对象 | 自建 runner 集群 / 第三方 SaaS CI |
| 部署位置 | Cloudflare 边缘 |

## 相关概念
- [Cloudflare Workers](tool-cloudflare-workers.md) — 同生态；cloudflare/ci 跑在 Workers 上
- [Apollo (ESP32 语音助手)](tool-apollo-esp32-voice.md) — 同样基于 Cloudflare Workers / 边缘能力

## 项目链接
- 项目主页：<https://github.com/cloudflare/ci>