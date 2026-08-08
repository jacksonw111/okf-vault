---
type: "Tool"
title: "HTTrack"
description: "经典离线整站镜像工具：递归抓取整个网站到本地硬盘，可离线浏览，但不能处理登录墙与 JavaScript 渲染。"
resource: "https://www.httrack.com/"
tags: [offline-mirror, web-archiving, browser-engine]
timestamp: "2026-08-08T20:00:00Z"
---

# HTTrack

## 它是什么

HTTrack 是一款经典的开源离线整站镜像工具，让用户把一个网站递归抓取下来存到本地硬盘，方便离线浏览。它从 1998 年发布至今仍是「把整站搬回家」最直接的方案。

## 为什么用它 / 适合什么场景

- 想完整保存一个公开网站的内容做本地阅读 / 备份。
- 离线研究、教学、镜像场景。
- 不需要登录、不需要执行 JavaScript 的站点。

## 关键能力

| 能力 | 说明 |
|------|------|
| 递归抓取 | 把整站按链接递归拉下来，保持目录结构 |
| 离线浏览 | 抓完后可在本地按原站路径浏览 |
| 跨平台 | Windows / macOS / Linux 均有版本 |
| 链接修复 | 本地化后自动调整站内链接，指向本地文件 |

## 局限

- 无法处理登录墙 / Cookie / Session 后的内容。
- 不执行 JavaScript，对 SPA 站点几乎无效。
- 不做内容清洗 / 结构化抽取。

## 相关概念

- [Deepclone Website](./tool-deepclonewebsite.md) — 同样目标但能处理登录态，并自动产出 Markdown 分析
- [Sparkfetch](./tool-sparkfetch.md) — 不镜像整站，而把单个 URL 转成干净 Markdown/JSON
- [Firecrawl](./tool-firecrawl.md) — 云端网页清洗与抓取工具