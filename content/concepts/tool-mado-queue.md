---
type: "Tool"
title: "MADO-queue（Memuro-Town/MADO-queue）"
description: "日本北海道芽室町自研的行政窗口排队叫号系统，Flask + Python 3.14 + SQLite，已在镇政府大厅运行，Docker 一键部署。"
resource: "https://github.com/Memuro-Town/MADO-queue"
tags: [self-host, queue, civic-tech, flask, docker]
timestamp: "2026-06-23T15:30:00Z"
---

# MADO-queue（Memuro-Town/MADO-queue）

## 它是什么

日本北海道芽室町（Memuro）自己开发的行政窗口排队叫号系统。技术上轻到不能再轻：Flask + Python 3.14 + SQLite，不依赖厅内专网，Docker 一键起；已经在该镇政府大厅实际运行，居民不再需要反复填表。

## 为什么用它 / 适合什么场景

- **小规模自治体 / 社区**：村委、街道办、物业前台，想用低成本方案替代高价 SaaS；
- **断网 / 弱网环境**：SQLite 本地存储，断网期间数据先留本地，恢复后同步；
- **政务数字化起步**：可作为「先让流程跑起来」的最小可行系统（MVP）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 技术栈轻量 | Flask + Python 3.14 + SQLite |
| 离线可用 | 厅内网络断开也不影响本地运行 |
| Docker 一键部署 | docker compose up 即可上线 |
| 真实运行 | 北海道芽室町政府大厅在用 |
| 政务场景适配 | 重复填表 / 多窗口叫号 |

## 媒体 / 原始链接

- 项目链接：<https://github.com/Memuro-Town/MADO-queue>

## 相关概念

- [SafeBucket](concepts/tool-safebucket.md) — 同属「自托管 / 替代 SaaS」路径（文件共享场景）
- [Seeder](concepts/tool-seeder.md) — 同属「自托管项目管理 + MCP 化」路径
- [Single Server](concepts/tool-single-server.md) — 把这类自托管服务部署到一台 Linux 机器上的标准 Playbook