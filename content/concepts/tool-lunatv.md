---
type: Tool
title: "LunaTV"
description: "MoonTechLab 出的 Docker 一键部署视频网站，配置一个资源地址就能看最新电影 / 解锁会员电视剧，部署在 VPS 上不耗服务器流量。"
resource: "https://github.com/MoonTechLab/LunaTV"
tags: "[iptv, video, docker, self-hosted, movies]"
timestamp: "2026-09-07T13:16:00Z"
---

# LunaTV

## 它是什么
MoonTechLab 出的 Docker 一键部署视频网站项目。给一台 VPS 装好 Docker + docker-compose，把 LunaTV 起来后，配置一个"神秘的资源地址"，就能在网页上看最新电影和"会员"电视剧。流量逻辑：视频流量不消耗自建服务器的带宽。

## 部署步骤
1. VPS 上安装 Docker
2. 用 docker-compose 部署 LunaTV
3. 访问 Web 页面，登录后台
4. 在配置区填入"资源地址"（社区维护的解析源），保存
5. 直接在网页上看视频

## 关键能力
| 能力 | 说明 |
|------|------|
| Docker 一键 | 不需要手装环境 |
| 资源地址可换 | 后台切换解析源 |
| 不耗自建流量 | 视频走外链解析 |
| 简洁 Web UI | 入门零学习成本 |

## 适用场景
- 自建个人影视聚合站点
- VPS 多用途：不只跑代理节点，也跑影音库

## 参考
- 项目链接：<https://github.com/MoonTechLab/LunaTV>

## 相关概念
- [Free-TV/IPTV](tool-free-tv-iptv.md) — 全球免费电视频道 M3U 列表
- [iptv-org](tool-iptv-org.md) — 全球免费 IPTV 直播源大宝库
- [Cinema Manager](tool-cinema-manager.md) — 找片 Skill，多源搜索 + 质量评分 + 自动转存