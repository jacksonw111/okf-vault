---
type: Tool
title: "Xerj（Rust 从零写的统一 AI 搜索引擎）"
description: "用 Rust 从头实现的统一搜索引擎，替代 AI 系统所需的全套检索栈。全文搜索、向量、混合检索、Agent 记忆、日志分析，兼容 Elasticsearch 协议。"
resource: "https://github.com/xerj-org/xerj"
tags: [search-engine, rust, vector-search, hybrid-search, elasticsearch-compatible, agent-memory]
timestamp: "2026-07-28T07:10:00.000Z"
---

# Xerj

## 它是什么

**Rust 从头实现的统一搜索引擎**——目标是把 AI 系统所需的全部检索能力装进一个二进制：

| 能力 | 说明 |
|------|------|
| 全文搜索 | BM25 / 倒排 |
| 向量搜索 | embedding 检索 |
| 混合检索 | 全文 + 向量融合 |
| Agent 记忆 | 长期存储 + 检索 |
| 日志分析 | OLAP 风格 |
| Elasticsearch 兼容 | 协议级兼容 |

![示意图](https://pbs.twimg.com/media/HONpP1NasAAImri.jpg)

## 为什么替代 Elasticsearch

| 维度 | Elasticsearch | Xerj |
|------|--------------|------|
| 资源占用 | JVM 重 | Rust 轻量 |
| AI 工作负载 | 需插件拼凑 | 原生支持 |
| 启动复杂度 | 集群配置 | 单二进制 |
| ES 协议兼容 | — | 兼容 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 全栈 AI 检索 | 不必拼 4 个库 |
| ES 协议兼容 | 客户端 / Kibana 复用 |
| Rust 实现 | 性能 + 资源占用友好 |
| 适合 Agent 系统 | 记忆 / 日志 / RAG 一套 |

## 原始链接

- [项目仓库](https://github.com/xerj-org/xerj)
- [推文剪藏](https://x.com/QingQ77/status/2082000603329581541)

## 相关概念

- [gold-pan](./tool-gold-pan.md) — 隐私优先多模态数据提取 + 本地 RAG 工作台
- [Zestmem（多智能体协作持久化记忆）](./tool-zestmem.md) — PostgreSQL + pgvector 的记忆服务
- [Cocoindex Code](./tool-cocoindex-code.md) — AST 语义代码搜索引擎
- [Zerj-类似 ES 替代品（OpenSearch）外的产品定位](./tool-openseek-moonbit.md) — MoonBit 写的编程助手基础库