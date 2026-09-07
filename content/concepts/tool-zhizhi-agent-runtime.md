---
type: Tool
title: "zhizhi-agent-runtime"
description: "Go 应用的模型无关生产级 Agent 执行层：把普通 Go 函数包装成带校验的类型化工具，自动构建依赖安全的并行执行图，处理条件分支、有界重规划与副作用管控。"
resource: "https://github.com/cocoyes/zhizhi-agent-runtime"
tags: "[go, agent, runtime, typed-tools, execution-graph]"
timestamp: "2026-09-07T13:09:00Z"
---

# zhizhi-agent-runtime

## 它是什么
为 Go 应用提供的、与模型无关的生产级 Agent 执行层。开发者只需把普通 Go 函数"挂"到 runtime 上，runtime 会：

1. 把它包成带 schema 校验的"类型化工具"
2. 解析工具之间的依赖关系
3. 自动构建一个依赖安全的并行执行图
4. 处理条件分支（if / switch）、有界重规划（bounded replan）
5. 控制副作用（哪些工具改写外部状态、需不需要回滚）

## 核心特性
| 特性 | 说明 |
|------|------|
| 模型无关 | 不绑定 OpenAI / Anthropic / Ollama，可换 LLM |
| 类型化工具 | 函数签名 → JSON Schema，运行时校验 |
| 并行执行 | 依赖图自动并行无依赖分支 |
| 有界重规划 | 失败时重规划次数受限，不会无限循环 |
| 副作用管控 | 标记 / 隔离 / 回滚高风险工具调用 |

## 适用场景
- 把现有 Go 微服务改造成 Agent 工具集
- 需要"硬约束 + 类型安全 + 并行执行"的企业级 Agent 后端
- 想用 Go 而不是 Python 做 Agent 基础设施

## 关键能力
| 能力 | 说明 |
|------|------|
| 模型无关执行层 | 同 runtime 适配多家 LLM |
| 自动依赖图 | 函数签名推导依赖 |
| 并行执行 | 无依赖分支自动并发 |
| 有界重规划 | 失败策略可控 |
| 副作用管控 | 高风险动作隔离 |

## 参考
- 项目链接：<https://github.com/cocoyes/zhizhi-agent-runtime>

## 相关概念
- [Microsoft Agent Framework (Go 版)](tool-agent-framework-go-microsoft.md) — 另一个 Go 多智能体框架
- [VAF](tool-vaf.md) — Python 自主智能体框架，对比参考