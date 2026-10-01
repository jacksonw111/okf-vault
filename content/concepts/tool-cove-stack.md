---
type: Tool
title: "Cove Stack（TanStack Start 全栈样板）"
description: "原名 TanStarter 的开源全栈样板：把 React + TanStack Start + Router + Query + Drizzle + Better Auth + Vite Plus + Nitro 等现代前端与轻栈生态整合到一个项目里，一行 `pnpm create cove` 交互式初始化。"
resource: "https://github.com/mugnavo/cove"
tags: [tanstack, react, fullstack, typescript, vite-plus, drizzle, better-auth, boilerplate]
timestamp: 2026-10-01T05:03:18Z
---

# Cove Stack

## 它是什么

**Cove Stack**（原名 TanStarter）是一个面向 **TanStack Start** 的开源全栈样板项目，GitHub 已收获 1.3k+ Star。它把「现代前端 + 轻量全栈」生态里被广泛认可的几件套整合到一个项目骨架里，目的是让个人开发者或小团队可以快速拉起一个**类型安全、可部署、可写实际业务**的全栈原型。

`pnpm create cove` 交互式初始化后，依次 `vpr env:load`、`vpr db generate`、`vpr dev` 即可起本地开发。项目采用 **Unlicense** 协议，个人学习与商业二开都无版权负担。

## 为什么用它 / 适合什么场景

- 想用 TanStack Start 但不想花时间把周边拼齐。
- 已经在写 React 全栈应用，希望服务端函数 + 类型安全路由开箱即用。
- 想做轻量 SaaS / 副业项目的脚手架。

## 关键能力

| 能力 | 说明 |
|------|------|
| 应用骨架 | React + TanStack Start + TanStack Router + TanStack Query（类型安全路由 + 服务端函数） |
| 构建运行时 | Vite Plus (vp) + Nitro，本地极速构建，多平台部署（Vercel / Netlify / Node） |
| UI 与样式 | Tailwind CSS + shadcn/ui + Base UI，自带深浅色主题切换 Provider |
| 数据 / 鉴权 | Drizzle ORM + PostgreSQL + Better Auth（含鉴权中间件与 Schema 生成脚本） |
| 工程化 | Varlock（`.env.schema` 严格环境变量）、evlog（结构化请求日志）、Oxfmt + Oxlint（替代 ESLint/Prettier） |
| 测试 | Vitest + Playwright 测试骨架 |
| 协议 | Unlicense |

## 参考链接

- 仓库：<https://github.com/mugnavo/cove>

## 媒体

- ![](https://pbs.twimg.com/media/HTYpCFIbwAAp1xg.png)（同类项目图示占位）

## 相关概念

- [TanStack Start](https://tanstack.com/start) — 项目骨架的核心运行时（外部链接）
- [Drizzle ORM](https://orm.drizzle.team/) — 配套 ORM
