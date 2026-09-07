---
type: Tool
title: "ternssh"
description: "浏览器即 SSH 工作台：终端 + SFTP + 服务器状态监控 + 可拖拽仪表盘聚合在一个 Web 页面，可部署到 Cloudflare Workers 或 Docker 自建。"
resource: "https://github.com/HaradaKashiwa/ternssh"
tags: "[ssh, web, sftp, cloudflare-workers, docker, dashboard]"
timestamp: "2026-09-07T13:20:00Z"
---

# ternssh

## 它是什么
基于浏览器的 SSH 工作台，不需要额外装客户端，打开浏览器就能连接远程主机。集成了终端、SFTP、服务器状态监控、可拖拽仪表盘，把常用运维操作集中到一个页面。

## 部署形态
- **Cloudflare Workers**：可直接跑在 Workers 上，零基础设施
- **Docker 自建**：适合内网 / 团队内私有部署

## 关键能力
| 能力 | 说明 |
|------|------|
| 浏览器终端 | 免客户端，浏览器即开即用 |
| SFTP | 文件上传下载与浏览 |
| 服务器状态 | CPU / 内存 / 磁盘 / 网络 |
| 可拖拽仪表盘 | 按需摆放监控 widget |
| 灵活部署 | Workers / Docker 双形态 |

## 适用场景
- 个人 VPS 多台管理：聚合到一个面板
- 团队内共用：避免每个成员都装客户端
- 临时办公 / 出差：在任意设备上管理服务器

## 参考
- 项目链接：<https://github.com/HaradaKashiwa/ternssh>

## 相关概念
- [OpenMac](tool-openmac.md) — macOS 本地 HTTP 服务，把系统能力暴露成 API
- [EasySNI](tool-easysni.md) — SNI / XRay / 域名前置单文件面板（与 ternssh 在"服务器控制面聚合"思路上一致）