---
type: "Tool"
title: "Droidspaces"
description: "让闲置安卓机秒变 Linux 微型服务器的神器，不是模拟器、不依赖 Termux，直接在内核层用 Namespace 容器隔离跑 systemd（PID 1），单文件静态二进制仅 400KB，原生 GPU 加速（Turnip / VirGL）、独立网络命名空间。"
resource: "https://github.com/ravindu644/droidspaces-oss"
tags: "[android, linux, server, namespace, container, systemd, gpu, self-hosted]"
timestamp: "2026-09-16T16:16:00Z"
---

# Droidspaces

## 它是什么

[ravindu644/droidspaces-oss](https://github.com/ravindu644/droidspaces-oss) 把**闲置安卓机**变成**高能 Linux 微型服务器**：**不是模拟器、也不依赖 Termux 中间层**，直接在内核层用 **Namespace 容器隔离**跑完整 **systemd（PID 1）**。单文件静态二进制仅 **400KB**，原生 GPU 加速（Turnip / VirGL）、独立网络命名空间与端口转发，配一个漂亮的 Android App 控制台。

## 为什么用它 / 适合什么场景

- 闲置安卓手机 / 平板想榨干剩余硬件价值，做家庭服务器 / 学习机。
- 不想装 Termux + Proot 这类模拟层，希望真 systemd 接管服务。
- 想跑 Docker / 自托管服务又不想专门买树莓派。
- 想随时随地开一台带 GPU 加速的图形桌面。

## 关键能力

| 能力 | 说明 |
|------|------|
| 内核 Namespace 隔离 | 不是用户态模拟，直接走 Linux 内核能力 |
| systemd PID 1 | 服务管理、依赖、日志与服务器版 Linux 一致 |
| 单文件 400KB | 静态二进制，免安装、便于拷贝 |
| 原生 GPU 加速 | Turnip / VirGL，图形桌面也能跑 |
| 独立网络命名空间 | 端口转发 / 网络隔离可控 |
| Android App 控制台 | 移动端可视化管理 |

## 相关概念

- [Mobile-Harness](./tool-mobile-harness.md) — 同为「安卓机变 AI 编码站」的思路，Droidspaces 偏服务器向
- [Super LAN Cache](./tool-super-lan-cache.md) — Droidspaces 上常跑的局域网缓存代理