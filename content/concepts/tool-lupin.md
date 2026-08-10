---
type: "Tool"
title: "Lupin"
description: "Fanfulla 开源的本地代理：把 Claude Code 的「壳」借给别的模型用——MCP 服务器、Skills、CLAUDE.md、hooks、记忆、插件配置原样保留；带真实会话评分工具告诉用户借过来的模型扛不扛得住。"
resource: "https://github.com/Fanfulla/Lupin"
tags: [claude-code, model-routing, eval, mcp, skills, local-agent]
timestamp: "2026-08-10T09:39:00Z"
---

# Lupin

## 它是什么

[Lupin](https://github.com/Fanfulla/Lupin) 是个跑在本地的小代理，核心思路是 **Claude Code 的外壳不动，里面换成别的模型**：MCP 服务器、Skills、CLAUDE.md、hooks、记忆、插件**全部照旧**，开发者不用重配。通路选择上自己动脑子——Kimi、DeepSeek、GLM、Ollama 这些本来就讲 Anthropic 协议的直连；OpenAI、Gemini 按量计费的走翻译层；ChatGPT 订阅和 Gemini Code Assist 订阅则是私有协议，各配一个翻译器，OAuth 登录就能用。

更关键的是它附带一个**真实会话评分工具**——拿真实工作会话去跑借过来的模型，给量化评分，把「这个模型扛不扛得住」从感觉变成数字。

## 为什么用它 / 适合什么场景

- 已经有完整的 Claude Code Skills / MCP 配置，但想把模型切到 Kimi / DeepSeek / GLM 来降本——不想为换模型重写技能栈。
- 想做 AB：同一套 Skills / MCP 在多个模型上的实际表现差异，肉眼能感觉但需要量化工具。
- 想用 ChatGPT 订阅（含 GPT-5 / Code Assist）但又希望保持 Claude Code 工作流与生态。

## 关键能力

| 能力 | 说明 |
|------|------|
| 壳不变换模型 | Claude Code 整套配置原样保留 |
| 多协议适配 | Anthropic 直连 / OpenAI 翻译 / 订阅私有翻译 |
| OAuth 登录 | ChatGPT 订阅 / Gemini Code Assist 订阅直登 |
| 会话评分工具 | 真实工作会话量化打分，借过来的模型也能量化评估 |

## 媒体

- 视频：<https://video.twimg.com/amplify_video/2086402012518940672/vid/avc1/1920x1080/SVKQ4Ztik9g-HARo.mp4?tag=29>

## 参考链接

- [项目仓库](https://github.com/Fanfulla/Lupin)
- [原始链接](https://x.com/QingQ77/status/2086749142798532672)

## 相关概念

- [pi-bifrost](./tool-pi-bifrost.md) — Pi 的模型自动切换层，按任务复杂度 / 价格 / 速度路由，同属「把多家模型统一到一个 agent 外壳里」
- [Vigla](./tool-vigla.md) — Claude Code / Codex CLI / Antigravity 统一面板 + 授权边界 + 一键回退
