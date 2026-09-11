---
type: "Tool"
title: "Docker"
description: "开源容器化引擎：把应用与依赖打包进独立、可移植的镜像，让「在我机器上能跑」变成「在任何机器上都能跑」——AI 编码工具与本地服务栈的事实标准底座。"
resource: "https://www.docker.com/"
tags: [docker, container, devops, deployment]
timestamp: "2026-09-11T21:40:00Z"
---

# Docker

## 它是什么

[Docker](https://www.docker.com/) 是开源的**容器化引擎**：把应用及其全部依赖（运行时、库、配置）打包进一个独立的「镜像」，再以轻量级「容器」跑在任何装了 Docker 的机器上。解决了「开发环境能跑、生产环境跑不起来」「本机能跑、同事机器跑不起来」的经典问题。

## 为什么用它 / 适合什么场景

- **环境一致性**：开发 / 测试 / CI / 生产跑同一份镜像，杜绝「我机器上是好的」。
- **轻量级虚拟化**：容器共享宿主机内核，比虚拟机秒级启动、几乎无性能损耗。
- **AI 工具本地部署**：很多 AI 编码 agent、向量库、RAG 服务、自托管网关都用 `docker compose up` 一键启动。
- **本地服务栈**：PostgreSQL / Redis / Nginx / LangChain / Ollama 等任意服务，几行 YAML 即可拉起。
- **隔离实验环境**：临时拉个镜像玩，跑完即丢，不污染主机。

## 关键能力

| 能力 | 说明 |
|------|------|
| 镜像打包 | `Dockerfile` 描述构建步骤，镜像层可缓存复用 |
| 容器运行 | `docker run` 启容器，秒级启动 |
| Compose 编排 | `docker-compose.yml` 一键起多容器服务栈 |
| 镜像仓库 | Docker Hub / GHCR / 自建 Registry 分发镜像 |
| 卷与网络 | 持久化数据、容器间互通、与主机互联 |
| 跨平台 | Linux / macOS / Windows（WSL2）通用 |

## 核心概念速查

| 概念 | 含义 |
|------|------|
| 镜像（Image） | 只读模板，相当于「类」 |
| 容器（Container） | 镜像的运行实例，相当于「对象」 |
| Dockerfile | 描述镜像构建步骤的文本 |
| Compose | 多容器应用的 YAML 编排 |
| Volume | 持久化数据卷 |
| Network | 容器间 / 容器与主机的虚拟网络 |

## 适合谁

- 任何想让代码 / 服务「一次构建、到处跑」的开发者。
- 想本地跑 AI 模型、向量库、RAG 服务的 AI 工程师。
- 维护多服务、想用 Compose 管栈的独立开发者与小团队。

## 参考链接

- 官方网站：<https://www.docker.com/>
- Docker Hub：<https://hub.docker.com/>

## 相关概念

- [super-lan-cache](./tool-super-lan-cache.md) — 基于 Docker 部署的局域网游戏缓存代理
- [docker-android](./tool-docker-android.md) — 把 Android 模拟器 + ADB 打包进 Docker
- [docker-images-sync](./tool-docker-images-sync.md) — Docker 镜像多 Registry 同步工具
- [Enzo（自托管 LLM 网关）](./tool-enzo.md) — docker compose up 一键起 300+ 模型
</content>
</invoke>