---
type: "Tool"
title: "Knockoff（Amazon 山寨品牌过滤 Chrome 扩展）"
description: "Chrome 扩展，自动过滤 Amazon 搜索结果中的「商标抢注 / 山寨品牌」商品，让用户优先看到真实、有知名度的老牌厂商商品。"
resource: "https://github.com/Shpigford/knockoff"
tags: "[chrome-extension, amazon, shopping, anti-counterfeit, brand]"
timestamp: "2026-07-08T13:10:00Z"
---

# Knockoff

## 它是什么

[Knockoff](https://github.com/Shpigford/knockoff) 是一款 **Chrome 扩展**，专门对付 Amazon 搜索结果里**借大牌名蹭流量的「商标抢注 / 山寨品牌」**——这些商品往往名字里带「Sony」「Apple」「Nike」之类大牌词，但实际卖家是无名小厂，质量参差。

Knockoff 在搜索结果展示阶段就**自动过滤掉这些疑似山寨商品**，让真实老牌厂商的商品排到前面。

## 解决的痛点

| 痛点 | Knockoff 的解法 |
|------|----------------|
| 搜索结果被「碰瓷大牌」淹没 | 过滤掉疑似商标抢注品牌 |
| 点进去才发现不是真货 | 在结果展示层直接屏蔽 |
| 需要自己识别山寨 | 扩展自动判断 |
| 想优先看到可信品牌 | 把老牌厂商商品排前 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 自动过滤 | 在 Amazon 搜索结果页自动隐藏山寨条目 |
| 品牌识别 | 基于品牌注册 / 商标数据库判定 |
| 客户端运行 | 作为 Chrome 扩展，无需服务端 |
| 开源 | GitHub 公开，可审计规则 |

## 适合谁

- 在 Amazon 海淘 / 买电子产品的消费者。
- 对「李鬼品牌」不胜其烦的买家。
- 想研究「品牌识别 / 反假冒」规则的开发者。

## 参考链接

- [项目仓库](https://github.com/Shpigford/knockoff)

## 相关概念

- [Anysearch Skill](./tool-anysearch-skill.md) — 同为「搜索体验增强」类工具，但偏通用搜索
- [Dating Coach Skill](./tool-dating-coach-skill.md) — 同为「细分场景的浏览器 / 客户端辅助」