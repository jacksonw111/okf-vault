---
type: "Tool"
title: "QuantoScript（PySudo/QuantoScript）"
description: "C 写的小脚本语言,既能当解释器跑也能编译成字节码虚拟机,还能把算得多的代码直接翻译成 C 提速,三档执行模型自适配。"
resource: "https://github.com/PySudo/QuantoScript"
tags: "[scripting-language, interpreter, bytecode, jit, transpiler, c]"
timestamp: "2026-07-15T08:48:00Z"
---

# QuantoScript

[QuantoScript](https://github.com/PySudo/QuantoScript) 是一套用 **C 写的脚本语言**,工程上同时提供三种执行模型:解释器、字节码虚拟机、热点路径直接翻译成 C 提速。

## 它解决了什么

很多脚本语言只能选一边——要么解释慢、要么启动慢、要么扩展复杂。QuantoScript 把三档塞进同一个运行时,启动慢的代码自动升档到字节码,热点代码自动翻译成 C 编译。

## 关键能力

| 能力 | 说明 |
|------|------|
| 三档执行模型 | 解释器 / 字节码 VM / C 代码生成 |
| 热点自适应 | 跑得多的代码自动转 C |
| 全栈 C 实现 | 解释器、编译器、运行库都 C 写 |
| 小语言易嵌入 | 可作为宿主程序的脚本引擎 |

## 参考链接

- [项目仓库](https://github.com/PySudo/QuantoScript)

## 相关概念

(无清晰相关概念,单飞)
