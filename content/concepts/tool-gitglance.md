---
type: Tool
title: "gitglance"
description: "自部署 GitHub 统计 SVG 卡片生成器：README 不再依赖公共服务限流，自己跑一份就稳定输出。"
resource: "https://github.com/rafaeloliveiraz/gitglance"
tags: [github, stats, svg, self-hosted, readme]
timestamp: "2026-08-24T04:32:00Z"
---

# gitglance

## 它是什么

[rafaeloliveiraz/gitglance](https://github.com/rafaeloliveiraz/gitglance) 是自部署的 GitHub 统计 SVG 卡片生成器。给 README 用 GitHub 统计卡片的人不再被第三方公共服务限流 / 隐私条款卡住：自己跑一份服务，输出稳定可控。

## 为什么用它 / 适合什么场景

- 用过 [github-readme-stats](https://github.com/anuraghazra/github-readme-stats) 类公共服务，但被 rate limit 反复折磨。
- 想自己掌控卡片的样式、数据范围、刷新频率。
- 想避免把自己的仓库访问模式上报给第三方。
- 团队 / 公司想统一为多个 repo 出「同款风格」的统计卡片。

## 关键能力

| 能力 | 说明 |
|------|------|
| 自托管 | 服务跑在自己机器 / 自己的云上 |
| 稳定输出 | 无第三方公共服务限流问题 |
| SVG 卡片 | 输出可直接嵌入 README |
| 自定义样式 | 卡片外观可调 |
| 数据可控 | 决定展示哪些字段 |

## 相关概念

- [minimal-github-stats](./tool-minimal-github-stats.md) — 同类方案，用 GitHub Actions 替代独立服务
- [GitHub Profile Achievements](./tool-github-profile-achievements.md) — GitHub 主页展示相关

## 参考链接

- [项目链接](https://github.com/rafaeloliveiraz/gitglance)
- ![](https://pbs.twimg.com/media/HQc2RCGboAA2aUt.jpg)