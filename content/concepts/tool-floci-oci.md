---
type: Tool
title: "floci-oci（Oracle Cloud Infrastructure 本地模拟器）"
description: "Oracle Cloud 没有官方本地模拟器；floci-oci 用一个 Docker 容器在本地模拟 OCI 服务，让 SDK、CLI 和 Terraform 无需改动即可离线开发测试"
resource: "https://github.com/floci-io/floci-oci"
tags: [oci, oracle-cloud, localstack-alternative, docker, devops]
timestamp: "2026-08-23T15:26:00Z"
---

# floci-oci（Oracle Cloud Infrastructure 本地模拟器）

## 它是什么

[floci-io/floci-oci](https://github.com/floci-io/floci-oci) 是 **Oracle Cloud Infrastructure（OCI）的本地模拟器**——一个 Docker 容器，跑起来后能让 SDK / CLI / Terraform **无需改动**，把请求打到本地容器，模拟真实 OCI 服务。

针对的痛点：Oracle Cloud 没有官方本地模拟器，要测 OCI 集成必须用真实租户和凭证。

## 为什么用它 / 适合什么场景

- 不想为本地开发 / CI 申请真实 OCI 租户、配 IAM、配 VCN。
- CI 流水线里需要"无凭证、可复现"的 OCI 集成测试环境。
- 想在离线 / 内网环境开发 OCI 集成。

## 关键能力

| 能力 | 说明 |
|------|------|
| Docker 单容器 | 一行 `docker run` 起一个本地 OCI |
| SDK / CLI / Terraform 无侵入 | 不需要改业务代码 |
| 离线开发 | 无需真实 OCI 账号 |
| 与 floci 思路一致 | 同组织另一款 AWS 模拟器 Floci 的 OCI 版 |

## 媒体

- ![](https://pbs.twimg.com/media/HQYECc9bEAAY90G.jpg)

## 相关概念

- [Floci](./tool-floci.md) — 同组织的 AWS 本地模拟器（LocalStack 替代），思路同源
- [Single Server](./tool-single-server.md) — 自托管环境部署的同类思路

## 参考链接

- [项目链接](https://github.com/floci-io/floci-oci)
