---
type: Tool
title: "awesome-grokbot"
description: "把 4 个社区来源的 Grok Bot 目录合并去重，用脚本检查每个链接是否存活，给每条记录补中文摘要与 origin 来源，生成可搜索的统一索引。"
resource: "https://github.com/kydlikebtc/awesome-grokbot"
tags: [grok, grokbot, awesome-list, awesome, x-twitter]
timestamp: 2026-09-02T12:00:00Z
---

# awesome-grokbot

## 它是什么

Grok Bot 在多个社区里被零散分享，质量参差、中英文索引都没有。`awesome-grokbot` 把 4 个社区目录（社区机器人清单 / Awesome 风格收录 / 推特讨论等）合并去重，跑一个链接活性检查脚本剔除失效记录，并对每条机器人补一份中文摘要和原始来源链接，最终产物是一份可搜索、有中文索引的统一 Grok Bot 目录。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多源合并去重 | 4 个社区目录合并，避免同一机器人被收录多次 |
| 链接活性自检 | 跑脚本验证每条目录是否仍可访问，失效即标红 |
| 中文摘要 + origin | 每条补充中文摘要 + 原始来源 URL，便于中文用户快速识别 |

## 项目链接

- [项目主页](https://github.com/kydlikebtc/awesome-grokbot)

## 相关概念

- [OpenBot](./tool-openbot.md) — 另一种对机器人 / 浏览器 Agent 的封装思路
