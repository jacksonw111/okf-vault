---
type: "Tool"
title: "binja-diff（matteyeux/binja-diff）"
description: "Binary Ninja 插件,用 QBinDiff 做引擎,处理两个二进制的并排对比;把第二个文件拖到 diff 视图上,自动分析并按函数对齐,差异分控制流图 / 汇编 / LLIL / MLIL / HLIL 五层展示。"
resource: "https://github.com/matteyeux/binja-diff"
tags: "[binary-ninja, reverse-engineering, diff, qbindiff, plugin, security]"
timestamp: "2026-08-11T16:00:00Z"
---

# binja-diff

[binja-diff](https://github.com/matteyeux/binja-diff) 是 Binary Ninja 的**插件**,以 [QBinDiff](https://github.com/bquarks/QBinDiff) 做引擎,把两个二进制放一起做并排对比;拖入第二个文件即可自动分析并按函数对齐,差异按**控制流图 / 汇编 / LLIL / MLIL / HLIL 五层**展示。

项目链接：<https://github.com/matteyeux/binja-diff>

## 它是什么

Binary Ninja 的**二进制差异分析插件**:面向逆向工程师,解决"两个版本二进制到底改了什么"的问题,从高层语义到低层汇编全覆盖。

## 为什么用它 / 适合什么场景

- **二进制 patch 分析**:对比发布版 vs 上一版,定位改动的函数与代码块。
- **多层级展示**:CFG / 汇编 / LLIL / MLIL / HLIL 五层,从高级语义到底层细节都可对照。
- **QBinDiff 引擎**:成熟的二进制 diff 引擎,函数对齐准确度高。

## 关键能力

| 能力 | 说明 |
|------|------|
| QBinDiff 引擎 | 成熟的二进制 diff 函数对齐 |
| 拖放触发 | 把第二个文件拖到 diff 视图即开始 |
| 五层差异展示 | CFG / 汇编 / LLIL / MLIL / HLIL |
| 函数自动对齐 | 跨二进制同名 / 同结构函数自动匹配 |
| Binary Ninja 集成 | 与 BN 主流程无缝衔接 |
| 适合逆向分析 | 找补丁 / 找后门 / 比对版本改动 |

## 媒体

![](https://pbs.twimg.com/media/HPU47JZasAAg9TW.jpg)

## 参考链接

- [项目仓库](https://github.com/matteyeux/binja-diff)

## 相关概念

- [Falco (Rust browser engine)](./tool-falco-browser-engine.md) — 浏览器引擎逆向工程,本工具是另一类二进制分析路线