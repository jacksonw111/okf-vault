---
type: Tool
title: "proxypin-mcp-workbench（带本地 AI 分析的抓包工作台）"
description: "sinyu1012/proxypin-mcp-workbench：把抓包从一次性行为变成可积累的工作流：归档 / 整理 / Mock 一套带走，并能接入本地 AI 直接分析流量"
resource: "https://github.com/sinyu1012/proxypin-mcp-workbench"
tags: [packet-capture, mcp, local-ai, mock, debugging]
timestamp: "2026-08-23T01:16:00Z"
---

# proxypin-mcp-workbench（带本地 AI 分析的抓包工作台）

## 它是什么

[sinyu1012/proxypin-mcp-workbench](https://github.com/sinyu1012/proxypin-mcp-workbench) 把**抓包从一次性行为**升级为**可积累的工作流**：归档 / 整理 / Mock 一套带走，并能接入**本地 AI** 直接帮你分析流量。

针对的痛点：普通抓包工具只能一条条翻请求，看完就丢。

## 为什么用它 / 适合什么场景

- 调试 API、移动 App 时，希望抓包结果能"沉淀"成可复用的资产（Mock / 用例 / 文档）。
- 想让本地 LLM 直接帮你读抓包结果、定位异常、给修复建议。
- 做协议逆向 / 移动端爬虫 / 移动安全测试，需要持续保存与回放请求。

## 关键能力

| 能力 | 说明 |
|------|------|
| 抓包归档 | 请求可命名、分类、长期保存 |
| Mock 一套带走 | 把抓到的请求作为 Mock 服务复放 |
| MCP 接入 | 与 AI 助手通过 MCP 协议打通 |
| 本地 AI 分析 | 让本地 LLM 直接读抓包结果、解释、定位异常 |

## 媒体

- ![](https://pbs.twimg.com/media/HQT_geCbQAAuqDm.jpg)

## 相关概念

- [DevSpace](./tool-devspace-mcp.md) — 自托管 MCP 编程工作台
- [Codex Control Plane MCP](./tool-codex-control-plane-mcp.md) — 持久化任务队列 MCP
- [Bot-Signal](./tool-bot-signal.md) — 同类机器人检测 / 抓包分析工具

## 参考链接

- [项目链接](https://github.com/sinyu1012/proxypin-mcp-workbench)
