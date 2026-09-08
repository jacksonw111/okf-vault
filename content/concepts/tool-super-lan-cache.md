---
type: Tool
title: "super-lan-cache"
description: "HDR-Performance 开源的局域网游戏缓存代理容器：把 Steam、Xbox 等多平台游戏的下载缓存引擎与管理界面封装进 Docker，同网段其他机器直接命中缓存、不再走外网。"
resource: "https://github.com/HDR-Performance/super-lan-cache"
tags: [lan-cache, gaming, docker, steam, xbox, network]
timestamp: "2026-09-08T00:00:00Z"
---

# super-lan-cache

## 它是什么
HDR-Performance 开源的**局域网游戏下载缓存代理**：把多个平台（Steam、Xbox 等）的下载缓存引擎连同 Web 管理界面封装进一个 Docker 容器，部署到家里/办公室的一台主机上后，同网段其他机器更新/下载游戏时直接命中这台机器的本地缓存，不再每次都从公网拉一遍。

## 为什么用它 / 适合什么场景
- 家里或小机房多台机器玩同一批游戏，带宽被反复下载吃满。
- 国内/弱网环境下 Steam / Xbox 服务器下载慢，第一次缓存完后后续命中秒完成。
- 想统一管理缓存命中情况，不想每台机都开 Steam 自带的本地缓存。

## 关键能力
| 能力 | 说明 |
|------|------|
| 容器化部署 | 一个 `docker run` 启动整栈，自带 Web UI |
| 多平台缓存 | 支持 Steam、Xbox 等多家分发平台的下载流量 |
| 同网段透明命中 | 同 LAN 设备无需装客户端，DNS/网关级命中 |
| 管理界面 | 自带 Web 面板查看缓存命中、清理、状态 |
| 节省外网带宽 | 一台机下完、N 台机复用，适合小机房/合租 |

## 参考
- 原始链接：<https://github.com/HDR-Performance/super-lan-cache>

## 媒体
- ![](https://pbs.twimg.com/media/HRqILNeaUAIhoYN.jpg)

## 相关概念
- [Docker](./tool-docker.md) — 容器化运行底座
