---
type: Tool
title: "glance（GitHub · Docker · SSH 桌面仪表盘）"
description: "macOS 原生桌面仪表盘，用 Go（Wails）+ React/TypeScript 把 GitHub 活动 / Docker 容器 / SSH 服务器三块信息合到一个界面。"
resource: "https://github.com/veyselaksin/glance"
tags: [dashboard, github, docker, ssh, macos]
timestamp: "2026-07-07T12:00:00Z"
---

# glance（GitHub · Docker · SSH 桌面仪表盘）

## 它是什么
`glance` —— 一款 macOS 原生桌面仪表盘：针对开发者日常关注的 **GitHub 动态 / Docker 状态 / SSH 服务器**，传统要切多个终端 / 网站 / 桌面客户端，glance 把它们合并到一个原生应用里。技术栈 Go（Wails）+ React/TypeScript。

## 为什么用它 / 适合什么场景
- 关注 **当日 GitHub 贡献**、手里有哪些容器在跑、SSH 服务器健康状态——但不想装 3 个应用。
- 喜欢 macOS 原生体验 + 不依赖浏览器扩展。
- 想给团队里"非全职 SRE"的开发者一个低门槛运维看板。

## 关键能力
| 能力 | 说明 |
|------|------|
| GitHub | 通过 Device Flow 授权（**不存储密码**），查看今日贡献和提交数 |
| Docker | 列出容器状态 / CPU · 内存占用 / 启停 / 日志流式查看 |
| SSH | SSH 连接 / 内嵌终端 / 实时 CPU · 内存 · 磁盘指标 |
| 原生桌面 | Wails（Go 壳）+ React，前端体验顺滑、启动快 |
| 三合一看板 | 一个应用代替多个独立工具 |

## 相关概念
- [CasaOS](tool-casaos.md) — 个人云 OS，10 万+ Docker 镜像一键装
- [tabiew](tool-tabiew.md) — Rust 写的 TUI 表格数据查看器
- [DataBuff](tool-databuff.md) — 国产 AI Native OpenTelemetry APM，链路追踪 + AI 智能分析
- [dory](tool-dory.md) — macOS 上 Docker Desktop 的开源替代品
