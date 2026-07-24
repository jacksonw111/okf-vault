---
type: Tool
title: "Network Doctor（TUI 网络诊断链）"
description: "终端 TUI 网络诊断工具：自动按依赖图顺序依次跑完网卡 / TCP 出口 / DNS / TCP 连接 / TLS 握手 / HTTP/HTTPS 响应整套链路检查,既可指定目标地址也可只做本地诊断,把原始输出拼成「哪里断了、为什么、怎么修」的结论。"
resource: "https://github.com/heymaikol/network-doctor"
tags: [tui, network, diagnostics, terminal, rust]
timestamp: "2026-07-24T00:00:00Z"
---

# Network Doctor（TUI 网络诊断链）

## 它是什么
[Network Doctor](https://github.com/heymaikol/network-doctor) 是一款终端 TUI 工具：传统排查「家里 / 服务器断网」要在 shell 里挨个跑 `ping`、`dig`、`curl`、`traceroute`，再把一堆原始输出拼起来人肉猜问题。Network Doctor 把整条诊断链串成一个 TUI 流程——跑完直接告诉你 **断在哪、为什么、怎么修**。

## 为什么用它 / 适合什么场景
- 网络出问题时，希望「一条命令 + 一个界面」看完整个诊断链。
- 不想每次手动决定先 `dig` 还是先 `traceroute`，工具帮你按合理顺序跑。
- 想给非网络专业的同事一个低门槛故障排查入口。

## 关键能力
| 能力 | 说明 |
|------|------|
| 依赖图诊断 | 自动按链路顺序跑网卡 → TCP 出口 → DNS → TCP 连接 → TLS 握手 → HTTP/HTTPS 响应 |
| 双模式 | 支持输入目标地址做端到端检测,也可只跑本地链路 |
| 一键诊断 | 无需手动决定先 dig 还是先 traceroute,工具按合理顺序跑 |
| TUI 界面 | 全终端操作，远程 SSH 也能用 |
| 结论导向 | 不只贴原始输出，直接给出「断在哪、为什么、怎么修」 |
| 链式定位 | DNS / 路由 / TLS / 端到端逐段判定 |
| 轻量 | 单进程、单二进制 |

## 相关概念
- [tabiew](tool-tabiew.md) — Rust 写的 TUI 表格数据查看器（同生态）

## 参考链接
- 项目链接: <https://github.com/heymaikol/network-doctor>
- 视频演示: <https://video.twimg.com/tweet_video/HNlQYWuaYAAIWjz.mp4>
