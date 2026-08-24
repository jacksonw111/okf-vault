---
type: Tool
title: "minimal-github-stats"
description: "用 GitHub Actions + Python 标准库在自家仓库生成 GitHub 统计 SVG 卡片，不依赖第三方托管服务、不需要个人 access token、无追踪脚本。"
resource: "https://github.com/antonisloukis/minimal-github-stats"
tags: [github, stats, svg, github-actions, python, readme]
timestamp: "2026-08-24T08:30:00Z"
---

# minimal-github-stats

## 它是什么

[antonisloukis/minimal-github-stats](https://github.com/antonisloukis/minimal-github-stats) 是一个 README GitHub 统计卡片的「零依赖」模板：完全跑在你自己仓库的 GitHub Actions + Python 标准库里，生成 SVG 卡片直接嵌进 README。

不依赖第三方托管服务（不像 [github-readme-stats](https://github.com/anuraghazra/github-readme-stats) 经常被限流）、不需要个人 access token、没有追踪脚本。

## 为什么用过它 / 适合什么场景

- 想在 README 放 GitHub 统计卡片，但被第三方公共服务限流 / 隐私担忧卡住。
- 想完全自托管，输出资产放在自己仓库的 Pages / 提交历史里。
- 不想给「要装 Node + 跑 gh CLI」的方案再加一台服务器。
- 重视隐私：不愿被第三方看到自己仓库的访问情况。

## 关键能力

| 能力 | 说明 |
|------|------|
| 零服务器 | 完全跑在 GitHub Actions 上 |
| 标准库 | 只用 Python 标准库，无第三方依赖 |
| 无 token | 用 GitHub Actions 自带 GITHUB_TOKEN 即可 |
| 无追踪 | 不向任何第三方上报数据 |
| SVG 输出 | 卡片可直接嵌入 README |

## 相关概念

- [gitglance](./tool-gitglance.md) — 同样思路的「自托管 GitHub 统计卡片」方案
- [GitHub Profile Achievements](./tool-github-profile-achievements.md) — 完善 GitHub 个人主页展示

## 参考链接

- [项目链接](https://github.com/antonisloukis/minimal-github-stats)
- ![](https://pbs.twimg.com/media/HQc6c4paoAAE2D6.jpg)