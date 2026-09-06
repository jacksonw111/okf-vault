---
type: Tool
title: "Flea"
description: "给 Omarchy 写的独立文件管理器：Quickshell 做界面、Rust 做后端；后端拿全量目录，窗口只留看得见的行；10 万个文件约 1.2 秒就绪，比 dolphin 快 4 倍多。"
resource: "https://github.com/thisisgm/flea"
tags: [file-manager, omarchy, rust, quickshell, linux]
timestamp: "2026-09-06T00:00:00Z"
---

# Flea

## 它是什么

[thisisgm/flea](https://github.com/thisisgm/flea) 是给 [Omarchy](https://omarchy.org/) 写的**独立文件管理器**：前端用 Quickshell，后端用 Rust。架构上把**全量目录**在后台拿齐、**窗口只渲染可见行**，因此即使超大规模目录也能秒开。

定位：

- **Omarchy 专属**：深度集成到 Omarchy Linux 发行版的桌面环境。
- **极致性能**：作者跑了可复现基准——10 万个文件约 **1.2 秒就绪**，比 Dolphin 快 4 倍多。

## 为什么用它 / 适合什么场景

- 在用 Omarchy，想找一个原生、极速的文件管理器。
- 日常管理大目录（10 万+ 文件）时，主流文件管理器卡顿。
- 喜欢「后台全量数据 + 窗口只渲染可见」的现代 GUI 思路。

## 关键能力

| 能力 | 说明 |
|------|------|
| 极速首屏 | 10 万文件 ≈ 1.2 秒就绪 |
| 内存 / CPU | 在同类工具中排前列 |
| 缩略图优化 | 只在停下来时加载当前屏的缩略图 |
| Quickshell 前端 | 深度集成 Omarchy 桌面 |
| Rust 后端 | 单二进制、高性能 |
| 全量后台 | 后端拿全量目录，前端按需渲染 |

## 相关概念

- [Obsidian](./tool-obsidian.md) — 文件组织视角相关，但 Obsidian 是笔记 / 知识库管理器
- [Niamos](./tool-niamos.md) — 同类「为特定生态定制的工具」思路

## 项目链接

- 项目主页：<https://github.com/thisisgm/flea>
- 原始推文：<https://x.com/QingQ77/status/2096392183188480255>
