---
type: "Note"
title: "从零到完整 coding agent 的实战教程笔记（7-e1even/learn-agent）"
description: "从零到完整 coding agent 的实战教程笔记, 每个机制都附带零依赖可运行的 Node.js 示例, 便于边读边改边学。"
resource: "https://github.com/7-e1even/learn-agent"
tags: "[coding-agent, tutorial, nodejs, learning, agent-basics]"
timestamp: "2026-07-17T02:38:00Z"
---

# learn-agent：从零到完整 coding agent

[learn-agent](https://github.com/7-e1even/learn-agent) 是一份面向**自学者的实战教程笔记**, 主线是把「一个完整可用的 coding agent」按机制逐个剖开——prompt / tool call / 文件系统访问 / 子 agent / 上下文压缩 / 重试 / 自检——每一节都附带**零依赖可运行的 Node.js 示例**。

## 为什么值得收

agent 框架满天飞, 但「读完文档依旧不会写自己的 agent」是常态。learn-agent 的定位是「读 + 改 + 跑」三步闭环：

- **读** —— 章节先讲设计意图, 再讲最小实现
- **改** —— 代码可独立运行, 一行行改着试错
- **跑** —— 每段机制在 Node.js 里能直接看效果 (零依赖 = 不装 npm 包)

## 关键话题覆盖

| 话题 | 焦点 |
|------|------|
| 工具调用 | JSON Schema → 自然语言 → Tool 路由器 |
| 上下文管理 | 截断、压缩、摘要, 边界与失真 |
| 文件系统安全 | 路径白名单 / 越界阻断 |
| 子 agent | spawn / cancel / 进度回灌 |
| 自检与重试 | 失败分类、退避、熔断 |

## 媒体

![](https://pbs.twimg.com/media/HNRPFpSbIAAqdEf.jpg)

## 参考链接

- [项目仓库](https://github.com/7-e1even/learn-agent)

## 相关概念

- [深入理解 AI Agent](./note-ai-agent-book.md) — bojieli 整理的中文 AI Agent 电子书, 与本笔记互补: 一份偏系统理论, 本笔记偏工程最小实践
- [12-Factor Agents](./tool-12-factor-agents.md) — 12 条工程原则, 本笔记可作为各原则的具体落地范例
- [OpenSeek（MoonBit DeepSeek 编程助手框架）](./tool-openseek-moonbit.md) — 另一个从底层写起的小型编程助手框架
