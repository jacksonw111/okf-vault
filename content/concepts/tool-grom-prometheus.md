---
type: Tool
title: "Grom（Prometheus btop 终端仪表盘）"
description: "qf-studio 用 Go 写的终端工具，把 Prometheus 指标渲染成 btop 风格的终端仪表盘，并支持读取现有 Grafana 面板 JSON 在终端复现相同布局。"
resource: "https://github.com/qf-studio/grom"
tags: "[prometheus, grafana, terminal, dashboard, tui, monitoring]"
timestamp: "2026-07-11T20:00:00Z"
---

# Grom（Prometheus btop 终端仪表盘）

## 它是什么

`qf-studio/grom` 是一个**Go 写的 Prometheus 终端仪表盘工具**。两个核心能力：

1. **btop 风格终端渲染**——把 Prometheus 指标以 btop 那种「高密度 + 美观」的终端 UI 呈现。
2. **读 Grafana 面板 JSON**——把现有 Grafana 仪表盘的 JSON 配置导入，在终端复现相同布局（无需启动 Grafana）。

## 为什么用它 / 适合什么场景

- 运维 / SRE 想 SSH 到机器上直接看 Prometheus 指标，不想开 Grafana。
- 在没有浏览器的环境（远程终端、嵌入式场景）下用 Grafana 同款布局看监控。
- 想给 Prometheus 指标配一个「随手能开」的轻量视图。

## 关键能力

| 能力 | 说明 |
|------|------|
| Prometheus 直读 | 直接 query Prometheus API |
| btop 风格 UI | 高密度 + 美观的终端渲染 |
| Grafana JSON 兼容 | 读 Grafana dashboard JSON，在终端复现 |
| Go 实现 | 单二进制，部署简单 |

## 媒体参考

- 演示视频：<https://video.twimg.com/tweet_video/HM1GLaZaAAAxuyt.mp4>

## 相关概念

- [btop](https://github.com/aristocratos/btop) — 灵感来源
- [Glance Dashboard](tool-glance-dashboard.md) — 另一款 macOS 三合一开发者桌面仪表盘
- [Datalab Lift](tool-datalab-lift.md) — 数据实验平台

## 项目链接

- 项目仓库：<https://github.com/qf-studio/grom>