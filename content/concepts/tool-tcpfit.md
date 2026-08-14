---
type: "Tool"
title: "tcpfit"
description: "Kylin010 开源的 Linux VPS TCP 调优脚本：按本机带宽探测缓冲区与拥塞控制，再用测速找到「丢包起点」，把出口平滑压到略低于限速点，避免「买了 500M 跑不满、一满就掉速」。"
resource: "https://github.com/Kylin010/tcpfit"
tags: ["linux", "tcp", "networking", "vps", "tuning", "open-source", "shell"]
timestamp: "2026-08-14T19:50:00Z"
---

# tcpfit

## 它是什么
tcpfit 是给 Linux VPS 用的 TCP 调优脚本。**不套用固定参数**：先用测速摸到当前机器的可用带宽，据此调整拥塞控制算法与缓冲区，再做测速找到「机房端口限速开始丢包」的那个拐点，把出口平滑压在略低一点。它不「加速」物理线路，也不改路径；只在已有带宽内把「丢包 / 重传」换掉。

## 为什么用它 / 适合什么场景
- 场景一：买了 500M 但跑不满、跑满就掉速 / 抖。
- 场景二：跑代理 / 跨国 TCP，需要在「已经限速」的线路上稳定压高利用率。
- 场景三：硬限速机房（OpenVZ / KVM 部分套餐），TCP 调优可拉回一截可用率。

## 关键能力
| 能力 | 说明 |
|------|------|
| 探测方式 | 自动测速找带宽上限 |
| 调优对象 | 拥塞控制、缓冲区 |
| 防抖策略 | 找到丢包起点，把出口平滑压在该点略低 |
| 适用 | Linux VPS、代理 / 跨国 TCP |
| 限制 | 不改线路、不加速；瓶颈在国际或已调过 BBR 时基本不出力 |

## 相关概念
- [3X-UI](./tool-3x-ui.md) — Xray 图形面板，常见「代理 + 调优」组合里的面板侧
- [WARP-Manager](./tool-warp-manager.md) — 纯 Bash VPS 工具，nftables TPROXY + sing-box 域名级 WARP 路由，与 tcpfit 同属 VPS 自调工具
