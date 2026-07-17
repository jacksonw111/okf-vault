---
type: "Tool"
title: "doubao-international（chuansd/doubao-international）"
description: "开源 Chrome/Edge 浏览器插件, 从 ihmily/doubao-nomark 派生而来, 主要多了 dola.com (豆包国际版) 的支持; 它劫持页面的 JSON.parse 和网络请求, 拿到豆包后端本来就会返回的无水印原图、原视频地址, 在页面塞一个下载按钮。"
resource: "https://github.com/chuansd/doubao-international"
tags: "[browser-extension, doubao, image-download, video-download, chrome]"
timestamp: "2026-07-17T07:43:00Z"
---

# doubao-international

[doubao-international](https://github.com/chuansd/doubao-international) 是一个**Chrome / Edge 浏览器插件**, 由 [ihmily/doubao-nomark](https://github.com/ihmily/doubao-nomark) 派生而来——主要差异是**多了对 [dola.com](https://dola.com/) (豆包国际版) 的支持**。

技术路径清晰: **劫持页面的 `JSON.parse` 和网络请求**, 从豆包后端原本就会返回的 JSON / 二进制流里**直接抠出无水印原图和原视频地址**, 然后在页面注入一个下载按钮。

## 它和「按右键 → 另存为」的差别

豆包对生成内容加了多层: 水印 / 压缩 / 跨域 / 视频转码 / Blob 加密。普通右键「图片另存为」拿到的是带水印的低清副本。doubao-international 利用「**后端其实一直在返回原始资源 URL**」这一事实, 在前端就拦截:

| 步骤 | 行为 |
|------|------|
| 1. 注入 hook | 覆盖页面 `JSON.parse`, 监听 fetch / XHR |
| 2. 抠原 URL | 抓到所有返回里的 `original_url` / `video_url` 等字段 |
| 3. 注入按钮 | 在页面对应作品下方塞一个「下载原图 / 原视频」按钮 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 原图抓取 | 拿的是无水印的全分辨率图像 |
| 原视频抓取 | 拿到无压缩原始 mp4, 不带水印 overlay |
| dola.com (国际版) 支持 | 在 ihmily/doubao-nomark 基础上的关键增量 |
| 浏览器原生插件 | Chrome / Edge Web Store 即装即用 |

## 参考链接

- [项目仓库](https://github.com/chuansd/doubao-international)
- [上游项目 ihmily/doubao-nomark](https://github.com/ihmily/doubao-nomark)

## 相关概念

- [sitecheck](./tool-sitecheck.md) — 浏览器扩展嗅探网站技术栈 / Geo / DNS / WHOIS, 同属「注入 hook + 旁路取原数据」的浏览器侧工具思路
