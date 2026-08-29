---
type: Tool
title: "Bookshelf（无数据库的自托管电子书发布：R2 / 本地目录 + OPDS）"
description: "把自有 EPUB / PDF 收藏发不成可在浏览器与 Kobo 等 OPDS 客户端阅读的站点，无需绑数据库——后端用 Cloudflare R2 或本地目录当对象存储，即拷即用。"
resource: "https://github.com/murerkinn/bookshelf"
tags: [ebook, epub, pdf, self-hosted, opds, kobo, r2, serverless]
timestamp: "2026-08-28T00:00:00Z"
---

# Bookshelf

## 它是什么
[murerkinn/bookshelf](https://github.com/murerkinn/bookshelf) 是**无数据库的自托管电子书发布方案**。痛点：自己有一堆 EPUB / PDF 想随时阅读，但市面上的自托管书库（Calibre-Web、COPS 等）通常**绑死 PostgreSQL / SQLite + 一套 Web 框架**，部署、迁移、备份都要先跟数据库打交道。

Bookshelf 的解法：

- **没有数据库**——后端用**对象存储**承载全部元数据与文件；
- 支持 **Cloudflare R2**（零运维、几乎免费）或**本地目录**（纯私有部署）；
- 暴露标准的 **OPDS 协议**——任何 OPDS 客户端（Kobo、Calibre 配套阅读 App、浏览器插件）都能直接对接；
- 浏览器端亦可直接阅读（EPUB / PDF 在线打开）。

## 为什么用它 / 适合什么场景
- 已有 EPUB / PDF 收藏想**无运维发不成个人书站**；
- 用 Kobo / 其他 OPDS 阅读器，想**同步自己书库**而非绑某个商业商店；
- 不想跑数据库——纯 R2 或本地目录就够了；
- 部署在 Cloudflare R2 上时，**几乎零成本**且免运维。

## 关键能力
| 能力 | 说明 |
|------|------|
| 无数据库 | 全靠对象存储（R2 / 本地目录） |
| 双存储后端 | Cloudflare R2（云端 / 零运维）或本地目录（纯私有） |
| OPDS 协议 | 兼容 Kobo、Calibre 客户端等标准 OPDS 阅读器 |
| 浏览器阅读 | EPUB / PDF 在线直接打开 |
| 自托管 | 全部资产与权限自管 |
| 迁移简单 | 无 schema，拷文件即迁移 |

## 相关概念
- [Cobalt Kobo](tool-cobalt-kobo.md) — Kobo 应用平台（启动器 / 应用商店 / 模拟器）；Bookshelf 是与之配套的**内容源**
- [Cendre Nvim](tool-cendre-nvim.md) — 完全不同的领域（Neovim 配色），但同属「无数据库 / 零配置」工具哲学的实例

## 参考链接
- 项目链接：<https://github.com/murerkinn/bookshelf>
- 原始推文：<https://x.com/QingQ77/status/2093214494675636387>
- 媒体：<https://pbs.twimg.com/media/HQskueYasAAHpfP.jpg>
