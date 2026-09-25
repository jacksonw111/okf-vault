---
type: "Tool"
title: "jev-seo（本地 SEO 审计 + 多格式报告生成）"
description: "输入一个网站首页地址，自动完成实时 SEO 审计（52 项规则检查 + PageSpeed + Jev 判定），输出 PDF / XLSX / Markdown 三种格式的可执行改进清单；规则结果与模型判断写进同一份 audit.json。"
resource: "https://github.com/AgriciDaniel/jev-seo"
tags: "[seo, audit, jev, pagespeed, python, claude-code-skill, pdf-report, excel-report, open-source]"
timestamp: "2026-09-25T15:55:00Z"
---

# jev-seo（本地 SEO 审计 + 多格式报告生成）

## 它是什么

[jev-seo](https://github.com/AgriciDaniel/jev-seo) 是一个**本地 Python 命令行工具**，也能装成 **Claude Code skill**——输入一个网站首页地址，自动完成实时 SEO 审计：

1. 抓取页面
2. 跑 **52 项 SEO 规则检查**
3. 读 PageSpeed 数据
4. 让 **Jev 模型**判断页面类型 / 搜索意图 / 内容质量 / 标题 / 描述
5. 规则结果 + 模型判断 → 同一份 **`audit.json`**
6. 同一份 `audit.json` → 生成 **PDF / Excel / Markdown** 三份可执行报告

## 为什么用它 / 适合什么场景

- 想给客户 / 自己网站做**一次性 SEO 体检**，不需要订阅昂贵的 SaaS。
- 想**本地、可复现**地跑审计——`audit.json` 一份就能复现报告，方便对照修复前后。
- 想要**多格式分发**——同一份审计，PDF 给老板、Excel 给运营 / 客户、Markdown 喂给编码 Agent 改页面。
- 偏好「**规则 + LLM 判定**」双管齐下：规则给出硬伤、LLM 给出主观判断（意图 / 标题质量），互相对照。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | Python CLI / Claude Code skill |
| 输入 | 网站首页 URL |
| 规则检查 | 52 项 SEO 规则 |
| 性能数据 | PageSpeed Insights |
| LLM 判定 | Jev 判断页面类型 / 搜索意图 / 内容质量 / 标题 / 描述 |
| 中间产物 | `audit.json`（规则 + 模型判断合并） |
| 报告输出 | PDF / XLSX / Markdown |
| 部署 | 本地运行 |

## 媒体

![](https://pbs.twimg.com/media/HTBxrkOawAADwNl.jpg)

## 相关概念

- [Jev](./term-jev.md) — 本项目用于「主观判断」的 TypeSafe 模型
- [seo-monster](./tool-seo-monster.md) — 把 Search Console / GA4 / PageSpeed / Cloudflare 70 个 SEO 工具塞进 AI 助手，更偏「数据源汇聚」
- [geo-score](./tool-geo-score.md) — 同作者思路的 GEO（答案引擎优化）评分工具，与 SEO 是相邻赛道
