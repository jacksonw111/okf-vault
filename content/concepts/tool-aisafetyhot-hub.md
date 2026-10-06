---
type: "Tool"
title: "AISafetyHot-Hub（AI 安全中文日报）"
description: "wuyoscar 开源——手动追 AI 安全论文和事件太分散，这个仓库每天 08:00 出一份中文日报，把攻击、防御、对齐、评测、治理方向的精选动态和论文按日期归档，并提供只读 API、RSS、Skill 和 MCP 接入，让人和 Agent 都能直接查询。"
resource: "https://github.com/wuyoscar/AISafetyHot-Hub"
tags: "[ai-safety, chinese, daily, alignment, mcp]"
timestamp: "2026-10-06T22:51:00Z"
---

# AISafetyHot-Hub（AI 安全中文日报）

## 它是什么

**AISafetyHot-Hub** 是 wuyoscar 开源的仓库——手动追 AI 安全论文和事件太分散，这个仓库**每天 08:00（北京时间）出一份中文日报**，把攻击、防御、对齐、评测、治理方向的精选动态和论文按日期归档；并提供只读 API、RSS、**Skill**和 **MCP** 接入，让人和 Agent 都能直接查询。

## 为什么用它 / 适合什么场景

- **AI 安全从业者**：每天一杯咖啡时间看完安全领域精选
- **研究人员**：按方向（攻击 / 防御 / 对齐 / 评测 / 治理）系统归档
- **Agent 接入**：通过 MCP / Skill 让 Agent 也能查最新动态
- **中文优先**：相较英文一手资料，降低中文研究者门槛

## 关键能力

| 能力 | 说明 |
|------|------|
| 每日 08:00 自动出日报 | GitHub Actions 定时跑 |
| 中文摘要 | 论文 / 事件的中文摘要 |
| 5 大方向分类 | 攻击 / 防御 / 对齐 / 评测 / 治理 |
| 多通道查询 | 只读 API / RSS / Skill / MCP |
| 按日期归档 | 历史日报可回看 |

## 参考链接

- 项目链接：<https://github.com/wuyoscar/AISafetyHot-Hub>

## 相关概念

- [MCP（Model Context Protocol）](./term-mcp.md) — 接入 Agent 的协议
- [AI Hot](./tool-aihot.md) — 同为热点聚合框架
