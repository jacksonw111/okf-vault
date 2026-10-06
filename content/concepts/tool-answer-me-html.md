---
type: "Tool"
title: "answer-me-with-html（AI Agent 一页式 HTML 回答）"
description: "QingYunA 出品的 Claude Code Skill：让 AI Agent 用一页 HTML 回答复杂问题，模型只写内容草稿，版式 / 配色 / 图表坐标由随 Skill 分发的 CLI 生成，省去手写 CSS 与 SVG。"
resource: "https://github.com/QingYunA/answer-me-with-html"
tags: "[ai-agent, html, skill, claude-code, visualization, answer]"
timestamp: "2026-10-06T00:35:00Z"
---

# answer-me-with-html

## 它是什么

[answer-me-with-html](https://github.com/QingYunA/answer-me-with-html) 是给 Claude Code 等 AI Agent 的 Skill——让 Agent **用一页 HTML 回答复杂问题**：模型只写内容草稿，**版式 / 配色 / 图表坐标** 全部交给随 Skill 分发的 CLI 自动生成。

## 关键能力

| 能力 | 说明 |
|------|------|
| 关注点分离 | 模型只产内容，版式 / 配色由 CLI 算 |
| 省去手工 | 无需 Agent 写 CSS / SVG 坐标 |
| CLI 协同 | 随 Skill 一同分发的命令行生成最终页面 |
| 视觉稳定 | 版式由代码生成，避免模型「自由发挥」失控 |

## 工作流

1. 用户提问 → Agent 调 LLM 写内容草稿（Markdown / 段落 / 数据点）
2. CLI 接收草稿 → 按预设主题渲染一页 HTML（卡片、表格、配色）
3. 图表坐标 → 由 CLI 根据数据点算出并写好 SVG
4. 输出最终单文件 HTML，可直接在浏览器打开

## 适合场景

- AI Agent 答完题想给一个「可分享 / 可视化」的结果
- 不希望模型自己写样式代码导致失控 / 跑偏
- 想用 Claude Code / 类似 Agent 出可交付的「报告型 HTML」

## 参考链接

- 项目链接：<https://github.com/QingYunA/answer-me-with-html>

## 相关概念

- [Claude Code](./term-claude-code.md) — 主要消费 Agent
- [Agent Skills](./term-agent-skills.md) — Skill 的分发形态