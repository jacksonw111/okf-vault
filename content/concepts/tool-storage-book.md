---
type: Tool
title: "storage-book + KnotFS（结绳记事到日志结构化文件系统教学）"
description: "从结绳记事讲到 Flash 物理、文件系统理论、LittleFS 源码剖析，并带动手实现的存储技术书，配一个教学级纯 C 日志结构化文件系统 KnotFS。"
resource: "https://github.com/Lularible/storage-book"
tags: [tool, storage, filesystem, littlefs, teaching, c]
timestamp: 2026-07-12T16:30:00Z
---

# storage-book + KnotFS（结绳记事到日志结构化文件系统教学）

## 它是什么
一本开源的存储技术书 + 配套教学级文件系统实现。书从结绳记事讲起，延伸到 Flash 物理、文件系统理论、LittleFS 源码剖析，并带动手实现；配套项目 KnotFS 是一个教学级纯 C 日志结构化文件系统（Log-Structured File System），用来印证书里的概念。

## 为什么用它 / 适合什么场景
- 想系统补存储 / 文件系统底层知识：从人文（结绳）到硬件（Flash）到理论（LSFT）到源码（LittleFS）。
- 想动手写一个最小可用的 LFS，从 0 实现到跑通基本 mount / read / write。
- 嵌入式开发需要为设备挑 / 改造文件系统（LittleFS / FAT / LFS），希望先理解底层。

## 关键能力
| 能力 | 说明 |
|------|------|
| 通识讲法 | 从结绳记事到现代存储的连贯叙述 |
| 硬件层 | Flash 物理特性、磨损均衡、坏块管理 |
| 理论层 | 文件系统理论、日志结构化思想 |
| 源码剖析 | LittleFS 源码逐段精读 |
| 配套实现 | KnotFS：教学级纯 C LFS，可编译运行 |

## 参考链接
- [项目链接](https://github.com/Lularible/storage-book)
- [原始链接](https://x.com/QingQ77/status/2076149045890830571)

## 相关概念
- [Linear Algebra Made Easy（线性代数交互式学习）](note-linear-algebra-made-easy.md) — 同类"教科书 + 配套实现"思路的学习资料