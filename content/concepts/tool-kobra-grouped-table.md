---
type: "Tool"
title: "Kobra Grouped Table（Linear 风格分组表格交互）"
description: "haaarshsingh 复刻自 Linear 的表格分组交互：行拖拽到表头就成组，组可以折叠 / 重命名 / 嵌套，整张表被重新组织为「任务流水线」。kobra.systems/grouped-table 提供下载。"
resource: "https://kobra.systems/grouped-table"
tags: "[table, linear, group, drag-drop, interaction, kobra, ui-pattern]"
timestamp: "2026-10-02T01:30:00Z"
---

# Kobra Grouped Table（Linear 风格分组表格交互）

## 它是什么

[Kobra Grouped Table](https://kobra.systems/grouped-table) 是 haaarshsingh 出品的**单文件交互实现**——把 Linear 标志性的「行即卡片、拖到表头自动成组、组可折叠 / 重命名 / 嵌套」这套体验搬到任何 HTML 表格上。原推视频见参考资料。

## 为什么用它 / 适合什么场景

- 想要 **Linear / Height / Notion DB 那种「表格里直接做看板」** 的体验，又不想引入整个 SaaS。
- 后台列表（订单 / 任务 / 工单）想从「干巴巴的 `<table>`」升级到「可拖拽分组」的看板视图。
- 评审、设计稿里需要「直接演示」，用一组 HTML + 一段 JS 就能说服对方。

## 关键能力

| 能力 | 说明 |
|------|------|
| 行 → 表头 | 拖一行到列名处就成组 |
| 组可折叠 | 单击表头折叠 / 展开组成员 |
| 组可重命名 | 双击表头就地改组名 |
| 组可嵌套 | 把一个组再拖到另一组下面即可 |
| 单文件 | 一个 `.html` / `.js` 就能跑，零依赖 |

## 实现要点（社区拆解）

- 监听 `dragstart` / `dragover` / `drop`，把 `dataTransfer` 里的 row id 落到 `<th>` 上触发分组。
- 用 `<tr>` 内嵌 `data-group` 属性 + CSS `display: none` 控制折叠，**不要为每个组维护独立的子树 DOM**——重渲染成本最低。
- 组顺序持久化：把 `groupOrder: string[]` 写进 `localStorage`，刷新后保留。

## 参考链接

- 原始链接：<https://x.com/haaarshsingh/status/2105719659282461137>
- 项目链接：<https://kobra.systems/grouped-table>
- 视频：<https://video.twimg.com/amplify_video/2105710068465344512/vid/avc1/2504x2024/B5EthuR_S1G0vRLS.mp4?tag=29>

## 相关概念

- [Kobra（动效组件库）](./tool-kobra-motion.md) — 同作者的另一套带音效 shadcn 替代品
- [transitions.dev](./tool-transitions-dev.md) — 网页过渡效果精选，本交互里的折叠动画可参考其节奏
