---
type: "Tool"
title: "henrydennis/petal（macOS 实时磁盘 sunburst）"
description: "henrydennis 出品的 macOS 磁盘空间分析工具：用 getattrlistbulk + openat 铺满所有核边扫描边画精确到字节的 sunburst 图，附标注安全等级的可清理清单。"
resource: "https://github.com/henrydennis/petal"
tags: "[macos, disk-usage, sunburst, visualization, sysadmin]"
timestamp: "2026-10-04T03:00:00Z"
---

# petal

## 它是什么

[petal](https://github.com/henrydennis/petal) 是 **henrydennis** 出品的 macOS 磁盘空间分析工具——边扫描边画出精确到字节的 sunburst 图，并给出标注了**安全等级**的可清理清单。

## 关键能力

| 能力 | 说明 |
|------|------|
| 系统调用 | `getattrlistbulk` + `openat`（macOS 原生高效路径） |
| 并行 | 铺满所有核 |
| 速度 | 600 万文件约 25 秒 |
| 大目录响应 | 9 万条目文件夹 1 秒内出结果 |
| 可视化 | sunburst（多层环形），按 10 次/秒实时刷新快照 |
| 精度 | 精确到字节 |
| 输出 | 标注安全等级的可清理清单 |

## 适合场景

- macOS 磁盘满了想清出空间但不知道哪里能清
- 想看清「磁盘都被什么占着」的全貌
- 大目录扫描 / 重复文件查找前的概览

## 参考链接

- 项目链接：<https://github.com/henrydennis/petal>

## 相关概念

- [DaisyDisk](./tool-daisydisk.md) — 同类商业工具（macOS 老牌 sunburst 磁盘分析）