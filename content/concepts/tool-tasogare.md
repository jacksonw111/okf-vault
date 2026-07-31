---
type: "Tool"
title: "Tasogare（EnhydrInk/tasogare）"
description: "网页阅读器：能打开 PDF/EPUB/TXT、翻页、划线、写笔记；支持两人「真人与 AI」在书页上各画各的线（玉绿与琥珀），配 MCP 服务器让 AI 通过它翻书、划线、写批注、看对方动态。"
resource: "https://github.com/EnhydrInk/tasogare"
tags: "[reader, mcp, pdf, epub, annotation, ai-human-collab, web-app]"
timestamp: "2026-07-31T20:30:00Z"
---

# Tasogare（EnhydrInk/tasogare）

[Tasogare](https://github.com/EnhydrInk/tasogare) 是一款**网页阅读器 + 协同标注工具**：一个人和（或）一个 AI 在同一本书上画线写批注，**各自颜色不同**——谁写的哪笔一眼能认出。同时配套一个 **MCP 服务器**，让 AI 通过它翻书、划线、写批注、看对方最近的动态。

## 它是什么

- **支持的格式**：PDF、EPUB、TXT
- **基础能力**：翻页、划线、写笔记
- **协同画线**：两人（如一个真人 + 一个 AI）用不同颜色（玉绿 vs 琥珀），物理上像两支荧光笔
- **MCP 服务器**：AI 通过 MCP 协议调用——「翻一下」「划这一段」「看看对方最近读到什么」都可程序化

## 为什么用它 / 适合什么场景

| 痛点 | Tasogare 的回应 |
|------|------------------|
| 单人阅读 → AI 笔记分离，读完对不上 | 真人与 AI 同书同页，画线即标注 |
| 想让 AI 跟一段时间看读完没 | MCP 服务让 agent 查对方动态 |
| 想看 AI 划了哪儿而自己划了哪儿 | 颜色一眼区分 |
| 不在 Mac / 想用浏览器读 PDF / EPUB | 纯网页应用，跨平台 |

## 关键能力

| 能力 | 说明 |
|------|------|
| PDF / EPUB / TXT 阅读 | 主流电子书格式全支持 |
| 双色标注 | 真人一色，AI 一色，物理隔离 |
| 划线 + 笔记 | 基础阅读器功能 |
| MCP 服务器 | 让 AI 编程 agent 通过 MCP 协议读这本书 |
| 共享动态 | 看对方最近的阅读进展 |

## 相关概念

- [NodeGraph](./tool-nodegraph.md) — VS Code 扩展，读论文自动建图，与 Tasogare 同属「AI 读 + 注」范式
- [paperless-brain](./tool-paperless-brain.md) — 给 Paperless-ngx 加 AI，与 Tasogare 同属「AI 帮你消化文档」一族
- [graft](./tool-graft.md) — 给 agent 喂代码结构地图，Tasogare 的 MCP 服务与它同属「为 agent 暴露可读接口」
- [hermes-browser-extension](./tool-hermes-browser-extension.md) — 浏览器内的 Hermes Agent，可与 Tasogare 的「AI 读网页」联动
- [Agent Skills（代理技能包）](./term-agent-skills.md) — Tasogare 的 MCP 服务是典型的「agent skill」化身
