---
type: "Tool"
title: "Open-Box（OpenWrt 一键 sing-box 透明代理）"
description: "给 OpenWrt 路由器提供一条命令装完的 sing-box 透明代理：订阅 / 节点 / 分流 / DNS 全部浏览器面板点选，配错一键恢复直连。"
resource: "https://github.com/liandu2024/Open-Box"
tags: "[openwrt, sing-box, proxy, networking, router]"
timestamp: "2026-09-11T22:00:00Z"
---

# Open-Box

## 它是什么

[liandu2024/Open-Box](https://github.com/liandu2024/Open-Box) 是 **OpenWrt 路由器上的一键 sing-box 透明代理**：一条命令装完，订阅 / 节点 / 分流 / DNS 全部通过浏览器面板点选，配错可一键恢复直连。

## 协议覆盖

| 协议 | 支持 |
|------|------|
| shadowsocks | ✓ |
| vmess | ✓ |
| vless（含 REALITY） | ✓ |
| trojan | ✓ |
| hysteria2 | ✓ |
| tuic | ✓ |
| anytls | ✓ |
| wireguard | ✓ |

订阅兼容 **Clash YAML** 与 **base64 分享链接**；节点按地区自动改名分组。

## 为什么用它 / 适合什么场景

- 家里 / 小公司用 OpenWrt 路由器需要科学上网 / 透明代理。
- 想用 sing-box 的多协议能力但不想手敲配置。
- 想保留「配错能秒回直连」的安全网，避免把自家网络锁死。

## 关键能力

| 能力 | 说明 |
|------|------|
| 一键安装 | 单条命令在 OpenWrt 上跑完 |
| Web 面板 | 订阅 / 节点 / 分流 / DNS 全部 GUI 操作 |
| 多协议 | 覆盖主流代理协议（含 REALITY） |
| 订阅兼容 | Clash YAML + base64 分享链接 |
| 节点改名 | 按地区自动分组排序 |
| 一键直连 | 配错秒级恢复，避免锁死网络 |

## 参考链接

- 项目仓库：<https://github.com/liandu2024/Open-Box>

## 媒体

- ![](https://pbs.twimg.com/media/HRvlmNvb0AAhz8L.jpg)

## 相关概念

- [Lucky](./tool-lucky.md) — DDNS + ACME + 反代瑞士军刀
- [3X-UI](./tool-3x-ui.md) — Xray 图形面板
- [playbook-vless-bypass-telecom-qos](./playbook-vless-bypass-telecom-qos.md) — 绕过电信 QoS 的 VLESS 部署剧本
</content>
</invoke>