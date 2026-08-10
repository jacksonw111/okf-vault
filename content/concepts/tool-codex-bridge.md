---
type: "Tool"
title: "codex-bridge"
description: "Sateezg 开源的 Claude Code 插件：把 Codex CLI 里已有的 ChatGPT 登录借过来，让 Claude 不用配 OpenAI API key 也能调用 gpt-image-2 出图，以及把重活路由到 GPT-5 子代理。"
resource: "https://github.com/Sateezg/codex-bridge"
tags: [claude-code, codex, gpt-image-2, gpt-5, plugin, bridge]
timestamp: "2026-08-10T12:07:00Z"
---

# codex-bridge

## 它是什么

[codex-bridge](https://github.com/Sateezg/codex-bridge) 是一个装进 Claude Code 的小插件：观察到一个具体痛点——**Claude 自己不擅长出图，重活都跑又烧光 Claude 配额**。这个插件把 Codex CLI 里**已经存在的 ChatGPT 登录会话**借过来，让 Claude 在需要出图时直接调 gpt-image-2，在需要把脏活累活甩出去时丢给 GPT-5 子代理。OpenAI API key 都不用配——靠的是借用 Codex CLI 里已经 OAuth 过的会话。

## 为什么用它 / 适合什么场景

- 想在 Claude Code 里直接出图，又不想单独申请 / 计费 OpenAI API key。
- 想把 Claude 处理不了的「高 reasoning / 重度计算」任务下放给 GPT-5，省 Claude 配额。
- 同时用 Codex CLI 的用户：插件复用同一份 ChatGPT 登录会话，不引入新账号。

## 关键能力

| 能力 | 说明 |
|------|------|
| 借 ChatGPT 登录 | 不配 OpenAI API key 就能用 |
| gpt-image-2 出图 | Claude 直接调用原生图像生成 |
| GPT-5 子代理 | 把脏活路由出去，省 Claude 配额 |
| 装入 Claude Code | 一次安装即用 |

## 参考链接

- [项目仓库](https://github.com/Sateezg/codex-bridge)
- [原始链接](https://x.com/QingQ77/status/2086786388222177675)

## 相关概念

- [Lupin](./tool-lupin.md) — 把 Claude Code 整套壳借给别的模型用，反向操作（这里是把 ChatGPT 登录借给 Claude）
- [modeldock](./tool-modeldock.md) — Codex 里给 DeepSeek 补识图 / 语音 / 联网 / 记忆的 Responses 桥接
