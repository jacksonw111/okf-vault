---
type: "Tool"
title: "Immich Insights（自托管 Immich 统计面板）"
description: "laurinml 开源——给自托管 Immich 用户的照片库做统计面板，按成员各自的 API key 分析自己的库并缓存成本地快照；可视化家庭 / 团队的照片使用情况。"
resource: "https://github.com/laurinml/Immich-Insights"
tags: "[immich, photo, self-hosted, dashboard, statistics]"
timestamp: "2026-10-06T22:51:00Z"
---

# Immich Insights（自托管 Immich 统计面板）

## 它是什么

**Immich Insights** 是 laurinml 开源的 Immich 统计面板——给自托管 Immich 用户的照片库做统计视图，**按成员各自的 API key**分析自己的库，并把分析结果缓存成本地快照，避免反复调用 Immich API。

## 为什么用它 / 适合什么场景

- **家庭 / 团队使用统计**：谁上传多少、谁的相册最多、存储占用分布
- **隐私友好**：分析在自己机器上跑，照片元数据不上云
- **缓存友好**：分析结果本地缓存，下次秒开
- **API key 隔离**：每个成员独立分析自己的库

## 关键能力

| 能力 | 说明 |
|------|------|
| 成员维度统计 | 上传数 / 占用空间 / 设备分布 |
| 本地快照缓存 | 分析结果缓存成本地文件 |
| API key 隔离 | 每成员独立分析 |
| 图表展示 | 折线 / 饼图 / 柱状图 |
| 自托管 | 与 Immich 部署在一起 |

## 参考链接

- 项目链接：<https://github.com/laurinml/Immich-Insights>

## 相关概念

- [Self-Hosted](./term-self-hosted.md) — 部署形态
- [Immich](https://immich.app) — 底层照片库
