---
type: Tool
title: "Mihari"
description: "终端里管理 mihomo 内核的订阅、系统代理、TUN 模式与 Web 面板，替代 Clash Party / Sparkle 这类 GUI 工具。"
resource: "https://github.com/mihari-proxy/mihari"
tags: [mihomo, clash, proxy, terminal, subscription, tun]
timestamp: "2026-08-25T19:30:00Z"
---

# Mihari

## 它是什么

[mihari-proxy/mihari](https://github.com/mihari-proxy/mihari) 是一个**终端优先**的 mihomo 内核管理工具。mihomo（Clash Meta 的活跃分支）通常被 GUI 客户端（Clash Party / Sparkle 等）控制，但 GUI 在 server / headless 环境不便。Mihari 把 mihomo 的所有日常管理动作——**订阅更新、系统代理开关、TUN 模式切换、Web 面板启停**——都暴露到命令行里，让「无人值守的代理节点管理」成为可能。

![](https://pbs.twimg.com/media/HQdGE0-aAAEtI1A.png)

## 为什么用它 / 适合什么场景

- **headless / 服务器场景**：没有 GUI，用 CLI 全程操作 mihomo。
- **喜欢终端流**：用 alias / tmux 把代理切换做成快捷命令。
- **想替代 GUI 客户端**：Clash Party / Sparkle 之类的桌面客户端觉得重。
- **自动化 / 脚本化**：订阅刷新、节点测速、定时切换都能 shell 化。

## 关键能力

| 能力 | 说明 |
|------|------|
| 订阅管理 | 拉取 / 解析 / 刷新 mihomo 订阅 |
| 系统代理开关 | 命令行启停系统代理 |
| TUN 模式 | 一键开启 TUN，处理非系统代理流量 |
| Web 面板 | 命令行启停 mihomo 自带 Web Dashboard |
| 节点测速 / 切换 | 命令行测速、选择最优节点 |

## 相关概念

- [3X-UI](./tool-3x-ui.md) — mihomo / xray 图形面板，与 Mihari 在「可视化」光谱另一端互补
- [VLESS 绕过电信 QoS](./playbook-vless-bypass-telecom-qos.md) — 同样依赖代理节点，绕过运营商限速

## 参考链接

- 项目链接: <https://github.com/mihari-proxy/mihari>
- 原始链接: <https://x.com/QingQ77/status/2092140417123021018>