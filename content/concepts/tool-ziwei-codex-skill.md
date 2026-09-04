---
type: Tool
title: "紫微斗数排盘 Codex 技能（带证据标签与置信度）"
description: "把古籍《紫微斗数》的排盘规则装进 Codex：按精确到小时的出生时间与精确到城市的出生地点推算指定年/月/日运势，每条结论挂原典页码、证据标签与置信度，字段不全时降精度而不硬造星曜。"
resource: "https://x.com/QingQ77/status/2095712454424801539"
tags: [codex, agent-skill, grounded-reasoning, provenance, confidence, chinese-classics]
timestamp: 2026-09-04T12:00:00Z
---

# 紫微斗数排盘 Codex 技能（带证据标签与置信度）

## 它是什么

把古籍《紫微斗数》的排盘规则整理成一套可被 Codex 执行的技能：输入**精确到小时的出生时间**和**精确到城市的出生地点**，即可推算任意一年 / 月 / 日的财运、事业、感情、学业等运势。

![](https://pbs.twimg.com/media/HRRTg-ibAAAk5cN.jpg)

## 真正值得借鉴的部分：溯源约束

抛开命理本身，这个技能在**「让模型照古籍推理而不是照感觉编」**上的做法是可迁移的：

| 约束 | 说明 |
|------|------|
| 原典页码 | 每条结论都挂上出处页码，可回查原文 |
| 证据标签 | 标注该结论由哪一类证据支持 |
| 置信度 | 每条结论带置信度，读者自行取舍 |
| 降精度而非编造 | 输入字段不全（如只知道日期不知道时辰）时**降低输出精度**，绝不硬造星曜补齐 |

这套「引用 + 标签 + 置信度 + 缺数据就降精度」的组合，适用于任何**以固定规则文本为准绳**的推理场景（法规解读、合同审阅、标准符合性检查）。

## 参考链接

- 原始链接：<https://x.com/QingQ77/status/2095712454424801539>
- 原文附带的仓库链接：<https://github.com/lin96008-maxlin/prd-outputs-interactive>（原文给出的链接与 [prd-outputs-interactive](./tool-prd-outputs-interactive.md) 相同，疑为笔误，本技能仓库地址待确认）

## 相关概念

- [prd-outputs-interactive](./tool-prd-outputs-interactive.md) — 原始材料给出的仓库链接指向该项目，两者链接关系待确认；方法上同属「模型遇到信息缺口时不臆造」的思路
