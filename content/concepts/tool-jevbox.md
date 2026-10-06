---
type: "Tool"
title: "jevbox（带权限管控的文档库 + AI 问答）"
description: "Extend 团队开源的 TypeScript 全栈文档库：把文档解析 / 分层归档 / 层级检索 / 带原文引用的 AI 问答放进同一应用，权限交给 SpiceDB 判定；浏览界面用 Extend UI Finder，支持 3D Finder / 网格 / 列表 / 分栏 / 画廊五种视图。"
resource: "https://github.com/extend-hq/jevbox"
tags: "[document-management, permission, spicedb, ai-qa, typescript, fullstack]"
timestamp: "2026-10-06T00:35:00Z"
---

# jevbox

## 它是什么

[jevbox](https://github.com/extend-hq/jevbox) 是 **Extend 团队** 开源的 **TypeScript 全栈文档库应用**——把**文档解析、分层归档、层级检索、带原文引用的 AI 问答**放进同一个应用，**权限交给 SpiceDB 判定**。

## 关键能力

| 能力 | 说明 |
|------|------|
| 文档解析 | 自动抽取文档结构与层级 |
| 分层归档 | 按组织 / 项目 / 主题分级 |
| 层级检索 | 支持按层级深度筛选 |
| AI 问答 | 问答结果带原文片段引用，可追溯 |
| 权限模型 | SpiceDB（Google 系 Zanzibar 实现）做关系型授权 |
| 浏览视图 | 3D Finder / 网格 / 列表 / 分栏 / 画廊五种视图 |
| 底层 UI | Extend UI Finder — 团队自研组件 |

## 适合场景

- 团队需要一个统一入口管理「文档 + AI 问答」
- 文档涉密，需要细粒度（基于关系）权限
- 想摆脱 Notion / Confluence 的云依赖

## 参考链接

- 项目链接：<https://github.com/extend-hq/jevbox>

## 相关概念

- [SpiceDB](./tool-spicedb.md) — 项目使用的权限引擎
- [RAG](./term-rag.md) — AI 问答底层的检索增强生成模式