---
type: Tool
title: "Cloudflare Trace API"
description: "Cloudflare 提供的免注册访客网络信息端点，可返回 IP、国家代码和接入数据中心代码。"
resource: "https://www.cloudflare.com/cdn-cgi/trace"
tags: [cloudflare, api, geolocation]
timestamp: "2026-07-25T00:00:00Z"
---

# Cloudflare Trace API

Cloudflare 提供的免注册访客网络信息端点，可返回 IP、国家代码和接入数据中心代码。

## 适用场景

- 需要通过 GET 请求直接调用，不需要账号或 API Key的场景。

## 关键能力

| 能力 | 说明 |
|------|------|
| 零凭证访问 | 通过 GET 请求直接调用，不需要账号或 API Key。 |
| 轻量网络信息 | 响应包含 loc（国家代码）、ip 与 colo（数据中心代码）等字段。 |
| 适用场景 | 适合轻量地判断访客出口位置与 Cloudflare 接入点；不应替代精确地理定位服务。 |

## 链接与媒体

- [项目链接](https://www.cloudflare.com/cdn-cgi/trace)
- [原始链接](https://x.com/austinit/status/2080928090201715074)

![](https://pbs.twimg.com/media/HODxDONaEAAOIMe.jpg)

## 相关概念

暂无需要强关联的现有概念。
