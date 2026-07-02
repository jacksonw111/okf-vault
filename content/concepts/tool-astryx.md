---
type: Tool
title: "Astryx"
description: "Meta（Facebook）开源的设计系统，StyleX 样式底层、150+ 可访问组件、CSS 变量级换肤、文档/API/CLI 同一套约定，撑起 Meta 内部 8 年 13000+ 应用。"
resource: "https://github.com/facebook/astryx"
tags: "[design-system, react, facebook, meta, open-source, stylex]"
timestamp: "2026-07-02T16:10:00Z"
---

# Astryx

## 它是什么
Meta（Facebook）内部用了 8 年的设计系统，于 2026 年开源。底层样式基于 StyleX，组件库内置 150+ 个并默认满足无障碍要求。

## 为什么用它 / 适合什么场景
- 公司级前端基础设施：Meta 内部 13000+ 应用都跑在它身上，规模与稳定性已被验证。
- 想「开箱即用 + 自由换肤」：主题只是 CSS 变量覆盖，设计师改色不必 fork 组件或包一层源码。
- 想要 AI 辅助写界面：文档、API 与 CLI 按同一套约定设计，人和 AI 助手看的是同一份参考。
- 需要深定制时可导出组件源码到项目本地继续接手，组件可在任意层级拆开重组。

## 关键能力
| 能力 | 说明 |
|------|------|
| 组件库 | 150+ 可访问组件，缺省即合规 |
| 主题机制 | CSS 变量覆盖，不动组件代码即可换肤 |
| 样式底层 | 基于 StyleX，无需额外装样式库即可使用 |
| 暗色模式 | 内置 |
| 现成模板 | 提供多种应用模板 |
| 深定制 | 可将单个组件的完整源码导出到项目里自己接手 |
| 文档统一性 | 文档、API、CLI 共用一套约定，人与 AI 看到的是同一份参考 |

## 相关概念
- [Vercel Design System](tool-vercel-design-system.md) — 同类「公开设计系统页」参考对象
- [Penpot](tool-penpot.md) — 开源设计工具，与 Astryx 等设计系统互补（工具层 vs 组件层）
- [DESIGN.md 最佳实践](note-design-md-best-practices.md) — 把设计系统装进 .md 喂给 AI 的写法，与 Astryx 的「文档/API/CLI 同约定」思路相通

## 项目链接
- 项目主页：<https://github.com/facebook/astryx>