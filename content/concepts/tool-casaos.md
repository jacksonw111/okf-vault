---
type: Tool
title: "CasaOS（个人云操作系统）"
description: "开源的个人云操作系统，Go 编写，可在 ZimaBoard / NUC / 树莓派 / 旧电脑上运行，友好 Web UI 管理文件、安装 Docker 应用（10 万+ Docker 镜像支持）、监控系统资源，让任何硬件变成易用的个人云。"
resource: "https://github.com/IceWhaleTech/CasaOS"
tags: [self-hosted, personal-cloud, docker, home-server, casaos]
timestamp: 2026-06-26T16:50:00Z
---

# CasaOS

## 它是什么

CasaOS 是 [IceWhaleTech](https://github.com/IceWhaleTech) 出品的**开源个人云操作系统**——口号是"让任何硬件变成一个简单易用的个人云系统，无需编程或技术背景"。

- 实现：Go 编写
- 兼容硬件：ZimaBoard、NUC、树莓派、旧电脑等
- 形态：友好的 **Web UI**
- 能力：
  - 文件管理（图形化操作）
  - **Docker 应用一键安装**（10 万+ Docker 镜像支持）
  - 系统资源监控

## 为什么用它

| 痛点 | CasaOS 解法 |
|------|-------------|
| 自建 NAS 要写命令 | 图形化 Web UI |
| 想跑 Docker 应用但不会 docker run | 一键安装 10 万+ 镜像 |
| 旧电脑 / NUC 想废物利用 | 装上即变个人云 |
| 树莓派做家庭服务器 | 内置适配 |
| ZimaBoard 这类 x86 小主机 | 完美兼容 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 多硬件支持 | ZimaBoard / NUC / 树莓派 / 旧 PC |
| Web UI | 浏览器即管理，无需 SSH |
| Docker 一键 | 内置应用市场，10 万+ 镜像 |
| 文件管理 | 图形化上传 / 下载 / 分享 |
| 资源监控 | CPU / 内存 / 磁盘 / 网络实时 |
| 零基础上手 | 装好即用 |

## 原始链接

- [项目仓库](https://github.com/IceWhaleTech/CasaOS)
- [原始推文剪藏](https://x.com/QingQ77/status/2070517438710452521)

## 相关概念

- [Seahi-Serial](./tool-seahi-serial.md) — 同样面向"小型硬件 / 创客"，但偏串口调试
- [NasberryPi](./tool-nasberry-pi.md) — 同样给树莓派做 NAS，但走 CLI 而非 Web UI
- [Seahi-Serial 多串口调试工具](./tool-seahi-serial.md) — 与本工具组合使用，可在 CasaOS 上跑多串口调试服务
