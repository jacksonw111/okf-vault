---
type: Tool
title: "Cloudflare Kumo"
description: "Cloudflare 开源的前端 UI 组件库与文档框架,TypeScript + React,主打企业级内部系统(dashboard / 工单 / 监控)的快速搭建。"
resource: "https://github.com/cloudflare/kumo"
tags: [kumo, cloudflare, ui-library, react, frontend]
timestamp: "2026-07-04T15:00:00Z"
---

# Cloudflare Kumo

## 它是什么

Cloudflare Kumo(`cloudflare/kumo`)是 Cloudflare 官方在 GitHub 上开源的 UI 组件库与文档框架。它给开发者一套 TypeScript + React 写的「能直接抄进项目」的企业级组件,目标是快速搭 dashboard / 工单 / 监控 / 运维后台。

项目链接：<https://github.com/cloudflare/kumo>

## 为什么用它 / 适合什么场景

- **Cloudflare 内部用过**:不是「写个 demo 就开源」的玩具,本身承载过 Cloudflare 真实业务场景的检验。
- **TypeScript-first + Headless 友好**:tree-shakable,可搭配 Tailwind / emotion / CSS Modules 任意样式方案。
- **重视 a11y / 国际化**:WAI-ARIA 属性、键盘导航、RTL 支持都按规范做齐。

## 关键能力

| 能力 | 说明 |
|------|------|
| 组件库 | Table / Tree / Pagination / ComboBox / Dialog / Toast / Tabs / Accordion 等 |
| 主题系统 | 主题包通过 Provider 注入,支持多套配色(cloudflare 风格默认深色) |
| 文档站点 | 自带 docs 渲染器,React 组件直接当 markdown 用 |
| 国际化 | i18n helper + 复数形式 + 占位符插值 |
| 类型安全 | 完整 TS 类型,组件 props 自动化补全 |

## 使用示例

```bash
# 安装
npm i @cloudflare/kumo
```

```tsx
import { Table, Pagination } from "@cloudflare/kumo";

export function TicketsList({ rows }) {
  return (
    <Table
      columns={[
        { key: "id", header: "工单号" },
        { key: "title", header: "标题" },
        { key: "status", header: "状态" }
      ]}
      rows={rows}
    />
  );
}
```

## 相关概念

- [Toolcraft](tool-toolcraft.md) — pixel-point 出的创意类应用 UI starter kit,同样面向前端
- [Componentry](tool-componentry.md) — 组件目录式组件库
- [Astryx](tool-astryx.md) — Meta 开源设计系统,150+ 可访问组件
- [Cloudflare Kumo 仓库](https://github.com/cloudflare/kumo) — 项目链接
