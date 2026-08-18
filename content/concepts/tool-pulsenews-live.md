---
type: Tool
title: "PulseNews-Live (jinit-00/PulseNews-Live-AI-News-Streaming-Platform)"
description: "实时新闻 AI 流式平台：从多源抓取、向量索引到 AI 问答 / 流式分析串成一条完整流水线，解决新闻平台更新滞后、搜索缺上下文、分析不实时的问题"
resource: "https://github.com/jinit-00/PulseNews-Live-AI-News-Streaming-Platform"
tags: [news, realtime, rag, kafka, fastapi, react, streaming]
timestamp: "2026-08-18T12:00:00Z"
---

# PulseNews-Live (jinit-00/PulseNews-Live-AI-News-Streaming-Platform)

## 它是什么
`jinit-00/PulseNews-Live-AI-News-Streaming-Platform` 是把**实时新闻从多源抓取、向量索引到 AI 问答 / 流式分析**串成一条完整流水线的开源平台，针对「新闻平台更新滞后 / 搜索缺上下文 / 分析不实时」三个痛点设计。架构跑在 Python 3.11 + FastAPI + React 上，用 Docker 一次起全套，支持**单机内存模式**与 **Kafka + Qdrant + Elasticsearch 集群模式**两种部署。

## 为什么用它 / 适合什么场景
- 想搭一个面向特定主题 / 行业的实时新闻聚合站，又不想从零搭后端。
- AI 产品需要「实时检索增强」：每次刷新都能拉到最新新闻而不只是历史快照。
- 想把「新闻 → 向量化 → 问答 → 流式分析」跑成一条可观测的流水线，便于排查延迟。

## 关键能力
| 能力 | 说明 |
|------|------|
| 多源 RSS 抓取 | 持续从全球 RSS 源收稿 |
| 去重 + 情感分析 + 关键词提取 | 入库前完成预处理 |
| Apache Kafka 数据流 | 消息流而非轮询，新事件即时分发 |
| WebSocket 推前端 | 不用刷新页面也能看到新内容 |
| Qdrant 向量索引 + Elasticsearch 全文 | 检索双引擎 |
| 双部署模式 | 单机内存模式 vs 集群模式按需切换 |

## 媒体
- ![](https://pbs.twimg.com/media/HP5H5IxasAAJybu.jpg)
- ![](https://pbs.twimg.com/media/HP5H98_asAAVYgW.jpg)

## 相关概念
- [项目链接](https://github.com/jinit-00/PulseNews-Live-AI-News-Streaming-Platform) — 仓库地址
