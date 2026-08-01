---
type: Tool
title: "chrome-client (Cronet)"
description: "komAAmok/chrome_client，给 Python 一个基于 Chromium Cronet 的真实浏览器 TLS 指纹 HTTP 客户端——爬虫 / 自动化场景用它拿到和真 Chrome 一样的 TLS 握手特征。"
resource: "https://github.com/komAAmok/chrome_client"
tags: "[python, http-client, cronet, tls-fingerprint, scraping, chromium]"
timestamp: "2026-08-01T20:30:00Z"
---

# chrome-client (Cronet)

## 它是什么

[`komAAmok/chrome_client`](https://github.com/komAAmok/chrome_client) 是一个 **Python HTTP 客户端**，底层用 **Chromium Cronet**（Chrome 内置的网络库）。它的杀手锏是：**TLS 握手指纹和真 Chrome 完全一致**——爬虫 / 自动化场景用它可以绕过基于 TLS 指纹的反爬检测。

## 为什么需要它

很多网站（Cloudflare、Akamai、DataDome 等）的反爬系统不只看你「User-Agent 是不是 Chrome」，还会看「TLS Client Hello 的特征（密码套件顺序、扩展、ALPN 等）」是不是和真 Chrome 一致。普通 Python HTTP 客户端（requests / httpx / aiohttp）的指纹一对比就露馅。

用 Cronet（Chrome 自己的网络库）发请求，TLS 握手就是「真 Chrome」级别的指纹。

## 关键能力

| 能力 | 说明 |
|------|------|
| Chromium Cronet 底层 | 复用 Chrome 的真实 TLS 实现 |
| Python API | 熟悉的 Python 调用方式 |
| 真实浏览器指纹 | TLS 握手看起来就是 Chrome |
| HTTP/2 / HTTP/3 支持 | Cronet 原生支持的现代协议 |

## 适合什么场景

- 爬虫被基于 TLS 指纹的反爬挡了（用 requests / httpx 拿到 403 / 521）
- 想在不被识别的情况下跑大量自动化请求
- 需要稳定通过 Cloudflare / Akamai 验证

## 与同类工具的差异

| 工具 | 指纹 | 差异 |
|------|------|------|
| requests / httpx | Python 默认 TLS | 易被识别 |
| [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver) | Selenium | 浏览器级，更重 |
| curl-impersonate | curl TLS 模拟 | 仅 curl 生态 |
| chrome_client (Cronet) | Python + 真 Chrome TLS | Python API + 真 Cronet |

## 原始链接

- [项目仓库](https://github.com/komAAmok/chrome_client)
- [原始推文](https://x.com/QingQ77/status/2083421465764843888)

## 相关概念

- [obscura-headless-browser](./tool-obscura-headless-browser.md) — 同为反指纹浏览器方向，但走完整浏览器控制