---
type: Tool
title: "lkv"
description: "嵌入式 KV 存储库，用哈希表换读性能与零拷贝查找，适合把配置 / 主数据这类不常改的内容存成本地文件——对比 LMDB / RocksDB 体积更轻、内存开销更小。"
resource: "https://github.com/nuskey8/lkv"
tags: "[kv, storage, embedded, hash-table, open-source]"
timestamp: "2026-08-13T19:53:00Z"
---

# lkv

## 它是什么
一个**嵌入式 KV（key-value）存储库**。嵌入式 KV 库不少，但读得快的（LMDB、RocksDB）要么**重**要么**内存开销大**——lkv 用**哈希表**换读性能与**零拷贝查找**，把「配置 / 主数据这种不常改的东西」存成本地文件。

## 为什么用它 / 适合什么场景
- 配置存储：应用启动读、运行期几乎不写的小数据集。
- 主数据：用户偏好、词典、查表数据。
- 需要 LMDB / RocksDB 级别的读性能，但不想要那层 B+ 树 / LSM 的复杂度与内存压力。
- 嵌入式 / 边缘设备场景，资源预算紧。
- 把 KV 当只读资源用——哈希表 + 零拷贝查找契合该场景。

## 关键能力
| 能力 | 说明 |
|------|------|
| 存储形态 | 嵌入式 KV |
| 数据结构 | 哈希表 |
| 查找 | 零拷贝 |
| 文件大小 | 相对 LMDB / RocksDB 更轻 |
| 内存开销 | 更小 |
| 适用数据 | 配置 / 主数据 / 查表 |

## 相关概念
- （暂无强相关概念——独立存储库）

## 媒体
- 示意图：<https://pbs.twimg.com/media/HPfYOoqbwAA4Z7L.png>

## 项目链接
- 项目主页：<https://github.com/nuskey8/lkv>