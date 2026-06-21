---
type: "Tool"
title: "Single Server（一台 Linux 服务器的极简统一部署）"
description: "一台 Linux 服务器串起 Cloudflare + Tailscale + Docker + Kamal + GitHub，把所有个人应用跑在一台机器上：交互式脚本初始化，singleserver add <repo> 接入仓库，git push 后 5 秒内自动发布上线，无构建队列、无需逐 app 付费。"
resource: "https://github.com/qingq77/single-server"
tags: "[deploy, kamal, docker, tailscale, cloudflare, self-hosted, github]"
timestamp: "2026-06-21T16:00:00Z"
---

# Single Server（一台 Linux 服务器的极简统一部署）

## 它是什么

一套把「一台 Linux 服务器当 PaaS 用」的极简部署方案：把 Cloudflare、Tailscale、Docker、Kamal 和 GitHub Actions 串成一条流水线。一次性跑通交互式安装脚本做初始化，之后每加一个项目用 `singleserver add <repo>` 注册一次，下次 `git push` 到 main 就在 5 秒内发布上线，**不引入构建队列，也不必为每个应用单独买 PaaS 套餐**。

## 为什么用它 / 适合什么场景

- 一个人 / 小团队维护一堆 side-project / SaaS，不想每个都挂 Vercel / Render / Railway 单独计费。
- 手里就一台干净的 Linux VPS（或自购小服务器），想把它榨干。
- 喜欢「git push 就上线」这种极简工程体验，不愿意维护庞大的 CI/CD 配置。

## 关键能力

| 能力 | 说明 |
|------|------|
| 一次性安装 | 交互式脚本把 Cloudflare、Tailscale、Docker、Kamal、GitHub Actions 全部串起来 |
| 接入仓库 | `singleserver add <repo>` 注册仓库（自动写 GitHub Actions + Kamal 配置） |
| 发布节奏 | `git push` 后 5 秒内线上生效（无构建队列、单实例直接换） |
| 网络 | Cloudflare 做 DNS / 反代，Tailscale 私有组网直连服务器管理面 |
| 容器化 | Docker + Kamal 部署应用容器 |
| 成本 | 一台服务器的钱撑 N 个应用，不按 app 计费 |

## 适用边界

- 单机能 hold 住的负载（个人 / 小团队 / 内部工具向）；碰到要水平扩容、流量的场景仍是水平扩 + 真 PaaS 的活。
- 应用需要能塞进 Docker 镜像；非容器化遗留项目得先容器化。

## 相关概念

- [3X-UI](tool-3x-ui.md) — 同为「一台服务器撑起整套自托管工具栈」的瑞士军刀思路
- [Lucky](tool-lucky.md) — 同为面向自托管者的轻量运维面板
- [ngrok / webernetes](tool-ngrok-webernetes.md) — 在「把本地/单节点暴露到公网」这件事上的另一条路