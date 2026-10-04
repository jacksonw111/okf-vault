---
type: "Note"
title: "awesome-esp32（ESP32 圈自己的精选清单）"
description: "curisama 维护的 ESP32 awesome 清单：按硬件型号索引项目，桌宠 / 显示 / 游戏 / 工具 / 代理协作硬件全覆盖，每条注明跑了什么板子。"
resource: "https://github.com/curisama/awesome-esp32"
tags: "[awesome, esp32, iot, hardware, embedded]"
timestamp: "2026-10-04T08:00:00Z"
---

# awesome-esp32

## 它是什么

[awesome-esp32](https://github.com/curisama/awesome-esp32) 是 **curisama** 维护的 ESP32 精选项目清单，副标题「值得做、值得抄、值得看着它跑的项目」——把社区里用 ESP32 实际做出来的项目系统收齐。每条项目结尾标注跑在什么硬件上：微雪 / LilyGO / M5Stack / Ulanzi 等成品设备全部入册。

## 主要板块与代表项目

| 板块 | 代表项目 | 亮点 |
|------|---------|------|
| 桌宠 / 对话硬件 | xiaozhi-esp32 | MCP 协议对话固件，几十元板子可跑 |
| 桌宠 / 像素宠物 | pixelcat | 电子宠物机像素猫，摸有反应，永远不死 |
| 桌宠 / 口袋妖怪复刻 | pocket-pet | 初代口袋妖怪计步手表屏 |
| 代理协作硬件 | Vibe Watch | 戴手腕上的 M5Stack，coding agent 并行干活，按键审批 |
| 代理协作硬件 | Code Familiar | 接 Codex / Claude Code，圆屏显权限请求 |
| 显示类 | OpenEPaperLink | 把超市电子价签回收成无线墨水屏阵列 |
| 显示类 | 航空罗盘 | M5Stack 模拟真仪表的磁罗盘卡 |
| 游戏 | esp32-gameos | 一块触摸板跑六个程序生成的游戏，60 帧 |
| 游戏 | infinite-golf | IMU 测挥杆打高尔夫 |
| 老牌实用 | Tasmota / WLED / Meshtastic | 经典开源 IoT 项目 |
| 新工具 | ESP-KVM | ESP32-P4 加 HDMI 采芯片，伪键鼠远程管理 BIOS |
| 新工具 | esp_ble_finder | 靠 BLE 信号强度找丢在家里的手机 |
| 新工具 | ESP32Drop | ESP32 直接出现在 iPhone AirDrop 列表 |
| 新工具 | familybox | 出差家长和不识字小孩的传话设备 |

## 入门辅助

清单开头附开发实践指南，所有经验从收录项目里提炼，每条注明踩坑来源。无硬件可用 Wokwi 浏览器仿真，或用 ESP Web Tools 从网页直接刷固件。

## devices.md

`devices.md` 单独做索引：「你手里有哪块板子，搜名字就列出对应全部项目」。

## 协议

CC0 协议，做出新东西可按 `CONTRIBUTING` 提 PR。

## 参考链接

- 项目链接：<https://github.com/curisama/awesome-esp32>

## 相关概念

- [Tasmota](https://github.com/tasmota/tasmota) — 经典 ESP32 智能家居固件（外链，OKF 未收录）