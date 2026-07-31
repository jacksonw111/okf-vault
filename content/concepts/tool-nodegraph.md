---
type: "Tool"
title: "NodeGraph（Jeong-jin-Han/NodeGraph，VS Code 扩展）"
description: "VS Code 扩展：读完论文后自动生成交互式知识图谱，每条观点都带原文引用，右键跳转到 PDF 对应位置核对；支持 AI agent 自动建图与手动拖拽两种工作流，节点内容支持 Markdown / LaTeX / 图片 / 折叠章节。"
resource: "https://github.com/Jeong-jin-Han/NodeGraph"
tags: "[vscode-extension, knowledge-graph, paper-reading, ai-agent, latex, markdown]"
timestamp: "2026-07-31T20:30:00Z"
---

# NodeGraph

[NodeGraph](https://github.com/Jeong-jin-Han/NodeGraph) 是为 VS Code 设计的扩展，**读完论文后自动生成交互式知识图谱**。每条观点都带原文引用，右键就能跳到 PDF 对应位置核对；节点内容支持 Markdown 表格、LaTeX（KaTeX）、行内图片、折叠章节，全部在一张卡片里渲染。

## 它是什么

把「论文阅读笔记」从文本流变成**可视化的节点网络**：

- **自动化工作流**：让 AI agent（Claude Code / Codex 等）读 PDF 后自动建图
- **手动工作流**：自行拖拽节点搭建
- **可溯源**：每条观点都带原文引用，右键 → 跳 PDF 段落
- **节点里能塞**：Markdown 表格 / LaTeX / 图片 / 折叠章节

## 为什么用它 / 适合什么场景

| 痛点 | NodeGraph 怎么解 |
|------|------------------|
| 论文笔记写完没法看章节关系 | 用图谱看节点之间的连接 |
| 引用来源找不到原句位置 | 右键跳 PDF 对应位置 |
| 不同论文的笔记混在一起 | 节点卡片统一渲染所有富文本 |
| AI 读完论文产出的笔记不容易自己整理 | 让 agent 直接落图 |

## 关键能力

| 能力 | 说明 |
|------|------|
| AI 自动建图 | Claude Code / Codex 等 agent 读完 PDF 直接产出图谱 |
| 手动拖拽 | 不用 AI 也可手动布置节点 |
| 原文跳转 | 右键节点 → 在 PDF 打开原始段落 |
| 富内容卡片 | Markdown 表格、KaTeX LaTeX、行内图片、折叠章节 |
| 集成 VS Code | 与现有编辑器无缝同住 |

## 相关概念

- [Archify](./tool-archify.md) — LLM→JSON→SVG 架构图，把对话转成架构图
- [Hyperagent 设计网格 Skill](./tool-hyperagent-design-skill.md) — 同样是「AI 生成的可视化」范式，但聚焦设计网格
- [Solar Wanderer](./tool-solar-wanderer.md) — 浏览器内实时太阳系 3D 模拟，可视化思路同类
- [Componentry](./tool-componentry.md) — 节点卡片这种「一卡片多内容」的渲染风格同类（demo + 源码 + 复制按钮）
- [Penpot](./tool-penpot.md) — 开源设计协作工具，与 NodeGraph 共享「可视化可编辑」范式
