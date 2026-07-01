---
type: Tool
title: "FlareMo"
description: "realchendahuang 写的 Cloudflare 原生个人笔记系统，部署在 Cloudflare Workers + D1 + R2 上实现零服务器运维。Flomo 风格时间线 + 标签 / 附件 / 搜索 / 归档 / 回收站 / 公开分享，并兼容 Memos /api/v1 API。"
tags: "[cloudflare, notes, self-hosted, memo]"
timestamp: "2026-07-01T01:50:00Z"
resource: "https://github.com/realchendahuang/FlareMo"
---

# FlareMo

## 它是什么
realchendahuang 写的个人知识管理系统，定位是「Cloudflare 原生的 Flomo/Memos」。跑在 Cloudflare Workers 上，用 D1 当数据库、R2 当对象存储，全程在 Cloudflare 免费套餐内运行，零服务器运维。

## 为什么用它 / 适合什么场景
- 喜欢 Flomo 风格的时间线笔记但不想订阅
- 想把笔记系统托管在 Cloudflare 免运维
- 已在用 Memos / flomo 想自部署但又不想买 VPS
- 想白嫖 Cloudflare 免费额度

## 关键能力
| 能力 | 说明 |
|------|------|
| 零服务器运维 | 仅依赖 Cloudflare Workers + D1 + R2 |
| 时间线 UI | Flomo 风格的瀑布流卡片 |
| 标签 | 多标签聚合 |
| 附件 | 文件上传存 R2 |
| 全文搜索 | D1 FTS 索引 |
| 归档 / 回收站 | 软删除与恢复 |
| 公开分享链接 | 单条笔记可生成公开 URL |
| API 兼容 | 兼容 Memos /api/v1 API 子集，可对接 Memos 客户端 |
| 免费额度内 | 个人规模可永久白嫖 |

## 相关概念
- [cfnew-deployer](tool-cfnew-deployer.md) — Cloudflare Pages 部署器面板，FlareMo 一键部署的同生态工具
- [Second Brain on Cloudflare](tool-second-brain-cloudflare.md) — 另一个部署在 Cloudflare Workers 上的开源共享记忆层，更偏「多 Agent 共用记忆」
- [Memos / flomo 风格笔记](note-front-end-resources.md) — csaba_kissi 五件套的设计风格参考
- [OKF 是什么](term-okf.md) — 个人知识库根入口，FlareMo 是「轻量笔记 OKF」的一种实现

## 原始链接
- [项目仓库](https://github.com/realchendahuang/FlareMo)
- [截图](https://pbs.twimg.com/media/HMEPF3BXIAAeABj.jpg)