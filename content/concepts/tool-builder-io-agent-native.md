---
type: "Tool"
title: "BuilderIO/agent-native"
description: "BuilderIO 推出的「agent-native 仓库」：把 AI agent 在前端项目里能直接用上的脚手架、模式与文件组织方式打包，让 agent（Claude Code、Codex 等）能像人一样 fork 后立即接手 React/Vue/Next 项目。"
tags: "[agent, frontend, builderio, scaffold, ai-native]"
timestamp: "2026-06-20T00:00:00Z"
resource: "https://github.com/BuilderIO/agent-native"
---

# BuilderIO / agent-native

## 它是什么

[`BuilderIO/agent-native`](https://github.com/BuilderIO/agent-native) 是 BuilderIO 推出的「**agent-native 仓库模板**」——**不是给前端工程师用的 starter，而是给 AI agent 用的**。它把 agent 在前端项目里能直接调用的脚手架、目录约定、模式封装好，让 Claude Code、Codex、Cursor 等 agent 客户端能像人一样「fork → 接管」一个 React/Vue/Next 项目。

## 解决了什么问题

普通前端项目对 agent 并不友好：

- 依赖一装半天（agent 容易被卡在 `pnpm install` / 锁文件冲突）
- 配置文件散落各处（agent 不知道哪个是 source of truth）
- 约定只在 CONTRIBUTING.md 里写一行（agent 读不到上下文）

**agent-native** 的策略是：

1. **预装好一切**：仓库 clone 下来 `pnpm i` 就能跑；agent 不用装环境
2. **结构化约定**：用目录命名 + 注释明确告诉 agent「这一层是放什么的」
3. **典型工作流预设**：跑测试 / 跑 lint / 启 dev server / 发 PR 的命令都封装好
4. **可被 agent 调用的 helper**：内置 agent skill / slash command，让 agent 能直接 `pnpm agent:check` 之类的工具

## 关键能力

| 能力 | 说明 |
|------|------|
| 预装依赖 | 仓库 clone 后无需 `pnpm i` 之外的操作 |
| 目录约定 | 用结构 + README 注释告诉 agent "这是什么/为什么" |
| 内置 skill | agent 客户端可直接调用的 helper（check / build / deploy） |
| 跨框架 | 同套约定适用于 React / Next / Vue / Svelte 等 |
| 渐进式 fork | 不必从零搭——fork 这个仓库 → 改业务代码即可 |

## 怎么用

```bash
# 1. fork 或 clone
git clone https://github.com/BuilderIO/agent-native
# 2. 让 agent 接管
# Claude Code / Codex / Cursor 打开后，agent 能直接读懂结构、跑命令
# 3. 开始改业务
```

## 适用场景

- **从零起一个 React/Vue 项目**，不想从 starter 又配一遍 → agent-native 给你「agent ready」状态
- **多 agent 协作**：每个 agent 拿一份 fork，约定一致不用重新对齐
- **AI 编码 demo / 教程**：教学时 agent 一上手就能跑，避免"装环境"打断学习流

## 与本知识库的关系

- 与 [Niamos](tool-niamos.md) 思路同源：**仓库即约定、约定即文档、agent 直接能读**——Niamos 服务于「Obsidian 知识库」，agent-native 服务于「前端代码项目」
- 与 [Agent Skills 是什么](term-agent-skills.md)：agent-native 内置的 helper / slash command 本身就是一份**针对前端项目的 Skill 集合**
- 与 [Claude Code](tool-claude-code.md)：Claude Code 是这个仓库最常见的消费客户端

## 相关概念

- [Niamos](tool-niamos.md) — 同思路的「Obsidian 知识库版」agent-ready 仓库
- [Agent Skills 是什么](term-agent-skills.md) — agent-native 内置的 helper 实际就是一份 Skill 集合
- [Claude Code](tool-claude-code.md) — 最常见的 agent-native 消费客户端
- [Cabinet](tool-cabinet.md) — 另一个把"agent 友好的知识/工作台"做到位的工具
