---
type: "Tool"
title: "amlogic-s9xxx-armbian（电视盒子 → Linux 服务器）"
description: "把运营商送的魔百盒 / 外贸盒子（CM311-1a / E900V22D / X96 Max+ 等）改装成 7×24h 低功耗 Linux 个人服务器（2-5W 待机），支持 Amlogic / Rockchip / Allwinner 多系列芯片，内置刷机备份 / eMMC 安装 / 内核更新 / Docker 一键部署。"
resource: "https://github.com/ophub/amlogic-s9xxx-armbian"
tags: "[armbian, linux, tv-box, homelab, self-hosted, nas, docker, tool]"
timestamp: "2026-09-24T21:55:00Z"
---

# amlogic-s9xxx-armbian（电视盒子 → Linux 服务器）

## 它是什么

[amlogic-s9xxx-armbian](https://github.com/ophub/amlogic-s9xxx-armbian) 是一个基于 Debian/Ubuntu 深度定制的项目，专门把「运营商送的电视盒子」（魔百盒 / 外贸盒子）改装成低功耗 Linux 个人服务器——待机功耗仅 2-5W，整年电费不过几块钱。

## 支持芯片生态

| 厂商 | 代表型号 |
|------|----------|
| Amlogic（晶晨） | S905 系列、S905X2/X3、S922X、A311D |
| Rockchip（瑞芯微） | RK3588、RK3568、RK3399 |
| Allwinner（全志） | H618、H6 |
| 其他数十款 | 主流 ARM 板卡 |

## 内置工具链

| 命令 | 作用 |
|------|------|
| armbian-ddbr | 刷机前完整备份原厂 Android，随时可回退 |
| armbian-install | U 盘体验满意后一键写入内部 eMMC，独立开机 |
| armbian-update | 在线平滑更新或回退 Linux 内核 |
| armbian-software | 一键安装 Docker / 面板环境 / 常用服务 |
| armbian-swap | 扩充虚拟内存 |
| armbian-openvfd | 控制机身 LED 面板 |

## 构建方式

- 本地：`./rebuild` 打包
- 云端：完备的 GitHub Actions 工作流，无需本地编译机也能打包专属固件

## 适用场景

- 挂载移动硬盘做轻量 NAS
- 部署 Home Assistant 智能家居中枢
- 跑 Docker 微服务
- 作为旁路由去广告
- 任何需要 7×24h 低功耗主机的家庭 / 实验场景

## 原始链接
- 项目主页：<https://github.com/ophub/amlogic-s9xxx-armbian>

## 相关概念