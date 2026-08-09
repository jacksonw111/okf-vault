---
type: "Tool"
title: "macos-disk-cleanup"
description: "himynameisben 写的 macOS 只读磁盘清理扫描脚本：按危险程度分级列出可疑「系统资料」，覆盖 ~/.cache/uv / ~/.npm / ~/.gradle 等藏在用户目录的包管理器缓存；扫描是只读的，40 秒出一份报告，--deep 加查各语言包管理器缓存。"
resource: "https://github.com/himynameisben/macos-disk-cleanup"
tags: [macos, cleanup, disk-space, cli, package-manager-cache]
timestamp: "2026-08-09T19:35:00Z"
---

# macos-disk-cleanup

## 它是什么

[himynameisben/macos-disk-cleanup](https://github.com/himynameisben/macos-disk-cleanup) 是一个**只读扫描** macOS 磁盘空间的脚本：扫描脚本本身不会删除任何东西，仅按危险程度分级列出「占空间但说不清来源」的目录，方便人工确认后再清理。设计上偏向「谨慎」——任何被认为有风险的目标都不会自动清掉。

## 为什么用它 / 适合什么场景

- macOS「关于本机 → 储存空间」报告的颗粒度太粗，定位不到深层的包管理器缓存。
- 想清理 `~/.cache/uv`、`~/.npm`、`~/.gradle`、`~/Library/Caches` 等藏在用户目录的目录。
- 想做一次「按危险等级」的盘点，再人工决策哪些能删、哪些要保留。
- 想在 CI / 容器镜像 / 临时开发机里快速定位可瘦身点。

## 关键能力

| 能力 | 说明 |
|------|------|
| 只读扫描 | 脚本不删除任何文件，仅输出报告 |
| 危险分级 | 报告按「安全 / 谨慎 / 不建议自动清」分级，方便人工判断 |
| 用户目录深扫 | `~/.cache/uv`、`~/.npm`、`~/.gradle`、`~/Library/Caches` 等包管理器缓存 |
| `--deep` 选项 | 额外查各语言包管理器缓存与开发工具运行时残留 |
| 报告输出 | 40 秒内出一份分级清单，可定向清理 |

## 相关概念

- [appmop](./tool-appmop.md) — macOS 应用连带残留一起丢进废纸篓的清理工具