---
type: Note
title: "Reverse Engineering Linear's Sync Engine"
description: "wzhudev 对 Linear 客户端 Sync Engine 的逆向研究文章 / 仓库：拆解模型定义 / IndexedDB 事务 / 服务端 delta 上报 / 部分加载 / undo，附 Linear CTO 推荐"
resource: "https://github.com/wzhudev/reverse-linear-sync-engine"
tags: [linear, sync-engine, indexeddb, architecture, reverse-engineering]
timestamp: 2026-09-05T15:00:00Z
---

# Reverse Engineering Linear's Sync Engine

## 文章定位
`wzhudev/reverse-linear-sync-engine` 是一篇**非 AI 主题的纯技术逆向研究**：作者详细拆解了 **Linear 客户端同步引擎（Linear Sync Engine）** 的实现思路——从模型怎么定义、怎么进 IndexedDB 事务、怎么上报、服务端怎么回 delta、怎么做部分加载和 undo，全链路讲透。Linear CTO 也公开称赞过这篇分析。

## 为什么值得读
- 想理解**离线优先 / 乐观更新**类同步架构的实战参考（不只是协议层，而是「体验为什么丝滑」的工程取舍）。
- IndexedDB 事务模型在工程上很容易被低估，这篇把事务粒度、冲突策略讲得很细。
- 不依赖 AI 主题也能写得精彩——给非 LLM 类深度技术文章打样。

## 关键拆解维度
| 维度 | 内容 |
|------|------|
| 模型定义 | 客户端数据模型与字段约束 |
| IndexedDB 事务 | 写入粒度、事务边界、读一致性 |
| 上报机制 | 客户端变更如何上报服务端 |
| Delta 回包 | 服务端增量下发，节省带宽 |
| 部分加载 | 按需加载策略，避免一次拉全 |
| Undo 实现 | 客户端撤销如何与服务端状态对账 |
| 乐观更新 | 用户操作先本地生效，失败回滚的设计 |

## 相关概念
- [原始链接](https://github.com/wzhudev/reverse-linear-sync-engine)