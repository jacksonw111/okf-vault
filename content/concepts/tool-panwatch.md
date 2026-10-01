---
type: Tool
title: "PanWatch（自托管的 AI 盯盘与投研工作台）"
description: "TNT-Likely 出品的自托管盯盘应用：把 A 股、港股、美股的盯盘、持仓分析、异动提醒、定时报告统一到一个 Web 服务里，后端 FastAPI + SQLAlchemy + APScheduler，前端 React 18 + TypeScript + Tailwind + shadcn/ui，Docker 一条命令拉起。"
resource: "https://github.com/TNT-Likely/PanWatch"
tags: [trading, stocks, a-shares, hk-stocks, us-stocks, self-hosted, dashboard, fastapi, react]
timestamp: 2026-10-01T02:29:00Z
---

# PanWatch

## 它是什么

**PanWatch** 是 [TNT-Likely](https://github.com/TNT-Likely) 开源的**自托管 AI 盯盘与投研工作台**——核心定位：**A 股 / 港股 / 美股**一站式盯盘，把「盯盘 + 持仓分析 + 异动提醒 + 定时报告」统一到一个 Web 服务里，省去同时打开行情软件、Excel、推送脚本的繁琐。

技术栈：

- **后端**：FastAPI + SQLAlchemy + APScheduler
- **前端**：React 18 + TypeScript + Tailwind CSS + shadcn/ui
- **部署**：Docker 一条命令拉起，数据存在挂载卷里
- **数据源**：覆盖 A / 港 / 美三市

## 为什么用它 / 适合什么场景

- 个人投资者希望**自己掌握行情数据**，不依赖商业终端。
- 想跨 A / 港 / 美三市统一持仓视图与异动提醒，而不是装多个 App。
- 需要**可定制**的 AI 投研助手（让 LLM 接入自己的持仓/盯盘数据）。
- 已经跑 NAS / 迷你主机，希望 24×7 监听 + 推送。

## 关键能力

| 能力 | 说明 |
|------|------|
| 市场覆盖 | A 股 / 港股 / 美股 |
| 功能 | 盯盘 / 持仓分析 / 异动提醒 / 定时报告 |
| 后端 | FastAPI + SQLAlchemy + APScheduler |
| 前端 | React 18 + TypeScript + Tailwind + shadcn/ui |
| 部署 | Docker 单命令 |
| 数据存储 | 挂载卷 |
| 形态 | 自托管 Web 服务 |

## 参考链接

- 仓库：<https://github.com/TNT-Likely/PanWatch>

## 媒体

- ![](https://pbs.twimg.com/media/HTcqq0TbcAAUqh2.jpg)

## 相关概念

- [OpenObserve](./tool-openobserve.md) — 同为自托管类项目，但偏可观测方向
- [edge-scanner](./tool-edge-scanner.md) — 同类美股分钟行情扫描思路
