---
type: Tool
title: "go-llama（llama.cpp 的纯 Go 移植：零 cgo、零共享库、单静态二进制）"
description: "把 llama.cpp 的推理完整搬进纯 Go——不碰 cgo、不依赖任何 C 共享库，GGUF 模型在 Go 能编译到的任何平台都能跑，构建产物是单静态二进制。"
resource: "https://github.com/goccy/go-llama"
tags: [llama, gguf, golang, inference, llama.cpp, static-binary, port]
timestamp: "2026-08-28T00:00:00Z"
---

# go-llama

## 它是什么
[goccy/go-llama](https://github.com/goccy/go-llama) 是**llama.cpp 的纯 Go 移植**。

llama.cpp 本身是 C/C++ 实现，跑 GGUF 模型最快、覆盖面最广，但要在 Go 项目里集成就得用 **cgo**——而 cgo 意味着跨平台编译复杂、需要链接系统 C 库、产物不是单二进制、部署麻烦。

go-llama 把推理逻辑**完全重写**进 Go：

- **不碰 cgo**；
- **不依赖任何 C 共享库**；
- Go 能编译到的任何平台（Linux / macOS / Windows / BSD / ARM / MIPS …）都能跑 GGUF 模型；
- 构建产物是**单静态二进制**。

## 为什么用它 / 适合什么场景
- Go 项目想本地跑 GGUF 模型而**不想引入 cgo 复杂度**；
- 部署场景要求**单文件可执行**——拷一个二进制到目标机就完事；
- 跨平台分发——一份 Go 工具链能覆盖几乎所有架构；
- 看重**纯 Go 生态**的简单性、调试性、工具链一致性。

## 关键能力
| 能力 | 说明 |
|------|------|
| 纯 Go 实现 | 不调用任何 C 代码 / cgo |
| 零共享库 | 不依赖系统级 C 库 |
| GGUF 支持 | 完整支持 llama.cpp 主流 GGUF 模型 |
| 跨平台 | Go 能编译到的所有平台均能运行 |
| 静态二进制 | 单文件可执行，部署无外部依赖 |
| 性能 | 紧追 llama.cpp 主线持续优化 |

## 相关概念
- [Llama.cpp](tool-llama-cpp.md) — go-llama 的源头；两者关系类似 cgo llama.cpp ↔ 纯 Go 移植
- [Ollama](tool-ollama.md) — 同样面向 GGUF 模型，但走的是 CLI / 服务化路线；go-llama 是**库级别**的纯 Go 集成方案

## 参考链接
- 项目链接：<https://github.com/goccy/go-llama>
- 原始推文：<https://x.com/QingQ77/status/2093199143380631588>
