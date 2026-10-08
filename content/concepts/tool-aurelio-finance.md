---
type: "Tool"
title: "Aurelio Finance（自托管个人财富分析）"
description: "LosaLosSantos 开源：自托管的个人财富分析应用，后端 FastAPI + 前端 React + TypeScript，数据存本机 backend/data.db，更新前自动备份；要看 AI 建议时再用自家 OpenRouter key 连一次。"
resource: "https://github.com/LosaLosSantos/aurelio-finance"
tags: "[finance, self-hosted, wealth-tracking, fastapi, react, privacy]"
timestamp: "2026-10-08T23:50:00Z"
---

# Aurelio Finance

## 它是什么

[Aurelio Finance](https://github.com/LosaLosSantos/aurelio-finance) 是 LosaLosSantos 开源的「**自托管个人财富分析应用**」：

- 后端 **FastAPI**
- 前端 **React + TypeScript**
- 数据存本机 `backend/data.db`，**不出本机**
- 更新前自动备份
- **要看 AI 建议时再拿自己的 OpenRouter key 连一次**

## 为什么用它 / 适合什么场景

- **隐私敏感**：个人资产数据不想交给云端 SaaS
- **想用 AI 但不愿把数据交给 AI**：平时全本地，看建议时一次性调用
- **不愿被订阅费绑架**：自托管零月费
- **想完全控制数据格式**：SQLite 文件 + 备份机制

## 关键能力

| 能力 | 说明 |
| ------ | ------ |
| 形态 | 自托管 Web 应用 |
| 后端 | FastAPI（Python） |
| 前端 | React + TypeScript |
| 数据 | 本机 SQLite `backend/data.db` |
| 备份 | 更新前自动备份 |
| AI 接入 | 自带 OpenRouter key 临时调用 |
| 隐私 | 数据不上云 |

## 参考链接

- 项目链接：<https://github.com/LosaLosSantos/aurelio-finance>

## 媒体

![](https://pbs.twimg.com/media/HUE_gldbkAANC_Z.jpg)

## 相关概念

- [Self-Hosted（自托管）](./term-self-hosted.md) — 概念总览
- [Financial_freedom 学习清单](./note-financial-freedom-list.md) — 投资学习侧的资料清单，与本工具互补