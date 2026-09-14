---
type: "Tool"
title: "Regen Icons（Shopify 设计师开源的 AI Agent 图标系统）"
description: "Shopify 设计师 kazdenc 开源的「给 AI Agent 构建的图标系统」：225 个图标 + 极简 JSON 绘图语言 + 设计规范 + Agent 指令文件（AGENTS.md / CLAUDE.md / SKILL.md）+ 编译产物（SVG / React / sprite / icons.json）+ 视觉平衡报告。"
resource: "https://github.com/kazdenc/regen-icons"
tags: "[icons, ai-agent, json-dsl, design-system, source-first, react]"
timestamp: "2026-09-14T22:30:00Z"
---

# Regen Icons（Shopify 设计师开源的 AI Agent 图标系统）

## 它是什么

[kazdenc/regen-icons](https://github.com/kazdenc/regen-icons) 是 Shopify 设计师 **kazdenc** 开源的**图标系统**。它**不是**又一个 SVG 图标库——它是一整套**「给 AI Coding Agent 用」**的图标基础设施：

> 把整套图标做成了一个「**源码 → 编译 → 多格式输出**」的系统，其中「源码」不是 SVG，是一种**极简的 JSON 绘图语言**；并且围绕这套语言写了一份**机器可执行的设计规范**，让 Coding Agent 能够独立地画出符合家族风格的新图标。

## 核心设计：Source-first 架构

传统图标库（Lucide / Tabler）的 **SVG 文件就是「源头」**。**Regen Icons 里，SVG 是编译产物**，真正的源头是 `generator/src/<名字>.icon.json`。

编译器 `build-icons.mjs` 接受 **12 种基元**：line / polyline / rect / circle / arc / bend / quad / ellipse / dot / arrow / path / use，把它们编译成统一的 SVG path。

一次构建同时产出：

| 产物 | 说明 |
|------|------|
| 独立 SVG | outline + filled 双形态 |
| React 组件 | `icons.tsx` |
| sprite | 雪碧图 |
| icons.json | 可搜索的目录 |
| 预览画廊 | HTML 预览页 |
| 平衡度报告 | 视觉平衡打分 |

## 设计规范：硬约束 vs 视觉建议分层

**硬约束**（编译器 `validate()` 强制执行，违反直接报错）：

- 24×24 画布，安全区 2-22，所有点必须在整数或半格网格上
- 圆心 / 半径必须在半格上；弧线必须是 45° 倍数；旋转必须是 90° 倍数
- 平行的轴对齐笔画中心距不得小于 3
- 圆角不超过短边 50%、零长度线、未知基元、重名等

**视觉建议**（报告里标记但不拦截）：

- 墨量超过中位数 2.2 倍、中心偏移超过 1.25、包围盒小于 12 时点名
- 「移动质量去修，永远不要改笔画宽度」

> 这个分层非常关键：机器管不了的（曲线、斜线、美感）明确交给人眼审查，机器管得了的全部自动化。

## 为 Agent 而建：三层指令 + 闭环工作流

| 文件 | 用途 |
|------|------|
| `AGENTS.md` | 通用入口，读 spec / 先搜重 / 四步工作流 |
| `CLAUDE.md` | Claude Code 的精简版（10 行，指向 AGENTS.md） |
| `.dev/SKILL.md` | Agent 加载的技能包，含最完整工作流 |

工作流：编辑 JSON 源 → `pnpm check` 验证 → `pnpm preview <名字> <邻居> --matrix` 生成对比矩阵 → Agent 真的打开浏览器看渲染 → `pnpm test` 全量检查 → PR / CI。

> 「生成的截图不是审查，要去看它」（SKILL.md 原话）

## 项目链接

- 仓库：<https://github.com/kazdenc/regen-icons>
