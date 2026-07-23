---
type: "Tool"
title: "OpenBrowser（本地桌面指纹浏览器 + RPA）"
description: "lyu0805/OpenBrowser，本地的桌面指纹浏览器，拿隔离的 Chromium 环境管多个浏览器配置，每个环境能单独设代理 / 改指纹 / 同步窗口 / 跑 RPA，主攻多账号管理和自动化操作。"
resource: "https://github.com/lyu0805/OpenBrowser"
tags: "[browser, fingerprint, rpa, multi-account, automation]"
timestamp: "2026-07-23T09:49:00Z"
---

# OpenBrowser（本地桌面指纹浏览器 + RPA）

## 它是什么

[`lyu0805/OpenBrowser`](https://github.com/lyu0805/OpenBrowser) 是一个**本地优先的桌面指纹浏览器**——它给你一份份「相互隔离」的 Chromium 环境，每份可以单独配置代理、修改浏览器指纹、同步窗口，并能跑 RPA 自动化。

## 关键能力

| 能力 | 说明 |
|------|------|
| 隔离 Chromium | 每个 profile 一个独立 Chromium 进程 |
| 代理配置 | 每个 profile 单独设代理 |
| 指纹修改 | canvas / WebGL / audio / fonts 等指纹可调 |
| 窗口同步 | 跨 profile 同步打开 / 关闭 |
| RPA | 内置脚本执行能力 |

## 为什么用它

- **多账号管理**：每个账号一个干净 profile，不被关联
- **反指纹检测**：可调 canvas / WebGL 等指纹骗过检测
- **本地数据不出门**：数据完全在本机（不像云端指纹浏览器那样上传）
- **RPA 友好**：内置脚本执行，能跑批量任务

## 适用场景

- 跨境电商多店铺运营
- 社交媒体多账号管理
- 自动化测试 / 爬虫
- 任何需要「环境隔离 + 反检测」的场景

## 媒体

![](https://pbs.twimg.com/media/HN4U4LbaIAACHDj.png)

## 相关概念

- [Bot Signal](./tool-bot-signal.md) — 反向：检测机器人 / 多账号是否被人识别
- [Synapse CE](./tool-synapse-ce.md) — 安全研究侧的「侦察 + 证据采集 + 报告」控制平面
- [Wigolo](./tool-wigolo.md) — 让 AI Agent 搜索 / 抓取 / 研究网页的 MCP 服务

## 原始链接

- [项目仓库](https://github.com/lyu0805/OpenBrowser)