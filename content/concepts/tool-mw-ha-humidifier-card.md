---
type: Tool
title: "mw-ha-humidifier-card"
description: "Home Assistant Lovelace 卡片，把加湿器与其所插的功率计智能插座合并到同一张卡片——不必为两个设备各占一张卡片。"
resource: "https://github.com/visaodeempresa/mw-ha-humidifier-card"
tags: "[home-assistant, lovelace, dashboard, iot, open-source]"
timestamp: "2026-08-13T19:53:00Z"
---

# mw-ha-humidifier-card

## 它是什么
一个 **Home Assistant Lovelace 自定义卡片**，解决一个具体痛点：

> 加湿器通常插在一只带功率计的智能插座上，两个设备在 HA 里得各占一张卡片，状态看不全也难联动。

mw-ha-humidifier-card 把**加湿器实体 + 智能插座（功率计）**合并到**同一张 Lovelace 卡片**里——一并显示开关、功率、湿度。

## 为什么用它 / 适合什么场景
- Home Assistant 用户用「智能插座 + 加湿器」组合。
- 想把「物理分离的两个设备」在面板上**虚拟聚合**。
- 想在一个卡片里看到功率 + 加湿状态的对应关系（插座电流高 / 低反映加湿器在不在工作）。

## 关键能力
| 能力 | 说明 |
|------|------|
| 平台 | Home Assistant |
| 卡片类型 | Lovelace 自定义卡片 |
| 聚合对象 | 加湿器 + 带功率计智能插座 |
| 替代效果 | 原本需要两张卡片 |
| 信息合并 | 开关 / 功率 / 湿度等 |

## 相关概念
- （暂无强相关概念——独立 HA 卡片）

## 媒体
- 卡片截图：<https://pbs.twimg.com/media/HPfUk8jaUAAQEgp.jpg>

## 项目链接
- 项目主页：<https://github.com/visaodeempresa/mw-ha-humidifier-card>