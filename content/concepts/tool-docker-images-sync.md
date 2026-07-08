---
type: "Tool"
title: "docker_images_sync（GitHub Actions 白嫖同步海外 Docker 镜像）"
description: "借助 GitHub Actions 的免费算力，把海外 Docker 镜像同步到国内可访问的镜像源（ghcr / Docker Hub 等），无需自购海外服务器、无需魔法上网、无拉取配额限制。"
resource: "https://github.com/you8023/docker_images_sync"
tags: "[docker, github-actions, mirror, registry, china-network, ci]"
timestamp: "2026-07-08T16:50:00Z"
---

# docker_images_sync

## 它是什么

[docker_images_sync](https://github.com/you8023/docker_images_sync) 是一个**借力 GitHub Actions 免费 CI 算力**来同步海外 Docker 镜像的开源项目。

在国内拉不动官方 Docker Hub / ghcr 镜像时，把上游镜像**自动同步**到自己可控的镜像仓库里，国内服务器再从这个镜像仓库拉——**零成本、零魔法、零配额**。

## 解决什么问题

| 痛点 | docker_images_sync 的解法 |
|------|---------------------------|
| 国内拉不动 Docker 官方镜像 | 用 GitHub Actions 在海外节点拉镜像 → 推到国内可达的镜像仓库 |
| 买海外机器要钱 | 用 GitHub Actions 免费额度当「免费的海外拉取器」 |
| 自建代理要挂梯子 | 全程走 GitHub Actions，不需要本地魔法 |
| 镜像源有拉取配额 | 自己账号 / 自己的镜像仓库，无外部限额 |
| 维护成本 | 丢进 GitHub Workflow，纯托管 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 纯白嫖 | 利用 GitHub Actions 免费额度，零服务器成本 |
| 免魔法 | 不需要本地代理 / 梯子 |
| 无限制 | 没有第三方镜像源的拉取配额 |
| 全自动 | 配置好仓库后，Workflow 自动同步 |
| 即开即用 | fork 仓库改配置即可运行 |

## 媒体

![docker_images_sync 流程示意](https://pbs.twimg.com/media/HMtA6NkbQAAjnov.jpg)

## 参考链接

- [项目仓库](https://github.com/you8023/docker_images_sync)

## 相关概念

- [Cloudflare Workers Cache](./tool-cloudflare-workers-cache.md) — 同为「免服务器成本」的网络 / 边缘玩法
- [DD JIT Container](./tool-dd-jit-container.md) — 同为 Docker 容器生态相关工具