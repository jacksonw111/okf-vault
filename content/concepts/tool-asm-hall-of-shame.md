---
type: "Tool"
title: "asm-hall-of-shame"
description: "xoreaxeaxeax（movfuscator 作者）写的「汇编指令延迟耻辱柱」：别人分析指令延迟是为了把代码跑快，这个仓库反着来——专门找单条指令最慢能慢到多少。"
resource: "https://github.com/xoreaxeaxeax/asm-hall-of-shame"
tags: [assembly, performance, x86, optimization, movfuscator]
timestamp: "2026-08-09T19:35:00Z"
---

# asm-hall-of-shame

## 它是什么

[asm-hall-of-shame](https://github.com/xoreaxeaxeax/asm-hall-of-shame) 是 movfuscator 作者 xoreaxeaxeax 开的「**汇编指令延迟耻辱柱**」：别人分析指令延迟是为了把代码跑快，**这个仓库反着来**——专门记录「单条 x86 指令最慢能慢到多少」，给编译器 / CPU 微码研究者做反例参考。

## 为什么用它 / 适合什么场景

- 编译器 / 操作系统 / 模拟器开发者：想知道某些指令在特定输入下的最坏延迟。
- 性能工程师：理解 CPU 微架构边界，识别不可优化的「延迟陷阱」。
- 安全研究：某些 x86 指令的可变延迟是 Spectre / MDS 等侧信道攻击的基础。
- 教学：用「最坏情况」案例讲清微架构差异（μops / 端口竞争 / 缓存命中）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 反例汇编 | 汇编「最坏延迟」清单 |
| x86 聚焦 | 覆盖 x86 / x86-64 主流指令 |
| 教学导向 | 配套解释为什么慢（端口 / μops / 微码） |
| 配套项目 | 作者的 [movfuscator](https://github.com/xoreaxeaxeax/movfuscator) 把整个程序编译成 `mov` 指令流 |

## 媒体

![](https://pbs.twimg.com/media/HPPlprKa0AAIfL0.jpg)

## 相关概念

（暂无直接相关概念）