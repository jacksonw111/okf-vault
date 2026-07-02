---
type: Tool
title: "12306-mcp"
description: "为 12306（中国铁路购票）做的 MCP 服务器，提供简洁 API 让 AI 助手直接查询车票、列车信息与中转方案。"
resource: "https://github.com/Joooook/12306-mcp"
tags: "[mcp, 12306, travel, ai-agent, china, railway]"
timestamp: "2026-07-02T11:20:00Z"
---

# 12306-mcp

## 它是什么
一个面向 12306（中国铁路 12306 购票官网）的 MCP（Model Context Protocol）服务器。让任意支持 MCP 的 AI 助手（Claude Code、Cursor、Codex 等）通过统一工具调用，直接查询车票与列车信息。

## 为什么用它 / 适合什么场景
- 想让 AI 助手帮你查「明天北京到上海的高铁余票」之类的出行问题。
- 想把路线规划、买票、订酒店整条出行链路交给 AI 一站式完成。
- 不想每次手动打开 12306 网页或 App。

## 关键能力
| 能力 | 说明 |
|------|------|
| 车票查询 | 按车次 / 日期 / 起讫站查余票 |
| 列车信息过滤 | 按车型 / 时段 / 用时筛选 |
| 过站查询 | 查询某次列车在指定区间经停哪些站 |
| 中转查询 | 当直达无票时给出中转方案 |
| MCP 接口 | 任何 MCP 兼容客户端均可调用 |
| 协议中立 | 不绑定特定 Agent / 模型 |

## 相关概念
- [DeepSeek MCP WebSearch](tool-deepseek-mcp-websearch.md) — 同类「MCP 联网 / 数据查询」工具
- [page-agent（阿里浏览器端 GUI Agent）](tool-page-agent.md) — 浏览器 GUI 自动化，与本 MCP 服务器互补：MCP 是数据接口，page-agent 是操作界面
- [memgui-agent](tool-memgui-agent.md) — 移动端 GUI Agent，针对手机屏幕而非 12306 网页
- [Proxide](tool-proxide.md) — 把 ChatGPT Pro 等网页强模型接进 MCP 客户端

## 项目链接
- 项目主页：<https://github.com/Joooook/12306-mcp>