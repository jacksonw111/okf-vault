---
type: Tool
title: "opencode-cc"
description: "高性能 API 代理，把 OpenCode Zen 协议桥接到 Anthropic / OpenAI 兼容格式，让 Claude Code / Codex CLI 等工具透明使用国产模型。"
resource: "https://github.com/Kiowx/opencode-cc"
tags: "[api-proxy, anthropic, openai, opencode, claude-code, codex, china-llm]"
timestamp: "2026-07-02T10:15:00Z"
---

# opencode-cc

## 它是什么
高性能 API 代理服务器。把 OpenCode Zen 协议桥接成 Anthropic 兼容 / OpenAI 兼容格式，让 Claude Code、Codex CLI 等「硬编码 Anthropic / OpenAI 协议」的工具能够透明调用国产大模型（DeepSeek / Qwen / GLM 等）。

## 为什么用它 / 适合什么场景
- 已经在用 Claude Code / Codex CLI，但希望把后端模型替换成国产（成本、合规或网络原因）。
- 想一份配置同时管理 Anthropic 协议 + OpenAI 协议工具链。
- 想要一个高性能（带优化）的中转代理，避免自建反向代理的性能瓶颈。

## 关键能力
| 能力 | 说明 |
|------|------|
| 协议桥接 | OpenCode Zen ↔ Anthropic 兼容 / OpenAI 兼容 |
| 透明替换 | Claude Code / Codex CLI 无需修改代码 |
| 高性能 | 代理层做了性能优化 |
| 国产模型支持 | 让 Claude Code / Codex CLI 能用 DeepSeek / Qwen / GLM 等 |

## 相关概念
- [Proxide](tool-proxide.md) — 同类「让任意 Agent 透明使用网页 / 多源模型」思路；opencode-cc 专注协议层桥接
- [pi-claude-bridge](tool-pi-claude-bridge.md) — Pi ↔ Claude Code 的双向桥；opencode-cc 是协议层转换
- [animarouter](tool-animarouter.md) — 多 LLM 路由器；opencode-cc 是协议转换器，两者可叠加使用
- [MCO](tool-mco.md) — 多代理编排层；opencode-cc 是模型层协议适配

## 项目链接
- 项目主页：<https://github.com/Kiowx/opencode-cc>

## 媒体
![](https://pbs.twimg.com/media/HMI-08Ua4AAYseL.jpg)