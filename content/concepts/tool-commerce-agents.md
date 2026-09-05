---
type: Tool
title: "anthropics/commerce-agents"
description: "面向电商企业的 Claude 智能体参考代码：购物助手 + 商家助手各定义一次，可在三种运行方式上复用，每智能体含五个技能流程"
resource: "https://github.com/anthropics/commerce-agents"
tags: [anthropic, claude, ecommerce, agent, reference]
timestamp: 2026-09-05T15:00:00Z
---

# anthropics/commerce-agents

## 它是什么
`anthropics/commerce-agents` 是 Anthropic 官方发布的**电商行业 Claude 智能体参考实现**：把面向顾客的购物助手与面向员工的商家助手各定义一次，就能在**三种运行方式**上复用，每个智能体内置五个技能流程。

## 为什么用它 / 适合什么场景
- 想给电商业务接 Claude agent，但不想从零设计 prompt / 工具集。
- 需要「顾客侧 + 员工侧」两条独立但风格统一的 agent。
- 想把同一份 agent 定义同时跑在 Web / CLI / IDE 等多个宿主上。

## 关键能力
| 能力 | 说明 |
|------|------|
| 购物助手 | 搜索、比价、规划、填购物车、查订单、记顾客偏好 |
| 商家助手 | 看经营数据、改商品、处理库存和订单告警、定价促销、起草活动 |
| 五项技能 / 智能体 | 每个智能体含 5 个独立技能流程 |
| 三种运行方式 | 同一份定义可在多种宿主上复用 |
| Anthropic 官方维护 | 参考实现由 Anthropic 发布 |

## 相关概念
- [原始链接](https://github.com/anthropics/commerce-agents)