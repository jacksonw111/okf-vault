---
type: Tool
title: "AdGuard Home Manager Mod"
description: "Magisk 模块 AdGuard Home For Android 的专用管理 App：自动读取模块配置连上（端口随机化也不影响），首页只留一个广告拦截总开关。"
resource: "https://github.com/liuzq2002/adguard-home-manager-mod"
tags: [adguard, android, magisk, dns, adblock]
timestamp: 2026-09-02T12:00:00Z
---

# AdGuard Home Manager Mod

## 它是什么

Android 上 [AdGuard Home](https://adguard.com/adguard-home.html) 常以 Magisk 模块的形式部署以获得系统级 DNS 拦截能力，但模块的 HTTP 管理端口是随机化的，每次重启都要手动翻配置文件查端口。`AdGuard Home Manager Mod` 把这个流程打包成一个独立 Android App：自动读取模块配置文件 → 自动连上 AdGuard Home 管理端口 → 首页只留一个广告拦截总开关。

## 关键能力

| 能力 | 说明 |
|------|------|
| 自动发现端口 | 启动时主动读模块配置文件，识别随机化的 HTTP 管理端口并自动连接 |
| 单开关操作 | 首页就是一个广告拦截总开关，开 / 关 / 暂停一目了然 |
| 配套模块管理 | 专注对接 AdGuard Home For Android 模块，不需要懂 DNS 完整配置也能用 |

## 项目链接

- [项目主页](https://github.com/liuzq2002/adguard-home-manager-mod)

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — 系统化整理某领域使用方法的封装思路
