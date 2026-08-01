---
type: Tool
title: "bbarit-agent-oss"
description: "bbarit/bbarit-agent-oss，用 Rust 重写的开源终端 AI 编程助手，单文件静态二进制替代 Claude Code / Codex CLI，免 Node / Python，支持 15+ 模型供应商和 1000+ 模型。"
resource: "https://github.com/bbarit/bbarit-agent-oss"
tags: "[rust, ai-coding, cli, claude-code-alternative, codex-alternative, single-binary, llm-router]"
timestamp: "2026-08-01T20:30:00Z"
---

# bbarit-agent-oss

## 它是什么

[`bbarit/bbarit-agent-oss`](https://github.com/bbarit/bbarit-agent-oss) 是一个**用 Rust 重写的开源终端 AI 编程助手**，目标成为 Claude Code / Codex CLI 的本地化、零依赖替代品——**单文件静态二进制**，下载就能跑，不用装 Node 和 Python；同时内置**15+ 模型供应商和 1000+ 模型**的统一接入。

## 关键卖点

| 卖点 | 说明 |
|------|------|
| 单文件静态二进制 | 下载即用，免 Node / Python 运行时 |
| Rust 实现 | 启动快、内存占用低、跨平台编译 |
| 替代 Claude Code / Codex CLI | 接口 / 工作流对标主流 AI 编程 CLI |
| 15+ 模型供应商 | OpenAI / Anthropic / Gemini / Ollama / Groq / DeepSeek 等 |
| 1000+ 模型 | 上述供应商的全部模型都能直接切 |

## 解决什么痛点

- Claude Code / Codex CLI 需要 Node ≥ 18 或 Python，环境装起来烦
- 想在最小依赖环境（容器 / 服务器 / 老机器）跑 AI 编程助手
- 想要一个**不绑定特定模型供应商**的「通用 AI 编程 CLI」

## 适合什么场景

- 在 CI / 容器 / 远程开发机里跑 AI 编程助手，环境干净到不想装 Node
- 想在不同模型之间快速切换（OpenAI 主用、本地 Ollama 兜底）
- 想要一个**比 Claude Code / Codex 更轻**的替代品做嵌入式集成

## 与同类工具的差异

| 工具 | 语言 | 形态 |
|------|------|------|
| Claude Code | Node | 官方 CLI |
| Codex CLI | Node / Rust（混合） | 官方 CLI |
| [openclaude-improved](./tool-openclaude-improved.md) | TypeScript | 通用 CLI，多 provider |
| [claude-code-router](./tool-claude-code-router.md) | Go | 本地网关 + 故障切换 |
| bbarit-agent-oss | Rust | 单文件二进制通用 CLI |

## 原始链接

- [项目仓库](https://github.com/bbarit/bbarit-agent-oss)
- [原始推文](https://x.com/QingQ77/status/2083482367168073855)

## 相关概念

- [openclaude-improved](./tool-openclaude-improved.md) — 同为「一家 CLI 接多家模型」的思路，TypeScript 实现
- [claude-code-router](./tool-claude-code-router.md) — 本地网关层把多 AI 编程工具统一接到同一组模型凭据上