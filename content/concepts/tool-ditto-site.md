---
type: "Tool"
title: "ditto.site（ion-design/ditto.site）"
description: "把公开网址变成一套能跑的 TypeScript 应用——抓浏览器真正渲染出来的样子, 确定性地生成 Next.js 或 Vite React 项目, 而非让大模型去猜着写页面。"
resource: "https://github.com/ion-design/ditto.site"
tags: "[code-generation, scraping, nextjs, vite, react, dev-tooling]"
timestamp: "2026-07-17T03:39:00Z"
---

# ditto.site

[ditto.site](https://github.com/ion-design/ditto.site) 是「**把任意公开网址克隆成一套可跑的 TypeScript 应用**」的工具。它抓的是浏览器真正**渲染出来**的样子, 然后**确定性地生成 Next.js 或 Vite React 项目**, 关键差异——**不让大模型去猜页面长什么样**。

## 它和「AI 直接抄」不一样

通常的「AI 克隆网页」路径是: 把 HTML 喂给 LLM, 让它「照着写一个」。问题是:

- LLM 看 HTML 看不到真实布局 / 字体 / 颜色
- 它会**脑补**合理但与原页面不一致的代码
- 动效 / 字体子集 / 关键 CSS 选择器经常丢

ditto.site 走的是「**像素级抓 + 确定性子工程**」:

1. 用真浏览器渲染, 拿到**最终像素 + DOM 结构 + 关键样式**
2. 把视觉骨架**直接转成模板**, 而不是让模型写
3. LLM 只负责**填空页面内容**, 不再操心布局

## 关键能力

| 能力 | 说明 |
|------|------|
| 真实浏览器渲染 | 抓到的就是用户看到的, 不靠 HTML 猜 |
| Next.js / Vite 双输出 | 两种主流 React 工程自选 |
| 确定性模板 | 不靠 LLM 拼 DOM, 模板是用抓取数据直接生成的 |
| 纯 TypeScript | 输出可维护、可改, 不是一次性脚本 |

## 媒体

![](https://pbs.twimg.com/media/HNRPPj4bkAAV-11.jpg)

## 参考链接

- [项目仓库](https://github.com/ion-design/ditto.site)

## 相关概念

- [OpenMontage](./tool-openmontage.md) — 视频域的「AI 渲染最终成片」思路, ditto.site 是网页域的同类思路
- [Archify](./tool-archify.md) — LLM → JSON → 架构图的确定性转换, 与 ditto.site 的「不让 LLM 猜布局」思路相通
