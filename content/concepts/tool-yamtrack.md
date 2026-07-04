---
type: Tool
title: "Yamtrack"
description: "Yamtrack 是给前 Trakt 用户准备的自托管媒体追踪平台:追电影 / 剧集 / 动画 / 音乐 / 播客,带副本级详情(分辨率/编码/码率)、跨媒体统计、智能列表与个性化推荐,Docker 一键部署。"
resource: "https://github.com/dannyvfilms/Yamtrack"
tags: [yamtrack, trakt, self-hosted, media-tracker, docker]
timestamp: "2026-07-04T15:00:00Z"
---

# Yamtrack

## 它是什么

Yamtrack(`dannyvfilms/Yamtrack`)是 Trakt 的开源自托管替代品。它不仅能做「电影 / 剧集 / 动漫」的播放历史统计,还把音乐、播客、收藏(数字版与实体版)纳入同一个时间线;追踪细节深入到副本级别 — 一部电影是 4K HDR 还是 1080p REMUX、用 H.264 还是 HEVC、平均码率多少,都能完整记录。

![截图](https://pbs.twimg.com/media/HMRwMJRagAA_-is.jpg)

项目链接：<https://github.com/dannyvfilms/Yamtrack>

## 为什么用它 / 适合什么场景

- **Trakt 升级 / 迁移工具**:Trakt 服务不稳、收费困惑、或单纯想数据归自己。
- **跨媒体统一面板**:不只是影视,加音乐 / 播客后能看出「我这周在 Netflix 看了 5 部剧、Spotify 听了 30 小时播客、AO3 读了 4 篇文」这种聚合数据。
- **本地收藏细节管理**:NAS / 硬盘里 1000 多部电影,每部的分辨率 / 编码 / 码率 / 是否国语音轨都能登记,生成可筛选面板。

## 关键能力

| 能力 | 说明 |
|------|------|
| 媒体追踪 | 电影 / 剧集 / 动漫(含单集进度)/ 音乐 / 播客 |
| 收藏管理 | 副本级详情:分辨率、编码、码率、音频语言、字幕都记 |
| 历史与统计 | 跨媒体类型深度分析,支持筛选、对比模式 |
| 智能列表 | 按规则自动生成自定义列表 |
| 个性化推荐 | 基于历史看未看的 |
| 一键集成 | Plex 同步、Last.fm 导入、Audiobookshelf 同步 |
| 自部署 | Docker 一键;SQLite 或 PostgreSQL 都能跑 |

## 部署形态

```bash
# 一般方式
docker compose up -d
```

— 数据库默认 SQLite,需要换成 PostgreSQL 在环境变量里改 `DATABASE_URL`。

## 相关概念

- [Plex TUI](tool-plex-tui.md) — Python 写的终端 Plex 客户端,跟 Yamtrack 的 Plex 同步互为补充
- [Cinema Manager](tool-cinema-manager.md) — 找片 Skill,多源搜索 + 质量评分 + 转存 + 整理成 Infuse/Plex/Jellyfin
- [Single Server](tool-single-server.md) — Yamtrack 可以挂在这种统一部署栈里
- [Yamtrack 仓库](https://github.com/dannyvfilms/Yamtrack) — 项目链接
