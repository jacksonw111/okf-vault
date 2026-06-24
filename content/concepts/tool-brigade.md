---
type: "Tool"
title: "Brigade（spinabot/brigade）"
description: "本地运行的 AI 代理团队系统，多个 agent 共享 Tideline 长期记忆，可互相派活，支持 Claude / GPT / Gemini / Llama 任意切换。"
resource: "https://github.com/spinabot/brigade"
tags: [agent, multi-agent, local-first, memory, mcp]
timestamp: "2026-06-23T15:30:00Z"
---

# Brigade（spinabot/brigade）

## 它是什么

一个开源的多 AI 代理协作框架。在本机启动一组共享长期记忆的代理，让它们像「一人公司里的几位同事」那样互相派活、接力写报告、定时巡检任务；底层使用自研的 Tideline 记忆协议，模型可随时换（Claude、GPT、Gemini、Llama），不会因换模型而丢失上下文。

## 为什么用它 / 适合什么场景

- **多代理实验**：想在本地复刻 AutoGen / CrewAI 那种「主管 + 助手」编排，但不想被云端 SaaS 绑死；
- **私有数据**：所有会话 / 记忆都留本机，零外部调用，企业内部研究合规友好；
- **跨模型稳定性**：换底层 LLM 时记忆不丢，可以做 A/B 对比实验。

## 关键能力

| 能力 | 说明 |
|------|------|
| Tideline 长期记忆 | 多代理共用的会话/事实/任务状态存储 |
| 模型可插拔 | Claude / GPT / Gemini / Llama 等都支持 |
| 多入口交互 | 终端聊天 / WhatsApp / 定时任务 / 子代理并行 |
| 上千应用连接器 | 通过 Composio 集成主流 SaaS |
| MCP 记忆服务 | 暴露为 MCP server，便于其它代理读取 |

## 媒体 / 原始链接

![架构示意](https://pbs.twimg.com/media/HLc9gMfaIAAnUle.jpg)

- 项目链接：<https://github.com/spinabot/brigade>

## 相关概念

- [ORGII](tool-orgii.md) — 同样把 AI 当「同事」的 Rust + Tauri 多 Agent 协作框架
- [EverOS](tool-everos.md) — 同样提供统一长期记忆层，让不同 agent 共享与进化记忆
- [Agent Skills](term-agent-skills.md) — 角色与工作流的打包方式