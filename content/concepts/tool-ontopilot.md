---
type: Tool
title: "ontopilot（deeplethe/ontopilot）"
description: "本地优先、自托管的本体工程工作台：领域专家 / 审阅者 / AI agent 在同一条生产线把政策 / 手册 / 产品规范转成可审查、可发布、可版本化的 TBox、SKOS 术语、ABox 知识图谱"
resource: "https://github.com/deeplethe/ontopilot"
tags: "[ontology, knowledge-graph, tbox, skos, abox, self-hosted]"
timestamp: "2026-08-19T16:00:00Z"
---

# ontopilot（deeplethe/ontopilot）

## 它是什么
[`deeplethe/ontopilot`](https://github.com/deeplethe/ontopilot) 是一个**本地优先、自托管**的**本体工程（Ontology Engineering）**工作台：让领域专家、审阅者、AI agent 在同一条「生产线」上把政策、手册、产品规范等文档转成**可审查、可发布、可版本化**的 TBox（术语 / 类）、SKOS 词表、ABox（实例 / 个体）**知识图谱**数据。

## 为什么用它 / 适合什么场景
- 公司 / 团队想沉淀领域知识为可机读本体，但不想用 Protege 等老旧桌面工具。
- 需要「人审 + AI 起草 + 可追溯版本」一条龙流水线。
- 数据敏感（医疗 / 法律 / 内部政策），必须自托管。

## 关键能力
| 能力 | 说明 |
|------|------|
| 本地优先 | 全部数据自托管、可离线运行 |
| 多角色协作 | 领域专家 / 审阅者 / AI agent 同台编辑 |
| 多本体产物 | 同时输出 TBox / SKOS / ABox，覆盖多种语义网标准 |
| 可审查 | 每条改动可回溯、可 diff |
| 可版本化 | 直接进 Git / 任意 VCS 工作流 |

## 媒体
- ![ontopilot 截图](https://pbs.twimg.com/media/HP-rXwYbwAAuDJ1.jpg)

## 相关概念
- [项目仓库](https://github.com/deeplethe/ontopilot) — 仓库主页
- [okf-static-html-visualizer](./tool-okf-static-html-visualizer.md) — OKF 自带的静态 HTML 可视化器（同样面向「可机读知识」）