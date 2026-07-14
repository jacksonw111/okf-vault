---
type: "Note"
title: "让 Agent 把 README 当纵向演示文稿设计——SVG 组件 + Markdown 内容的双层布局"
description: "GitHub 不能自定义 CSS 时,用可复用 SVG 设计首屏与章节标题、正文继续用 Markdown 的README 装修套路,适合给 Agent 做 GitHub 主页设计。"
resource: "https://github.com/oil-oil/oil-ppt"
tags: "[github, readme, svg, design, agent-prompting, markdown]"
timestamp: "2026-07-14T00:05:16Z"
---

# GitHub README 装修:SVG 组件 + Markdown 内容双层

GitHub 的 README 不允许自定义 CSS,但又希望视觉设计感强。一套解决思路:**首屏与章节标题用 SVG(像普通图片一样插入 README),正文继续用 Markdown**。

## 核心套路

让 Agent 遵循同一套规则批量出 SVG 部件,正文则是普通 Markdown。

| 部件 | 形式 | 由谁负责 |
|------|------|----------|
| 首屏 | 一张 SVG(1200 × 320) | Agent 设计 |
| 章节标题 | 一张 SVG(1200 × 138) | Agent 设计 |
| 正文 | Markdown | 真人 / Agent 写 |

## SVG 风格统一规则(可固化到 prompt)

1. **固定画布**——首屏 1200 × 320,章节标题 1200 × 138。
2. **统一语言**——浅色圆角容器、细网格、点阵、黄色短线作为强调色。
3. **清楚层级**——英文眉题 → 中文大标题 → 淡色章节编号。
4. **装饰克制**——右侧点阵和数字只负责平衡画面。
5. **系统字体**——避免 GitHub 加载不到外部字体,导致样式缺失。
6. **每个章节复用同一个模板,只替换标题、编号、眉题。**

## 给 Agent 的指令示例

> 把 README 当成一份纵向演示文稿:用一套可复用的 SVG 组件设计首屏和章节标题,正文继续用 Markdown。

## 优势

- **美观**:GitHub 上一眼出挑,相对传统 README 给人「小惊喜感」。
- **可维护**:样式规则统一,后续修改只动 SVG 模板。
- **搜索友好**:正文仍是 Markdown,GitHub 仍能搜到内容。
- **无需外部字体 / CSS 钩子**:遵守 GitHub 沙箱。

## 参考链接

- [示例仓库(oil-oil/oil-ppt)](https://github.com/oil-oil/oil-ppt) — 该方法落地的开源 PPT 主题项目

## 相关概念

- [Vibe Coding Rules](./tool-vibe-coding-rules.md) — 同样是给 Agent 定规则流水线,本方法聚焦在视觉资产层
- [Toolcraft](./tool-toolcraft.md) — 创意类应用 starter kit,提供 canvas / 工具栏 / 拾色器,适合把本方法做成可视化编辑器
