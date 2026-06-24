---
type: "Tool"
title: "HypoMux（Windows 多网卡带宽聚合）"
description: "Windows 平台的多网卡带宽并发聚合下载加速工具，通过 L3 物理层套接字绑定与双协议代理引擎进行连接级调度，无需修改系统路由表即可让有线 / Wi-Fi / 手机热点同时发力下载。"
resource: "https://github.com/Hypostasis-Cat/HypoMux"
tags: [windows, networking, bandwidth, download, multi-nic]
timestamp: "2026-06-24T15:30:00Z"
---

# HypoMux（Windows 多网卡带宽聚合）

## 它是什么

[`Hypostasis-Cat/HypoMux`](https://github.com/Hypostasis-Cat/HypoMux) 是一款**专为 Windows 平台打造的多网卡带宽并发聚合下载加速工具**。核心机制：

- **L3 物理层套接字绑定** — 把不同连接直接绑到不同物理网卡；
- **双协议代理引擎** — 同时调度 HTTP/HTTPS 流量；
- **连接级调度** — 不用动系统路由表，多张网卡就能为同一批高并发下载任务同时出力。

## 为什么用它 / 适合什么场景

- 桌面上同时插着**有线网线 + Wi-Fi + 手机 USB 热点**，想物尽其用；
- 下载大文件时（Steam 游戏更新、IDM 大文件、Bt 种子）单网卡慢到抓狂；
- 不想改路由表（怕搞坏网络栈）又想用多网卡；
- 适合 Windows 平台用户。

## 关键能力

| 能力 | 说明 |
|---|---|
| 多网卡聚合 | 有线 + Wi-Fi + 热点并发 |
| L3 套接字绑定 | 物理层直绑不同网卡 |
| 双协议代理 | HTTP / HTTPS 都覆盖 |
| 无需改路由 | 不动系统网络栈 |
| 连接级调度 | 不同连接分配到不同网卡 |
| 高并发下载 | Steam / IDM / 大文件场景 |

## 媒体 / 参考链接

![截图 1](https://pbs.twimg.com/media/HLi_1TwXAAANNKd.jpg)
![截图 2](https://pbs.twimg.com/media/HLi_4TCWAAAKrlS.png)

- [项目链接](https://github.com/Hypostasis-Cat/HypoMux)

## 相关概念

- [NasberryPi](tool-nasberry-pi.md) — 树莓派 NAS 工具，本机存储侧的另一形态
- [VLESS + WebSocket + TLS 绕过电信 QoS](playbook-vless-bypass-telecom-qos.md) — 网络层另一类优化方向
