---
type: "Tool"
title: "Papermorph（教材 PDF → 静态网页书）"
description: "DozenTwelve 出品的 Claude Code Skill——输入教材 PDF，输出一个**不用服务器的静态网页书**；流程写死成 6 步（PDF 拆章节 → 列章节地图 → 拷引擎与模板 → 第 1 章先做交人审 → 通过后顺序做剩余章节），避免 LLM 一次跑崩。"
resource: "https://github.com/DozenTwelve/Papermorph"
tags: "[pdf, ebook, static-site, skill, claude-code, agent]"
timestamp: "2026-10-06T22:51:00Z"
---

# Papermorph（教材 PDF → 静态网页书）

## 它是什么

**Papermorph** 是 DozenTwelve 出品的 Claude Code Skill——输入教材 PDF，输出一个**不用服务器的静态网页书**。把流程写死成 6 步，避免 LLM 一次跑崩：

1. 把 PDF 按书签拆成章节文本
2. 列一张带标题、单元、时长、状态的「章节地图」
3. 拷贝引擎与封面模板
4. 先做第 1 章交人审
5. 通过后才顺序做剩余章节
6. 输出静态站点（HTML + 资源），可直接部署到 GitHub Pages / Netlify

## 为什么用它 / 适合什么场景

- **教材电子化**：把 PDF 教材转成可在浏览器阅读的网页书（可搜索 / 可复制 / 可分享）
- **零服务器**：输出纯静态，丢 GitHub Pages / 对象存储即可
- **流程可控**：先做 1 章交人审，避免 LLM 全本跑完才发现方向错
- **Agent 友好**：作为 Skill 加载到 Claude Code，复用整套流程

## 关键能力

| 能力 | 说明 |
|------|------|
| PDF 按书签拆分 | 自动按 PDF outline 切章节 |
| 章节地图 | 标题、单元、时长、状态一表看清 |
| 引擎 / 模板 | 自带静态站引擎与封面模板 |
| 渐进生成 | 章节顺序做，每章可暂停 / 调整 |
| 输出静态 | HTML + 资源，可托管到任何静态服务 |

## 参考链接

- 项目链接：<https://github.com/DozenTwelve/Papermorph>

## 相关概念

- [Agent Skills 是什么](./term-agent-skills.md) — Skill 加载机制
- [Claude Code](./term-claude-code.md) — 主要宿主
