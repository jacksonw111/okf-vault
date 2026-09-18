---
type: Tool
title: "Yuki（Shizuku 权限框架开源安卓应用精选）"
description: "自动从 GitHub 抓仓库、按证据强弱打分，筛出真正使用 Shizuku 权限框架的开源 Android 应用，给 Shizuku 用户一份可靠的兼容清单。"
resource: "https://github.com/carlelieser/yuki"
tags: [android, shizuku, github, discovery, open-source, apps]
timestamp: 2026-09-18T12:36:00Z"
---

# Yuki（Shizuku 权限框架开源安卓应用精选）

## 它是什么

[carlelieser/yuki](https://github.com/carlelieser/yuki) 是一个**自动化的 Shizuku 应用精选器**。它定期从 GitHub 上抓仓库，按「是否真的接入了 [Shizuku](https://shizuku.rikka.app/) 权限框架」打分排序，把混在海量 Android 开源项目里的真正可用的 Shizuku 应用挑出来。

## 关键能力

| 能力 | 说明 |
|------|------|
| 自动抓取 | 周期性从 GitHub 拉仓库 |
| 证据打分 | 按代码层证据强弱判断「是否真的用了 Shizuku」，避免名单里出现挂着名头但实际是 stub 的项目 |
| 持续维护 | 仓库会随 GitHub 数据自动刷新，不用人工一张表维护 |
| 筛选开源 | 限定在开源 Android 应用范围内 |

## 适合什么场景

- 想用 [Shizuku](https://shizuku.rikka.app/) 拿更高的系统权限，又不知道哪些开源应用真的接入了它。
- 想发现新的、能借助 Shizuku 跳过广告 / 解锁受限功能 / 自动化操作的 Android 应用。
- 想避开「GitHub 列表里挂个 Shizuku badge 但代码里没有实际调用」的虚假项目。

## 与相关概念的关系

- [Self-Hosted（自托管）](./term-self-hosted.md) — Yuki 本身是一个由 GitHub 自动驱动的「应用策展」，形态接近轻量自托管的内容服务。

## 参考

- 项目链接：<https://github.com/carlelieser/yuki>

![策展页截图](https://pbs.twimg.com/media/HSdmqsFbsAAJ2N1.png)
