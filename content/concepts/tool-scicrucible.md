---
type: Tool
title: "SciCrucible（科研文献 PDF 自动整理 Claude Code Skills）"
description: "给 Claude Code 配的一套 skills：扔进去 PDF 自动抽元数据、写结构化笔记、跨文献查、每周自动扫描新论文、写论文时直接引用库里的笔记。"
resource: "https://github.com/Xinyang-Li666/SciCrucible"
tags: [claude-code, agent-skill, research, pdf, literature-review, sci-note]
timestamp: "2026-07-29T12:49:00.000Z"
---

# SciCrucible

## 它是什么

科研人员面对的文献管理痛点：

- PDF 读完了笔记散得到处是
- 想写 Introduction 又要重新翻所有笔记

SciCrucible 给 **Claude Code** 配了一组 Skills，组成一条完整链路：

```
PDF → 抽元数据 → 结构化笔记 → 跨文献查询 → 引用回写
         ↓
     每周自动扫描新论文
```

![示意图](https://pbs.twimg.com/media/HOSSqVnaQAEgV39.jpg)

## 它解决了什么

| 痛点 | SciCrucible |
|------|-------------|
| 笔记分散 | 结构化笔记统一存 |
| 写 Introduction 翻旧账 | 跨文献查询 |
| 新论文跟不上 | 周度自动扫描 |
| 引用要手敲 | 直接引用库里的笔记 |
| 笔记不复用 | 结构化 + 可检索 |

## 关键能力

| 能力 | 说明 |
|------|------|
| PDF 元数据抽取 | 自动解析 |
| 结构化笔记 | 统一格式便于检索 |
| 跨文献查询 | 写论文时直接调 |
| 周度新论文扫描 | 主动而非被动 |
| Claude Code Skill | 跑在 Claude Code 内 |
| 引用库 | 笔记变可复用素材 |

## 原始链接

- [项目仓库](https://github.com/Xinyang-Li666/SciCrucible)
- [推文剪藏](https://x.com/QingQ77/status/2082448303544054033)

## 相关概念

- [Obsidian Knowledge Agent](./tool-obsidian-knowledge-agent.md) — 六阶段 AI 管道把 PDF / 论文自动整理为 Obsidian 笔记
- [linXiv（本地优先学术论文管理）](./tool-linxiv.md) — Tauri 桌面 + Gemini 标注 + Obsidian 集成
- [Light Skills](./tool-light-skills.md) — 28 个科研全流程 AI Skill
- [Paper Lifecycle](./tool-paper-lifecycle.md) — 论文写作 Codex skills 套件