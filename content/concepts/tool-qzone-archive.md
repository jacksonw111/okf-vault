---
type: Tool
title: "QzoneArchive（QQ 空间历史动态 / 照片 / 视频本地归档，零平台依赖）"
description: "把 QQ 空间里的旧动态、照片、视频、点赞评论互动记录抓回本地 SQLite，随时可离线查看与导出，防止平台清理或服务关闭导致的历史数据丢失。"
resource: "https://github.com/Gaoshu705/QzoneArchive"
tags: [qzone, qq, archive, backup, sqlite, offline, web-scraping, preservation]
timestamp: "2026-08-28T00:00:00Z"
---

# QzoneArchive

## 它是什么
[Gaoshu705/QzoneArchive](https://github.com/Gaoshu705/QzoneArchive) 是**把 QQ 空间历史数据全部抓到本地 SQLite 的归档工具**。

痛点：QQ 空间里有十多年积攒的动态、照片、视频、点赞、评论，但平台政策变化、账号被封、空间清理等都可能让这部分**生活记忆永久消失**——而 QQ 官方并未提供完整的导出工具。

QzoneArchive 的解法：

- 自动抓取指定 QQ 号的**所有可见动态**、**相册**、**视频**、**点赞**、**评论**；
- 全部数据落到**本地 SQLite**，可离线浏览、检索、导出；
- 抓取结束后，**对平台的依赖降为零**——QQ 关停也不影响已归档数据。

## 为什么用它 / 适合什么场景
- 想为多年 QQ 空间内容**做完整备份**，防止平台政策或账号问题导致丢失；
- 想**离线浏览 / 检索**历史动态、评论、点赞；
- 想把数据**导出到自有格式**（如 JSON / HTML / 静态站点）做长期保存；
- 怀旧 / 整理个人历史 / 数字遗产管理的需求。

## 关键能力
| 能力 | 说明 |
|------|------|
| 完整抓取 | 动态 / 照片 / 视频 / 点赞 / 评论互动记录 |
| 本地存储 | 全量数据进 SQLite，文件可备份到任何介质 |
| 离线浏览 | 不依赖 QQ 服务可用 |
| 数据导出 | 可导出 JSON / HTML 等通用格式 |
| 防平台清理 | 抓取后即使平台服务下线数据也在 |
| 抗账号风险 | 即使 QQ 号被封，已抓数据不受影响 |

## 相关概念
- [Sift macOS](tool-sift-macos.md) — macOS 本地应用集中分析 / 清理；QzoneArchive 是**网络时代个人资产**的归档
- [FileApex](tool-fileapex.md) — 同局域网设备互传；QzoneArchive 在数据所有权维度上更彻底——**抓回本机才算自己的**

## 参考链接
- 项目链接：<https://github.com/Gaoshu705/QzoneArchive>
- 原始推文：<https://x.com/QingQ77/status/2093221541039223027>
- 媒体：<https://pbs.twimg.com/media/HQsnRXxbAAA4dpT.jpg>
