---
type: "Tool"
title: "Deepclone Website"
description: "把「克隆一个需要登录的网站并离线重建」做成任务式全自动工具：先用真实浏览器登录、再自动爬取重建离线多页站、并让 AI 逆推出产品结构 / 数据模型 / 后端接口 / 设计系统四份 Markdown 文档。"
resource: "https://github.com/hi5jeff/deepclonewebsite"
tags: [web-cloning, headless-browser, offline-archive, ai-reverse-engineering, site-mirror]
timestamp: "2026-08-07T09:46:00Z"
---

# Deepclone Website

## 它是什么

Deepclone Website 是一个任务式全自动网站克隆工具，定位「克隆需要登录的网站并离线重建」。它先用真实浏览器（含登录态）启动会话，再自动爬取 / 重建出离线可浏览的多页站，并由 AI 逆推出四份 Markdown 文档：产品结构、数据模型、后端接口、设计系统。

## 为什么用它 / 适合什么场景

- 想把一个私有 / 后台 / 登录后才有内容的网站离线镜像下来学习或迁移。
- 想直接拿到「别人家产品」的产品结构、数据模型、API 草图，而不是手动扒接口。
- 想做竞品分析，把对方网站的骨架作为 Markdown 文档入知识库。
- 想给设计系统做对照参考，让 AI 把页面拆解成可复用 token / 组件清单。

## 关键能力

| 能力 | 说明 |
|------|------|
| 真实浏览器登录 | 用 headless 浏览器承载 cookie / session，绕过登录墙 |
| 离线多页重建 | 不只是首页，连子页面也抓下来 + 修复内链 / 资源 |
| AI 逆推产品结构 | 自动生成「产品由哪些模块构成」的 Markdown 文档 |
| AI 逆推数据模型 | 抓取过程中的请求 / 响应反推实体与字段关系 |
| AI 逆推后端接口 | 汇总 REST / GraphQL 调用，列成接口清单 |
| AI 逆推设计系统 | 把页面视觉拆为颜色 / 字号 / 间距 / 组件 token |
| 四份 Markdown 产物 | 全部以 Markdown 形式产出，便于纳入知识库或喂给 LLM |
| 任务式一键运行 | 给一个入口 URL，跑完出一份离线站 + 4 份分析文档 |

## 媒体

- ![Deepclone Website 流程示意](https://pbs.twimg.com/media/HPAcIKZawAA2HPB.jpg)

## 相关概念

- [HTTrack](./tool-httrack.md) — 经典离线整站镜像工具，不处理登录墙与 AI 逆推
- [Firecrawl](./tool-firecrawl.md) — 在线 RAG-friendly 网页抓取工具，与本工具互为对照（在线清洗 vs 离线重建）
- [Webfetch via Sparkfetch](./tool-sparkfetch.md) — 同属「AI 友好的网页抽取」工具谱系