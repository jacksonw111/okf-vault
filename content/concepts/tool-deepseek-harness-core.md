---
type: Tool
title: "deepseek-harness（deepseek-ai 官方开源可插拔智能体框架）"
description: "DeepSeek 官方开源的智能体框架：推理循环每个环节（模型适配、工具、存储乃至 agent loop）都做成可插拔插件，可在配置层面整体替换，不必改内核。"
resource: "https://github.com/deepseek-ai/deepseek-harness"
tags: [deepseek, agent-framework, plugin, inference-loop, open-source, pluggable]
timestamp: "2026-08-29T21:30:00Z"
---

# deepseek-harness（deepseek-ai 官方开源可插拔智能体框架）

## 它是什么

[deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) 是 DeepSeek 官方开源的**智能体框架**：把推理循环（inference loop）的**每一个环节**——模型适配、工具调用、存储、会话记忆、甚至 agent loop 本身——都做成**可插拔插件**。

设计哲学：**配置可替换、内核不动**。任何想换的部分都不必改 dsh 源码，而是写一个 plugin、在配置里挂上去。这意味着：

- 同一套框架里可以混用不同 LLM（DeepSeek / Claude / 本地模型）；
- 工具集可以按场景整体替换（开发 / 客服 / 数据 / 浏览器 agent）；
- 存储后端可换（SQLite / Postgres / 向量库）；
- agent loop 策略本身也能换（ReAct / Plan-and-Execute / 多 agent 协作）。

## 为什么用它 / 适合什么场景

- 想用 DeepSeek 官方维护的 agent 框架，避开社区 fork 碎片化；
- 团队需要「一套框架、多种 agent 配置」，而不是为每个场景单独部署；
- 写 plugin 而不是改内核——长期可维护；
- 与 [deepseek-harness-handbook](./note-deepseek-harness-handbook.md) 等中文教程配套学习。

## 关键能力

| 能力 | 说明 |
|------|------|
| 全链路可插拔 | 模型 / 工具 / 存储 / loop 都能替换 |
| 配置驱动 | 不改代码，只改配置 |
| 模型无关 | DeepSeek / Claude / 本地 GGUF 都可挂 |
| 工具可换 | 整套工具集按场景整体替换 |
| 存储可换 | SQLite / Postgres / 向量库后端 |
| Loop 可换 | ReAct / Plan-Execute / 多 agent 协作 |
| DeepSeek 官方 | 与 deepseek-ai 其它项目（DeepSeek-V3 / R1 等）同源 |

## 相关概念

- [deepseek-harness-handbook](./note-deepseek-harness-handbook.md) — DeepSeek Harness 中文零基础手册
- [deepseek-harness-orange-book](./note-deepseek-harness-orange-book.md) — DSH 开源 24h 后写的非开发者视角电子书
- [deepseek-harness-desktop](./tool-deepseek-harness-desktop.md) — 把官方 Web UI 打包成桌面应用的壳
- [deepseek-harness-rs](./tool-deepseek-harness-rs.md) — DSH 的 Rust 绑定
- [deepseek-harness-studio](./tool-deepseek-harness-studio-fufankeji.md) — DSH 的图形化配置 / 调试工具
- [awesome-deepseek-harness](./tool-awesome-deepseek-harness.md) — DSH 周边生态汇总

## 参考链接

- 项目链接：<https://github.com/deepseek-ai/deepseek-harness>
- 原始推文：<https://x.com/QingQ77/status/2093683082503094564>
- 媒体：<https://pbs.twimg.com/media/HQ4YoJOaMAAiTRk.jpg>