---
type: "Note"
title: "Harness Engineering Guide（nexu-io 生产级实战指南）"
description: "把 Harness 工程讲到生产级的实战指南：从第一个小型 agent harness 到完整的大型编排全覆盖，含沙箱、编排、多 agent、长时运行 Harness 设计，以及评估，含真实可运行代码、踩坑与修复过程。"
resource: "https://github.com/mksglu/context-mode"
tags: "[harness, agent, engineering, production, sandbox, multi-agent, long-running]"
timestamp: "2026-09-13T09:03:00Z"
---

# Harness Engineering Guide（nexu-io 生产级实战指南）

## 它是什么

一份把 **Harness Engineering 讲到生产级**的实战指南合集（`nexu-io/harness-engineering-guide`，关联仓库 `mksglu/context-mode`）：从第一个小 agent harness 一路讲到完整的大型编排，覆盖沙箱、编排、多 agent、长时运行 Harness 的设计，**每篇文章都带可复制运行的真实代码**。

## 它讲了什么（按主题梳理）

| 主题 | 说明 |
|------|------|
| 沙箱 | 把工具执行锁在隔离环境 |
| 编排 | 多 agent / 任务的协调 |
| 多 Agent | 多角色协作下的边界划分 |
| 长时运行 Harness | 跨越几小时 / 几天任务的保活 |
| 评估 | 怎么给 harness 打分 |

## 为什么看它 / 适合谁

- **已经在跑生产级 agent 但遇到坑**的人——文档里有作者踩过的坑与修复过程。
- 想从「能跑」走向「能稳定跑 7×24」的人。
- 想抄一份「完整可运行」的 harness 代码起手。

## 与同类资源的差异

| 资源 | 差异 |
|------|------|
| 官方文档（Pi / Codex / Claude Code） | 官方偏介绍，harness engineering guide 偏「为什么这样选」与「踩坑实录」 |
| 12-Factor Agents | 12-Factor 给原则，harness engineering guide 给**生产级实现细节** |
| DeepSeek Harness 橙皮书 | 橙皮书偏小白级入门，harness engineering guide 偏生产级工程化 |

## 项目链接

- 关联仓库：<https://github.com/mksglu/context-mode>
- 命名空间：<https://github.com/nexu-io/harness-engineering-guide>

## 相关概念

- [What is an Agent Harness](./note-earendil-agent-harness.md) — harness 概念的入门科普
- [12-Factor Agents](./tool-12-factor-agents.md) — Agent 工程化原则清单
- [DeepSeek Harness 橙皮书（小白实战）](./note-deepseek-harness-orange-book.md) — 偏小白入门，对照阅读