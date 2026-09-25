---
type: "Tool"
title: "djev-run（DiffusionGemma-Jev 的 Cloud Run 一键部署脚本）"
description: "把 DiffusionGemma-Jev 模型打包成 Cloud Run 部署脚本，单张 RTX PRO 6000 上冷启动 47.5 秒内同时跑起 TypeSafe AI 兼容接口与三个浏览器小游戏。"
resource: "https://github.com/taeold/djev-run"
tags: "[cloud-run, diffusion, gemma, jev, typesafe, gpu, deploy, open-source]"
timestamp: "2026-09-25T15:55:00Z"
---

# djev-run（DiffusionGemma-Jev 的 Cloud Run 一键部署脚本）

## 它是什么

[djev-run](https://github.com/taeold/djev-run) 是把 [DiffusionGemma-Jev](https://huggingface.co/) 扩散模型打包成的 **Cloud Run 部署脚本**——目标硬件是单张 RTX PRO 6000，部署启动后能在 **47.5 秒冷启动** 内同时：

- 暴露 **TypeSafe AI 兼容**的推理 HTTP 接口（与 Jev / TypeSafe 客户端协议一致）
- 跑起 **三个浏览器可玩的小游戏**（用模型生成画面 + 实时交互）

## 为什么用它 / 适合什么场景

- 想在云端快速拉起一份「**扩散生成 + TypeSafe 推理**」复合服务，但不想自己写 Dockerfile / GPU 配额 / 冷启动优化。
- 做 demo / 内部分发时希望端到端启动时间可控（< 1 分钟），方便临时回收 / 重启。
- 想让一个模型实例既对外提供 API、又承载几个轻量交互示例，验证模型在多负载下的响应。

## 关键能力

| 能力 | 说明 |
|------|------|
| 一键部署 | 单仓库脚本，可直接推到 Cloud Run |
| 硬件目标 | 单张 RTX PRO 6000 |
| 冷启动 | 约 47.5 秒（含镜像拉取 + 模型加载） |
| API 协议 | TypeSafe AI 兼容 HTTP 接口 |
| 内置 Demo | 3 个浏览器可玩小游戏（生成 + 实时交互） |

## 媒体

视频演示：

<https://video.twimg.com/tweet_video/HTBKjc1bwAAqf99.mp4>

## 相关概念

- [laya-server](./tool-laya-server.md) — 把 Laya 的 System One 判定能力装进 Docker，对外暴露 TypeSafe Jev 兼容 HTTP 接口
- [Cloud Run](./tool-cloud-run.md) — Google 托管的无服务器容器运行时（同类部署目标）
