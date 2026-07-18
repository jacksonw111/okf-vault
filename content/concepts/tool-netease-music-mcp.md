---
type: "Tool"
title: "netease-music-mcp（Vael-KY/netease-music-mcp）"
description: "网易云音乐 MCP 服务：让 AI 助手带着你自己的网易云 Cookie，直接操控真实账号——搜歌、建歌单、加歌、翻听歌记录、红心收藏、拉每日推荐都能做。"
tags: "[mcp, netEase, music, ai-assistant, automation]"
timestamp: "2026-07-18T20:00:00Z"
resource: "https://github.com/Vael-KY/netease-music-mcp"
---

# netease-music-mcp（Vael-KY/netease-music-mcp）

## 它是什么

[`netease-music-mcp`](https://github.com/Vael-KY/netease-music-mcp) 是 Vael-KY 开源的 **MCP（Model Context Protocol）服务**，专为网易云音乐打造：

- 把用户的网易云 Cookie 注入到 MCP 服务；
- AI 助手（Claude Desktop 等支持 MCP 的客户端）就能像「会写代码的用户」一样**直接动真实账号**；
- 搜歌、建歌单、加歌、翻听歌记录、红心收藏、拉每日推荐——全部支持。

## 关键能力

| 能力 | 说明 |
|------|------|
| MCP 协议 | 兼容主流 AI 客户端（Claude Desktop、Cherry Studio 等） |
| 用真实账号 | 携带 Cookie，操作等同登录态 |
| 搜歌 | 按关键词 / 歌手 / 专辑搜索 |
| 建 / 改歌单 | 增删歌单内歌曲 |
| 红心收藏 | 标记喜欢的歌曲 |
| 听歌记录 | 拉取最近播放 |
| 每日推荐 | 抓取网易云的个性化推荐 |

## 适合什么场景

- 用 AI 助手日常「按心情 / 场景挑歌」；
- 想让 AI 根据你的听歌历史 / 红心自动生成歌单；
- 自动化整理网易云歌单、做数据导出；
- 跟其他 MCP 服务（飞书、Notion 等）拼成「个人数字生活自动化」。

## 注意事项

- **Cookie 是真实凭据**：跑这个 MCP 等同把账号操作权交给 AI 助手，请仅在本地 / 受信任环境使用；
- 不要把 Cookie 写进公开仓库 / 公开部署。

## 参考链接

- [原始链接](https://github.com/Vael-KY/netease-music-mcp)

## 相关概念

- [CodexPro](tool-codexpro.md) — 同样用 MCP / 桥接把 AI 客户端和真实账号串起来；netease-music-mcp 走「音乐账号」路线，CodexPro 走「ChatGPT Web 账号」路线