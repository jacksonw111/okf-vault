---
type: "Tool"
title: "Targie（LiruiYu33/Targie-The-Similar-Videos-Images-Finder）"
description: "macOS 上扫描并整理重复 / 视觉相似视频与图片的工具，SHA-256 + 感知指纹 + Vision 特征多维度比对，支持并排预览与批量删除。"
resource: "https://github.com/LiruiYu33/Targie-The-Similar-Videos-Images-Finder"
tags: [macos, dedupe, vision, swift, image, video]
timestamp: "2026-06-23T15:30:00Z"
---

# Targie（LiruiYu33/Targie-The-Similar-Videos-Images-Finder）

## 它是什么

macOS 上的「重复 / 视觉相似」媒体查找器：扫描文件夹找出 SHA-256 完全相同的文件，或感知哈希 / Vision 特征相近的「看起来一样但格式不同」文件，区分视频、图片、全部三种扫描模式，可并排预览、批量删除。

## 为什么用它 / 适合什么场景

- **相册整理**：iCloud / Photos 库塞满多年截图与同款照片，找出真正占空间的「视觉孪生兄弟」；
- **素材库清理**：设计师素材盘里同一张图被转存了 PNG / JPG / WebP 三份，一次扫完；
- **本地视频去重**：把 4K 录像和手机压过的低码率版本对一遍。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多维度比对 | SHA-256 哈希、感知指纹、元数据、Vision 特征 |
| 三种模式 | 仅视频 / 仅图片 / 全部 |
| 并排预览 | 找到相似组后逐组并排比较 |
| 批量删除 | 勾选一键清理 |
| 浏览模式 | 排序、筛选文件列表 |

## 媒体 / 原始链接

![界面截图](https://pbs.twimg.com/media/HLZOLhRbEAAlLbM.jpg)

- 项目链接：<https://github.com/LiruiYu33/Targie-The-Similar-Videos-Images-Finder>

## 相关概念

- [OpenMac](concepts/tool-openmac.md) — 同样基于 macOS Vision 框架的本地工具，可与 Targie 配合做内容提取后去重