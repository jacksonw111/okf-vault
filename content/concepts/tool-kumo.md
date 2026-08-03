---
type: Tool
title: "Cloudflare Kumo"
description: "Cloudflare 开源的前端 UI 组件库与文档框架，TypeScript + React，基于 Base UI 封装，键盘导航 / 焦点管理 / ARIA 内置；主约 45 个组件，覆盖按钮 / 对话框 / 日期选择 / Toast / Tooltip 等，按组件细粒度引入以利于 tree-shaking。"
resource: "https://github.com/cloudflare/kumo"
tags: [kumo, cloudflare, ui-library, react, base-ui, frontend]
timestamp: "2026-08-03T01:10:00Z"
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
| Base UI 封装 | 组件基于 Base UI 无样式原语封装，键盘导航 / 焦点管理 / ARIA 内置 |
| 约 45 个组件 | 按钮 / 对话框 / 日期选择 / Toast / Tooltip 等常见场景 |
| 细粒度导入 | 按组件粒度 tree-shaking，避免一个组件引一整库 |
| 重新导出 Base UI 原语 | 高级用户可直接用底层 Base UI 原语 |
| 主题系统 | 主题包通过 Provider 注入，支持多套配色（Cloudflare 风格默认深色） |
| 文档站点 | 自带 docs 渲染器，React 组件直接当 Markdown 用 |
| 国际化 | i18n helper + 复数形式 + 占位符插值 |
| 类安全 | 完整 TS 类型，组件 props 自动化补全 |

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
