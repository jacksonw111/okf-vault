---
type: "Tool"
title: "Piped"
description: "开源的 YouTube 替代前端——无广告、免登录、可后台播放、可自部署；通过代理 Invidious / 直接抓 YouTube 公开数据，提供隐私友好的视频观看 API，与 Invidious 同类。"
resource: "https://github.com/TeamPiped/Piped"
tags: "[piped, youtube, alternative, frontend, privacy, self-hosted]"
timestamp: "2026-10-06T22:51:00Z"
---

# Piped

## 定义

**Piped** 是一个开源的 YouTube 替代前端，目标与 [`Invidious`](tool-invidious.md) 类似——无广告、免登录、可后台播放、不向 Google 上报用户行为。它通过代理 YouTube 公开数据或借助 Invidious 实例提供视频流，让用户在不安装 YouTube 客户端的情况下观看视频，且可以自部署。

## 要点

- **仓库**：`https://github.com/TeamPiped/Piped`
- **能力**：无广告、免登录、后台播放、音频模式、订阅同步（通过 Invidious / NewPipe 协议）
- **API**：对外提供公开 REST API，便于第三方客户端（Piped-Frontend、LibreTube 等）调用
- **隐私**：不向 Google 暴露观看历史
- **部署**：Java + Quarkus 后端，可单机也可集群

## 相关概念

- [Invidious](./tool-invidious.md) — 同类项目，常配合使用
- [Self-Hosted（自托管）](./term-self-hosted.md) — 部署形态
