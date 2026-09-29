---
type: "Tool"
title: "claude-s40（emir/claude-s40，2007 诺基亚 S40 接 Claude）"
description: "2007 年诺基亚 Series 40 手机只支持 TLS 1.0 又不带 SNI，连不上任何现代服务。这个项目用 Java ME 客户端加一台自建 Go 服务器把手机接进 Claude API。"
resource: "https://github.com/emir/claude-s40"
tags: "[nokia, s40, java-me, go, legacy, claude, tls, tool]"
timestamp: "2026-09-29T16:00:00Z"
---

# claude-s40（emir/claude-s40，2007 诺基亚 S40 接 Claude）

## 它是什么

[claude-s40](https://github.com/emir/claude-s40) 是 emir 开源的「老手机复活」项目：2007 年的诺基亚 Series 40 手机只支持 TLS 1.0 又不带 SNI，连不上任何现代服务（含 Anthropic Claude API）。本项目用 Java ME 客户端加一台自建 Go 服务器，把这部手机接进 Claude API。

## 它要解决的问题

现代 Web 服务普及 TLS 1.2 / 1.3 + SNI，旧手机的协议栈与之完全不兼容：
- TLS 1.0 被现代 API 全面弃用
- SNI（Server Name Indication）缺失导致无法在共享 IP 上路由 HTTPS

claude-s40 通过自建 Go 服务器做协议转换，让 2007 年硬件能跟 2026 年 AI 对话。

## 关键能力

| 能力 | 说明 |
|------|------|
| Java ME 客户端 | 跑在 Series 40 手机的 Java ME 运行时 |
| Go 协议转换服务器 | 在云 / 自托管服务器上把现代 API 转成旧设备能用的协议 |
| Claude API 接入 | 通过代理把对话请求转给 Claude |

## 适合谁

- 怀旧 / 极客：想让 2007 年手机跑现代 AI
- 研究老旧设备与现代 API 的协议桥接
- 想理解 TLS / SNI 演进史

## 原始链接

- 项目主页：<https://github.com/emir/claude-s40>

## 相关概念

- [Self-Hosted（自托管）](./term-self-hosted.md) — 自托管协议转换服务器是常见形态