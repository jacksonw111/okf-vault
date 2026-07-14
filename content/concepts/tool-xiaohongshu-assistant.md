---
type: "Tool"
title: "xiaohongshu-assistant（薄荷工坊 / XunMengWinter）"
description: "React + Vite 桌面 Web 应用,把小红书创作拆成左中右三栏:人设 / 搜热门 + 本地 RAG / 模型配置,选热门、出选题、写文案、画封面一键串成流水线。"
resource: "https://github.com/XunMengWinter/xiaohongshu-assistant"
tags: "[xiaohongshu, content-creation, rag, react, vite, ai-assistant, self-media]"
timestamp: "2026-07-14T05:00:00Z"
---

# xiaohongshu-assistant(薄荷工坊)

[薄荷工坊](https://github.com/XunMengWinter/xiaohongshu-assistant) 是一个 **React + Vite 桌面 Web 应用**,把小红书内容创作的散装流程收拢进**三列工作台**。

## 三列布局

| 列 | 职责 |
|----|------|
| 左栏 | 品牌与人设管理(账号定位 / 风格约束) |
| 中栏 | 搜热门 / 存素材 / 本地 RAG / 出选题与文案 |
| 右栏 | 模型配置(切换模型、参数) |

## 关键能力

| 能力 | 说明 |
|------|------|
| 选热门 | 内置小红书热门抓取与排行 |
| 存素材 | 本地 RAG,自己攒的爆款可被检索增强 |
| 出选题 | 基于风格与热门生成候选选题 |
| 写文案 | 按选题 + 人设生成完整文案 |
| 画封面 | 出图 / 排版封面草图(可选) |
| 桌面 Web | 浏览器直接用,无需 Electron |

## 适合什么场景

- 个人 / 小团队**小红书矩阵运营**,想要一个统一工作台替代散装工具。
- 内容创作者用「**风格约束 + 历史爆款 RAG**」保证多账号调性一致。
- 不想订阅第三方 SaaS,又想跑一套可定制的小红书助手。

## 与同类资源的差别

| 资源 | 特征 | xiaohongshu-assistant |
|------|------|-----------------------|
| creatorhub | 多平台(抖/小红/快手)采集 | 本工具面向「创作」,creatorhub 面向「采集搬运」 |
| MediaCrawler | 多平台数据采集 | 只采集;本工具覆盖采集 + 创作全流水线 |
| AI Media Assistant | 短视频生成 Web 工具 | 偏视频域;本工具偏图文小红书 |

## 参考链接

- [项目仓库](https://github.com/XunMengWinter/xiaohongshu-assistant)

## 相关概念

- [creatorhub](./tool-creatorhub.md) — 同样面向自媒体但偏多平台采集
- [AI Media Assistant](./tool-ai-media-assistant.md) — 中文短视频生成工具,与本工具的图文 / 视频域互补
- [note-ai-medium-tutorials](./note-ai-medium-tutorials.md) — 通用 AI 创作教程
