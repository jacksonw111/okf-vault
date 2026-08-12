---
type: "Tool"
title: "Qwen-MM-Plugins"
description: "通义千问团队的多模态插件仓库：把多模态能力做成 skill + MCP server 插件，装到 Claude Code、Codex 等智能体框架里直接用，让任意智能体框架「多模态原生」而不用改框架。"
resource: "https://github.com/QwenLM/Qwen-MM-Plugins"
tags: ["qwen", "multimodal", "mcp", "skill", "agent", "plugin", "alibaba"]
timestamp: "2026-08-12T00:11:00Z"
---

# Qwen-MM-Plugins

[Qwen-MM-Plugins](https://github.com/QwenLM/Qwen-MM-Plugins) 是通义千问团队发布的**多模态插件仓库**，目标：让任意智能体框架"多模态原生"——但不必改框架本身。

## 它是什么

把图像、音频、视频等多模态能力封装成标准的 **skill + MCP server** 插件，装到 Claude Code、Codex 等现有智能体框架里就能直接调用。

## 为什么用它 / 适合什么场景

- **给现有 agent 加多模态**：不必 fork 或 hack 框架。
- **统一插件协议**：skill + MCP server 是当前 agent 生态的主流接口。
- **官方背书**：QwenLM 团队维护，质量和适配性有保障。
- **跨框架兼容**：Claude Code / Codex 都能用。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多模态能力封装 | 图像 / 音频 / 视频等的处理能力打包 |
| Skill 格式 | 符合主流 agent skill 开放规范 |
| MCP server | 通过 Model Context Protocol 提供工具 |
| 框架无关 | 装到任何支持 skill/MCP 的 agent 框架里即可 |
| 官方维护 | 通义千问团队持续更新 |

## 媒体

![](https://pbs.twimg.com/media/HPXdXcOboAAF9Q7.jpg)

## 参考链接

- [项目仓库](https://github.com/QwenLM/Qwen-MM-Plugins)

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — 多模态插件以 skill 形式分发
- [Gmail MCP](./tool-gmail-mcp.md) — 同属 MCP server 形式的工具扩展
- [Qwen AgentWorld](./tool-qwen-agentworld.md) — 通义千问的另一开源 agent 项目