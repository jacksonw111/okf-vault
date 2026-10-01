---
type: Tool
title: "Morphe Patcher Web（容器化的 Android 设备打补丁服务）"
description: "GROWNUPS 出品的 headless 容器化方案：把 Morphe CLI 装进容器当 Web 服务跑，局域网里 hot-folder 监听 + Webhook 通知，省掉桌面 / 手机端那套吃 CPU / 内存的客户端。"
resource: "https://github.com/GROWNUPS/Morphe-Patcher-Web"
tags: [morphe, android, patcher, container, headless, webhook, hot-folder, self-hosted]
timestamp: 2026-10-01T01:07:00Z
---

# Morphe Patcher Web

## 它是什么

**Morphe Patcher Web** 是 [GROWNUPS](https://github.com/GROWNUPS) 出品的**容器化方案**——把原本要装在桌面 / 手机上的 **Morphe CLI** 打成 **Web 服务**，放到 NAS / 迷你主机 24×7 运行。

它针对的是 Morphe 这类 Android 设备打补丁工具的传统痛点：每次都要打开客户端、占 CPU 占内存。容器化后：

- **Headless**：纯后台服务，无桌面依赖
- **局域网可装**：NAS / 迷你主机开着就行
- **hot-folder 监听**：放入文件即触发
- **Webhook 通知**：完成后通知下游
- **整条自动化**：少掉手动操作

## 为什么用它 / 适合什么场景

- 已有 Morphe CLI，但希望它在 NAS / 迷你主机后台跑，**不绑桌面机**。
- 想把多个设备的补丁流程统一到一个 Web 服务里管理。
- 喜欢 **hot-folder + Webhook** 这种「丢进去自动跑」的自动化思路。
- 希望**远程触发**补丁流程而不是每次手动开客户端。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | Web 服务（headless） |
| 部署 | 容器（Docker 等） |
| 内核 | 调用 Morphe CLI |
| 自动化 | hot-folder 监听 |
| 通知 | Webhook |
| 适用场景 | NAS / 迷你主机 24×7 运行 |
| 收益 | 省 CPU / 内存、释放桌面机 |

## 参考链接

- 仓库：<https://github.com/GROWNUPS/Morphe-Patcher-Web>

## 媒体

- ![](https://pbs.twimg.com/media/HTcVvfJbAAAR7G7.png)

## 相关概念

- [Morphe CLI](https://github.com/topjohnwu/Magisk) — 上游 Morphe 工具链（外部链接，需自核 Morphe 实际指向）
- [OpenObserve](./tool-openobserve.md) — 同为自托管类 Web 服务
