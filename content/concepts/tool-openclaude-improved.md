---
type: Tool
title: "openclaude-improved（多 AI 后端 CLI 编程代理）"
description: "TypeScript 写的命令行 AI 编程代理，支持 OpenAI、Ollama、Gemini、GitHub Models、Bedrock 等十几家 AI 后端。换模型不用改工具链——同一个 CLI 里改个配置就行。"
resource: "https://github.com/0xwilliamortiz/openclaude-improved"
tags: [ai-coding, cli, multi-provider, openai, ollama, gemini, bedrock, typescript]
timestamp: "2026-07-30T02:37:00.000Z"
---

# openclaude-improved

## 它是什么

**Provider-agnostic 的 CLI 编程代理**——同一个二进制里，可以无缝切换：

- OpenAI（gpt-4o / o1 / o3）
- Ollama（本地模型）
- Gemini（Google）
- GitHub Models
- AWS Bedrock
- 其他十几家 OpenAI 兼容端点

核心卖点：**不被任何一家模型厂商锁死**。今天用 Claude 风格的 CLI，明天要试本地 Llama，后天想切到 GPT-5，改一行配置即可，工具链、快捷键、工作流不用换。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多 backend 切换 | 十几家 provider，开箱即用 |
| OpenAI 兼容协议 | 接任意 OpenAI 兼容端点 |
| 配置文件驱动 | 切模型改 YAML / JSON |
| CLI 原生 | 不依赖 GUI，ssh 进去也能用 |
| TypeScript 实现 | 容易二次开发 / 加 provider |

## 适合谁

- 想自托管跑本地模型（Ollama）但又要保留 Claude Code / Codex 体验的团队
- 在多个云账号 / 多家供应商之间轮换的工程师
- 想脱离单一供应商绑定的组织（合规 / 成本 / 谈判筹码）

## 原始链接

- [项目仓库](https://github.com/0xwilliamortiz/openclaude-improved)
- [推文剪藏](https://x.com/QingQ77/status/2082656676306726978)

## 相关概念

- [pi-claude-bridge](./tool-pi-claude-bridge.md) — Pi 扩展，把 Claude Code 作为 provider 或 AskClaude 工具接入
- [opencode-cc](./tool-opencode-cc.md) — 把 OpenCode Zen 协议桥接为 Anthropic / OpenAI 兼容
- [animarouter](./tool-animarouter.md) — 聚合 16+ LLM 提供商免费额度到单一 OpenAI 兼容接口