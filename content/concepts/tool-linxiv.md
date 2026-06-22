---
type: "Tool"
title: "linXiv（本地优先学术论文管理桌面应用）"
description: "linxiv-dev/linXiv —— 本地优先的学术论文管理 Tauri 桌面应用，集成 SQLite + Google Gemini AI 标注 + Obsidian 笔记 + 论文网络图可视化，支持 arXiv / DOI / OpenAlex / CrossRef 检索。"
tags: "[academic, paper-manager, tauri, obsidian, local-first, arxiv, gemini]"
timestamp: "2026-06-22T16:07:00Z"
---

# linXiv（本地优先学术论文管理桌面应用）

## 它是什么

[`linxiv-dev/linXiv`](https://github.com/linxiv-dev/linXiv) 是面向研究人员的**本地优先论文管理桌面应用**。数据全存本地，不上传任何内容到外部服务。

技术栈：

- **桌面壳**：Tauri
- **前端**：React + TypeScript
- **后端**：Python
- **数据存储**：SQLite（本地）
- **AI 标注**：Google Gemini
- **笔记**：集成 Obsidian

核心能力：

- **本地存储**：数据不上传任何外部服务
- **PDF 上传**：直接拖入本地 PDF 入库
- **AI 标注**：调用 Gemini 给论文打摘要 / 标签
- **Obsidian 笔记集成**：与 Obsidian 双向打通
- **论文网络图可视化**：看论文之间引用 / 主题关系
- **多源检索**：arXiv / DOI / OpenAlex / CrossRef

> 视频：<https://video.twimg.com/tweet_video/HLUoHSXbUAEGeO6.mp4>

## 为什么用它 / 适合什么场景

- **本地优先 / 隐私**：研究人员对自己「未发表 / 内部资料」的论文笔记敏感。
- **AI 标注 + 离线**：本地入库 PDF 即可让 Gemini 生成摘要，不用自己啃。
- **Obsidian 联动**：论文笔记天然进 Obsidian Vault，与个人第二大脑无缝合并。
- **论文网络图**：可视化看主题聚类，找「这块还有谁在研究」。

适合：

- **研究生 / 博士**：长期维护文献库
- **科研团队**：本地共享笔记，但每台机器自己存
- **跨学科研究者**：从 arXiv 跟踪新论文

## 关键能力

| 能力 | 说明 |
|---|---|
| 本地优先 | 数据全在 SQLite，不上传 |
| Tauri 桌面 | 跨平台、低资源占用 |
| Gemini AI 标注 | 自动摘要 / 标签 / 提取实体 |
| Obsidian 集成 | 笔记 / 标签直接同步 Vault |
| 论文网络图 | 可视化引用 / 主题关系 |
| 多源检索 | arXiv / DOI / OpenAlex / CrossRef |
| 项目组织 | 按研究项目分组管理 |

## 工作流

```
PDF 上传 ─┐
arXiv 检索 ─┤
DOI 检索   ─┼─→  SQLite 本地库  ──→  Gemini 标注  ──→  Obsidian Vault
OpenAlex  ─┤                  │
CrossRef  ─┘                  └─→  论文网络图
```

## 参考链接

- [项目链接](https://github.com/linxiv-dev/linXiv)

## 相关概念

- [Obsidian](tool-obsidian.md) — linXiv 笔记直接落入 Obsidian Vault
- [Cabinet](tool-cabinet.md) — Obsidian + AI 代理（与 linXiv 同属「Obsidian 当研究底座」方向）
- [Datalab LIFT](tool-datalab-lift.md) — 视觉文档 JSON 抽取模型（论文 PDF 抽取元数据可叠加使用）