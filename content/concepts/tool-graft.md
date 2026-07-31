---
type: "Tool"
title: "graft（NanoNets/Graft）"
description: "把代码的依赖关系与模块边界预先整理成 Markdown，让 AI 编码助手（Cursor / Claude Code / Codex…）进仓库第一时间拥有「地图」，无需每次重新扫描文件结构。"
resource: "https://github.com/NanoNets/Graft"
tags: "[ai-coding, codebase-context, code-map, agent-onboarding, repository-awareness]"
timestamp: "2026-07-31T20:30:00Z"
---

# graft（NanoNets/Graft）

[graft](https://github.com/NanoNets/Graft) 是一款**给代码仓库预先画「结构地图」的工具**：它把代码的**依赖关系和模块边界**整理成 Markdown 文档，供 AI 编码 agent 启动时直接读取，省掉每次进仓库重新梳理文件结构的时间。

## 它是什么

把「代码 → 适合 agent 阅读的 Markdown」固化下来：

- AI 编码助手通常进新仓库要花大量回合爬文件、理解 import 关系、找到模块边界
- graft 一次性把这些信息生成可读的 Markdown，作为项目长期工件
- agent 启动时直接读它，跳过冷启动成本

## 为什么用它 / 适合什么场景

| 痛点 | graft 怎么解 |
|------|--------------|
| AI 进新仓库第一回合都在「爬文件」 | 直接读预生成的 Markdown 地图 |
| 复杂 monorepo 找不到主从模块 | 模块边界在 Markdown 里一目了然 |
| 多 agent 协作时各扫一遍仓库 | 同一份地图给所有 agent 共用 |
| 改动后的依赖关系容易过期 | 把 graft 当 pre-commit / CI 步骤定期重生成 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 依赖关系抽取 | import / require / package.json 关系汇总 |
| 模块边界识别 | 圈出项目核心模块和对外接口 |
| Markdown 输出 | 适合塞进 repo 根目录直接喂 agent |
| 与 agent 协同 | 当作项目 AGENTS.md / CLAUDE.md 的一部分 |

## 相关概念

- [Claude Code](./tool-claude-code.md) — 终端原生 AI 编码 agent，graft 的 Markdown 地图可直接喂给它
- [vibe-coding-rules](./tool-vibe-coding-rules.md) — 同样给 AI agent 装「前置上下文」，但聚焦编码纪律而非代码结构
- [Agent Skills（代理技能包）](./term-agent-skills.md) — graft 的产出可视为一种项目级「skill」
- [Toolcraft](./tool-toolcraft.md) — 配套 AI 指令让 agent 直接出视觉工具，跟 graft 同属「为 agent 准备 context」的范式
- [codebase-memory-mcp](./tool-codebase-memory-mcp.md) — 类似思路：让 agent 长期记住仓库结构
