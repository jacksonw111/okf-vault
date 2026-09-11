---
type: "Tool"
title: "fanzha-ai-proxy（国家反诈 AI 反向代理）"
description: "把\"国家反诈AI\"智能助手转成标准 OpenAI 兼容接口的反向代理，让 NextChat、LobeChat 等主流客户端能直接调用。"
resource: "https://github.com/lfzk550/fanzha-ai-proxy"
tags: "[openai, reverse-proxy, llm-gateway, ai-chat]"
timestamp: "2026-09-11T22:00:00Z"
---

# fanzha-ai-proxy

## 它是什么

[fanzha-ai-proxy](https://github.com/lfzk550/fanzha-ai-proxy) 是一个**轻量级反向代理**：把\"国家反诈AI\"智能助手封装为标准 OpenAI 兼容 API（`/v1/chat/completions` 等），任何支持 OpenAI API 协议的客户端（NextChat、LobeChat、ChatBox、Open WebUI 等）只需填入该代理的 base URL + 默认 key，就能直接调用反诈 AI 的对话能力，无需登录官方页面。

## 为什么用它 / 适合什么场景

- 想在自托管 / 第三方 Chat UI 里调用反诈 AI 模型，而不愿用网页端。
- 想把反诈 AI 接入自动化脚本、命令行、Agent 工作流。
- 想统一管理多个 LLM 接入（自家 + 公开反诈 AI 一起走 OpenAI 协议）。
- 纯粹出于学习目的，了解 OpenAI 协议反向代理如何实现。

## 关键能力

| 能力 | 说明 |
|------|------|
| OpenAI 兼容 | 标准 `/v1/chat/completions` 接口，messages 流式 / 非流式均支持 |
| 一键部署 | Python / Node 单文件即可启动，配好上游地址和端口即用 |
| 客户端通用 | NextChat / LobeChat / Open WebUI 等填 base URL 就能调 |
| 协议透明 | 上游是反诈 AI，下游是 OpenAI 协议，客户端无感 |

## 参考链接

- 项目仓库：<https://github.com/lfzk550/fanzha-ai-proxy>

## 相关概念

- [Enzo（自托管 LLM 网关）](./tool-enzo.md) — 同样把多家上游封装成 OpenAI 兼容接口
- [Open GENAI](./tool-open-genai.md) — 数字厅 GENAI 本地化版本，统一鉴权 + 模型路由
</content>
</invoke>