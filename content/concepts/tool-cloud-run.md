---
type: "Tool"
title: "Google Cloud Run（全托管无服务器容器运行时）"
description: "Google Cloud 旗下的全托管无服务器容器运行时：按请求计费、自动扩缩容、支持任意语言容器；适合「容器化 API + 流量波动大 / 想 0 运维」的部署场景，是 djev-run 等模型服务的常见部署目标。"
resource: "https://cloud.google.com/run"
tags: "[cloud-run, gcp, serverless, container, faas, gpu, deploy]"
timestamp: "2026-09-26T21:50:00Z"
---

# Google Cloud Run（全托管无服务器容器运行时）

## 它是什么

[Google Cloud Run](https://cloud.google.com/run) 是 **Google Cloud** 推出的全托管 **无服务器容器运行时**——把任意容器化 HTTP 服务丢上去，自动处理扩缩容、负载均衡、TLS、版本切换，按请求计费（无请求时不计运行费）。

## 为什么用它 / 适合什么场景

- 容器化 **API / 模型推理服务** 想要「**0 运维、自动伸缩、按用量付费**」，不想长期挂着 VM。
- 流量波动剧烈（白天高峰 / 夜晚低谷）的 API 接口，跑 VM 浪费严重。
- 想做**快速 demo / 临时分发**——推镜像上去，几秒内拿到一个 HTTPS URL。
- 适合与 [djev-run](./tool-djev-run.md) 这类「单仓库 + GPU + 一键部署」的模型服务脚本搭配。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | 全托管无服务器 |
| 触发 | HTTP 请求 |
| 计费 | 按请求 + 计算时间（无流量时无运行费） |
| 自动扩缩 | 0 → N（可设上限） |
| 容器 | 任意语言 / 任意镜像（OCI） |
| GPU | 支持 GPU 实例（如 djev-run 用 RTX PRO 6000） |
| HTTPS | 自动签发与续期证书 |
| 版本切换 | 支持流量灰度 |

## 相关概念

- [djev-run](./tool-djev-run.md) — 用 Cloud Run 一键部署 Jev 兼容模型的脚本
- [laya-server](./tool-laya-server.md) — Laya System One 的 Docker 化 HTTP API（也可部署到 Cloud Run 这类容器运行时）