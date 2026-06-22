---
type: "Tool"
title: "3D 打印文件自托管资产管理（多格式 + Moonraker/Klipper 工作流）"
description: "面向 3D 打印爱好者的自托管资源管理工具：支持 STL / 3MF / OBJ / STEP / G-code 多格式文件的上传、归类与检索，并集成 Moonraker / Klipper 打印机工作流（实时状态、远程发打印任务、历史与成本统计）。"
tags: "[3d-printing, self-hosted, moonraker, klipper, stl, 3mf, gcode]"
timestamp: "2026-06-22T07:20:00Z"
---

# 3D 打印文件自托管资产管理（多格式 + Moonraker/Klipper 工作流）

## 它是什么

一个面向 3D 打印爱好者的**自托管资源管理工具**，把打印文件资产管理与打印机控制合二为一：

- **多格式统一**：STL / 3MF / OBJ / STEP / G-code 全部支持；
- **归类 + 检索**：上传后能按项目、打印机、耗材等维度组织；
- **打印机工作流**：内置 **Moonraker / Klipper** 集成，可看实时状态、远程发打印任务、拉历史和成本统计。

> 项目名未在公开素材中给出；本文以功能维度记录。

![截图](https://pbs.twimg.com/media/HLTaHwBaYAA_yS7.jpg)

## 为什么用它 / 适合什么场景

- **多格式混乱**：Bambu Studio 出的 3MF、PrusaSlicer 出的 G-code、Thingiverse 下载的 STL，分散在不同文件夹，检索靠文件名搜索，效率极低。
- **打印工作流脱节**：打印文件管理工具（Thingiverse / Thangs / 自建 NAS）和打印机控制工具（Moonraker API / Fluidd / Mainsail）通常是两套东西。
- **成本追踪**：打印一次要花多少耗材、多少电、多少机时？大多数爱好者答不上来。

## 关键能力

| 能力 | 说明 |
|---|---|
| 多格式上传 | STL / 3MF / OBJ / STEP / G-code |
| 归类检索 | 自定义标签 / 项目 / 打印机 / 耗材等维度 |
| Moonraker / Klipper 集成 | 实时打印机状态（温度、进度、剩余时间） |
| 远程打印 | 在 UI 里点一下就发打印任务到 Klipper |
| 历史 + 成本 | 拉取打印历史，统计耗材 / 机时 / 电费 |

## 技术栈（推测）

- 自托管 → 大概率是 **Docker 镜像 / docker-compose** 起一个 web 服务。
- 后端需要解析 STL / 3MF 元数据（模型体积、耗材估算）。
- Klipper 通过 Moonraker 的 HTTP / WebSocket API 通信（无需在打印机上额外装东西）。

## 与同类工具的对比

| 维度 | 通用方案 | 本工具 |
|---|---|---|
| 文件管理 | NAS / 文件夹 | 专门的元数据 + 检索 |
| 切片 | Bambu Studio / PrusaSlicer | 不切片，只管文件与打印 |
| 打印机控制 | Fluidd / Mainsail | 集成 Moonraker，一站式 |
| 成本追踪 | 手动记 | 自动拉取历史统计 |

## 参考链接

- [原始链接](https://t.co/deQGccZEAc)

## 相关概念

- [NasberryPi](tool-nasberry-pi.md) — 树莓派轻量 NAS CLI（自托管存储底层）
- [Single Server](tool-single-server.md) — 一台 Linux 服务器串 Cloudflare + Tailscale + Docker + Kamal 一键部署（自托管部署参考）
- [OPG](tool-opg-backend.md) — 一人公司多 app 后端控制面