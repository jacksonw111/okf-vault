---
type: "Tool"
title: "json-render / tanstack-start（TanStack Start from JSON）"
description: "Vercel Labs 在 json-render 之上推出的 `@json-render/tanstack-start` 集成包——让 TanStack Start 应用可以直接从 JSON spec 生成：定义组件与数据 loader，AI 自动编排页面、布局、路由与 SSR，适合网站搭建器、CMS 驱动站点、客制化客户门户。"
resource: "https://github.com/vercel-labs/json-render"
tags: "[json-render, tanstack-start, generative-ui, vercel, ai-sdk, ai-coding-agent]"
timestamp: "2026-10-06T22:51:00Z"
---

# json-render / tanstack-start（TanStack Start from JSON）

## 它是什么

**`@json-render/tanstack-start`** 是 Vercel Labs 在 [`tool-json-render`](./tool-json-render.md) 之上推出的 **TanStack Start 集成包**——让 TanStack Start 应用**直接从 JSON spec 生成**：你定义组件与数据 loader，AI 编排页面、布局、路由与 SSR；面向**网站搭建器、CMS 驱动站点、可客制化客户门户**等场景。

## 为什么用它 / 适合什么场景

- **JSON → 真页面**：把网站骨架用 JSON 描述，AI 直接渲染成 TanStack Start 路由 + 页面
- **CMS 友好**：CMS 后端只存 JSON，前端用统一渲染器消费
- **客户门户**：每个客户拿一份 JSON spec + 自定义组件，AI 拼出个性化门户
- **网站搭建器**：把组件注册进渲染器，用户用自然语言 / 表单描述需求，AI 输出 JSON spec，渲染器立即出页面

## 关键能力

| 能力 | 说明 |
|------|------|
| JSON spec 输入 | 组件清单 + 数据 loader + 页面结构 |
| AI 自动编排 | 自动组合 page / layout / route |
| SSR | 原生支持 TanStack Start SSR |
| 跨端一致 | 一次 JSON schema，桌面 / 移动可同源渲染 |
| 可注册组件 | 用户 / 第三方可注册任意 React 组件 |

## 与 [json-render](./tool-json-render.md) 的关系

`@json-render/tanstack-start` 是 `json-render` 生态中的**TanStack Start 适配层**——上游仍是 Vercel Labs 的 json-render 范式（JSON schema → 真实 UI），下游落地到 TanStack Start 框架。

## 参考链接

- 项目链接：<https://github.com/vercel-labs/json-render>

## 相关概念

- [JSON-Render / HarnessAgent](./tool-json-render.md) — 上游范式
- [Generative UI（生成式 UI）](./tool-json-render.md) — 同一思想
- [Vercel AI SDK](https://sdk.vercel.ai/)
