---
type: Tool
title: "EchoesVault（OpenCode 持久记忆插件）"
description: "OpenCode 的持久记忆插件，提供 Obsidian 风格的知识库系统：会话结束自动记录决策与架构变化，下次 /echoes-start 一口气读回最近 3 天的日志和索引，使用 Google OKF 标准保证互通。"
resource: "https://github.com/psinetron/echoes-vault-opencode"
tags: [opencode, memory, obsidian, okf, knowledge-base, plugin]
timestamp: 2026-06-26T16:50:00Z
---

# EchoesVault（OpenCode 持久记忆插件）

## 它是什么

EchoesVault 是给 [OpenCode](https://opencode.ai/)（一个 AI 编码 Agent 终端工具）的**持久记忆插件**，目标是让 AI 代理在**会话之间保持记忆连续性**——下次开局不用再"喂一遍上下文"。

工作流：

1. 每次会话结束 → 自动把当天的**决策、架构变化、关键节点**写进 `EchoesVault/` 目录
2. 下次开会话 → 执行 `/echoes-start`，插件一口气读回**最近 3 天的日志和索引**，注入到上下文

知识库目录结构（兼容 Obsidian）：

```
EchoesVault/
├── pages/      # 百科全书式长期记忆
├── daily/      # 工作日志（每日）
└── assets/     # 图表 / 附件
```

因为结构与 Obsidian 兼容，用户可以随时在 Obsidian 里打开用图谱视图 / 搜索。

## 与 OKF 的关系

值得注意的是，**插件底层使用的是 Google 的 OKF（Open Knowledge Format）标准**，与本知识库采用的格式一致。这使得它的产物可以直接被其他 OKF 兼容工具消费，支持直接在 GitHub 上预览。

## 关键能力

| 能力 | 说明 |
|------|------|
| 持久记忆 | 跨会话保留决策 / 架构变化 / 关键节点 |
| 自动记录 | 会话结束自动写入 `daily/` |
| 快速回读 | `/echoes-start` 一键加载最近 3 天记忆 |
| Obsidian 兼容 | 文件结构与 Obsidian 一致，可直接打开用图谱视图 |
| OKF 标准 | 输出符合 Google OKF，与外部 AI 工具互通 |
| GitHub 预览 | 提交到 GitHub 即可在网页直接看 |

## 原始链接

- [项目仓库](https://github.com/psinetron/echoes-vault-opencode)
- [原始推文剪藏](https://x.com/QingQ77/status/2070401423574003796)

## 相关概念

- [OKF 是什么](./term-okf.md) — EchoesVault 采用的正是这一标准
- [OKF 参考示例 Bundles](./tool-okf-sample-bundles.md) — 同为 OKF 生态的参考样例
- [Recall（Claude Code 项目记忆插件）](./tool-recall-claude-code.md) — 同样给编码 Agent 加"项目记忆"，但走 TextRank 摘要路线，平台是 Claude Code
- [Obsidian](./tool-obsidian.md) — EchoesVault 选 Obsidian 作为目标格式
