---
type: "Tool"
title: "Stately Graph（Stately 出品的 TypeScript 图数据框架）"
description: "David Khourshid（Stately 创始人）开源的 TypeScript 图数据框架——支持纯 JSON 图、转换 DOT / Mermaid / GraphML 等格式、丰富的算法、可视化 + 结构化属性查询、完全类型安全且极速。"
resource: "https://github.com/statelyai/graph"
tags: "[graph, typescript, mermaid, dot, visualization, stately, state-machines]"
timestamp: "2026-10-07T14:33:00Z"
---

# Stately Graph

## 它是什么

[Stately Graph](https://github.com/statelyai/graph) 是 **David Khourshid**（Stately 创始人 / XState 作者）开源的 **TypeScript 图数据框架**。它不是单一用例的图库，而是「**通用图原语 + 格式互通 + 算法 + 属性查询**」的完整底座——既能装载纯 JSON 图，又能把 DOT / Mermaid / GraphML 等格式互转，还配可视化与结构化属性访问。

## 为什么用它 / 适合什么场景

- **图是越来越常被低估的数据结构**：状态机、依赖网络、社交关系、组织架构、知识图谱都本质上是图
- **格式互通**：DOT（Graphviz）/ Mermaid / GraphML 三种主流描述都能进 / 出，跟现有文档 / 工具链无缝衔接
- **类型安全**：纯 TypeScript 实现，所有 API 都有完整类型提示
- **性能**：核心操作 FAST，适合前端 / 服务端都可跑
- **可视化 + 结构化属性**：既能画图，又能查「节点 x 在第 3 层可达哪些边」

## 关键能力

| 能力 | 说明 |
|------|------|
| 数据格式 | 纯 JSON 图（最小可工作） |
| 格式互通 | DOT / Mermaid / GraphML 双向转换 |
| 算法 | 路径 / 最短路 / 拓扑 / 遍历 等 |
| 属性查询 | 节点 / 边的可视化 + 结构化属性 |
| 类型安全 | 完全 TypeScript 类型化 |
| 性能 | FAST（核心操作零拷贝 + 优化路径） |

## 参考链接

- 项目仓库：<https://github.com/statelyai/graph>

## 相关概念

无相关概念需要链入。
