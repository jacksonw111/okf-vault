---
type: Tool
title: "sitecheck（技术栈嗅探浏览器扩展）"
description: "浏览器扩展，打开任意网页自动识别其技术栈（CMS、JS 框架、CDN 等 3000+ 签名），并展示站点 IP / Geo / DNS / WHOIS / 邮箱。"
resource: "https://github.com/NUCL3ARN30N/sitecheck"
tags: [browser-extension, tech-detection, osint, devtools]
timestamp: "2026-06-25T01:07:00Z"
---

# sitecheck（技术栈嗅探浏览器扩展）

## 它是什么

一个浏览器扩展，**装好后打开任意网站**就能立刻告诉你：

- 它用了什么 CMS、什么 JS 框架、有没有 CDN、属于 3000+ 种签名的哪一种。
- 这个站点的 IP、服务器地理位置、DNS 记录、WHOIS。
- 页面里暴露的邮箱地址。

## 为什么用它

- 「看别人的网站到底怎么搭的」——以前要打开 DevTools + 多个外部查询工具，现在一次到位。
- 对 OSINT / 选型调研 / 竞品分析 / 安全初筛都有用。
- 浏览器扩展形态让「随手一查」成本几乎为零。

## 关键能力

| 能力 | 说明 |
|------|------|
| 技术栈识别 | 覆盖 3000+ 签名（CMS / 框架 / CDN / 分析脚本等） |
| IP / Geo | 站点服务器地理与网络位置 |
| DNS | 完整解析记录 |
| WHOIS | 注册人 / 注册商 / 时间线 |
| 邮箱抽取 | 页面里可抓到的邮箱地址 |

## 相关概念

- [ngrok / webernetes](./tool-ngrok-webernetes.md) — 同属「网络侦察 / 部署可见性」赛道，但 webernetes 关注暴露面，sitecheck 关注技术指纹