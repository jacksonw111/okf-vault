---
type: "Term"
title: "Docker Compose"
description: "Docker 官方出品的多容器编排工具——通过一个 `docker-compose.yml` 描述服务 / 网络 / 卷 / 依赖关系，用 `docker compose up` 一键拉起整套应用；是自托管 / 本地开发 / CI 中「单文件部署」的事实标准。"
resource: "https://docs.docker.com/compose/"
tags: "[docker, docker-compose, container, orchestration, self-hosted]"
timestamp: "2026-10-06T22:51:00Z"
---

# Docker Compose

## 定义

**Docker Compose** 是 Docker 官方出品的多容器应用编排工具——通过一份 `docker-compose.yml`（YAML）声明多个 service（每个一个 container）、network、volume、depends_on / healthcheck / env / ports，一行 `docker compose up` 拉起整套应用并保证依赖顺序与重启策略。是**自托管 / 本地开发 / 一次性评测环境**中「单文件部署」的事实标准。

## 要点

- **官方文档**：[docs.docker.com/compose](https://docs.docker.com/compose/)
- **格式**：YAML（`services` / `networks` / `volumes` / `configs` / `secrets`）
- **CLI**：`docker compose up / down / logs / ps / exec / restart / build`
- **典型场景**：本地起 PostgreSQL + Redis + 后端 + 前端；自托管 Immich / Nextcloud / Paperless；CI 中跑集成测试栈
- **生态**：Compose Spec 也被 `podman compose` / `nerdctl` / 部分 Kubernetes 工具支持

## 相关概念

- [Self-Hosted](./term-self-hosted.md) — 部署形态
- [Docker](https://www.docker.com) — 容器运行时
