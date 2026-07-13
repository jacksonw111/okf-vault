---
type: Tool
title: "pon"
description: "用 Rust 写的 Python 3.14 原生编译器，把 Python 直接编译成机器码运行（同时支持 JIT 与 AOT 提前编译），不依赖解释器；目标是做成 Python 版的 bun / v8。"
tags: "[python, compiler, rust, jit, aot, native, tool]"
timestamp: "2026-07-13T00:00:00Z"
resource: "https://github.com/can1357/pon"
---

# pon

一个用 **Rust** 写的 **Python 3.14 原生编译器**——把 Python **直接编译成机器码**运行（同时支持 **JIT** 与 **AOT** 提前编译），**不依赖解释器**；目标做成 **Python 版的 bun / v8**。

## 它是什么

- 一款 **Python → 原生机器码** 的编译器（不是 CPython 加速、不是 Cython）；
- **Rust** 实现前端与后端，对接 Python 3.14 语法与语义；
- 双模式：**JIT**（运行时按需编译热点）与 **AOT**（提前编译成可执行文件）；
- 想成为 **Python 生态的 bun / v8**——给 Python 跑出接近 V8 / Bun 那种"原生级"的体验。

## 关键能力

| 能力 | 说明 |
|------|------|
| 原生机器码 | 直接编出可执行机器码，不经 CPython 字节码 |
| JIT 模式 | 运行时识别热点路径并即时编译，提升长跑 / 数值密集场景速度 |
| AOT 模式 | 提前编译为可分发的二进制，免装 Python 环境 |
| Rust 内核 | 编译器本身用 Rust 写，内存安全 + 可控性能 |
| Python 3.14 兼容 | 对齐 3.14 语法 / 语义，不是用旧版本凑数 |
| 无解释器依赖 | 不再需要 `python` runtime 解释执行 |

## 为什么用它 / 适合什么场景

- 想给 Python 拿到 **Node→Bun / Chrome→V8** 那种"换引擎 = 性能/体验双跳"的飞跃；
- 部署 **无 Python 环境的边缘设备 / 容器**——AOT 编出的二进制就是它自己；
- 跑**数值密集 / 长跑循环**的 Python 脚本，JIT 能榨出比 CPython 多得多的性能；
- 想做 **Python → 二进制分发**（命令行工具、内部服务、单机 app）的工程化流水线；
- 研究 **JIT / AOT 编译器**与 **Python 语义层**怎么干净对接——这是开源领域少见的真实实现。

## 与同类思路的对比

| 项目 | 思路 | 与 pon 的关系 |
|------|------|---------------|
| CPython | 解释器 + 字节码 | pon 的目标是**替换**它 |
| PyPy | JIT 解释器 | pon 是**编译成机器码**，绕过字节码层 |
| Cython | Python → C 静态编译 | pon 走 Rust / 自家后端，更现代 |
| mypyc | 类型注解驱动 AOT | pon 支持任意 Python 3.14 代码 |
| Nuitka | Python → C++ → 二进制 | pon 是**直接到机器码**，中间更薄 |
| bun | Node 的原生替身 | pon 想成为 **Python 的 bun** |

## 设计哲学

1. **Pythonic 不能丢**——3.14 语法 / 标准库行为要忠实复刻；
2. **Native 是终点**——要么 JIT 跑，要么 AOT 编，不要再回解释器；
3. **薄中间层**——避免 Python → C/C++ → 二进制那种多步翻译开销；
4. **Rust 是工具，不是枷锁**——Rust 编译器内核面向未来扩展与维护性。

## 预览

![](https://pbs.twimg.com/media/HNA5XPqbIAAZUq5.jpg)

## 相关概念

- [Colibri](tool-colibri-inference.md) — 同样"用底层语言榨性能"思路，做的是 MoE 推理引擎
- [dd（JIT 容器）](tool-dd-jit-container.md) — JIT 思路的另一个落地场景：在 macOS 上直接跑 Linux 容器