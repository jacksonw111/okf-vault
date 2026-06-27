---
type: "Tool"
title: "Floci（轻量免费的本地 AWS 模拟器）"
description: "LocalStack 的免费开源替代品，目标是「轻量、蓬松、永远免费」的本地 AWS 模拟器，适合开发 / CI / 离线测试；与 LocalStack 接口兼容，可无缝迁移。"
tags: "[aws, localstack, devops, testing, ci, self-hosted]"
timestamp: "2026-06-27T15:46:00.000Z"
resource: "https://github.com/floci-io/floci"
---

# Floci（轻量免费的本地 AWS 模拟器）

## 它是什么

[`Floci`](https://github.com/floci-io/floci) 是 **LocalStack 的免费开源替代品**，目标是做一个「轻量、蓬松、永远免费」的**本地 AWS 模拟器**。它瞄准开发、CI、离线测试三大场景，**接口与 LocalStack 兼容**——用过 LocalStack 的可以直接迁移过来。

## 关键能力

| 能力 | 说明 |
|------|------|
| 本地 AWS 模拟 | 把 AWS 服务在本地跑起来 |
| LocalStack 兼容 | 接口对齐，可平滑迁移 |
| 轻量 | 启动快、资源占用低 |
| 永远免费 | 不收费、无功能阉割 |
| 场景适配 | 开发 / CI / 离线测试三类常见用法 |

## 适用场景

- 不想花钱订阅 LocalStack Pro 又想要核心能力
- CI 流水线里需要轻量、可复现的 AWS 测试环境
- 离线 / 内网环境开发，调用不了真实 AWS
- 学习 AWS 时想本地反复试验不烧钱

## 参考链接

- [项目链接](https://github.com/floci-io/floci)

## 相关概念

- [Single Server](tool-single-server.md) — 一台 Linux 服务器串 Cloudflare / Tailscale / Kamal 一键部署
- [llmaker](tool-llmaker.md) — 类似「一条命令拉起整套应用栈」思路的 LLM 编排工具