---
type: "Tool"
title: "ClashOmega（Clash 代理规则管理 Chrome 扩展）"
description: "Chrome 浏览器扩展，用于管理 Clash 代理规则的切换、域名匹配检测与 YAML 规则增删，致敬 SwitchyOmega / ZeroOmega 的代理切换体验。"
resource: "https://github.com/ciskonc/ClashOmega"
tags: [clash, proxy, chrome-extension, network, switchyomega]
timestamp: "2026-06-24T15:30:00Z"
---

# ClashOmega（Clash 代理规则管理 Chrome 扩展）

## 它是什么

[`ciskonc/ClashOmega`](https://github.com/ciskonc/ClashOmega) 是一款 **Chrome 浏览器扩展**，专注于管理 [Clash](https://github.com/Dreamacro/clash) 代理规则：

- 规则切换（按场景切换不同的 profile / proxy group）
- 域名匹配检测（看当前域名命中哪条规则）
- YAML 规则增删（在浏览器里直接编辑规则）

设计上致敬 [SwitchyOmega](https://github.com/FelisCatus/SwitchyOmega) / ZeroOmega。

## 为什么用它 / 适合什么场景

- Clash 桌面客户端已在跑，但浏览器侧希望有更细粒度的规则控制；
- 想从 SwitchyOmega 切到 Clash 生态、但又舍不得那个「域名匹配可视化」体验；
- 经常要临时改 YAML 规则、又不想每次都跑去 Clash 客户端。

## 关键能力

| 能力 | 说明 |
|---|---|
| 代理规则切换 | 一键切换 profile / proxy group |
| 域名匹配检测 | 当前域名命中哪条规则一目了然 |
| YAML 增删 | 浏览器内直接编辑规则 |
| SwitchyOmega UX | 致敬经典代理切换扩展的交互 |

## 媒体 / 参考链接

![截图](https://pbs.twimg.com/media/HLi7N1bWgAAFHr8.png)

- [项目链接](https://github.com/ciskonc/ClashOmega)

## 相关概念

- [3X-UI](tool-3x-ui.md) — Xray 图形面板，与 Clash 互补的代理服务端
- [EasySNI](tool-easysni.md) — Go 单二进制集成 SNI 隧道 + XRay/sing-box + 域名前置
- [VLESS + WebSocket + TLS 绕过电信 QoS](playbook-vless-bypass-telecom-qos.md) — 代理协议层的另一类方案
