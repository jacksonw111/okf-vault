---
type: "Tool"
title: "obsidian-knowledge-agent（Michael-OvO/obsidian-knowledge-agent）"
description: "AI 代理驱动的 Obsidian 笔记自动整理工具：六阶段管道把 PDF / 论文 / 课件 / URL 转化为结构化、教学质量的笔记，每次使用后自我进化。"
resource: "https://github.com/Michael-OvO/obsidian-knowledge-agent"
tags: [obsidian, agent, notes, pdf, ai-pipeline]
timestamp: "2026-06-23T15:30:00Z"
---

# obsidian-knowledge-agent（Michael-OvO/obsidian-knowledge-agent）

## 它是什么

把「读 PDF → 整理成 Obsidian 笔记」这条链路完整自动化的 AI 代理。它把流程切成六阶段：回忆（recollect）→ 摄入（ingest）→ 编译（compile）→ 分发（distribute）→ 提交（commit）→ 反思（reflect）。每一阶段都把中间产物落盘，便于排错与回溯；最后还能基于本次反馈修正后续策略，越用越顺。

## 为什么用它 / 适合什么场景

- **学生 / 研究者**：批量导入论文、课件、教材章节，让 AI 输出带双向链接的 Obsidian 卡片；
- **知识工作者**：把会议录音转写稿、网页剪藏、长 PDF 报告统一收敛到 vault；
- **教学辅助**：把教材拆成「概念卡 + 例子 + 自检题」三件套喂给 Obsidian。

## 关键能力

| 阶段 | 职责 |
|------|------|
| Rec | 检索已有 vault，避免重复造轮子 |
| Ingest | 解析 PDF / 幻灯片 / 论文 / URL |
| Compile | 生成结构化 Obsidian 笔记 |
| Distribute | 在 vault 中归位 / 加链接 |
| Commit | 写入 Git 或 Obsidian |
| Reflect | 复盘本次输出，优化下一轮策略 |

## 媒体 / 原始链接

- 项目链接：<https://github.com/Michael-OvO/obsidian-knowledge-agent>

## 相关概念

- [Obsidian](tool-obsidian.md) — 笔记产物落地的目标编辑器
- [Cabinet](tool-cabinet.md) — 同样在 Obsidian 之上挂一层 AI 代理运行时
- [Niamos](tool-niamos.md) — Obsidian PARA 模板的另一种「结构化入口」思路
- [OKF Enrichment Agent](tool-okf-enrichment-agent.md) — 同样的「AI 自动产出概念文档」模式（但目标是 OKF bundle）