---
type: "Tool"
title: "SpatialBoard（React 白板 / 节点图底层库）"
description: "hishamk 出品的 React 白板 / 节点图底层——平移缩放 / 撤销重做 / 吸附对齐等基础设施都做完，开发者只需往里注册自定义节点类型。"
tags: "[react, whiteboard, node-graph, canvas, open-source]"
timestamp: "2026-08-26T16:30:00Z"
resource: "https://github.com/hishamk/spatialboard"
---

# SpatialBoard（React 白板 / 节点图底层库）

## 它是什么

[`SpatialBoard`](https://github.com/hishamk/spatialboard) 是 hishamk 写的 React **白板 / 节点图**底层库——把这类应用里**共通的底层交互**（平移 / 缩放 / 撤销重做 / 吸附对齐……）做完，应用开发者**只需注册自己的节点类型**就能起一个白板。

## 为什么用它 / 适合什么场景

- 想在 React 里做白板 / 思维导图 / 流程图 / 节点编辑器
- 不愿意自己花几个月实现 viewport、撤销栈、dragging、snapping
- 想要一个**框架中立、零样式**的底层库，可以套任何 UI 主题

## 关键能力

| 能力 | 说明 |
|------|------|
| 平移 / 缩放 | viewport 基础 |
| 撤销 / 重做 | history 栈 |
| 吸附对齐 | snap-to-grid 等 |
| 自定义节点 | 开发者注册 node type 即可 |
| React | 直接当 React 组件用 |
| MIT 风格 | 自由使用 |

## 媒体

![](https://pbs.twimg.com/media/HQiPGzrbQAAYFap.jpg)

## 参考链接

- [项目链接](https://github.com/hishamk/spatialboard)

## 相关概念

- [Quickdraw](./tool-quickdraw.md) — 同类「无限画布白板 SDK」，MIT 许可、tldraw 的开源替代
- [vault-graph](./tool-vault-graph.md) — 给整库 Obsidian 出可交互图谱，与本条目共享节点图范式
