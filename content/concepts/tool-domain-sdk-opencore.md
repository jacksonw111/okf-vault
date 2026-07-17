---
type: "Tool"
title: "domain-sdk（opencoredev/domain-sdk）"
description: "把域名「增、查、列、验、删」的标准生命周期归一化了, 能返回客户侧要填的精确路由、所有权和证书 DNS 记录, 并按服务商自己的校验和证书状态判断就绪, 不会误报。"
resource: "https://github.com/opencoredev/domain-sdk"
tags: "[domain, dns, sdk, dev-tooling, devops]"
timestamp: "2026-07-17T00:37:00Z"
---

# domain-sdk

[domain-sdk](https://github.com/opencoredev/domain-sdk) 把域名的完整生命周期——**增 (Create)、查 (Read)、列 (List)、验 (Verify)、删 (Delete)**——归一化成一套跨服务商的 API, 同时返回客户侧要填的精确**路由、所有权和证书 DNS 记录**, 并依照服务商自己的校验与证书状态判断「是否就绪」, 避免误报。

## 它解决的问题

每个 DNS / 域名服务商 (Cloudflare / Route53 / 阿里云 / GoDaddy) 的控制面板命令、API 参数、DNS 记录类型都不一样。任何跨云的域名管理脚本都要面对三件事：

1. **填什么** —— 路由 / 所有权 / 证书记录值的字段名因服务商而异
2. **就绪与否** —— 单纯轮询 `propagated=true` 容易被「半就绪」状态骗到
3. **生命周期** —— 「增→验→删」链路拆得支离破碎

本 SDK 把这三点都封装掉, 用一套调用走全流程。

## 关键能力

| 能力 | 说明 |
|------|------|
| CRUD 归一化 | Create / Read / List / Verify / Delete 一套动词 |
| DNS 记录字典 | 直接给出每家服务商对应的具体记录值与字段名 |
| 就绪判定 | 取服务商自家的校验与证书状态, 不靠轮询误判 |
| 跨服务商统一接口 | Cloudflare / Route53 / 阿里 / GoDaddy 等可插拔适配 |

## 参考链接

- [项目仓库](https://github.com/opencoredev/domain-sdk)

## 相关概念

- [3X-UI](./tool-3x-ui.md) — Xray 图形面板, 域名是其 TLS 链路的一环, 本 SDK 可与之联动
- [Lucky](./tool-lucky.md) — DDNS + ACME + 反代瑞士军刀, 本 SDK 可补齐其「跨服务商」一角
