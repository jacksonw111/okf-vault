---
type: Tool
title: "opencode-usage（Chrome 扩展，把 opencode 用量同步本地 + 仪表盘）"
description: "Chrome 扩展，把 opencode 的 token 用量同步到本地存储并展示内置仪表盘，补齐 opencode 官方用量页不统计免费模型的缺口。"
resource: "https://github.com/xhang1108/opencode-usage"
tags: [opencode, chrome-extension, usage-tracking, token-metering, dashboard]
timestamp: "2026-08-29T21:30:00Z"
---

# opencode-usage（Chrome 扩展，把 opencode 用量同步本地 + 仪表盘）

## 它是什么

[xhang1108/opencode-usage](https://github.com/xhang1108/opencode-usage) 是一个**针对 opencode 的 Chrome 扩展**：把 opencode 的 token 用量同步到浏览器本地存储，再用一个内置仪表盘把消耗展示出来。

存在意义：opencode 官方用量页**不统计免费模型**——用户用了多少免费额度心里没数，这个扩展把免费 + 付费一并抓出来，弥补官方页面缺口。

## 为什么用它 / 适合什么场景

- opencode 重度用户想看真实 token 消耗、避免免费配额被悄悄用光；
- 想知道「这个月用了多少、哪个模型最费」来做调用策略优化；
- 不放心把用量数据交给云端服务，宁愿留在浏览器本地；
- 团队 / 公司想监控 opencode 调用成本但不想部署服务端。

## 关键能力

| 能力 | 说明 |
|------|------|
| 用量同步 | 抓取 opencode 调用数据写到本地存储 |
| 仪表盘 | 浏览器内看 token / 模型 / 时间维度统计 |
| 补齐免费模型 | 包含官方页面不显示的免费额度消耗 |
| 本地优先 | 数据存在浏览器本地，不必上传第三方 |

## 相关概念

- [opencode CC](./tool-opencode-cc.md) — opencode 的 Claude Code 兼容层
- [opencode Fusion](./tool-opencode-fusion.md) — 把多 provider / 多模型接入 opencode
- [opencode Senses](./tool-opencode-senses.md) — 给 opencode 加感知层（视觉 / 屏幕）

## 参考链接

- 项目链接：<https://github.com/xhang1108/opencode-usage>
- 原始推文：<https://x.com/QingQ77/status/2093591981968540004>
- 媒体：<https://pbs.twimg.com/media/HQyJskla4AAyBEm.jpg>