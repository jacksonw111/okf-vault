---
type: "Tool"
title: "wizarr（wizarrrr/wizarr）"
description: "自托管的媒体服务器自动化用户邀请与引导管理系统,给 Plex/Jellyfin/Emby 朋友/家人发一条邀请链接就能自动加入并跟着引导教程完成安装配置。"
resource: "https://github.com/wizarrrr/wizarr"
tags: "[media-server, plex, jellyfin, emby, invite, self-hosted, onboarding]"
timestamp: "2026-07-16T05:07:00Z"
---

# wizarr

[wizarr](https://github.com/wizarrrr/wizarr) 是一套**自托管的自动化用户邀请与管理系统**,专门服务 Plex、Jellyfin、Emby 这类媒体服务器——把朋友/家人的邀请从「手把手教账号密码」简化成「一条链接,点开即入」。

## 它解决了什么

自己搭了 Plex/Jellyfin 共享给亲友的人,经常要反复帮别人:注册账号、装客户端、配服务器地址、登录,这套流程通常需要逐人讲解。wizarr 把这一流程固化成一次性邀请链接,链接里可以预置过期时间、邀请码、可加入的库与权限,对方点开就在浏览器里走完整个新人引导。

## 关键能力

| 能力 | 说明 |
|------|------|
| 一键邀请链接 | 为每位用户生成一次性邀请 URL,过期时间可配置 |
| 多后端支持 | 兼容 Plex / Jellyfin / Emby 三家媒体服务器 |
| 自动建账号 | 链接激活后自动在媒体服务器里创建用户 |
| 引导式教程 | 内置交互式引导页,带新人一步步装客户端、配服务器 |
| 自托管 | 单 Docker 容器即可部署,数据始终在用户自己手里 |

## 媒体

![](https://pbs.twimg.com/media/HNKsBLsa8AAE0t0.jpg)

## 参考链接

- [项目仓库](https://github.com/wizarrrr/wizarr)

## 相关概念

- [tmux-workbench](./tool-tmux-workbench.md) — 同样面向「自托管家人/朋友共享场景」的本地管理工具,与本工具定位互补
