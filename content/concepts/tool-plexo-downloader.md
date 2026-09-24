---
type: "Tool"
title: "Plexo（多网卡并发下载管理器）"
description: "Electron 写的桌面下载管理器，覆盖 Windows / macOS / Linux。把单条 TCP 连接跑不满带宽时闲置的网卡（Wi-Fi / 以太网 / USB 共享网络）绑成多条并发连接同时下载同一个文件，最大化利用总带宽。"
resource: "https://github.com/anmolkapil/plexo"
tags: "[downloader, multi-nic, electron, http-range, network, tool]"
timestamp: "2026-09-24T21:55:00Z"
---

# Plexo（多网卡并发下载管理器）

## 它是什么

[Plexo](https://github.com/anmolkapil/plexo) 是 Electron 写的桌面下载管理器，覆盖 Windows、macOS、Linux。解决「单条 TCP 连接跑不满实际带宽、其余网卡闲置」的场景：把 Wi-Fi、以太网、USB 共享网络绑成多条并发连接，**同时下载同一个文件**。

## 关键技术点

| 设计 | 说明 |
|------|------|
| 文件分块 | 把文件切成最大 8MB 的分块 |
| 并发下载 | 通过 HTTP Range 请求并发取块 |
| 网卡绑定 | 每条连接通过 Node.js 的 `localAddress` 绑定到指定物理网卡 |
| 连接上限 | 单网卡最多 8 条连接、全局最多 32 条 |

## 适用场景

- 同时接入 Wi-Fi + 有线 + USB 共享网络，想榨干总带宽
- 单个 TCP 流被服务商限速，想绕开限速（注意合规）
- 移动热点 + 有线双接入的混合环境

## 注意点

- 同时使用多网卡需操作系统允许同时上网（Wi-Fi + Ethernet 共存）
- 服务端支持 HTTP Range 才能并发分块
- 多网卡并发不等同于「突破运营商单连接限速」——合规使用

## 原始链接
- 项目主页：<https://github.com/anmolkapil/plexo>

## 相关概念