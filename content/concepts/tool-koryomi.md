---
type: Tool
title: "Koryomi（自托管漫画/条漫阅读器）"
description: "一个镜像搞定的自托管漫画/条漫阅读 PWA：内置 MangaDex API + 通用抓取引擎，从发现、抓取、监控到阅读一条龙，支持 CBZ / CBR / 图片文件夹，多用户 + 排行榜 + TOTP 双因素。"
resource: "https://github.com/AngeloSha/koryomi"
tags: [self-hosted, manga, comic, pwa, docker, manga-reader]
timestamp: 2026-06-26T16:50:00Z
---

# Koryomi

## 它是什么

Koryomi 是一个**单 Docker 镜像的自托管漫画/条漫阅读器**，定位是替代"装五六个容器才能跑起来"的自托管漫画栈（下载器 + 刮削 + 元数据 + 存储 + Web UI + 用户系统）。

- 形态：PWA（桌面 / 移动浏览器都能装到主屏）
- 镜像格式：支持 CBZ、CBR、图片文件夹
- 来源：内置 MangaDex API + 通用解析引擎，**粘贴一个源站网址就能自动识别并开始抓取新章节**
- 离线：抓取后自动打包成 CBZ，可离线阅读
- 多用户：独立阅读进度、排行榜、TOTP 双因素认证

## 为什么用它

| 痛点 | Koryomi 解法 |
|------|-------------|
| 自托管漫画要装一坨容器 | 单镜像即可 |
| 不同源站要分别写爬虫 | 内置通用解析引擎 + MangaDex 官方 API |
| 抓下来要手动整理 | 自动打包 CBZ + 离线缓存 |
| 多人共用一个库 | 用户系统 + 独立进度 + 排行榜 |
| 暴露公网担心被刷 | TOTP 双因素 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 单镜像部署 | 不用 docker-compose 一长串 |
| 自动抓取 | 粘贴源站 URL，自动识别章节结构并按更新抓 |
| CBZ / CBR 支持 | 兼容主流漫画格式 |
| 通用解析引擎 | 不绑定 MangaDex，可扩展到任意站点 |
| PWA 阅读 | 类原生 App 体验，桌面/移动通吃 |
| 多用户 | 独立进度、排行榜、TOTP 双因素 |

## 原始链接

- [项目仓库](https://github.com/AngeloSha/koryomi)
- [原始推文剪藏](https://x.com/QingQ77/status/2070291700619116838)

## 相关概念

- [Seahi-Serial](./tool-seahi-serial.md) — 同样是"单工具替代多容器思路"，但面向多串口调试而非漫画
- [EasySNI](./tool-easysni.md) — Go 单二进制集成 SNI 隧道 + XRay/sing-box + 域名前置 + 扫描器，思路相近
- [Koryomi（同类对比）](./tool-linxiv.md) — linXiv 也是 Tauri 桌面 + SQLite 离线阅读，定位是"学术论文"而非"漫画"
