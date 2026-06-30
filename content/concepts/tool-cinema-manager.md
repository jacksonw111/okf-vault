---
type: Tool
title: "Cinema Manager（找片 Skill）"
description: "面向 AI 编码代理的「找片 + 媒体库整理」Skill——告诉代理想看什么片，它就多源搜索、按 4K/BluRay/REMUX/HDR/Atmos/字幕维度打分、自动转存网盘或 NAS，并整理成 Infuse / Plex / Jellyfin 可识别的目录结构。"
resource: "https://github.com/DavidBB-L/cinema-manager"
tags: "[skill, agent, media, nas, plex, jellyfin]"
timestamp: "2026-06-30T15:30:00Z"
---

# Cinema Manager（找片 Skill）

## 它是什么

Cinema Manager 是一款面向 AI 编码代理（Claude Code / Codex / Cursor / Windsurf 等）的 Skill：用户用自然语言告诉 Agent「我要看某部电影」，Agent 就去多个内容源里搜索、按清晰度 / 片源 / HDR / 音频 / 编码 / 字幕等维度打分，把最佳版本保存到夸克网盘或其它网盘 / NAS 目录，再按「电影名 (年份)」「剧名 / Season xx / SxxExx」的结构整理成 Infuse、Plex、Jellyfin 等媒体中心可直接识别的目录。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多源搜索 | 内容源插件式，可自行新增站点，不绑定单一来源 |
| 质量评分 | 按 4K / BluRay / REMUX / HDR / Atmos / 字幕等维度打分，优先高质量版本 |
| 网盘 & NAS 保存 | 搜到合适资源后一键存到自己的网盘或 NAS 目录 |
| 自动分类 | 通过 OMDB API 或内容源抓取识别类型，按动作 / 剧情 / 科幻等分类 |
| 媒体库整理 | 文件名与目录结构直接适配 Infuse / Plex / Jellyfin，省去手工刮削 |

## 适用场景

- 想看某部片但懒得自己找 / 挑版本 / 转存 / 改文件名 / 分文件夹。
- 让 AI 代理承担「搜 → 比 → 存 → 分」全链路。

## 相关概念

- [Cognee](./tool-cognee.md) — 同样是给 AI 代理补能力的 Skill 形态，但偏长期记忆
- [AIGX](./tool-aigx.md) — 同为面向 AI 编码代理的「上下文结构化」基础设施
- [Infuse / Plex / Jellyfin](https://plex.tv/) — 目标媒体中心（外部）

## 参考链接

- 项目链接：<https://github.com/DavidBB-L/cinema-manager>